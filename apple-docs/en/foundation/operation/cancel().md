---
title: cancel()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/operation/cancel()
source_url: 'https://developer.apple.com/documentation/foundation/operation/cancel()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/operation/cancel%28%29.json'
content_hash: 'sha256:1db4d7d7db8cbacf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Operation](../operation.md)

# cancel()

<sub>Instance Method</sub>

Advises the operation object that it should stop executing its task.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancel()
```

## Discussion

This method does not force your operation code to stop. Instead, it updates the object’s internal flags to reflect the change in state. If the operation has already finished executing, this method has no effect. Canceling an operation that is currently in an operation queue, but not yet executing, makes it possible to remove the operation from the queue sooner than usual.

In macOS 10.6 and later, if an operation is in a queue but waiting on unfinished dependent operations, those operations are subsequently ignored. Because it is already cancelled, this behavior allows the operation queue to call the operation’s [- start](<start().md>) method sooner and clear the object out of the queue. If you cancel an operation that is not in a queue, this method immediately marks the object as finished. In each case, marking the object as ready or finished results in the generation of the appropriate KVO notifications.

In versions of macOS prior to 10.6, an operation object remains in the queue until all of its dependencies are removed through the normal processes. Thus, the operation must wait until all of its dependent operations finish executing or are themselves cancelled and have their [- start](<start().md>) method called.

For more information on what you must do in your operation objects to support cancellation, see [Responding to the Cancel Command](../operation.md#Responding-to-the-Cancel-Command).

## See Also

### Related Documentation

- [cancelled](iscancelled.md) — A Boolean value indicating whether the operation has been cancelled
