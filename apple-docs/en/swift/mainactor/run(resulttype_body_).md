---
title: 'run(resultType:body:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mainactor/run(resulttype:body:)'
source_url: 'https://developer.apple.com/documentation/swift/mainactor/run(resulttype:body:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mainactor/run%28resulttype%3Abody%3A%29.json'
content_hash: 'sha256:3a556c6b3c6b2500'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MainActor](../mainactor.md)

# run(resultType:body:)

<sub>Type Method</sub>

Execute the given body closure on the main actor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func run<T>(resultType: T.Type = T.self, body: @MainActor @Sendable () throws -> T) async rethrows -> T where T : Sendable
```
