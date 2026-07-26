---
title: 'setDelegateQueue(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnection/setdelegatequeue(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/setdelegatequeue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/setdelegatequeue%28_%3A%29.json'
content_hash: 'sha256:28f28100f291ed97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# setDelegateQueue(_:)

<sub>Instance Method</sub>

Determines the operation queue that is used to call methods on the connection’s delegate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setDelegateQueue(_ queue: OperationQueue?)
```

## Parameters

- `queue` — The operation queue to use when calling delegate methods.

## Discussion

By default, a connection is scheduled on the current thread in the default mode when it is created. If you create a connection with the [- initWithRequest:delegate:startImmediately:](<init(request_delegate_startimmediately_).md>) method and provide [false](../../swift/false.md) for the `startImmediately` parameter, you can instead schedule the connection on an operation queue before starting it with the [- start](<start().md>) method.

You cannot reschedule a connection after it has started.

It is an error to schedule delegate method calls with both this method and the [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) method.

## See Also

### Scheduling Delegate Method Calls

- [- scheduleInRunLoop:forMode:](<schedule(in_formode_).md>) — Determines the run loop and mode that the connection uses to call methods on its delegate.
- [- unscheduleFromRunLoop:forMode:](<unschedule(from_formode_).md>) — Causes the connection to stop calling delegate methods in the specified run loop and mode.
