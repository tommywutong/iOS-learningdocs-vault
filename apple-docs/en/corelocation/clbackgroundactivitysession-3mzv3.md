---
title: CLBackgroundActivitySession
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbackgroundactivitysession-3mzv3
source_url: 'https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-3mzv3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbackgroundactivitysession-3mzv3.json'
content_hash: 'sha256:2b0624f941ade62e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLBackgroundActivitySession

<sub>Class</sub>

An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
final class CLBackgroundActivitySession
```

## Overview

Use `CLBackgroundActivitySession` to start a background activity session that allows a when-in-use authorized app to receive location updates or monitoring events.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a background activity session

- [init()](<clbackgroundactivitysession-3mzv3/init().md>) — Creates a new background activity session.

### Ending the session

- [invalidate()](<clbackgroundactivitysession-3mzv3/invalidate().md>) — Invalidates the background activity session.

### Classes

- [Diagnostics](clbackgroundactivitysession-3mzv3/diagnostics-swift.class.md)

### Structures

- [Diagnostic](clbackgroundactivitysession-3mzv3/diagnostic.md)

### Instance Properties

- [diagnostics](clbackgroundactivitysession-3mzv3/diagnostics-swift.property.md)

## See Also

### Essentials

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md) — Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md) — Enable background events by adding lifecycle event support.
- [CLLocationManager](cllocationmanager.md) — The object you use to start and stop the delivery of location-related events to your app.
- [CLLocationUpdate](cllocationupdate.md) — A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md) — Simplify location delivery using asynchronous events in Swift.
- [Monitoring location changes with Core Location](monitoring-location-changes-with-core-location.md) — Define boundaries and act on user location updates.
