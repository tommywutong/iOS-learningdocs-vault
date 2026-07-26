---
title: background
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/background
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/background'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/background.json'
content_hash: 'sha256:24ce8b35edffbb93'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# background

<sub>Type Property</sub>

The quality-of-service class for maintenance or cleanup tasks that you create.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let background: DispatchQoS
```

## Discussion

Background tasks have the lowest priority of all tasks. Assign this class to tasks or dispatch queues that you use to perform work while your app is running in the background.

## See Also

### Getting the Predefined QoS Objects

- [userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [default](default.md) — The default quality-of-service class.
- [utility](utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [unspecified](unspecified.md) — The absence of a quality-of-service class.
