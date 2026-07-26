---
title: 'unschedule(from:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnection/unschedule(from:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/unschedule(from:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/unschedule%28from%3Aformode%3A%29.json'
content_hash: 'sha256:09a84068d4025230'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# unschedule(from:forMode:)

<sub>Instance Method</sub>

Causes the connection to stop calling delegate methods in the specified run loop and mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func unschedule(from aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — The run loop instance to unschedule.

- `mode` — The mode to unschedule.

## Discussion

By default, a connection is scheduled on the current thread in the default mode when it is created. If you create a connection with the [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) method and provide [false](../../swift/false.md) for the `startImmediately` parameter, you can instead schedule connection on a different run loop or mode before starting it with the [- start](<start().md>) method. You can schedule a connection on multiple run loops and modes, or on the same run loop in multiple modes. Use this method to unschedule the connection from an undesired run loop and mode before starting the connection.

You cannot reschedule a connection after it has started. It is not necessary to unschedule a connection after it has finished.

## See Also

### Scheduling Delegate Method Calls

- [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) — Determines the run loop and mode that the connection uses to call methods on its delegate.
- [- setDelegateQueue:](<setdelegatequeue(__).md>) — Determines the operation queue that is used to call methods on the connection’s delegate.
