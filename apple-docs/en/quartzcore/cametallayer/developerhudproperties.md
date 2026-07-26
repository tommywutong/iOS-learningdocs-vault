---
title: developerHUDProperties
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cametallayer/developerhudproperties
source_url: 'https://developer.apple.com/documentation/quartzcore/cametallayer/developerhudproperties'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cametallayer/developerhudproperties.json'
content_hash: 'sha256:236f4b08aa2355c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAMetalLayer](../cametallayer.md)

# developerHUDProperties

<sub>Instance Property</sub>

The properties of the Metal performance heads-up display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var developerHUDProperties: [AnyHashable : Any]? { get set }
```

## Discussion

The Metal performance HUD provides real-time statistics and logging, including CPU and GPU render time and frame-presentation deadlines.
