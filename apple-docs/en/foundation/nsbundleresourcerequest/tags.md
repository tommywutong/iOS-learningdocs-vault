---
title: tags
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest/tags
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/tags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/tags.json'
content_hash: 'sha256:767ba8bc4dd60a00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# tags

<sub>Instance Property</sub>

A set of strings, with each string specifying a tag used to mark on-demand resources managed by the request. (read-only)

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var tags: Set<String> { get }
```

## Discussion

This value is read-only value and is set when the resource request is initialized. The value of each tag in the set corresponds to an identifier you created during app development.

## See Also

### Accessing the configuration

- [bundle](bundle.md) — A reference to the bundle used for storing the downloaded resources. (read-only) _(deprecated)_
