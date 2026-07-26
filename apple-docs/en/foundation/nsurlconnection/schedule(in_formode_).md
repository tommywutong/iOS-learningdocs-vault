---
title: 'schedule(in:forMode:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnection/schedule(in:formode:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/schedule(in:formode:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/schedule%28in%3Aformode%3A%29.json'
content_hash: 'sha256:36af1e1be11e614d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# schedule(in:forMode:)

<sub>Instance Method</sub>

Determines the run loop and mode that the connection uses to call methods on its delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func schedule(in aRunLoop: RunLoop, forMode mode: RunLoop.Mode)
```

## Parameters

- `aRunLoop` — The [RunLoop](../runloop.md) instance to use when calling delegate methods.

- `mode` — The mode in which to call delegate methods.

## Discussion

By default, a connection is scheduled on the current thread in the default mode when it is created. If you create a connection with the [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) method and provide [false](../../swift/false.md) for the `startImmediately` parameter, you can schedule the connection on a different run loop or mode before starting it with the [- start](<start().md>) method. You can schedule a connection on multiple run loops and modes, or on the same run loop in multiple modes.

You cannot reschedule a connection after it has started.

It is an error to schedule delegate method calls with both this method and the [- setDelegateQueue:](<setdelegatequeue(__).md>) method.

## See Also

### Scheduling Delegate Method Calls

- [- setDelegateQueue:](<setdelegatequeue(__).md>) — Determines the operation queue that is used to call methods on the connection’s delegate.
- [- unscheduleFromRunLoop:forMode:](<unschedule(from_formode_).md>) — Causes the connection to stop calling delegate methods in the specified run loop and mode.
