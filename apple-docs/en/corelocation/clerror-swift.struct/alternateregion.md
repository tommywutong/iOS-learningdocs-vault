---
title: alternateRegion
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.6+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clerror-swift.struct/alternateregion
source_url: 'https://developer.apple.com/documentation/corelocation/clerror-swift.struct/alternateregion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clerror-swift.struct/alternateregion.json'
content_hash: 'sha256:dabf6cc9a8d1eae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLError](../clerror-swift.struct.md)

# alternateRegion

<sub>Instance Property</sub>

A region that location services can monitor more effectively.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var alternateRegion: CLRegion? { get }
```

## Discussion

This property has a value only for errors of type [regionMonitoringResponseDelayed](regionmonitoringresponsedelayed.md).
