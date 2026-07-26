---
title: 'init(tags:bundle:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nsbundleresourcerequest/init(tags:bundle:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsbundleresourcerequest/init(tags:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsbundleresourcerequest/init%28tags%3Abundle%3A%29.json'
content_hash: 'sha256:3429079febaa83fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSBundleResourceRequest](../nsbundleresourcerequest.md)

# init(tags:bundle:)

<sub>Initializer</sub>

Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the specified bundle.

> [!warning] Deprecated
> Use Background Assets instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
init(tags: Set<String>, bundle: Bundle)
```

## Parameters

- `tags` — A set of strings, with each string specifying a tag assigned to resources stored in `bundle`. The value must not be `nil`.

- `bundle` — The bundle used to store the loaded resources. Pass `nil` for the main bundle. The bundle must be the same as the one used in the Xcode project for all the resources marked with the specified tags.

## Return Value

The initialized resource request.

## See Also

### Initializing a resource request

- [- initWithTags:](<init(tags_).md>) — Initializes a resource request for managing the on-demand resources marked with any of the set of specified tags. The managed resources are loaded into the main bundle. _(deprecated)_
