---
title: userInteractive
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/userinteractive
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/userinteractive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/userinteractive.json'
content_hash: 'sha256:769e34b70a56a439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# userInteractive

<sub>Type Property</sub>

The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let userInteractive: DispatchQoS
```

## Discussion

User-interactive tasks have the highest priority on the system. Use this class for tasks or queues that interact with the user or actively update your app’s user interface. For example, use this class for animations or for tracking events interactively.

## See Also

### Getting the Predefined QoS Objects

- [userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [default](default.md) — The default quality-of-service class.
- [utility](utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [background](background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [unspecified](unspecified.md) — The absence of a quality-of-service class.
