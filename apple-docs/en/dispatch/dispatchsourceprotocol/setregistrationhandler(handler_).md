---
title: 'setRegistrationHandler(handler:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceprotocol/setregistrationhandler(handler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/setregistrationhandler(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/setregistrationhandler%28handler%3A%29.json'
content_hash: 'sha256:cb988a987d338d91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# setRegistrationHandler(handler:)

<sub>Instance Method</sub>

Sets the registration handler work item for the dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setRegistrationHandler(handler: DispatchWorkItem)
```

## Parameters

- `handler` — The event handler block to submit to the source’s target queue.

## Discussion

The registration handler (if specified) is submitted to the source’s target queue as soon as the source has been fully set up and is ready to start delivering events. The set up of a dispatch source’s underlying event-delivery mechanism occurs asynchronously.

Installing a registration handler is a way to be notified when that set up is complete and the dispatch source is ready to start delivering events. After your operation handler is executed, the dispatch source uninstalls it. As such, registration handlers are executed only once after you resume the dispatch source. If you set a registration handler on a dispatch source that is already set-up and running, the handler is invoked immediately.

## See Also

### Installing Event Handlers

- [setEventHandler(handler:)](<seteventhandler(handler_).md>) — Sets the event handler work item for the dispatch source.
- [setEventHandler(qos:flags:handler:)](<seteventhandler(qos_flags_handler_).md>)
- [setRegistrationHandler(qos:flags:handler:)](<setregistrationhandler(qos_flags_handler_).md>)
- [DispatchSourceHandler](dispatchsourcehandler.md)
