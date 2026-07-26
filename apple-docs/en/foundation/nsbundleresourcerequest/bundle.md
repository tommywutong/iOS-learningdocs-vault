---
title: bundle
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsbundleresourcerequest/bundle
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/bundle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/bundle.json'
content_hash: 'sha256:2a8797df37ea1538'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# bundle

<sub>Instance Property</sub>

A reference to the bundle used for storing the downloaded resources. (read-only)

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
var bundle: Bundle { get }
```

## Discussion

This value is either the main bundle or the one specified in the call to [- initWithTags:bundle:](<init(tags_bundle_).md>). It is valid as soon as the [NSBundleResourceRequest](../nsbundleresourcerequest.md) object is created.

## See Also

### Accessing the configuration

- [tags](tags.md) — A set of strings, with each string specifying a tag used to mark on-demand resources managed by the request. (read-only) _(deprecated)_
