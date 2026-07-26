---
title: 'init(tags:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsbundleresourcerequest/init(tags:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/init(tags:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/init%28tags%3A%29.json'
content_hash: 'sha256:ae490f126d25a1c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# init(tags:)

<sub>Initializer</sub>

Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
convenience init(tags: Set<String>)
```

## Parameters

- `tags` — A set of strings, with each string specifying a tag assigned to resources stored in the main bundle. The value must not be `nil`.

## Return Value

The initialized resource request.

## See Also

### Related Documentation

- [Bundle](../bundle.md) — A representation of the code and resources stored in a bundle directory on disk.
- [On-Demand Resources Guide](https://developer.apple.com/library/archive/documentation/FileManagement/Conceptual/On_Demand_Resources_Guide/index.html#//apple_ref/doc/uid/TP40015083)

### Initializing a resource request

- [- initWithTags:bundle:](<init(tags_bundle_).md>) — Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle. _(deprecated)_
