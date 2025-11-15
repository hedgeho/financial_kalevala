import { MapContainer, TileLayer, GeoJSON, Tooltip } from 'react-leaflet';
import { Layer } from 'leaflet';
import { useEffect, useState } from 'react';
import { regions } from '../data/mockData';
import './FinlandMap.css';

const FinlandMap = () => {
  const [geoData, setGeoData] = useState<any>(null);
  const centerOfFinland: [number, number] = [64.5, 26.0];

  useEffect(() => {
    fetch('/data/finland_regions.geojson')
      .then(response => response.json())
      .then(data => setGeoData(data))
      .catch(error => console.error('Error loading GeoJSON:', error));
  }, []);

  const getRegionData = (regionId: string) => {
    return regions.find(r => r.id === regionId);
  };

  const styleFeature = (feature: any) => {
    const isUusimaa = feature.properties.Maakunta === 'Uusimaa';
    return {
      fillColor: isUusimaa ? '#88c0d0' : '#2e3440',
      weight: 1,
      opacity: 1,
      color: isUusimaa ? '#5e81ac' : '#4c566a',
      fillOpacity: isUusimaa ? 0.9 : 0.6,
    };
  };

  const onEachFeature = (feature: any, layer: Layer) => {
    const regionName = feature.properties.Maakunta;
    const regionData = getRegionData(regionName);
    if (regionData) {
      layer.bindTooltip(
        `<div class="region-tooltip">
          <strong>${regionData.name}</strong><br/>
          Wisdom Points: ${regionData.points.toLocaleString()}<br/>
          Rank: #${regionData.rank}<br/>
          Quests Completed: ${regionData.achievements}/${regionData.totalAchievements}
        </div>`,
        { permanent: false, direction: 'top' }
      );
    }

    layer.on({
      mouseover: (e) => {
        const target = e.target;
        const isUusimaa = feature.properties.Maakunta === 'Uusimaa';
        target.setStyle({
          fillOpacity: 1,
          weight: 2,
          fillColor: isUusimaa ? '#88c0d0' : '#3b4252',
        });
      },
      mouseout: (e) => {
        const target = e.target;
        const isUusimaa = feature.properties.Maakunta === 'Uusimaa';
        target.setStyle({
          fillOpacity: isUusimaa ? 0.9 : 0.6,
          weight: 1,
          fillColor: isUusimaa ? '#88c0d0' : '#2e3440',
        });
      },
    });
  };

  if (!geoData) {
    return <div className="map-container">Loading map...</div>;
  }

  return (
    <div className="map-container">
      <MapContainer
        center={centerOfFinland}
        zoom={5.5}
        style={{ height: '100%', width: '100%' }}
        zoomControl={true}
        zoomControlOptions={{ position: 'bottomright' }}
      >
        <TileLayer
          url="https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
        />
        <GeoJSON
          data={geoData}
          style={styleFeature}
          onEachFeature={onEachFeature}
        />
      </MapContainer>
    </div>
  );
};

export default FinlandMap;
