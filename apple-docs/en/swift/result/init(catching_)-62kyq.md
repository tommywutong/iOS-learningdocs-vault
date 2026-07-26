---
title: 'init(catching:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/result/init(catching:)-62kyq'
source_url: 'https://developer.apple.com/documentation/swift/result/init(catching:)-62kyq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/result/init%28catching%3A%29-62kyq.json'
content_hash: 'sha256:542f1ee5549d75d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Result](../result.md)

# init(catching:)

<sub>Initializer</sub>

Creates a new result by evaluating a throwing closure, capturing the returned value as a success, or any thrown error as a failure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(catching body: () throws(Failure) -> Success)
```

## Parameters

- `body` — A potentially throwing closure to evaluate.
