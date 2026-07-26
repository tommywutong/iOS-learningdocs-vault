---
title: 'init(title:action:modifierFlags:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uicommandalternate/init(title:action:modifierflags:)'
source_url: 'https://developer.apple.com/documentation/uikit/uicommandalternate/init(title:action:modifierflags:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicommandalternate/init%28title%3Aaction%3Amodifierflags%3A%29.json'
content_hash: 'sha256:9e9d64eb58b96318'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UICommandAlternate](../uicommandalternate.md)

# init(title:action:modifierFlags:)

<sub>Initializer</sub>

Creates a command alternative with the specified title, action, and modifier flags.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
convenience init(title: String, action: Selector, modifierFlags: UIKeyModifierFlags)
```

## Parameters

- `title` — The command alternative’s title.

- `action` — The action to take after a person selects the alternative command.

- `modifierFlags` — The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see [UIKeyModifierFlags](../uikeymodifierflags.md).

## Return Value

A command alternative object.

## See Also

### Creating a command alternative

- [- initWithCoder:](<init(coder_).md>) — Creates a command alternative from data in an unarchiver.
