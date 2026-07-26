---
title: UIKey
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikey
source_url: 'https://developer.apple.com/documentation/uikit/uikey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikey.json'
content_hash: 'sha256:9b236133bcedb671'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKey

<sub>Class</sub>

An object that provides information about the state of a keyboard key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor class UIKey
```

## Overview

[UIKey](uikey.md) provides relevant information about the current state of a key on a keyboard as a user presses and releases the key. To learn more, see [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md)

## Topics

### Determining key type

- [keyCode](uikey/keycode.md) — The HID usage code of the key.
- [modifierFlags](uikey/modifierflags.md) — The modifier keys pressed and held while the user presses the key.

### Getting key characters

- [characters](uikey/characters.md) — A string that represents the text value of the key combined with any active modifier keys.
- [charactersIgnoringModifiers](uikey/charactersignoringmodifiers.md) — A string that represents the text value of the key without modifier keys.

### Initializers

- [init(coder:)](<uikey/init(coder_).md>)

## See Also

### Physical keyboards

- [Handling key presses made on a physical keyboard](handling-key-presses-made-on-a-physical-keyboard.md) — Detect when someone presses and releases keys on a physical keyboard.
- [Navigating an app’s user interface using a keyboard](navigating-an-app-s-user-interface-using-a-keyboard.md) — Navigate between user interface elements using a keyboard and focusable UI elements in iPad apps and apps built with Mac Catalyst.
- [Adding hardware keyboard support to your app](adding-hardware-keyboard-support-to-your-app.md) — Enhance interactions with your app by handling raw keyboard events, writing custom keyboard shortcuts, and working with gesture recognizers.
- [UIKeyboardHIDUsage](uikeyboardhidusage.md) — A set of HID usage codes that identify the keys of a USB keyboard.
