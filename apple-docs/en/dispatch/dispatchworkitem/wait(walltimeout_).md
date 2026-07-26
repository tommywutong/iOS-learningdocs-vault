---
title: 'wait(wallTimeout:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchworkitem/wait(walltimeout:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchworkitem/wait(walltimeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchworkitem/wait%28walltimeout%3A%29.json'
content_hash: 'sha256:2b4de63d0f4b808b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchWorkItem](../dispatchworkitem.md)

# wait(wallTimeout:)

<sub>Instance Method</sub>

Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait(wallTimeout: DispatchWallTime) -> DispatchTimeoutResult
```

## Parameters

- `wallTimeout` — The time at which to stop waiting for the dispatch item to finish. Specifying [distantFuture](../dispatchtime/distantfuture.md) is equivalent to calling the [wait()](<wait().md>) method.

## Return Value

[DispatchTimeoutResult.success](../dispatchtimeoutresult/success.md) if the method returned because the work item finished executing, or [DispatchTimeoutResult.timedOut](../dispatchtimeoutresult/timedout.md) if the timeout value was reached.

## Discussion

This method returns immediately if the current work item has already finished executing.

## See Also

### Waiting for the Completion of a Work Item

- [wait()](<wait().md>) — Causes the caller to wait synchronously until the dispatch work item finishes executing.
- [wait(timeout:)](<wait(timeout_).md>) — Causes the caller to wait synchronously until the dispatch work item finishes executing, or until the specified time elapses.
- [DispatchTime](../dispatchtime.md) — A point in time relative to the default clock, with nanosecond precision.
- [DispatchWallTime](../dispatchwalltime.md) — An absolute point in time according to the wall clock, with microsecond precision.
