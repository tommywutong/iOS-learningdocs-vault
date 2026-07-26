---
title: UIStatusBarManager
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistatusbarmanager
source_url: 'https://developer.apple.com/documentation/uikit/uistatusbarmanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistatusbarmanager.json'
content_hash: 'sha256:52c784833d38d750'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIStatusBarManager

<sub>Class</sub>

An object that describes the configuration of the status bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIStatusBarManager
```

## Overview

Use a [UIStatusBarManager](uistatusbarmanager.md) object to get the current configuration of the status bar for its associated scene. You don’t create [UIStatusBarManager](uistatusbarmanager.md) objects directly. Instead, you retrieve an existing object from the [statusBarManager](uiwindowscene/statusbarmanager.md) property of a [UIWindowScene](uiwindowscene.md) object.

You don’t use this object to modify the configuration of the status bar. Instead, you set the status bar configuration individually for each of your [UIViewController](uiviewcontroller.md) objects. For example, to modify the default visibility of the status bar, override the [prefersStatusBarHidden](uiviewcontroller/prefersstatusbarhidden.md) property of your view controller.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting the status bar configuration

- [statusBarHidden](uistatusbarmanager/isstatusbarhidden.md) — A Boolean value that indicates whether the status bar is currently hidden.
- [statusBarStyle](uistatusbarmanager/statusbarstyle.md) — The current appearance of the status bar.

### Getting the frame rectangle

- [statusBarFrame](uistatusbarmanager/statusbarframe.md) — The frame rectangle of the status bar.

## See Also

### Device environment

- [UIDevice](uidevice.md) — A representation of the current device.
