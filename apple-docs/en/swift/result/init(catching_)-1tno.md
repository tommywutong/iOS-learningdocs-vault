---
title: 'init(catching:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/init(catching:)-1tno'
source_url: 'https://developer.apple.com/documentation/swift/result/init(catching:)-1tno'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/init%28catching%3A%29-1tno.json'
content_hash: 'sha256:8e1b96baa7583b48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# init(catching:)

<sub>Initializer</sub>

Creates a new result by evaluating an async throwing closure, capturing the returned value as a success, or any thrown error as a failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) init(catching body: nonisolated(nonsending) () async throws(Failure) -> Success) async
```

## Parameters

- `body` — A potentially throwing async closure to evaluate.
