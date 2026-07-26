---
title: CLBackgroundActivitySession
framework: Core Location
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clbackgroundactivitysession-4nl4y
source_url: 'https://developer.apple.com/documentation/corelocation/clbackgroundactivitysession-4nl4y'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clbackgroundactivitysession-4nl4y.json'
content_hash: 'sha256:ef4aca026acf8d47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLBackgroundActivitySession

<sub>Class</sub>

An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@interface CLBackgroundActivitySession : NSObject
```

## Overview

Use `CLBackgroundActivitySession` to start a background activity session that allows a when-in-use authorized app to receive location updates or monitoring events.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

## Topics

### Creating a background activity session

- [backgroundActivitySession](clbackgroundactivitysession-4nl4y/backgroundactivitysession.md) — Creates a new background activity session.

### Ending the session

- [invalidate](clbackgroundactivitysession-4nl4y/invalidate.md) — Invalidates the background activity session.

### Type Methods

- [backgroundActivitySessionWithQueue:handler:](clbackgroundactivitysession-4nl4y/backgroundactivitysessionwithqueue_handler_.md)

## See Also

### Essentials

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md) — Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md) — Enable background events by adding lifecycle event support.
- [CLLocationManager](cllocationmanager.md) — The object you use to start and stop the delivery of location-related events to your app.
