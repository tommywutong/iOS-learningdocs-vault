---
title: UIKeyModifierFlags
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeymodifierflags
source_url: 'https://developer.apple.com/documentation/uikit/uikeymodifierflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeymodifierflags.json'
content_hash: 'sha256:35cd575f12441ea4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyModifierFlags

<sub>Structure</sub>

Constants that indicate which modifier keys are pressed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UIKeyModifierFlags
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Modifier flags

- [UIKeyModifierAlphaShift](uikeymodifierflags/alphashift.md) — A modifier flag that indicates the user pressed the Caps Lock key.
- [UIKeyModifierShift](uikeymodifierflags/shift.md) — A modifier flag that indicates the user pressed the Shift key.
- [UIKeyModifierControl](uikeymodifierflags/control.md) — A modifier flag that indicates the user pressed the Control key.
- [UIKeyModifierAlternate](uikeymodifierflags/alternate.md) — A modifier flag that indicates the user pressed the Option key.
- [UIKeyModifierCommand](uikeymodifierflags/command.md) — A modifier flag that indicates the user pressed the Command key.
- [UIKeyModifierNumericPad](uikeymodifierflags/numericpad.md) — A modifier flag that indicates the user pressed a key located on the numeric keypad.

### Initializers

- [init(rawValue:)](<uikeymodifierflags/init(rawvalue_).md>) — Creates a modifier-flags structure from data in an unarchiver.

## See Also

### Getting information about the key command

- [title](uikeycommand/title.md) — The key command’s title.
- [image](uikeycommand/image.md) — The key command’s image.
- [input](uikeycommand/input.md) — The string of characters corresponding to the keys that must be pressed to match this key command.
- [action](uikeycommand/action.md) — The command’s action-method selector.
- [modifierFlags](uikeycommand/modifierflags.md) — The bit mask of modifier flags that must be pressed to match this key command.
- [discoverabilityTitle](uikeycommand/discoverabilitytitle.md) — An elaborated title that explains the purpose of the key command.
- [attributes](uikeycommand/attributes.md) — The attributes indicating the style of the key command.
- [state](uikeycommand/state.md) — The state of the key command.
