---
title: utility
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/utility
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/utility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/utility.json'
content_hash: 'sha256:3c0d01d9fc92b9e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# utility

<sub>Type Property</sub>

The quality-of-service class for tasks that the user does not track actively.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let utility: DispatchQoS
```

## Discussion

Utility tasks have a lower priority than default, user-initiated, and user-interactive tasks, but a higher priority than background tasks. Assign this quality-of-service class to tasks that do not prevent the user from continuing to use your app. For example, you might assign this class to long-running tasks whose progress the user does not follow actively.

## See Also

### Getting the Predefined QoS Objects

- [userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [default](default.md) — The default quality-of-service class.
- [background](background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
- [unspecified](unspecified.md) — The absence of a quality-of-service class.
