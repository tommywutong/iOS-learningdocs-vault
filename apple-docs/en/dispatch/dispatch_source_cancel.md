---
title: dispatch_source_cancel
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_cancel
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_cancel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_cancel.json'
content_hash: 'sha256:f6e1505843003d29'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_source_cancel

<sub>Function</sub>

Asynchronously cancels the dispatch source, preventing any further invocation of its event handler block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_source_cancel(dispatch_source_t source);
```

## Parameters

- `source` — The dispatch source to be canceled. This parameter cannot be `NULL`.

## Discussion

Cancellation prevents any further invocation of the event handler block for the specified dispatch source, but does not interrupt an event handler block that is already in progress. The optional cancellation handler is submitted to the target queue once the event handler block has been completed.

The cancellation handler is submitted to the source’s target queue when the source’s event handler has finished, indicating that it is safe to close the source’s handle (file descriptor or mach port).

The optional cancellation handler is submitted to the dispatch source object’s target queue only after the system has released all of its references to any underlying system objects (file descriptors or mach ports). Thus, the cancellation handler is a convenient place to close or deallocate such system objects. Note that it is invalid to close a file descriptor or deallocate a mach port currently being tracked by a dispatch source object before the cancellation handler is invoked.

## See Also

### Related Documentation

- [dispatch_source_set_cancel_handler](dispatch_source_set_cancel_handler.md) — Sets the cancellation handler block for the given dispatch source.

### Canceling a Dispatch Source

- [dispatch_source_testcancel](dispatch_source_testcancel.md) — Tests whether the given dispatch source has been canceled.
