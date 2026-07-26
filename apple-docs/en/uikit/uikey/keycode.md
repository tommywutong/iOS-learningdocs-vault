---
title: keyCode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.4+, iPadOS 13.4+, Mac Catalyst 13.4+, tvOS 13.4+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikey/keycode
source_url: 'https://developer.apple.com/documentation/uikit/uikey/keycode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikey/keycode.json'
content_hash: 'sha256:4f85748b40c7d310'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKey](../uikey.md)

# keyCode

<sub>Instance Property</sub>

The HID usage code of the key.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var keyCode: UIKeyboardHIDUsage { get }
```

## Discussion

Use this property to determine the HID (Human Interface Device) usage code that identifies the key of a USB (Universal Serial Bus) keyboard. For a list of HID usage codes, see [UIKeyboardHIDUsage](../uikeyboardhidusage.md).

Due to the variation of keyboards from language to language, it isn’t feasible to specify exact key mappings for every language. Where the HID usage code list isn’t specific for a key in a particular language, the keyboard firmware uses the closest equivalent key position so manufacturers can produce keyboards for different languages by simply printing different keycaps.

One example is the Y key on a North American keyboard. In Germany, the Z key typically occupies the Y key position. Rather than changing the keyboard firmware to put the Z usage code into that place in the descriptor list, the vendor uses the Y usage code on both the North American and German keyboards.

Because the key mapping may not be exact, use [charactersIgnoringModifiers](charactersignoringmodifiers.md) instead of [keyCode](keycode.md) to determine the text value of the key.

## See Also

### Determining key type

- [modifierFlags](modifierflags.md) — The modifier keys pressed and held while the user presses the key.
