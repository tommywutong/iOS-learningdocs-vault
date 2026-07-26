---
title: action
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/action
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/action.json'
content_hash: 'sha256:26d8aa6027ff5d1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# action

<sub>Instance Property</sub>

The command’s action-method selector.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var action: Selector? { get }
```

## See Also

### Getting information about the key command

- [title](title.md) — The key command’s title.
- [image](image.md) — The key command’s image.
- [input](input.md) — The string of characters corresponding to the keys that must be pressed to match this key command.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags that must be pressed to match this key command.
- [UIKeyModifierFlags](../uikeymodifierflags.md) — Constants that indicate which modifier keys are pressed.
- [discoverabilityTitle](discoverabilitytitle.md) — An elaborated title that explains the purpose of the key command.
- [attributes](attributes.md) — The attributes indicating the style of the key command.
- [state](state.md) — The state of the key command.
