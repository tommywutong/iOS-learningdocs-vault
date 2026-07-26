---
title: Monitoring location changes with Core Location
framework: Core Location
symbol_kind: article
role: sampleCode
role_heading: Sample Code
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, Xcode 15.3+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/monitoring-location-changes-with-core-location
source_url: 'https://developer.apple.com/documentation/corelocation/monitoring-location-changes-with-core-location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/monitoring-location-changes-with-core-location.json'
content_hash: 'sha256:bfc06beb34133247'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# Monitoring location changes with Core Location

<sub>Sample Code</sub>

Define boundaries and act on user location updates.

## Overview

> [!note] Note
> This sample code project is associated with WWDC24 session 10212: [What’s new in location authorization](https://developer.apple.com/wwdc24/10212/) and WWDC23 session 10147: [Meet Core Location Monitor](https://developer.apple.com/wwdc23/10147/).

### Configure the sample code project

Before you run the sample code project in Xcode, ensure that you’re using Xcode 16 or later and iOS 18 or later.

## See Also

### Essentials

- [Configuring your app to use location services](configuring-your-app-to-use-location-services.md) — Prepare your app to start collecting location data.
- [Supporting live updates in SwiftUI and Mac Catalyst apps](supporting-live-updates-in-swiftui-and-mac-catalyst-apps.md) — Enable background events by adding lifecycle event support.
- [CLLocationManager](cllocationmanager.md) — The object you use to start and stop the delivery of location-related events to your app.
- [CLBackgroundActivitySession](clbackgroundactivitysession-3mzv3.md) — An object that manages a visual indicator that keeps your app in use in the background, allowing it to receive updates or events.
- [CLLocationUpdate](cllocationupdate.md) — A structure that contains the location information the framework delivers with each update.
- [Adopting live updates in Core Location](adopting-live-updates-in-core-location.md) — Simplify location delivery using asynchronous events in Swift.

## Download

- [MonitoringLocationChangesWithCoreLocation.zip](https://docs-assets.developer.apple.com/published/60d004152b62/MonitoringLocationChangesWithCoreLocation.zip)
