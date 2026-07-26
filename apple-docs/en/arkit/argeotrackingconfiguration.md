---
title: ARGeoTrackingConfiguration
framework: ARKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.0+, iPadOS 14.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/arkit/argeotrackingconfiguration
source_url: 'https://developer.apple.com/documentation/arkit/argeotrackingconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/arkit/argeotrackingconfiguration.json'
content_hash: 'sha256:26459b20e10e1561'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [ARKit](../arkit.md)

# ARGeoTrackingConfiguration

<sub>Class</sub>

A configuration that tracks locations with GPS, map data, and a device’s compass.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class ARGeoTrackingConfiguration
```

## Overview

This configuration creates location anchors ([ARGeoAnchor](argeoanchor.md)) that specify a particular latitude, longitude, and optionally, altitude to enable an app to track geographic areas of interest in an AR experience.

> [!important] Important
> The [isSupported](arconfiguration/issupported.md) property returns [true](../swift/true.md) for this class on iOS 14 & iPadOS 14 devices that have an A12 chip or later and cellular (GPS) capability. Geotracking is available in specific geographic locations. To determine availability at the user’s location at runtime, call [+ checkAvailabilityWithCompletionHandler:](<argeotrackingconfiguration/checkavailability(completionhandler_).md>).

Geotracking occurs exclusively outdoors. If a geotracking app navigates users between waypoints, your app needs to handle any events along a route. The user must have an internet connection, and you can provide them information about data usage, as described in [ARGeoAnchor](argeoanchor.md).

### Encourage user safety

To keep your users’ focus on the road while traveling, discourage them from looking at the device when in motion, such as while riding a bike. Keep users informed when navigating through unfamiliar territory. For instance, you can recommend they steer clear of private property, or remind them to check their device’s battery level before beginning a long route.

### Refine the user’s position with imagery

To place location anchors with precision, geotracking requires a better understanding of the user’s geographic location than is possible with GPS alone. Based on the user’s GPS coordinates, ARKit downloads imagery that depicts the physical environment in that area. Apple collects this _localization imagery_ in advance by capturing photos of the view from the street and recording the geographic position at each photo. By comparing the device’s current camera image with this imagery, the session matches the user’s precise geographic location with the scene’s local coordinates. For information about the user’s position in local space, see [transform](arcamera/transform.md).

Localization imagery captures views from public streets and routes accessible by car, but doesn’t include images of gated or pedestrian-only areas.

Geotracking sessions use localization imagery in the [ARGeoTrackingStateLocalizing](argeotrackingstatus/state-swift.enum/localizing.md) state.

### Supported areas and cities

Localization imagery is available for specific areas in over 20 countries, including many metropolitan areas in Australia, Europe, Japan, and North America. To check availability in a particular location, see the [+ checkAvailabilityWithCompletionHandler:](<argeotrackingconfiguration/checkavailability(completionhandler_).md>) function.

> [!tip] Tip
> You can share an experience of geotracking with developers who live outside an area that supports it. Record a session in your app in an area that supports localization imagery for developers to create and test their geotracking app. For more information, see [Recording and Replaying AR Session Data](recording-and-replaying-ar-session-data.md).

## Relationships

- **Inherits From**: [ARConfiguration](arconfiguration.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a configuration

- [- init](<argeotrackingconfiguration/init().md>) — Initializes a new geotracking configuration.

### Checking availability

- [+ checkAvailabilityWithCompletionHandler:](<argeotrackingconfiguration/checkavailability(completionhandler_).md>) — Determines if geotracking supports the user’s current location.
- [+ checkAvailabilityAtCoordinate:completionHandler:](<argeotrackingconfiguration/checkavailability(at_completionhandler_).md>) — Determines if geotracking supports a particular location.

### Tracking surfaces

- [planeDetection](argeotrackingconfiguration/planedetection.md) — A value that specifies whether and how the session automatically attempts to detect flat surfaces in the camera-captured image.
- [PlaneDetection](arworldtrackingconfiguration/planedetection-swift.struct.md) — Options for whether and how the framework detects flat surfaces in captured images.

### Detecting or tracking images

- [detectionImages](argeotrackingconfiguration/detectionimages.md) — A set of images that ARKit searches for in the user’s environment.
- [maximumNumberOfTrackedImages](argeotrackingconfiguration/maximumnumberoftrackedimages.md) — The number of image anchors to monitor closely for position and orientation updates.
- [automaticImageScaleEstimationEnabled](argeotrackingconfiguration/automaticimagescaleestimationenabled.md) — A flag that instructs the framework to estimate and set the scale of a detected or tracked image on your behalf.

### Detecting and tracking real-world objects

- [detectionObjects](argeotrackingconfiguration/detectionobjects.md) — A set of 3D objects that the framework attempts to detect in the user’s environment.
- [trackingObjects](argeotrackingconfiguration/trackingobjects.md) — Objects to track in the scene. _(beta)_

### Creating realistic reflections

- [environmentTexturing](argeotrackingconfiguration/environmenttexturing.md) — An option that determines how the framework generates environment textures.
- [EnvironmentTexturing](arworldtrackingconfiguration/environmenttexturing-swift.enum.md) — The available environment texturing options for world tracking.
- [AREnvironmentProbeAnchor](arenvironmentprobeanchor.md) — An object that provides environmental lighting information for a specific area of space in a world-tracking AR session.
- [wantsHDREnvironmentTextures](argeotrackingconfiguration/wantshdrenvironmenttextures.md) — A flag that instructs the framework to create environment textures in HDR format.

### Accessing app clip codes

- [Interacting with App Clip Codes in AR](../appclip/interacting-with-app-clip-codes-in-ar.md) — Display content and provide services in an AR experience with App Clip Codes.
- [supportsAppClipCodeTracking](argeotrackingconfiguration/supportsappclipcodetracking.md) — A flag that indicates if the device tracks App Clip Codes.
- [appClipCodeTrackingEnabled](argeotrackingconfiguration/appclipcodetrackingenabled.md) — A Boolean value that indicates if the framework searches the physical environment for App Clip Codes.
- [ARAppClipCodeAnchor](arappclipcodeanchor.md) — An anchor that tracks the position and orientation of an App Clip Code in the physical environment.

## See Also

### Spatial Tracking

- [Understanding World Tracking](understanding-world-tracking.md) — Discover features and best practices for building rear-camera AR experiences.
- [ARWorldTrackingConfiguration](arworldtrackingconfiguration.md) — A configuration that tracks the position of a device in relation to objects in the environment.
- [AROrientationTrackingConfiguration](arorientationtrackingconfiguration.md) — A configuration that tracks only the device’s orientation using the rear-facing camera.
- [ARPositionalTrackingConfiguration](arpositionaltrackingconfiguration.md) — A configuration that tracks only the device’s position in 3D space.
