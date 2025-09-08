# Navigation Toolkit
A Python desktop application for outdoor navigation and route planning, starting with unit conversions and expanding toward comprehensive navigation functionality.

## Current Features
- **Tabbed interface** for different conversion categories
- **Length conversion**: meters, feet, inches, yards, miles
- **Weight conversion**: kilograms, pounds, ounces, grams
- **Input validation** with error handling
- **Clean GUI** built with Tkinter

## Current Status  
🚧 **Version 0.2** - Multi-category unit converter with tabbed interface

## Roadmap

### Phase 1: Enhanced Conversions
- [ ] Temperature conversion (Celsius, Fahrenheit, Kelvin)
- [ ] Angle conversion (degrees, radians, gradians)
- [ ] Real-time conversion (no button required)
- [ ] Conversion history log

### Phase 2: Basic Navigation Tools
- [ ] Coordinate system conversions (GPS, UTM, MGRS)
- [ ] Distance calculations between coordinates (Haversine formula)
- [ ] Bearing/azimuth calculations
- [ ] Basic route planning with waypoints

### Phase 3: Advanced Features
- [ ] Elevation profile analysis
- [ ] Travel time estimation
- [ ] Route optimization
- [ ] GPX file import/export

## Why Offline?
Navigation data is sensitive personal information. This desktop application ensures:
- **Privacy**: No data transmitted over networks
- **Reliability**: Works without internet connection
- **Security**: User maintains full control over their location data

## Tech Stack
- **Python 3.x** - Core language
- **Tkinter** - GUI framework
- **Planned additions**: 
  - `geopy` - Geographic calculations
  - `gpxpy` - GPX file handling
  - `numpy` - Mathematical operations

## Getting Started
```bash
git clone https://github.com/vitalina-tech/navigation-toolkit
cd navigation-toolkit
python main.py
