---
title: DispatchQoS.QoSClass.utility
framework: Dispatch
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/qosclass-swift.enum/utility
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/qosclass-swift.enum/utility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/qosclass-swift.enum/utility.json'
content_hash: 'sha256:3653cb20458cdb4a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Dispatch](../../../dispatch.md) · [DispatchQoS](../../dispatchqos.md) · [QoSClass](../qosclass-swift.enum.md)

# DispatchQoS.QoSClass.utility

<sub>Case</sub>

The quality-of-service class for tasks that the user does not track actively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case utility
```

## Discussion

Utility tasks have a lower priority than default, user-initiated, and user-interactive tasks, but a higher priority than background tasks. Assign this quality-of-service class to tasks that do not prevent the user from continuing to use your app. For example, you might assign this class to long-running tasks whose progress the user does not follow actively.

## See Also

### Getting the Quality-of-Service Class

- [DispatchQoS.QoSClass.userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updating your app’s user interface.
- [DispatchQoS.QoSClass.userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [DispatchQoS.QoSClass.default](default.md) — The default quality-of-service class.
- [DispatchQoS.QoSClass.background](background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [DispatchQoS.QoSClass.unspecified](unspecified.md) — The absence of a quality-of-service class.
