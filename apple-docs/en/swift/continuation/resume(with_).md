---
title: 'resume(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/continuation/resume(with:)'
source_url: 'https://developer.apple.com/documentation/swift/continuation/resume(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuation/resume%28with%3A%29.json'
content_hash: 'sha256:1aeaddd148bea80c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Continuation](../continuation.md)

# resume(with:)

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it either return or throw an error based on the state of the given `Result` value

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func resume(with result: consuming sending Result<Success, Failure>)
```

## Parameters

- `result` — A value to either return or throw from the continuation
