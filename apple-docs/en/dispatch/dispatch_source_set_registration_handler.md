---
title: dispatch_source_set_registration_handler
framework: Dispatch
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_source_set_registration_handler
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_source_set_registration_handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_source_set_registration_handler.json'
content_hash: 'sha256:c9e56ad026441bf7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# dispatch_source_set_registration_handler

<sub>Function</sub>

Sets the registration handler block for the given dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern void dispatch_source_set_registration_handler(dispatch_source_t source, dispatch_block_t handler);
```

## Parameters

- `source` — The dispatch source to modify. This parameter cannot be `NULL`.

- `handler` — The registration handler block to install. The previous registration handler (if any) is released before the new one is installed. This function uses a `Block_copy` call to store a copy of the new registration handler. This parameter can be `NULL`.

## Discussion

The registration handler (if specified) is submitted to the source’s target queue as soon as the source has been fully set up and is ready to start delivering events. The set up of a dispatch source’s underlying event-delivery mechanism occurs asynchronously. Installing a registration handler is a way to be notified when that set up is complete and the dispatch source is ready to start delivering events.

After your operation handler is executed, the dispatch source uninstalls it. Thus, registration handlers are executed only once after you resume the dispatch source.

If you install a registration handler on a dispatch source that is already set up and running, your handler is invoked immediately.

## See Also

### Managing Event Handlers

- [dispatch_source_set_registration_handler_f](dispatch_source_set_registration_handler_f.md) — Sets the registration handler function for the given dispatch source.
- [dispatch_source_set_event_handler_f](dispatch_source_set_event_handler_f.md) — Sets the event handler function for the given dispatch source.
- [dispatch_source_set_event_handler](dispatch_source_set_event_handler.md) — Sets the event handler block for the given dispatch source.
- [dispatch_source_set_cancel_handler_f](dispatch_source_set_cancel_handler_f.md) — Sets the cancellation handler function for the given dispatch source.
- [dispatch_source_set_cancel_handler](dispatch_source_set_cancel_handler.md) — Sets the cancellation handler block for the given dispatch source.
