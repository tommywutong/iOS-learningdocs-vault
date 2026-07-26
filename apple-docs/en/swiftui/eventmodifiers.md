---
title: EventModifiers
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/eventmodifiers
source_url: 'https://developer.apple.com/documentation/swiftui/eventmodifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/eventmodifiers.json'
content_hash: 'sha256:25b8cbcf469cd0f4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# EventModifiers

<sub>Structure</sub>

A set of key modifiers that you can add to a gesture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen struct EventModifiers
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Copyable](../swift/copyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting modifier keys

- [all](eventmodifiers/all.md) — All possible modifier keys.
- [capsLock](eventmodifiers/capslock.md) — The Caps Lock key.
- [command](eventmodifiers/command.md) — The Command key.
- [control](eventmodifiers/control.md) — The Control key.
- [numericPad](eventmodifiers/numericpad.md) — Any key on the numeric keypad.
- [option](eventmodifiers/option.md) — The Option key.
- [shift](eventmodifiers/shift.md) — The Shift key.

### Creating a set of options

- [init(rawValue:)](<eventmodifiers/init(rawvalue_).md>) — Creates a new set from a raw value.
- [rawValue](eventmodifiers/rawvalue.md) — The raw value.

### Deprecated modifiers

- [function](eventmodifiers/function.md) — The Function key. _(deprecated)_

## See Also

### Creating keyboard shortcuts

- [keyboardShortcut(_:)](<view/keyboardshortcut(__).md>) — Assigns a keyboard shortcut to the modified control.
- [keyboardShortcut(_:modifiers:)](<view/keyboardshortcut(__modifiers_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut(_:modifiers:localization:)](<view/keyboardshortcut(__modifiers_localization_).md>) — Defines a keyboard shortcut and assigns it to the modified control.
- [keyboardShortcut](environmentvalues/keyboardshortcut.md) — The keyboard shortcut that buttons in this environment will be triggered with.
- [KeyboardShortcut](keyboardshortcut.md) — Keyboard shortcuts describe combinations of keys on a keyboard that the user can press in order to activate a button or toggle.
- [KeyEquivalent](keyequivalent.md) — Key equivalents consist of a letter, punctuation, or function key that can be combined with an optional set of modifier keys to specify a keyboard shortcut.
