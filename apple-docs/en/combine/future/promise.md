---
title: Future.Promise
framework: Combine
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/future/promise
source_url: 'https://developer.apple.com/documentation/combine/future/promise'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/future/promise.json'
content_hash: 'sha256:474b387b707d96b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Future](../future.md)

# Future.Promise

<sub>Type Alias</sub>

A type that represents a closure to invoke in the future, when an element or error is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias Promise = (Result<Output, Failure>) -> Void
```

## Discussion

The promise closure receives one parameter: a `Result` that contains either a single element published by a [Future](../future.md), or an error.

## See Also

### Creating a future

- [init(_:)](<init(__).md>) — Creates a publisher that invokes a promise closure when the publisher emits an element.
