---
title: NetworkBrowser
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkbrowser
source_url: 'https://developer.apple.com/documentation/network/networkbrowser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkbrowser.json'
content_hash: 'sha256:a3521979365a3eca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NetworkBrowser

<sub>Class</sub>

Discover advertised services and devices on the network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NetworkBrowser<Provider> where Provider : BrowserProvider
```

## Overview

Whenever services become available, get modified, or go away, the browser will generate a set of browse results tracking those changes. You can subscribe to and receive these updates as long as the browser is active.

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(for:using:)](<networkbrowser/init(for_using_).md>) — Create a browser that will browse for the service specified by a BrowserProvider, with parameters.

### Instance Methods

- [onStateUpdate(_:)](<networkbrowser/onstateupdate(__).md>) — Set a closure to be called when the browser’s state changes.
- [run(_:)](<networkbrowser/run(__)-31x4b.md>) — Run the browser and receive updates when when the set of discovered endpoints change.
- [run(_:)](<networkbrowser/run(__)-wqyo.md>)

### Type Aliases

- [StateUpdateHandler](networkbrowser/stateupdatehandler.md)

### Enumerations

- [RunResult](networkbrowser/runresult.md)
- [State](networkbrowser/state.md) — Possible states for the browser to be in.
