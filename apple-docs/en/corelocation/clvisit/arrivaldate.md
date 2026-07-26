---
title: arrivalDate
framework: Core Location
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corelocation/clvisit/arrivaldate
source_url: 'https://developer.apple.com/documentation/corelocation/clvisit/arrivaldate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/clvisit/arrivaldate.json'
content_hash: 'sha256:2f708df89c68c8d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Location](../../corelocation.md) · [CLVisit](../clvisit.md)

# arrivalDate

<sub>Instance Property</sub>

The approximate time at which the user arrived at the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var arrivalDate: Date { get }
```

## Discussion

When the visit object does not include arrival information, this property is set to the date returned by the [distantPast](../../foundation/nsdate/distantpast.md) method of [NSDate](../../foundation/nsdate.md).

## See Also

### Getting the visit duration

- [departureDate](departuredate.md) — The approximate time at which the user left the specified location.
