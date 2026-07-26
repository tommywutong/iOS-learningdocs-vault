---
title: CLLocationUpdate
framework: Core Location
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocationupdate
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationupdate.json'
content_hash: 'sha256:8e5029978d35423d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationUpdate

<sub>Structure</sub>

A structure that contains the location information the framework delivers with each update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CLLocationUpdate
```

## Overview

You use `CLLocationUpate` events to observe changes in the device’s location, and to determine the activity type.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining movement and location

- [isStationary](cllocationupdate/isstationary.md) — A Boolean value that indicates whether the user is stationary. _(deprecated)_
- [location](cllocationupdate/location.md) — The user’s location, if available.

### Receiving location updates

- [liveUpdates(_:)](<cllocationupdate/liveupdates(__).md>) — Tells Core Location to start delivering the location updates it produces for the configuration you specify.
- [LiveConfiguration](cllocationupdate/liveconfiguration.md) — Values for indicating the kind of updates the framework delivers.
- [Updates](cllocationupdate/updates.md) — A structure that represents an asynchronous sequence of location updates.

### Instance Properties

- [accuracyLimited](cllocationupdate/accuracylimited.md)
- [authorizationDenied](cllocationupdate/authorizationdenied.md)
- [authorizationDeniedGlobally](cllocationupdate/authorizationdeniedglobally.md)
- [authorizationRequestInProgress](cllocationupdate/authorizationrequestinprogress.md)
- [authorizationRestricted](cllocationupdate/authorizationrestricted.md)
- [insufficientlyInUse](cllocationupdate/insufficientlyinuse.md)
- [locationUnavailable](cllocationupdate/locationunavailable.md)
- [serviceSessionRequired](cllocationupdate/servicesessionrequired.md)
- [stationary](cllocationupdate/stationary.md)

## See Also

### Essentials

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md) — Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md) — Enable background events by adding lifecycle event support.
- [CLLocationManager](cllocationmanager.md) — The object you use to start and stop the delivery of location-related events to your app.
- [CLBackgroundActivitySession](clbackgroundactivitysession-3mzv3.md) — An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md) — Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md) — Define boundaries and act on user location updates.
