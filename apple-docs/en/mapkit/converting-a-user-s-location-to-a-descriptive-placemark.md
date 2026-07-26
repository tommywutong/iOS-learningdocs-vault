---
title: Converting a user’s location to a descriptive placemark
framework: MapKit
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/mapkit/converting-a-user-s-location-to-a-descriptive-placemark
source_url: 'https://developer.apple.com/documentation/mapkit/converting-a-user-s-location-to-a-descriptive-placemark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/converting-a-user-s-location-to-a-descriptive-placemark.json'
content_hash: 'sha256:b3d5b7ba1b604104'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [MapKit](../mapkit.md) · [MapKit for AppKit and UIKit](mapkit-for-appkit-and-uikit.md) · [MKMapView](mkmapview.md)

# Converting a user’s location to a descriptive placemark

<sub>Article</sub>

Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.

## Overview

You can show a user’s location on a map in order to orient them to elements of your app that use map content. For instance, a user’s current location can be a point of reference for retrieving search results or calculating directions. Additionally, you can display location information outside of the map, such as a search field pre-filled with the user’s current city or street address. To provide this information in your app, configure your map view to display the user’s location, and then translate the location to informative, user-friendly data.

### Display the user location annotation

To provide user-friendly place information, configure your map view to display the user’s current location by enabling [showsUserLocation](mkmapview/showsuserlocation.md). After enabling this property, the map delegate begins receiving updates to the user’s location, represented with a [MKUserLocation](mkuserlocation.md) object, through [- mapView:didUpdateUserLocation:](<mkmapviewdelegate/mapview(__didupdate_).md>).

### Geocode the user location annotation

[CLPlacemark](../corelocation/clplacemark.md) objects represent user place names, and include properties for street name, city name, country or region name, and many other location identifiers. When [- mapView:didUpdateUserLocation:](<mkmapviewdelegate/mapview(__didupdate_).md>) receives updates on the user’s location, convert the [MKUserLocation](mkuserlocation.md) object to a [CLPlacemark](../corelocation/clplacemark.md) by reverse geocoding the [location](mkuserlocation/location.md) property with a [CLGeocoder](../corelocation/clgeocoder.md). Readable descriptions of the user’s location are available as properties on the placemark, such as the city information stored in the [locality](../corelocation/clplacemark/locality.md) property.

> [!important] Important
> Geocoding requests are rate-limited for each app. Issue new geocoding requests only when the user has moved a significant distance and after a reasonable amount of time has passed.

```swift
func mapView(_ mapView: MKMapView, didUpdate userLocation: MKUserLocation) {
        guard let newLocation = userLocation.location else { return }
        
        let currentTime = Date()
        let lastLocation = self.currentLocation
        self.currentLocation = newLocation
        
        // Only get new placemark information if you don't have a previous location,
        // if the user has moved a meaningful distance from the previous location, such as 1000 meters,
        // and if it's been 60 seconds since the last geocode request.
        if let lastLocation = lastLocation,
            newLocation.distance(from: lastLocation) <= 1000,
            let lastTime = lastGeocodeTime,
            currentTime.timeIntervalSince(lastTime) < 60 {
            return
        }
        
        // Convert the user's location to a user-friendly place name by reverse geocoding the location.
        lastGeocodeTime = currentTime
        geocoder.reverseGeocodeLocation(newLocation) { (placemarks, error) in
            guard error == nil else {
                self.handleError(error)
                return
            }
            
            // Most geocoding requests contain only one result.
            if let firstPlacemark = placemarks?.first {
                self.mostRecentPlacemark = firstPlacemark
                self.currentCity = firstPlacemark.locality
            }
        }
    }
```

## See Also

### Related Documentation

- [Converting between coordinates and user-friendly place names](../corelocation/converting-between-coordinates-and-user-friendly-place-names.md) — Convert between a latitude and longitude pair and a more user-friendly description of that location.

### Displaying the user’s location

- [showsUserLocation](mkmapview/showsuserlocation.md) — A Boolean value that indicates whether the map tries to display the user’s location.
- [userLocationVisible](mkmapview/isuserlocationvisible.md) — A Boolean value that indicates whether the user’s location is visible in the map view.
- [userLocation](mkmapview/userlocation.md) — The annotation object that represents the user’s location.
- [userTrackingMode](mkmapview/usertrackingmode.md) — The mode to use for tracking the user’s location.
- [- setUserTrackingMode:animated:](<mkmapview/setusertrackingmode(__animated_).md>) — Sets the mode to use for tracking the user’s location, with optional animation.
- [MKUserTrackingMode](mkusertrackingmode.md) — The mode to use for tracking the user’s location on the map.
