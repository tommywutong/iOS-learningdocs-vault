---
title: 'setRegistrationHandler(qos:flags:handler:)'
framework: Dispatch
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/dispatch/dispatchsourceprotocol/setregistrationhandler(qos:flags:handler:)'
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchsourceprotocol/setregistrationhandler(qos:flags:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchsourceprotocol/setregistrationhandler%28qos%3Aflags%3Ahandler%3A%29.json'
content_hash: 'sha256:5c016d9113acc65d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchSourceProtocol](../dispatchsourceprotocol.md)

# setRegistrationHandler(qos:flags:handler:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setRegistrationHandler(qos: DispatchQoS = .unspecified, flags: DispatchWorkItemFlags = [], handler: Self.DispatchSourceHandler?)
```

## See Also

### Installing Event Handlers

- [setEventHandler(handler:)](<seteventhandler(handler_).md>) — Sets the event handler work item for the dispatch source.
- [setEventHandler(qos:flags:handler:)](<seteventhandler(qos_flags_handler_).md>)
- [setRegistrationHandler(handler:)](<setregistrationhandler(handler_).md>) — Sets the registration handler work item for the dispatch source.
- [DispatchSourceHandler](dispatchsourcehandler.md)
