---
title: yield()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/task/yield()
source_url: 'https://developer.apple.com/documentation/swift/task/yield()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/task/yield%28%29.json'
content_hash: 'sha256:2cb7c6f9d5a009e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Task](../task.md)

# yield()

<sub>Type Method</sub>

Suspends the current task and allows other tasks to execute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func yield() async
```

## Discussion

A task can voluntarily suspend itself in the middle of a long-running operation that doesn’t contain any suspension points, to let other tasks run for a while before execution returns to this task.

If this task is the highest-priority task in the system, the executor immediately resumes execution of the same task. As such, this method isn’t necessarily a way to avoid resource starvation.

## See Also

### Suspending Execution

- [sleep(nanoseconds:)](<sleep(nanoseconds_).md>) — Suspends the current task for at least the given duration in nanoseconds.
- [sleep(for:tolerance:clock:)](<sleep(for_tolerance_clock_).md>) — Suspends the current task for the given duration.
- [sleep(until:tolerance:clock:)](<sleep(until_tolerance_clock_).md>) — Suspends the current task until the given deadline within a tolerance.
