---
title: DispatchQoS.QoSClass.default
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/qosclass-swift.enum/default
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/qosclass-swift.enum/default.json'
content_hash: 'sha256:8b95f5ec9b289102'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQoS](../../dispatchqos.md) · [QoSClass](../qosclass-swift.enum.md)

# DispatchQoS.QoSClass.default

<sub>Case</sub>

The default quality-of-service class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case `default`
```

## Discussion

Default tasks have a lower priority than user-initiated and user-interactive tasks, but a higher priority than utility and background tasks. Assign this class to tasks or queues that your app initiates or uses to perform active work on the user’s behalf.

## See Also

### Getting the Quality-of-Service Class

- [DispatchQoS.QoSClass.userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.utility](utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.background](background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](unspecified.md) — The absence of a quality-of-service class.
