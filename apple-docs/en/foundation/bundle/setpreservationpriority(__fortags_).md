---
title: 'setPreservationPriority(_:forTags:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/bundle/setpreservationpriority(_:fortags:)'
source_url: 'https://developer.apple.com/documentation/foundation/bundle/setpreservationpriority(_:fortags:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/bundle/setpreservationpriority%28_%3Afortags%3A%29.json'
content_hash: 'sha256:79560fb4080f3017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Bundle](../bundle.md)

# setPreservationPriority(_:forTags:)

<sub>Instance Method</sub>

A hint to the system of the relative order for purging tagged sets of resources in the bundle.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func setPreservationPriority(_ priority: Double, forTags tags: Set<String>)
```

## Parameters

- `priority` — A number specifying the relative priority of preserving the resources in the group specified by `tag`. Possible values are between `0.0` and `1.0`. The default is `0.0`. The system will attempt to purge resources with lower priorities first.

- `tags` — A set of tag names specifying resources stored in the bundle. Must not be `nil`. An exception is thrown if any of the tags in the set do not exist in your app.

## See Also

### Managing preservation priority for on-demand resources

- [- preservationPriorityForTag:](<preservationpriority(fortag_).md>) — Returns the current preservation priority for the specified tag. _(deprecated)_
