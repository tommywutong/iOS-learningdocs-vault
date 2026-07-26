---
title: headingAvailable
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+（4.0 起废弃）, iPadOS 3.0+（4.0 起废弃）, macOS 10.15+（10.15 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/corelocation/cllocationmanager/headingavailable-swift.property
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationmanager/headingavailable-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationmanager/headingavailable-swift.property.json'
content_hash: 'sha256:82a527cd039efaeb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocationManager](../cllocationmanager.md)

# headingAvailable

<sub>Instance Property</sub>

A Boolean value indicating whether the location manager is able to generate heading-related events.

> [!warning] Deprecated
> Use the [+ headingAvailable](<headingavailable().md>) class method instead.

<sub>macOS, visionOS</sub>

```swift
var headingAvailable: Bool { get }
```

## Discussion

Heading data may not be available on all iOS-based devices. You should check the value of this property before asking the location manager to deliver heading-related events.
