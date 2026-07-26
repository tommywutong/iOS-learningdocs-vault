---
title: UIPointerInteraction
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerinteraction
source_url: 'https://developer.apple.com/documentation/uikit/uipointerinteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerinteraction.json'
content_hash: 'sha256:de8aafd347f55fd8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPointerInteraction

<sub>Class</sub>

An interaction that enables support for effects on a view or customizes the pointer’s appearance within a region of an app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UIPointerInteraction
```

## Overview

If you use a [UIButton](uibutton.md) as an interface object, use the button’s [pointerInteractionEnabled](uibutton/ispointerinteractionenabled.md) and [pointerStyleProvider](uibutton/pointerstyleprovider-1d4d2.md) to customize the proposed effect before constructing your own custom pointer effect using a [UIPointerInteraction](uipointerinteraction.md).

> [!note] Note
> In iPadOS, the visual interactions when using mouse or trackpad input versus Apple Pencil input are slightly different: For example, pointer styles such as the system pointer aren’t visible while using Apple Pencil. However, both input devices support effect-based pointers, but have a slightly different visual appearance depending on which device is in use.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [UIInteraction](uiinteraction.md)

## Topics

### Create pointer interactions

- [- initWithDelegate:](<uipointerinteraction/init(delegate_).md>) — Initializes a pointer interaction object with a specified delegate object.

### Manage pointer interactions

- [delegate](uipointerinteraction/delegate.md) — An object that responds to pointer movements.
- [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) — An interface for handling pointer movements within the interaction’s view.

### Activate pointer interactions

- [enabled](uipointerinteraction/isenabled.md) — A Boolean value that indicates whether the pointer interaction is an enabled state.

### Trigger a pointer update

- [- invalidate](<uipointerinteraction/invalidate().md>) — Causes the interaction to update the pointer in response to an event.

## See Also

### Essentials

- [UIPointerInteractionDelegate](uipointerinteractiondelegate.md) — An interface for handling pointer movements within the interaction’s view.
- [Integrating pointer interactions into your iPad app](integrating-pointer-interactions-into-your-ipad-app.md) — Support touch interactions in your iPad app by adding pointer interactions to your views.
- [Enhancing your iPad app with pointer interactions](enhancing-your-ipad-app-with-pointer-interactions.md) — Provide a great user experience with pointing devices, by incorporating pointer content effects and shape customizations.
