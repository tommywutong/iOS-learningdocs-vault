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
doc_path: '/documentation/combine/future/init(_:)'
source_url: 'https://developer.apple.com/documentation/combine/future/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/future/init%28_%3A%29.json'
content_hash: 'sha256:8b2b1da5f28f3b89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Future](../future.md)

# init(_:)

<sub>Initializer</sub>

Creates a publisher that invokes a promise closure when the publisher emits an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ attemptToFulfill: @escaping (@escaping Future<Output, Failure>.Promise) -> Void)
```

## Parameters

- `attemptToFulfill` — A [Promise](promise.md) that the publisher invokes when the publisher emits an element or terminates with an error.

## See Also

### Creating a future

- [Promise](promise.md) — A type that represents a closure to invoke in the future, when an element or error is available.
