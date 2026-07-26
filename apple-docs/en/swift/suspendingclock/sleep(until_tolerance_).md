---
title: 'sleep(until:tolerance:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/suspendingclock/sleep(until:tolerance:)'
source_url: 'https://developer.apple.com/documentation/swift/suspendingclock/sleep(until:tolerance:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/suspendingclock/sleep%28until%3Atolerance%3A%29.json'
content_hash: 'sha256:c7d8641ffcf08305'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [SuspendingClock](../suspendingclock.md)

# sleep(until:tolerance:)

<sub>Instance Method</sub>

Suspend task execution until a given deadline within a tolerance. If no tolerance is specified then the system may adjust the deadline to coalesce CPU wake-ups to more efficiently process the wake-ups in a more power efficient manner.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func sleep(until deadline: SuspendingClock.Instant, tolerance: Duration? = nil) async throws
```

## Discussion

If the task is canceled before the time ends, this function throws `CancellationError`.

This function doesn’t block the underlying thread.
