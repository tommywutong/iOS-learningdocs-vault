---
title: 'wait(timeout:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchgroup/wait(timeout:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/wait(timeout:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/wait%28timeout%3A%29.json'
content_hash: 'sha256:c1039002712da1ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# wait(timeout:)

<sub>Instance Method</sub>

Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait(timeout: DispatchTime) -> DispatchTimeoutResult
```

## Parameters

- `timeout` — The latest time to wait for a group to complete.

## Return Value

A result value indicating whether the method returned due to a timeout.

## See Also

### Waiting for Tasks to Finish Executing

- [wait()](<wait().md>) — Waits synchronously for the previously submitted work to finish.
- [wait(wallTimeout:)](<wait(walltimeout_).md>) — Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
