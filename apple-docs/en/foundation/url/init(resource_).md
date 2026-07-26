---
title: 'init(resource:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/url/init(resource:)'
source_url: 'https://developer.apple.com/documentation/foundation/url/init(resource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/url/init%28resource%3A%29.json'
content_hash: 'sha256:d25b3af01d66c943'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URL](../url.md)

# init(resource:)

<sub>Initializer</sub>

Creates a URL from a resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(resource: URLResource)
```

## Parameters

- `resource` — A [URLResource](../urlresource.md) that provides a reference to a resource in a given bundle.

## Discussion

Use this initializer to resolve [URLResource](../urlresource.md) instances, possibly received from other processes, into [URL](../url.md) instances.
