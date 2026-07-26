---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/unsafecontinuation/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafecontinuation/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafecontinuation/init%28_%3A%29.json'
content_hash: 'sha256:6c8a6f378037e948'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeContinuation](../unsafecontinuation.md)

# init(_:)

<sub>Initializer</sub>

Convert a non-copyable continuation to an [UnsafeContinuation](../unsafecontinuation.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ continuation: consuming Continuation<T, E>)
```

## Discussion

An unsafe continuation may be escaped into contexts where the non-copyable semantics would not be able to statically enforce the resume-once semantics, however the correct use of the continuation is enforced in some way at runtime.
