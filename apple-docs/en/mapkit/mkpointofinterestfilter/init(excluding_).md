---
title: 'init(excluding:)'
framework: MapKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkpointofinterestfilter/init(excluding:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter/init(excluding:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkpointofinterestfilter/init%28excluding%3A%29.json'
content_hash: 'sha256:c8548b5407e66eb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKPointOfInterestFilter](../mkpointofinterestfilter.md)

# init(excluding:)

<sub>Initializer</sub>

Initialize the point of interest filter with a list of categories to exclude.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(excluding categories: [MKPointOfInterestCategory])
```

## Parameters

- `categories` — An array of categories to exclude.

## See Also

### Creating filters

- [filterExcludingAllCategories](excludingall.md) — A filter that excludes all point of interest categories.
- [filterIncludingAllCategories](includingall.md) — A filter that includes all point of interest categories.
- [- initIncludingCategories:](<init(including_).md>) — Initialize the point of interest filter with a list of categories to include.
