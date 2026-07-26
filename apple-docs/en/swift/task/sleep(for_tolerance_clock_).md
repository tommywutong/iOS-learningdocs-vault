---
title: 'sleep(for:tolerance:clock:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/task/sleep(for:tolerance:clock:)'
source_url: 'https://developer.apple.com/documentation/swift/task/sleep(for:tolerance:clock:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/sleep%28for%3Atolerance%3Aclock%3A%29.json'
content_hash: 'sha256:9b763dded4f66f61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# sleep(for:tolerance:clock:)

<sub>Type Method</sub>

Suspends the current task for the given duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func sleep<C>(for duration: C.Instant.Duration, tolerance: C.Instant.Duration? = nil, clock: C = .continuous) async throws where C : Clock
```

## Discussion

If the task is canceled before the time ends, this function throws `CancellationError`.

This function doesn’t block the underlying thread.

```swift
  try await Task.sleep(for: .seconds(3))
```

## See Also

### Suspending Execution

- [yield()](<yield().md>) — Suspends the current task and allows other tasks to execute.
- [sleep(nanoseconds:)](<sleep(nanoseconds_).md>) — Suspends the current task for at least the given duration in nanoseconds.
- [sleep(until:tolerance:clock:)](<sleep(until_tolerance_clock_).md>) — Suspends the current task until the given deadline within a tolerance.
