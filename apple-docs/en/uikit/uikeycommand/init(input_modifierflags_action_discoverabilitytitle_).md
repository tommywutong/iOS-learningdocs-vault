---
title: 'init(input:modifierFlags:action:discoverabilityTitle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uikeycommand/init(input:modifierflags:action:discoverabilitytitle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uikeycommand/init(input:modifierflags:action:discoverabilitytitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uikeycommand/init%28input%3Amodifierflags%3Aaction%3Adiscoverabilitytitle%3A%29.json'
content_hash: 'sha256:5f249800b6ca7841'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIKeyCommand](../uikeycommand.md)

# init(input:modifierFlags:action:discoverabilityTitle:)

<sub>Initializer</sub>

Creates a key command object that matches the specified input and has a title.

> [!warning] Deprecated
> Use [+ keyCommandWithInput:modifierFlags:action:](<init(input_modifierflags_action_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
convenience init(input: String, modifierFlags: UIKeyModifierFlags, action: Selector, discoverabilityTitle: String)
```

## Parameters

- `input` — The keys that a person must press. The string must contain one or more characters corresponding to the keys a person pressed. For a list of special characters that don’t have a textual representation, see [Input strings for special keys](../input-strings-for-special-keys.md).

- `modifierFlags` — The bit mask of modifier keys that a person must press. You can use this parameter to specify which modifier keys (Command, Option, and so on) a person must also press. You may specify more than one modifier key. For a list of possible values, see [UIKeyModifierFlags](../uikeymodifierflags.md).

- `action` — The action method to execute on the responder object.

- `discoverabilityTitle` — An elaborated title that explains the purpose of the key command.

## Return Value

The initialized key command object.

## Discussion

After creating a key command object, you can add it to a view controller using the [- addKeyCommand:](<../uiviewcontroller/addkeycommand(__).md>) method of the view controller. You can also override any responder class and return the key command directly from the responder’s [keyCommands](../uiresponder/keycommands.md) property.
