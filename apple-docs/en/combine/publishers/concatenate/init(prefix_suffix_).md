---
title: 'init(prefix:suffix:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/concatenate/init(prefix:suffix:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/concatenate/init(prefix:suffix:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/concatenate/init%28prefix%3Asuffix%3A%29.json'
content_hash: 'sha256:5a52b94cf1a95739'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [Concatenate](../concatenate.md)

# init(prefix:suffix:)

<sub>Initializer</sub>

Creates a publisher that emits all of one publisher’s elements before those from another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(prefix: Prefix, suffix: Suffix)
```

## Parameters

- `prefix` — The publisher to republish, in its entirety, before republishing elements from `suffix`.

- `suffix` — The publisher to republish only after `prefix` finishes.
