---
title: 'excludes(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpointofinterestfilter/excludes(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/excludes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointofinterestfilter/excludes%28_%3A%29.json'
content_hash: 'sha256:29f195e8da44a836'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPointOfInterestFilter](../mkpointofinterestfilter.md)

# excludes(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the filter excludes the point of interest category.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func excludes(_ category: MKPointOfInterestCategory) -> Bool
```

## Parameters

- `category` — A point of interest category that the method checks for exclusion in the filter.

## Return Value

`true` if the filter excludes the point of interest category; otherwise, `false`.

## See Also

### Querying filter behavior

- [- includesCategory:](<includes(__).md>) — Returns a Boolean value indicating whether the filter includes the point of interest category.
