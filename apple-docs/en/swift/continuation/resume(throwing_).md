---
title: 'resume(throwing:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/continuation/resume(throwing:)'
source_url: 'https://developer.apple.com/documentation/swift/continuation/resume(throwing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuation/resume%28throwing%3A%29.json'
content_hash: 'sha256:511a8d7057bf80c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Continuation](../continuation.md)

# resume(throwing:)

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it throw an error from its suspension point

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func resume(throwing error: Failure)
```

## Parameters

- `error` — The error to throw from the continuation
