---
title: 'sleep(nanoseconds:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/task/sleep(nanoseconds:)'
source_url: 'https://developer.apple.com/documentation/swift/task/sleep(nanoseconds:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/sleep%28nanoseconds%3A%29.json'
content_hash: 'sha256:a48dff3343617f89'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# sleep(nanoseconds:)

<sub>Type Method</sub>

Suspends the current task for at least the given duration in nanoseconds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func sleep(nanoseconds duration: UInt64) async throws
```

## Discussion

If the task is canceled before the time ends, this function throws `CancellationError`.

This function doesn’t block the underlying thread.

## See Also

### Suspending Execution

- [yield()](<yield().md>) — Suspends the current task and allows other tasks to execute.
- [sleep(for:tolerance:clock:)](<sleep(for_tolerance_clock_).md>) — Suspends the current task for the given duration.
- [sleep(until:tolerance:clock:)](<sleep(until_tolerance_clock_).md>) — Suspends the current task until the given deadline within a tolerance.
