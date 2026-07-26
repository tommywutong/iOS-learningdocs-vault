---
title: CLLocationUpdater
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationupdater
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdater'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdater.json'
content_hash: 'sha256:ede2dd71a2321ca3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationUpdater

<sub>Class</sub>

An object that provides device location updates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLLocationUpdater : NSObject
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Creating a location updater

- [liveUpdaterWithConfiguration:queue:handler:](cllocationupdater/liveupdaterwithconfiguration_queue_handler_.md) — Creates a location updater with the configuration and queue that you specify.
- [liveUpdaterWithQueue:handler:](cllocationupdater/liveupdaterwithqueue_handler_.md) — Creates a location updater on the queue you specify.
- [CLLiveUpdateConfiguration](clliveupdateconfiguration.md) — Specifies the types of locations that a location updater generates.

### Controlling the updater

- [invalidate](cllocationupdater/invalidate.md) — Invalidates the updater.
- [pause](cllocationupdater/pause.md) — Pauses the updater.
- [resume](cllocationupdater/resume.md) — Resumes the updater.

## See Also

### Location updates

- [Getting the current location of a device](getting-the-current-location-of-a-device.md) — Start location services and provide information the system needs to optimize power usage for those services.
- [Handling location updates in the background](handling-location-updates-in-the-background.md) — Configure your app to receive location updates when it isn’t running in the foreground.
- [Creating a location push service extension](creating-a-location-push-service-extension.md) — Add and configure an extension to enable your location-sharing app to access a person’s location in response to a request from someone else.
- [CLLocation](cllocation.md) — The latitude, longitude, and course information reported by the system.
- [CLLocationCoordinate2D](cllocationcoordinate2d.md) — The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [CLFloor](clfloor.md) — The floor of a building on which the user’s device is located.
- [CLVisit](clvisit.md) — Information about the user’s location during a specific period of time.
- [CLLocationSourceInformation](cllocationsourceinformation.md) — Information about the source that provides a location.
- [CLServiceSession](clservicesession-2ddhd.md)
- [CLServiceSessionDiagnostic](clservicesessiondiagnostic.md)
- [CLBackgroundActivitySessionDiagnostic](clbackgroundactivitysessiondiagnostic.md)
