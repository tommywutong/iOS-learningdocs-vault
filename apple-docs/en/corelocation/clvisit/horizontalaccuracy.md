---
title: horizontalAccuracy
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clvisit/horizontalaccuracy
source_url: 'https://developer.apple.com/documentation/corelocation/clvisit/horizontalaccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clvisit/horizontalaccuracy.json'
content_hash: 'sha256:659ab59e8052388e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLVisit](../clvisit.md)

# horizontalAccuracy

<sub>Instance Property</sub>

The horizontal accuracy (in meters) of the specified coordinate.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var horizontalAccuracy: CLLocationAccuracy { get }
```

## Discussion

The latitude and longitude specified by the [coordinate](coordinate.md) property identify the center of the circle, and this value indicates the radius of that circle.

## See Also

### Getting the location

- [coordinate](coordinate.md) — The geographical coordinate information.
