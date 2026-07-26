---
title: discoverabilityTitle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/discoverabilitytitle
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/discoverabilitytitle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/discoverabilitytitle.json'
content_hash: 'sha256:9b6482c886c22547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# discoverabilityTitle

<sub>Instance Property</sub>

An elaborated title that explains the purpose of the key command.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var discoverabilityTitle: String? { get set }
```

## Discussion

The system uses this property to display information about the command. In iOS, the system displays this title in the discoverability heads-up display (HUD). If this property is `nil`, the HUD displays the [title](../uicommand/title.md) property.

In Mac apps built with Mac Catalyst, the system displays the discoverability title as a tooltip.

## See Also

### Getting information about the key command

- [title](title.md) — The key command’s title.
- [image](image.md) — The key command’s image.
- [input](input.md) — The string of characters corresponding to the keys that must be pressed to match this key command.
- [action](action.md) — The command’s action-method selector.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags that must be pressed to match this key command.
- [UIKeyModifierFlags](../uikeymodifierflags.md) — Constants that indicate which modifier keys are pressed.
- [attributes](attributes.md) — The attributes indicating the style of the key command.
- [state](state.md) — The state of the key command.
