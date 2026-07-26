---
title: 'resume(returning:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/continuation/resume(returning:)-5fa8w'
source_url: 'https://developer.apple.com/documentation/swift/continuation/resume(returning:)-5fa8w'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuation/resume%28returning%3A%29-5fa8w.json'
content_hash: 'sha256:1a99474da5574ead'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Continuation](../continuation.md)

# resume(returning:)

<sub>Instance Method</sub>

Resume the task awaiting the continuation by having it return from its suspension point

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
consuming func resume(returning value: consuming sending Success)
```

## Parameters

- `value` — The value to return from the continuation
