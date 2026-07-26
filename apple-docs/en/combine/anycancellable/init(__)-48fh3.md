---
title: 'init(_:)'
framework: Combine
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/anycancellable/init(_:)-48fh3'
source_url: 'https://developer.apple.com/documentation/combine/anycancellable/init(_:)-48fh3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/anycancellable/init%28_%3A%29-48fh3.json'
content_hash: 'sha256:d00d8f26be3e4b3b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [AnyCancellable](../anycancellable.md)

# init(_:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<C>(_ canceller: C) where C : Cancellable
```

## See Also

### Creating a type-erased cancellable

- [init(_:)](<init(__)-3icn3.md>) — Initializes the cancellable object with the given cancel-time closure.
