---
title: modifierFlags
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/modifierflags
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/modifierflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/modifierflags.json'
content_hash: 'sha256:858364a063a23243'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# modifierFlags

<sub>Instance Property</sub>

The bit mask of modifier flags that must be pressed to match this key command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var modifierFlags: UIKeyModifierFlags { get }
```

## See Also

### Getting information about the key command

- [title](title.md) — The key command’s title.
- [image](image.md) — The key command’s image.
- [input](input.md) — The string of characters corresponding to the keys that must be pressed to match this key command.
- [action](action.md) — The command’s action-method selector.
- [UIKeyModifierFlags](../uikeymodifierflags.md) — Constants that indicate which modifier keys are pressed.
- [discoverabilityTitle](discoverabilitytitle.md) — An elaborated title that explains the purpose of the key command.
- [attributes](attributes.md) — The attributes indicating the style of the key command.
- [state](state.md) — The state of the key command.
