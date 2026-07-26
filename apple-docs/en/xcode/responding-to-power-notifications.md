---
title: Responding to power notifications
framework: xcode
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/xcode/responding-to-power-notifications
source_url: 'https://developer.apple.com/documentation/xcode/responding-to-power-notifications'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/xcode/responding-to-power-notifications.json'
content_hash: 'sha256:412a03002806c52c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Xcode](../xcode.md) · [Performance and metrics](performance-and-metrics.md) · [Reducing your app’s battery use](reducing-your-app-s-battery-use.md)

# Responding to power notifications

<sub>Article</sub>

Adopt more power-efficient strategies to prolong the device’s battery life.

## Overview

Certain situations cause a device to reduce the amount of work it does and the amount of power it uses. People who want to increase the time before their device needs charging can turn on Low Power Mode. When a device is in Low Power Mode, the system enacts energy-saving measures, including reducing animations, and increasing the time between certain power-consuming actions like fetching data over the network.

Additionally, if the system detects that the temperature is too high, it reduces the amount of power it uses until the temperature decreases.

Register for system notifications about power- and thermal-state changes so you can take steps to help the system conserve energy and reduce its temperature.

### Detect and react to power-state notifications

In your app, register for [NSProcessInfoPowerStateDidChange](../foundation/nsnotification/name-swift.struct/nsprocessinfopowerstatedidchange.md) to discover when the device’s power state changes. When you receive the notification, query the value of [isLowPowerModeEnabled](../foundation/processinfo/islowpowermodeenabled.md) to determine if the system’s in Low Power Mode.

If Low Power Mode is active, take additional steps to help the system conserve energy, including:

- Pausing any optional activities
- Reducing display updates
- Minimizing animations
- Reducing the frequency of network connections
- Stopping location updates

### Detect and react to thermal-state notifications

In your app, register for [thermalStateDidChangeNotification](../foundation/processinfo/thermalstatedidchangenotification.md) to discover when the device’s thermal state changes. When you receive the notification, adjust your app’s behavior according to the value of [thermalState](../foundation/processinfo/thermalstate-swift.property.md):

- **[ProcessInfo.ThermalState.nominal](../foundation/processinfo/thermalstate-swift.enum/nominal.md)** — Enable all of your app’s functionality.
- **[ProcessInfo.ThermalState.fair](../foundation/processinfo/thermalstate-swift.enum/fair.md)** — Defer work for which a person doesn’t immediately need the results; for example, background video processing.
- **[ProcessInfo.ThermalState.serious](../foundation/processinfo/thermalstate-swift.enum/serious.md)** — Reduce networking and location activity, screen updates, and animations.
- **[ProcessInfo.ThermalState.critical](../foundation/processinfo/thermalstate-swift.enum/critical.md)** — To prevent the device becoming hotter and potentially unusable, reduce or stop all work that your app is doing. Minimize computation, and stop or significantly reduce use of the camera, Bluetooth, location, and other power-intensive subsystems.

## See Also

### Essentials

- [Scheduling CPU work efficiently](scheduling-cpu-work-efficiently.md) — Use concurrent programming and adjust the prioritization of background activities to improve the performance of your app.
