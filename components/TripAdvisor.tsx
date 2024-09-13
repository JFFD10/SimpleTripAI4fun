import React, { useState } from 'react';
import { PlusIcon, MapPinIcon, StarIcon } from 'lucide-react';

interface Place {
  id: number;
  name: string;
}

interface Information {
  information: string;
}

const TripAdvisor: React.FC = () => {
  const [places, setPlaces] = useState<Place[]>([]);
  const [newPlaceName, setNewPlaceName] = useState('');
  const [selectedPlace, setSelectedPlace] = useState('');
  const [selectedCategory, setSelectedCategory] = useState('');
  const [information, setInformation] = useState<Information | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const handleAddPlace = (e: React.FormEvent) => {
    e.preventDefault();
    if (newPlaceName.trim()) {
      const newPlace: Place = {
        id: Date.now(),
        name: newPlaceName.trim(),
      };
      setPlaces(prevPlaces => [...prevPlaces, newPlace]);
      setNewPlaceName('');
      setSelectedPlace(newPlace.name);
    }
  };

  const handleGetInformation = async () => {
    if (!selectedPlace || !selectedCategory) {
      alert('Please select both a place and a category');
      return;
    }

    setIsLoading(true);
    try {
      const response = await fetch('/api/get-information', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ place: selectedPlace, category: selectedCategory }),
      });

      const data = await response.json();
      if (data.error) {
        throw new Error(data.error);
      }
      setInformation(data);
      console.log('Received information:', data.information);  // Add this line for debugging
    } catch (error) {
      console.error('Error:', error);
      setInformation({ information: `Error: ${error.message}` });
    } finally {
      setIsLoading(false);
    }
  };

  const renderStars = (rating: string) => {
    const numStars = parseFloat(rating);
    return Array.from({ length: 5 }, (_, i) => (
      <StarIcon
        key={i}
        className={`h-5 w-5 ${i < numStars ? 'text-yellow-400' : 'text-gray-300'}`}
        fill={i < numStars ? 'currentColor' : 'none'}
      />
    ));
  };

  return (
    <div className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-md mx-auto bg-white rounded-2xl shadow-lg overflow-hidden">
        <div className="px-8 pt-8 pb-6">
          <h1 className="text-3xl font-bold text-gray-900 mb-6">Trip Advisor</h1>
          
          <div className="space-y-6">
            <div>
              <label htmlFor="new-place" className="block text-sm font-medium text-gray-700 mb-1">
                Add a new place
              </label>
              <div className="mt-1 relative rounded-md shadow-sm">
                <input
                  type="text"
                  id="new-place"
                  className="block w-full pr-10 sm:text-sm border-gray-300 rounded-md focus:ring-indigo-500 focus:border-indigo-500"
                  placeholder="Enter a place"
                  value={newPlaceName}
                  onChange={(e) => setNewPlaceName(e.target.value)}
                />
                <button
                  onClick={handleAddPlace}
                  className="absolute inset-y-0 right-0 pr-3 flex items-center"
                >
                  <PlusIcon className="h-5 w-5 text-gray-400 hover:text-gray-500" aria-hidden="true" />
                </button>
              </div>
            </div>

            <div>
              <label htmlFor="place" className="block text-sm font-medium text-gray-700 mb-1">
                Select a place
              </label>
              <select
                id="place"
                className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                value={selectedPlace}
                onChange={(e) => setSelectedPlace(e.target.value)}
              >
                <option value="">Choose a place</option>
                {places.map((place) => (
                  <option key={place.id} value={place.name}>
                    {place.name}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label htmlFor="category" className="block text-sm font-medium text-gray-700 mb-1">
                Select a category
              </label>
              <select
                id="category"
                className="mt-1 block w-full pl-3 pr-10 py-2 text-base border-gray-300 focus:outline-none focus:ring-indigo-500 focus:border-indigo-500 sm:text-sm rounded-md"
                value={selectedCategory}
                onChange={(e) => setSelectedCategory(e.target.value)}
              >
                <option value="">Choose a category</option>
                <option value="Hotels">Hotels</option>
                <option value="Restaurants">Restaurants</option>
                <option value="Attractions">Attractions</option>
              </select>
            </div>

            <button
              onClick={handleGetInformation}
              className="w-full flex justify-center py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
              disabled={isLoading}
            >
              {isLoading ? 'Loading...' : 'Get Information'}
            </button>
          </div>
        </div>

        {information && (
          <div className="px-8 py-6 bg-gray-50 border-t border-gray-200">
            <div className="flex items-center mb-4">
              <MapPinIcon className="h-5 w-5 text-gray-400 mr-2" aria-hidden="true" />
              <h2 className="text-lg font-medium text-gray-900">Top {selectedCategory} in {selectedPlace}</h2>
            </div>
            <div className="mt-2 text-sm text-gray-700 space-y-2">
              <p>{information.information}</p>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default TripAdvisor;