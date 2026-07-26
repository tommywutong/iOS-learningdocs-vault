---
title: default
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/default
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/default.json'
content_hash: 'sha256:cbc957d08390af1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# default

<sub>Type Property</sub>

The default quality-of-service class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let `default`: DispatchQoS
```

## Discussion

Default tasks have a lower priority than user-initiated and user-interactive tasks, but a higher priority than utility and background tasks. Assign this class to tasks or queues that your app initiates or uses to perform active work on the user’s behalf.

## See Also

### Getting the Predefined QoS Objects

- [userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [utility](utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [background](background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [unspecified](unspecified.md) — The absence of a quality-of-service class.
