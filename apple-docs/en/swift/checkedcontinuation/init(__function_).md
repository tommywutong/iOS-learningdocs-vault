---
title: 'init(_:function:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/checkedcontinuation/init(_:function:)'
source_url: 'https://developer.apple.com/documentation/swift/checkedcontinuation/init(_:function:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/checkedcontinuation/init%28_%3Afunction%3A%29.json'
content_hash: 'sha256:f1b7ee60eedd3364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CheckedContinuation](../checkedcontinuation.md)

# init(_:function:)

<sub>Initializer</sub>

Convert a non-copyable continuation to a [CheckedContinuation](../checkedcontinuation.md)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ continuation: consuming Continuation<T, E>, function: String = #function)
```

## Discussion

A checked continuation may be escaped into contexts where the non-copyable semantics would not be able to statically enforce the resume-once semantics, however the correct use of the continuation is enforced in some way at runtime.
