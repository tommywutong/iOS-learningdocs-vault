---
title: 'distance(from:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.2+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkdistanceformatter/distance(from:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkdistanceformatter/distance(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkdistanceformatter/distance%28from%3A%29.json'
content_hash: 'sha256:35c5a99f9b58ff1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKDistanceFormatter](../mkdistanceformatter.md)

# distance(from:)

<sub>Instance Method</sub>

Returns the distance value parsed from the specified string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from distance: String) -> CLLocationDistance
```

## Parameters

- `distance` — A formatted string that specifies a distance.

## Return Value

The distance value represented by the string or `-1.0` if the string does not contain a recognized distance value.

## Discussion

This method searches the provided string for a number that could represent a distance. Specify distances as purely numerical values. Don’t specify distances as fractions such as “1/4 mile,” use distances and standard distance designations instead, such as “0.25 miles,” “1.2 km,” “120 yards,” and so on.

## See Also

### Converting distances

- [- stringFromDistance:](<string(fromdistance_).md>) — Creates a string representation of the specified distance.
