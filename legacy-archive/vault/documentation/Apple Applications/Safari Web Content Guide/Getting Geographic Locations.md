---
title: Safari Web Content Guide
apple_id: TP40002051
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: User Experience
technology: null
published: '2016-12-12'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariWebContent/GettingGeographicalLocations/GettingGeographicalLocations.html
archived_at: '2026-07-15T05:19:13.055298Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Web Content Guide](Developing%20Web%20Content%20for%20Safari.md)


[Next](HTML%20Basics.md)[Previous](Storing%20Data%20on%20the%20Client.md)

# Getting Geographic Locations

Use the JavaScript classes described in this chapter to obtain or track the current geographic location of the host device. These classes hide the implementation details of how the location information is obtained—for example, using Global Positioning System (GPS), IP addresses, Wi-Fi, Bluetooth, or some other technology. The classes allow you to get the current location or get continual updates on the location as it changes.

The `Navigator` object has a read-only `Geolocation` instance variable. You obtain location information from this `Geolocation` object. The parameters to the `Geolocation` methods that get location information are mostly callbacks, instances of `PositionCallback` or `PositionErrorCallback`. Because there may be a delay in getting location information, it cannot be returned immediately by these methods. The callbacks that you specify are invoked when the location information is obtained or an error occurs. If the location information is obtained, the position callback is passed a position object describing the geographic location. If an error occurs, the error callback is passed an instance of `PositionError` describing the error. The position object represents the location in latitude and longitude coordinates.

The most common use of the `Geolocation` class is to get the current location. For example, your web application can get the current location and display it on a map for the user. Use the `getCurrentPosition` method in `Geolocation` to get the current location from the `Navigator` object. Pass your callback function as the parameter to the `getCurrentPosition` method as follows:

```
   // Get the current location
    navigator.geolocation.getCurrentPosition(showMap);
```

Your callback function—the `showMap` function in this example—should take a position object as the parameter as follows:

```
    function showMap(position) {
      // Show a map centered at position
    }
```

Use the `coords` instance variable of the passed-in position object to obtain the latitude and longitude coordinates as follows:

```
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
```


You can also track the current location. For example, if your web application displays the current location on a map, you can register for location changes and continually scroll the map as the current location changes. When you register for location changes, you receive a callback every time the location changes. The callbacks are continual until you unregister for location changes.

Use the `watchPosition` method in the `Geolocation` class to register for location changes. Pass your callback function as the parameter. In this example, the `scrollMap` function is invoked every time the current location changes:

```
    // Register for location changes
    var watchId = navigator.geolocation.watchPosition(scrollMap);
```

The callback function should take a position object as the parameter as follows:

```
    function scrollMap(position) {
      // Scroll the map to center position
    }
```

Similar to [Getting the Current Location](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdanjrfvbuqnjnknltc), use the `coords` instance variable of the passed in position object to obtain the latitude and longitude coordinates.

Use the `clearWatch` method in the `Geolocation` class to unregister for location changes. For example, unregister when the user clicks a button or taps a finger on the map as follows:

```
    function buttonClickHandler() {
      // Unregister when the user clicks a button
      navigator.geolocation.clearWatch(watchId);
    }
```


Your web application should handle errors that can occur when requesting location information. For example, display a message to the user if the location cannot be determined due to poor network connectivity or some other error.

When registering for location changes, you can optionally pass an error callback to the `watchPosition` method in the `Geolocation` class as follows:

```
    // Register for location changes
    var watchId = navigator.geolocation.watchPosition(scrollMap, handleError);
```

The error callback should take a `PositionError` object as the parameter as in:

```
    function handleError(error) {
      // Update a div element with the error message
    }
```

[Next](HTML%20Basics.md)[Previous](Storing%20Data%20on%20the%20Client.md)

