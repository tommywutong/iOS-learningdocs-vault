---
title: UIFocusSystem
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uifocussystem
source_url: 'https://developer.apple.com/documentation/uikit/uifocussystem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uifocussystem.json'
content_hash: 'sha256:15ebfe6e96bfa1ce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIFocusSystem

<sub>Class</sub>

Queries and reevaluates the currently focused item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIFocusSystem
```

## Overview

Use a [UIFocusSystem](uifocussystem.md) object to obtain the focus-related state for the objects of your app. You can get state information for your app’s views, view controllers, windows, and other objects that adopt the [UIFocusEnvironment](uifocusenvironment.md) protocol. The [UIFocusSystem](uifocussystem.md) object lists the currently focused item, if any, for a window or view hierarchy. You can use it to force the system to update the focus state, and you can register custom sounds to be played during focus changes.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Getting a focus system object

- [+ focusSystemForEnvironment:](<uifocussystem/init(for_).md>) — Retrieves a focus system object that contains the state information for the specified object. _(deprecated)_

### Getting the currently focused item

- [focusedItem](uifocussystem/focuseditem.md) — The item that’s currently focused.

### Managing focus updates

- [- requestFocusUpdateToEnvironment:](<uifocussystem/requestfocusupdate(to_).md>) — Submits a request to update the focus state of the specified object.
- [- updateFocusIfNeeded](<uifocussystem/updatefocusifneeded().md>) — Forces the system to act on a pending focus update for the current environment.

### Registering custom sounds

- [+ registerURL:forSoundIdentifier:](<uifocussystem/register(__forsoundidentifier_).md>) — Registers the specified sound file with the focus engine.

### Responding to focus-related keys and notifications

- [UIFocusUpdateAnimationCoordinatorKey](uifocussystem/animationcoordinatoruserinfokey.md) — Updates the animation coordinator.
- [UIFocusDidUpdateNotification](uifocussystem/didupdatenotification.md) — The focus for the UI has been updated.
- [UIFocusUpdateContextKey](uifocussystem/focusupdatecontextuserinfokey.md) — Updates the context key.
- [UIFocusMovementDidFailNotification](uifocussystem/movementdidfailnotification.md) — The focus failed to move to another item.

### Structures

- [DidUpdateMessage](uifocussystem/didupdatemessage.md)
- [MovementDidFailMessage](uifocussystem/movementdidfailmessage.md)

### Initializers

- [init(forEnvironment:)](<uifocussystem/init(forenvironment_).md>) _(deprecated)_

### Type Methods

- [focusSystem(for:)](<uifocussystem/focussystem(for_)-5htbd.md>)
- [focusSystem(for:)](<uifocussystem/focussystem(for_)-7tm2f.md>)

## See Also

### Focus interactions

- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [About focus interactions for Apple TV](about-focus-interactions-for-apple-tv.md) — Design and implement intuitive control schemes for menus and interactive user interface layouts.
- [Adding user-focusable elements to a tvOS app](adding-user-focusable-elements-to-a-tvos-app.md) — Create intuitive and easily manipulated user-interactive controls for your tvOS app.
- [UIFocusEnvironment](uifocusenvironment.md) — A set of methods that define the focus behavior for a branch of the view hierarchy.
- [UIFocusUpdateContext](uifocusupdatecontext.md) — An object that provides information relevant to a specific focus update from one view to another.
- [UIFocusItem](uifocusitem.md) — An object that can become focused.
- [UIFocusMovementHint](uifocusmovementhint.md) — Provides movement hint information for the focused item.
- [UIFocusItemContainer](uifocusitemcontainer.md) — The container responsible for providing geometric context to focus items within a given focus environment.
- [UIFocusItemScrollableContainer](uifocusitemscrollablecontainer.md) — A type of focus item container that supports automatic scrolling of focusable content.
- [UIFocusGroupPriority](uifocusgrouppriority.md) — The importance of an item within a focus group, used by the focus system to determine the group’s primary item.
