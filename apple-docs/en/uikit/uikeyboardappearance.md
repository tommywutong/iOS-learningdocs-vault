---
title: UIKeyboardAppearance
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uikeyboardappearance
source_url: 'https://developer.apple.com/documentation/uikit/uikeyboardappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeyboardappearance.json'
content_hash: 'sha256:b2ad079edec6d9e5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIKeyboardAppearance

<sub>Enumeration</sub>

Constants that specify the appearance of the keyboard for a text-based view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIKeyboardAppearance
```

## Overview

Use these constants with the [keyboardAppearance](uitextinputtraits/keyboardappearance.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UIKeyboardAppearanceDefault](uikeyboardappearance/default.md) — Specifies the default keyboard appearance for the current input method.
- [UIKeyboardAppearanceDark](uikeyboardappearance/dark.md) — Specifies a keyboard appearance suitable for a dark UI look.
- [UIKeyboardAppearanceLight](uikeyboardappearance/light.md) — Specifies a keyboard appearance suitable for a light UI look.
- [UIKeyboardAppearanceAlert](uikeyboardappearance/alert.md) — Specifies a keyboard appearance suitable for an alert panel. _(deprecated)_

### Initializers

- [init(rawValue:)](<uikeyboardappearance/init(rawvalue_).md>)

## See Also

### Configuring the keyboard appearance

- [keyboardType](uitextinputtraits/keyboardtype.md) — The keyboard type for the text object.
- [UIKeyboardType](uikeyboardtype.md) — Constants that specify the type of keyboard to display for a text-based view.
- [keyboardAppearance](uitextinputtraits/keyboardappearance.md) — The appearance style of the keyboard for the text object.
- [returnKeyType](uitextinputtraits/returnkeytype.md) — The visible indication of what the Return key does.
- [UIReturnKeyType](uireturnkeytype.md) — Constants that specify the type of Return key the keyboard displays.
- [textContentType](uitextinputtraits/textcontenttype.md) — The semantic meaning for a text input area.
- [UITextContentType](uitextcontenttype.md) — Constants that identify the semantic meaning for a text-entry area.
