---
title: 'init(softwareSimulationState:andExternalAccessoryState:)'
framework: Core Location
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationsourceinformation/init(softwaresimulationstate:andexternalaccessorystate:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationsourceinformation/init(softwaresimulationstate:andexternalaccessorystate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationsourceinformation/init%28softwaresimulationstate%3Aandexternalaccessorystate%3A%29.json'
content_hash: 'sha256:a18ff9e05b687c15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationSourceInformation](../cllocationsourceinformation.md)

# init(softwareSimulationState:andExternalAccessoryState:)

<sub>Initializer</sub>

Creates an instance of location source information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(softwareSimulationState isSoftware: Bool, andExternalAccessoryState isAccessory: Bool)
```

## Parameters

- `isSoftware` — A Boolean value that indicates software is generating or simulating the location information.

- `isAccessory` — A Boolean value that indicates an external device is providing the location information.
