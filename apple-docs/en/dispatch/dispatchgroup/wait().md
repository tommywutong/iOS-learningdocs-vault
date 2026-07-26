---
title: wait()
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchgroup/wait()
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchgroup/wait()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchgroup/wait%28%29.json'
content_hash: 'sha256:b3dcae2c33e2e806'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchGroup](../dispatchgroup.md)

# wait()

<sub>Instance Method</sub>

Waits synchronously for the previously submitted work to finish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func wait()
```

## See Also

### Waiting for Tasks to Finish Executing

- [wait(timeout:)](<wait(timeout_).md>) — Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
- [wait(wallTimeout:)](<wait(walltimeout_).md>) — Waits synchronously for the previously submitted work to complete, and returns if the work is not completed before the specified timeout period has elapsed.
