---
title: Accessing the device’s location efficiently
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/accessing-the-device-s-location-efficiently
source_url: 'https://developer.apple.com/documentation/xcode/accessing-the-device-s-location-efficiently'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/accessing-the-device-s-location-efficiently.json'
content_hash: 'sha256:6bd3f5706b21757d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# Accessing the device’s location efficiently

<sub>Article</sub>

Use Core Location features to manage energy use, receive updates, and minimize location update frequency.

## Overview

Discovering a person’s location — particularly to a high [desiredAccuracy](../corelocation/cllocationmanager/desiredaccuracy.md) — requires combining information from multiple device subsystems that each consume power while they’re active. Minimize the frequency with which your app requests location updates, and don’t leave location updates running when your app doesn’t need them.

Use [CLLocationUpdate](../corelocation/cllocationupdate.md) to receive updates from the system when the device’s location changes. If the device becomes stationary, Core Location sets the [stationary](../corelocation/cllocationupdate/stationary.md) flag and stops providing updates until the device moves again. When this happens, if you don’t expect movement again soon, consider stopping location updates and using [CLMonitor](../corelocation/clmonitor-2r51v.md) to get notified of significant changes to the device’s location. Set [distanceFilter](../corelocation/cllocationmanager/distancefilter.md) to the distance the device needs to move before the system notifies your app.

If you need to receive location updates when your app is in the background, use [CLBackgroundActivitySession](../corelocation/clbackgroundactivitysession-3mzv3.md), or call [requestAlwaysAuthorization()](<../corelocation/cllocationmanager/requestalwaysauthorization().md>). For more information, see [Handling location updates in the background](../corelocation/handling-location-updates-in-the-background.md). However, only register for background location updates if your app’s functionality doesn’t work without it, as background updates increase your app’s energy use.

## See Also

### Networking and location

- [Reducing networking and Bluetooth power usage](reducing-networking-and-bluetooth-power-usage.md) — Schedule requests strategically and minimize background network activity to decrease your app’s energy use.
