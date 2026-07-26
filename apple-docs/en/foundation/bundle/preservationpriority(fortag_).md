---
title: 'preservationPriority(forTag:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/bundle/preservationpriority(fortag:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/preservationpriority(fortag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/preservationpriority%28fortag%3A%29.json'
content_hash: 'sha256:4cab7ab99e5d97aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# preservationPriority(forTag:)

<sub>Instance Method</sub>

Returns the current preservation priority for the specified tag.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func preservationPriority(forTag tag: String) -> Double
```

## Parameters

- `tag` — A string specifying the identifier for a group of related resources. An exception is thrown if `tag` does not exist in your app.

## Return Value

The preservation priority for the specified `tag`. Possible values are between `0.0` and `1.0`

## See Also

### Managing preservation priority for on-demand resources

- [- setPreservationPriority:forTags:](<setpreservationpriority(__fortags_).md>) — A hint to the system of the relative order for purging tagged sets of resources in the bundle. _(deprecated)_
