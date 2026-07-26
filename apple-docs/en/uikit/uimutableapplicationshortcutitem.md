---
title: UIMutableApplicationShortcutItem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutableapplicationshortcutitem
source_url: 'https://developer.apple.com/documentation/uikit/uimutableapplicationshortcutitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutableapplicationshortcutitem.json'
content_hash: 'sha256:b74456c4ef9f6b88'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIMutableApplicationShortcutItem

<sub>Class</sub>

A mutable Home Screen dynamic quick action, which is an item that specifies a configurable user-initiated action for your app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class UIMutableApplicationShortcutItem
```

## Overview

This class is a convenience subclass of [UIApplicationShortcutItem](uiapplicationshortcutitem.md), helping you work with registered, and therefore immutable, quick actions. For information about how to use objects of this class in your app, read the overview in [UIApplicationShortcutItem](uiapplicationshortcutitem.md).

## Relationships

- **Inherits From**: [UIApplicationShortcutItem](uiapplicationshortcutitem.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSMutableCopying](../foundation/nsmutablecopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting a Home Screen dynamic mutable quick action

- [localizedTitle](uimutableapplicationshortcutitem/localizedtitle.md) — The required, user-visible title for the Home Screen dynamic mutable quick action.
- [localizedSubtitle](uimutableapplicationshortcutitem/localizedsubtitle.md) — The optional, user-visible subtitle for the Home Screen dynamic mutable quick action.
- [type](uimutableapplicationshortcutitem/type.md) — A required, app-specific string that you can employ to identify the type of quick action to perform.
- [icon](uimutableapplicationshortcutitem/icon.md) — The optional icon for the Home Screen dynamic mutable quick action.
- [userInfo](uimutableapplicationshortcutitem/userinfo.md) — Optional, app-specific information that you can provide for use when your app performs the Home Screen dynamic mutable quick action.

### Designating the scene to activate

- [targetContentIdentifier](uimutableapplicationshortcutitem/targetcontentidentifier.md) — The object that determines which scene handles the quick action.

## See Also

### Home Screen quick actions

- [Add Home Screen quick actions](add-home-screen-quick-actions.md) — Expose commonly used functionality with static or dynamic 3D Touch Home Screen quick actions.
- [UIApplicationShortcutItem](uiapplicationshortcutitem.md) — An application shortcut item, also called a Home Screen dynamic quick action, that specifies a user-initiated action for your app.
- [UIApplicationShortcutIcon](uiapplicationshortcuticon.md) — An image you can optionally associate with a Home Screen quick action to improve its appearance and usability.
