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
doc_path: '/documentation/swift/suspendingclock/measure(_:)-1zuvn'
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/measure(_:)-1zuvn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/measure%28_%3A%29-1zuvn.json'
content_hash: 'sha256:04e3717dd3834890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SuspendingClock](../suspendingclock.md)

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
