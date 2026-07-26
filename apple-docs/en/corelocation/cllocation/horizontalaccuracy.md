---
title: horizontalAccuracy
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/horizontalaccuracy
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/horizontalaccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/horizontalaccuracy.json'
content_hash: 'sha256:f7a7a906a687baa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# horizontalAccuracy

<sub>Instance Property</sub>

The radius of uncertainty for the location, measured in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var horizontalAccuracy: CLLocationAccuracy { get }
```

## Discussion

The location’s latitude and longitude identify the center of the circle, and this value indicates the radius of that circle. A negative value indicates that the latitude and longitude are invalid.

### Special Considerations

In iOS, this property is declared as `nonatomic`. In macOS, it is declared as `atomic`.

## See Also

### Getting the location accuracy

- [verticalAccuracy](verticalaccuracy.md) — The validity of the altitude values, and their estimated uncertainty, measured in meters.
- [CLLocationAccuracy](../cllocationaccuracy.md) — The accuracy of a geographical coordinate.
