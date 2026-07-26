---
title: 'init(name:subdirectory:locale:bundle:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/urlresource/init(name:subdirectory:locale:bundle:)'
source_url: 'https://developer.apple.com/documentation/foundation/urlresource/init(name:subdirectory:locale:bundle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlresource/init%28name%3Asubdirectory%3Alocale%3Abundle%3A%29.json'
content_hash: 'sha256:a63183c49996fec6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLResource](../urlresource.md)

# init(name:subdirectory:locale:bundle:)

<sub>Initializer</sub>

Creates a URL resource from the given bundle, name, and subdirectory, optionally specifying a locale.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(name: String, subdirectory: String? = nil, locale: Locale = .current, bundle: Bundle = .main)
```

## Parameters

- `name` — The name of the resource in the bundle. This should include both the resource name and its extension, to avoid confusion.

- `subdirectory` — The subdirectory, if any, of the resource.

- `locale` — The locale of the resource, as provided by the process that creates the resource. This defaults to [current](../locale/current.md).

- `bundle` — The bundle containing the resource. This defaults to [mainBundle](../bundle/main.md).
