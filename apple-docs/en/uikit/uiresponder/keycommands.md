---
title: keyCommands
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/keycommands
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/keycommands'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/keycommands.json'
content_hash: 'sha256:52c8608e4a4cc253'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# keyCommands

<sub>Instance Property</sub>

The key commands that trigger actions on this responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var keyCommands: [UIKeyCommand]? { get }
```

## Discussion

A responder object that supports hardware keyboard commands can redefine this property and use it to return an array of [UIKeyCommand](../uikeycommand.md) objects that it supports. Each key command object represents the keyboard sequence to recognize and the action method of the responder to call in response.

The key commands you return from this method are applied to the entire responder chain. When a key combination is pressed that matches a key command object, UIKit walks the responder chain looking for an object that implements the corresponding action method. It calls that method on the first object it finds and then stops processing the event.
