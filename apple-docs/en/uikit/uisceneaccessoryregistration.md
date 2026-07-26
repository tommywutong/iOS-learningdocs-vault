---
title: UISceneAccessoryRegistration
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uisceneaccessoryregistration
source_url: 'https://developer.apple.com/documentation/uikit/uisceneaccessoryregistration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneaccessoryregistration.json'
content_hash: 'sha256:d71be1245ffb6880'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneAccessoryRegistration

<sub>Class</sub>

A type which represents the registration for a given scene accessory.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UISceneAccessoryRegistration
```

## Overview

Instances of this type allow for observing availability of a given scene accessory, as well as controlling whether the contents should be displayed when the system determines the scene is available.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Observing availability and controlling display

- [available](uisceneaccessoryregistration/isavailable.md) — Whether the associated scene accessory is available for display by the system or not. _(beta)_
- [enabled](uisceneaccessoryregistration/isenabled.md) — Whether the content defined by this scene accessory should be displayed or not. _(beta)_

## See Also

### Scene accessories

- [UISceneAccessory](uisceneaccessory.md) — A type which can be used to register for a specific type of scene accessory presentation. _(beta)_
