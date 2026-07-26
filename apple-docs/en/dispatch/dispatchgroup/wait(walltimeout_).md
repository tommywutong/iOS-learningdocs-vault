---
title: 'wait(wallTimeout:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchgroup/wait(walltimeout:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/wait(walltimeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/wait%28walltimeout%3A%29.json'
content_hash: 'sha256:bd1add3530d28e21'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# wait(wallTimeout:)

<sub>Instance Method</sub>

Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait(wallTimeout timeout: DispatchWallTime) -> DispatchTimeoutResult
```

## Parameters

- `timeout` — The latest time to wait for a group to complete.

## Return Value

[DispatchTimeoutResult.timedOut](../dispatchtimeoutresult/timedout.md) if the method returned due to a timeout, or [DispatchTimeoutResult.success](../dispatchtimeoutresult/success.md) if the tasks completed.

## See Also

### Waiting for Tasks to Finish Executing

- [wait()](<wait().md>) — Waits synchronously for the previously submitted work to finish.
- [wait(timeout:)](<wait(timeout_).md>) — Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
