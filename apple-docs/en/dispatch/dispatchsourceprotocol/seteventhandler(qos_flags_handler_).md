---
title: 'setEventHandler(qos:flags:handler:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceprotocol/seteventhandler(qos:flags:handler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/seteventhandler(qos:flags:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/seteventhandler%28qos%3Aflags%3Ahandler%3A%29.json'
content_hash: 'sha256:a41072b7c601c508'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# setEventHandler(qos:flags:handler:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setEventHandler(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], handler: Self.DispatchSourceHandler?)
```

## See Also

### Installing Event Handlers

- [setEventHandler(handler:)](<seteventhandler(handler_).md>) — Sets the event handler work item for the dispatch source.
- [setRegistrationHandler(handler:)](<setregistrationhandler(handler_).md>) — Sets the registration handler work item for the dispatch source.
- [setRegistrationHandler(qos:flags:handler:)](<setregistrationhandler(qos_flags_handler_).md>)
- [DispatchSourceHandler](dispatchsourcehandler.md)
