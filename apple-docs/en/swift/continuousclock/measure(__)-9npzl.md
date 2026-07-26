---
title: 'measure(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/continuousclock/measure(_:)-9npzl'
source_url: 'https://developer.apple.com/documentation/swift/continuousclock/measure(_:)-9npzl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/continuousclock/measure%28_%3A%29-9npzl.json'
content_hash: 'sha256:82daf8b6599bd8bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContinuousClock](../continuousclock.md)

# measure(_:)

<sub>Instance Method</sub>

Measure the elapsed time to execute an asynchronous closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func measure(_ work: nonisolated(nonsending) () async throws -> Void) async rethrows -> Self.Instant.Duration
```

## Discussion

```swift
  let clock = ContinuousClock()
  let elapsed = await clock.measure {
     await someWork()
  }
```
