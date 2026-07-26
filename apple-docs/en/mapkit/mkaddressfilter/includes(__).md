---
title: 'includes(_:)'
framework: MapKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/mapkit/mkaddressfilter/includes(_:)'
source_url: 'https://developer.apple.com/documentation/mapkit/mkaddressfilter/includes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/mapkit/mkaddressfilter/includes%28_%3A%29.json'
content_hash: 'sha256:75a3e380f6accfa1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [MapKit](../../mapkit.md) · [MKAddressFilter](../mkaddressfilter.md)

# includes(_:)

<sub>Instance Method</sub>

Indicates whether options are included for filtering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func includes(_ options: MKAddressFilter.Options) -> Bool
```

## Parameters

- `options` — The filters to check for inclusion.

## Return Value

Returns `true` if the passed options are included in the filtering options; otherwise, `false`.

## Discussion

A filter includes or excludes a set of filter options. Use this method to query the filter instance for one or more options.

```swift
let filter = MKAddressFilter(including: [.locality,  .subLocality])
let result = filter.includes(.locality)
```

The method returns `true` because `filter` includes [Locality](../../mapkitjs/addresscategory/locality.md).

## See Also

### Filtering results

- [Options](options.md) — A structure that contains options for filtering results in a search.
- [filterExcludingAll](excludingall.md) — A list of categories to exclude from a search.
- [filterIncludingAll](includingall.md) — A list of categories to include in a search.
- [- excludesOptions:](<excludes(__).md>) — Indicates whether options are excluded from filtering.
