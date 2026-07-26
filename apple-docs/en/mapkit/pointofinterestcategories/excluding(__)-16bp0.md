---
title: 'excluding(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/pointofinterestcategories/excluding(_:)-16bp0'
source_url: 'https://developer.apple.com/documentation/mapkit/pointofinterestcategories/excluding(_:)-16bp0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/pointofinterestcategories/excluding%28_%3A%29-16bp0.json'
content_hash: 'sha256:b13369cf91fb5930'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [PointOfInterestCategories](../pointofinterestcategories.md)

# excluding(_:)

<sub>Type Method</sub>

Show all points of interest except those belonging to certain categories using the array you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func excluding(_ categories: [MKPointOfInterestCategory]) -> PointOfInterestCategories
```

## Parameters

- `categories` — An array of points of interest categories to exclude.

## Return Value

Returns a set of point of interest categories to exclude.

## See Also

### Modifying the categories to include or exclude

- [excluding(_:)](<excluding(__)-4jo9h.md>) — Show all points of interest except those belonging to certain categories using the list you provide.
- [including(_:)](<including(__)-22f7x.md>) — Show only points of interest belonging to certain categories from the provided array.
- [including(_:)](<including(__)-6flda.md>) — Show only points of interest belonging to certain categories from the provided list.
