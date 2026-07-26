---
title: unspecified
framework: Dispatch
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatchqos/unspecified
source_url: 'https://developer.apple.com/documentation/dispatch/dispatchqos/unspecified'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatchqos/unspecified.json'
content_hash: 'sha256:bd2de7e33823de6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Dispatch](../../dispatch.md) · [DispatchQoS](../dispatchqos.md)

# unspecified

<sub>Type Property</sub>

The absence of a quality-of-service class.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let unspecified: DispatchQoS
```

## See Also

### Getting the Predefined QoS Objects

- [userInteractive](userinteractive.md) — The quality-of-service class for user-interactive tasks, such as animations, event handling, or updates to your app’s user interface.
- [userInitiated](userinitiated.md) — The quality-of-service class for tasks that prevent the user from actively using your app.
- [default](default.md) — The default quality-of-service class.
- [utility](utility.md) — The quality-of-service class for tasks that the user does not track actively.
- [background](background.md) — The quality-of-service class for maintenance or cleanup tasks that you create.
