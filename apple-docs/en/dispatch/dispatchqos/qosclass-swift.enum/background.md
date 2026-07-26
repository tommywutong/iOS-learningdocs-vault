---
title: DispatchQoS.QoSClass.background
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/qosclass-swift.enum/background
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/qosclass-swift.enum/background.json'
content_hash: 'sha256:0cdb0a451cc90e02'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQoS](../../dispatchqos.md) · [QoSClass](../qosclass-swift.enum.md)

# DispatchQoS.QoSClass.background

<sub>Case</sub>

The quality-of-service class for maintenance or cleanup tasks that you create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case background
```

## Discussion

Background tasks have the lowest priority of all tasks. Assign this class to tasks or dispatch queues that you use to perform work while your app is running in the background.

## See Also

### Getting the Quality-of-Service Class

- [DispatchQoS.QoSClass.userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](default.md) — The default quality-of-service class.
- [DispatchQoS.QoSClass.utility](utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [DispatchQoS.QoSClass.unspecified](unspecified.md) — The absence of a quality-of-service class.
