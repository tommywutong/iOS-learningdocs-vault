---
title: verticalAccuracy
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/cllocation/verticalaccuracy
source_url: 'https://developer.apple.com/documentation/corelocation/cllocation/verticalaccuracy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocation/verticalaccuracy.json'
content_hash: 'sha256:c224c693d61edf0a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLLocation](../cllocation.md)

# verticalAccuracy

<sub>Instance Property</sub>

The validity of the altitude values, and their estimated uncertainty, measured in meters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var verticalAccuracy: CLLocationAccuracy { get }
```

## Discussion

A positive [verticalAccuracy](verticalaccuracy.md) value represents the estimated uncertainty associated with [altitude](altitude.md) and [ellipsoidalAltitude](ellipsoidalaltitude.md). This value is available whenever altitude values are available.

If [verticalAccuracy](verticalaccuracy.md) is `0` or a negative number, [altitude](altitude.md) and [ellipsoidalAltitude](ellipsoidalaltitude.md) values are invalid. If [verticalAccuracy](verticalaccuracy.md) is a postive number, [altitude](altitude.md) and [ellipsoidalAltitude](ellipsoidalaltitude.md) values are valid.

A positive [verticalAccuracy](verticalaccuracy.md) value represents an uncertainty that’s approximately 68 percent, or one standard deviation, above and below the altitude values.

> [!note] Note
> In iOS, this property is declared as `nonatomic`. In macOS, it’s declared as `atomic`.

## See Also

### Getting the location accuracy

- [horizontalAccuracy](horizontalaccuracy.md) — The radius of uncertainty for the location, measured in meters.
- [CLLocationAccuracy](../cllocationaccuracy.md) — The accuracy of a geographical coordinate.
