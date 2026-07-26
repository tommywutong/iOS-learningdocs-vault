---
title: 'setEventHandler(handler:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceprotocol/seteventhandler(handler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/seteventhandler(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/seteventhandler%28handler%3A%29.json'
content_hash: 'sha256:b6f5eadbea3510e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# setEventHandler(handler:)

<sub>Instance Method</sub>

Sets the event handler work item for the dispatch source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setEventHandler(handler: DispatchWorkItem)
```

## Parameters

- `handler` — The event handler block to submit to the source’s target queue.

## Discussion

The event handler (if specified) is submitted to the source’s target queue in response to the arrival of an event.

## See Also

### Installing Event Handlers

- [setEventHandler(qos:flags:handler:)](<seteventhandler(qos_flags_handler_).md>)
- [setRegistrationHandler(handler:)](<setregistrationhandler(handler_).md>) — Sets the registration handler work item for the dispatch source.
- [setRegistrationHandler(qos:flags:handler:)](<setregistrationhandler(qos_flags_handler_).md>)
- [DispatchSourceHandler](dispatchsourcehandler.md)
