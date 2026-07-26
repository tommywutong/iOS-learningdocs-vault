---
title: 'init(continuation:function:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/checkedcontinuation/init(continuation:function:)'
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation/init(continuation:function:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation/init%28continuation%3Afunction%3A%29.json'
content_hash: 'sha256:28d7a613d4516956'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CheckedContinuation](../checkedcontinuation.md)

# init(continuation:function:)

<sub>Initializer</sub>

Creates a checked continuation from an unsafe continuation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(continuation: UnsafeContinuation<T, E>, function: String = #function)
```

## Parameters

- `continuation` — An instance of `UnsafeContinuation` that hasn’t yet been resumed. After passing the unsafe continuation to this initializer, don’t use it outside of this object.

- `function` — A string identifying the declaration that is the notional source for the continuation, used to identify the continuation in runtime diagnostics related to misuse of this continuation.

## Discussion

Instead of calling this initializer, most code calls the `withCheckedContinuation(function:_:)` or `withCheckedThrowingContinuation(function:_:)` function instead. You only need to initialize your own `CheckedContinuation<T, E>` if you already have an `UnsafeContinuation` you want to impose checking on.
