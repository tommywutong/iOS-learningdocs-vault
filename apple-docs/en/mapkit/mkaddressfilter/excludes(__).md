---
title: 'excludes(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkaddressfilter/excludes(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressfilter/excludes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressfilter/excludes%28_%3A%29.json'
content_hash: 'sha256:18e6593301f61b4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressFilter](../mkaddressfilter.md)

# excludes(_:)

<sub>Instance Method</sub>

Indicates whether options are excluded from filtering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func excludes(_ options: MKAddressFilter.Options) -> Bool
```

## Parameters

- `options` — The filters to check for exclusion.

## Return Value

Returns `true` if the passed options are excluded from the filtering options; otherwise, `false`.

## Discussion

A filter includes or excludes a set of filter options. Use this method to query the filter instance for one or more options.

```swift
let filter = MKAddressFilter(including: [.locality,  .subLocality])
let result = filter.excludes(.postalCode)
```

The method returns `true` because `filter` doesn’t include [PostalCode](../../mapkitjs/addresscategory/postalcode.md).

## See Also

### Filtering results

- [Options](options.md) — A structure that contains options for filtering results in a search.
- [filterExcludingAll](excludingall.md) — A list of categories to exclude from a search.
- [filterIncludingAll](includingall.md) — A list of categories to include in a search.
- [- includesOptions:](<includes(__).md>) — Indicates whether options are included for filtering.
