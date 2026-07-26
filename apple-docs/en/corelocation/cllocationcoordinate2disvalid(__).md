---
title: 'CLLocationCoordinate2DIsValid(_:)'
framework: Core Location
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corelocation/cllocationcoordinate2disvalid(_:)'
source_url: 'https://developer.apple.com/documentation/corelocation/cllocationcoordinate2disvalid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corelocation/cllocationcoordinate2disvalid%28_%3A%29.json'
content_hash: 'sha256:a4c38650723f6967'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Location](../corelocation.md)

# CLLocationCoordinate2DIsValid(_:)

<sub>Function</sub>

Returns a Boolean value indicating whether the specified coordinate is valid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CLLocationCoordinate2DIsValid(_ coord: CLLocationCoordinate2D) -> Bool
```

## Parameters

- `coord` — A coordinate containing latitude and longitude values.

## Return Value

[true](../swift/true.md) if the coordinate is valid or [false](../swift/false.md) if it is not.

## Discussion

A coordinate is considered invalid if it meets at least one of the following criteria:

- Its latitude is greater than 90 degrees or less than -90 degrees.
- Its longitude is greater than 180 degrees or less than -180 degrees.

## See Also

### Validating a coordinate

- [kCLLocationCoordinate2DInvalid](kcllocationcoordinate2dinvalid.md) — An invalid coordinate value.
