---
title: UISceneAccessory
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/uikit/uisceneaccessory
source_url: 'https://developer.apple.com/documentation/uikit/uisceneaccessory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisceneaccessory.json'
content_hash: 'sha256:f143c05d265807b9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneAccessory

<sub>Class</sub>

A type which can be used to register for a specific type of scene accessory presentation.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor class UISceneAccessory
```

## Overview

A scene accessory declares supplementary content that the system presents on the app’s behalf when an associated piece of system functionality becomes available, for example when an external display is connected. The app declares what content to provide; the system decides when and where to present it. Scene accessories enhance the app’s experience when available, but the app must remain fully functional without them.

Use an instance of this type along with `UIViewController.registerSceneAccessory(_:)`.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Type Methods

- [+ externalNonInteractiveSceneAccessoryWithConfiguration:](<uisceneaccessory/externalnoninteractive(sceneconfiguration_).md>) — Creates a new scene accessory configuration for presenting non-interactive content on an external display. _(beta)_
- [+ externalNonInteractiveSceneAccessoryWithConfiguration:userInfo:](<uisceneaccessory/externalnoninteractive(sceneconfiguration_userinfo_).md>) — Creates a new scene accessory configuration for presenting non-interactive content on an external display. _(beta)_

## See Also

### Scene accessories

- [UISceneAccessoryRegistration](uisceneaccessoryregistration.md) — A type which represents the registration for a given scene accessory. _(beta)_
