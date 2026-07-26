---
title: CLLiveUpdateConfiguration
framework: Core Location
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clliveupdateconfiguration
source_url: 'https://developer.apple.com/documentation/corelocation/clliveupdateconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clliveupdateconfiguration.json'
content_hash: 'sha256:bda0b3deb664b723'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLiveUpdateConfiguration

<sub>Enumeration</sub>

Specifies the types of locations that a location updater generates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
enum CLLiveUpdateConfiguration : NSInteger;
```

## Topics

### Update types

- [CLLiveUpdateConfigurationDefault](clliveupdateconfiguration/clliveupdateconfigurationdefault.md) — The default configuration.
- [CLLiveUpdateConfigurationAirborne](clliveupdateconfiguration/clliveupdateconfigurationairborne.md) — A configuration for airborne use cases.
- [CLLiveUpdateConfigurationAutomotiveNavigation](clliveupdateconfiguration/clliveupdateconfigurationautomotivenavigation.md) — A configuration for automotive navigation use cases.
- [CLLiveUpdateConfigurationFitness](clliveupdateconfiguration/clliveupdateconfigurationfitness.md) — A configuration for fitness use cases.
- [CLLiveUpdateConfigurationOtherNavigation](clliveupdateconfiguration/clliveupdateconfigurationothernavigation.md) — A configuration for other navigation use cases.

### Enumeration Cases

- [CLLiveUpdateConfigurationMaritime](clliveupdateconfiguration/clliveupdateconfigurationmaritime.md) _(beta)_

## See Also

### Creating a location updater

- [liveUpdaterWithConfiguration:queue:handler:](cllocationupdater/liveupdaterwithconfiguration_queue_handler_.md) — Creates a location updater with the configuration and queue that you specify.
- [liveUpdaterWithQueue:handler:](cllocationupdater/liveupdaterwithqueue_handler_.md) — Creates a location updater on the queue you specify.
