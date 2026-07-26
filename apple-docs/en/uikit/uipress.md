---
title: UIPress
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipress
source_url: 'https://developer.apple.com/documentation/uikit/uipress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipress.json'
content_hash: 'sha256:a9ce126f4715e411'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPress

<sub>Class</sub>

An object that represents the presence or movement of a button press on the screen for a particular event.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class UIPress
```

## Overview

The press specifically encapsulates the pressing of some physically actuated button. All of the press types represent actual physical buttons on one of a variety of remotes. You access [UIPress](uipress.md) objects through [UIEvent](uievent.md) objects passed into responder objects for event handling. The [gestureRecognizers](uipress/gesturerecognizers.md) property returns the gesture recognizers — instances of a concrete subclass of [UIGestureRecognizer](uigesturerecognizer.md) — that are currently handling the given button press.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting a press object’s gesture recognizers

- [force](uipress/force.md) — The force of the button press.
- [gestureRecognizers](uipress/gesturerecognizers.md) — The gesture recognizers that are receiving the press.

### Responding to press events

- [responder](uipress/responder.md) — A responder object.

### Getting the press’s location

- [window](uipress/window.md) — The window in which the press initially occurred.

### Getting press attributes

- [key](uipress/key.md) — The key pressed or released on a physical keyboard.
- [type](uipress/type.md) — The type of the specified press.
- [phase](uipress/phase-swift.property.md) — The current press phase of the object.
- [timestamp](uipress/timestamp.md) — The time when the press occurred or when it was last mutated.

### Constants

- [Phase](uipress/phase-swift.enum.md) — Constants that represent the phases of a button press.
- [PressType](uipress/presstype.md) — Constants that represent buttons that a person can press.

## See Also

### Button presses

- [UIPressesEvent](uipressesevent.md) — An event that describes the state of a set of physical buttons that are available to the device, such as those on an associated remote or game controller.
