---
title: image
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeycommand/image
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/image'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/image.json'
content_hash: 'sha256:6dc1949696b00f31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# image

<sub>Instance Property</sub>

The key command’s image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var image: UIImage? { get set }
```

## Discussion

Only the [contextSystem](../uimenusystem/context.md) command system supports the display of an image, and only when the app is running in iOS.

## See Also

### Getting information about the key command

- [title](title.md) — The key command’s title.
- [input](input.md) — The string of characters corresponding to the keys that must be pressed to match this key command.
- [action](action.md) — The command’s action-method selector.
- [modifierFlags](modifierflags.md) — The bit mask of modifier flags that must be pressed to match this key command.
- [UIKeyModifierFlags](../uikeymodifierflags.md) — Constants that indicate which modifier keys are pressed.
- [discoverabilityTitle](discoverabilitytitle.md) — An elaborated title that explains the purpose of the key command.
- [attributes](attributes.md) — The attributes indicating the style of the key command.
- [state](state.md) — The state of the key command.
