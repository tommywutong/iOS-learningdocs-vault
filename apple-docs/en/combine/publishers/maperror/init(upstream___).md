---
title: 'init(upstream:_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publishers/maperror/init(upstream:_:)'
source_url: 'https://developer.apple.com/documentation/combine/publishers/maperror/init(upstream:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/maperror/init%28upstream%3A_%3A%29.json'
content_hash: 'sha256:054b177e60ae5684'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Publishers](../../publishers.md) · [MapError](../maperror.md)

# init(upstream:_:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(upstream: Upstream, _ map: @escaping (Upstream.Failure) -> Failure)
```

## See Also

### Creating an error-mapping publisher

- [init(upstream:transform:)](<init(upstream_transform_).md>) — Creates a publisher that converts any failure from the upstream publisher into a new error.
