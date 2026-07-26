---
title: 'init(textInput:delegate:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextselectiondisplayinteraction/init(textinput:delegate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/init(textinput:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction/init%28textinput%3Adelegate%3A%29.json'
content_hash: 'sha256:0159ea6cb9e7a3fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md)

# init(textInput:delegate:)

<sub>Initializer</sub>

Creates a new text selection display interaction object for the specified text view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(textInput: any UITextInput, delegate: any UITextSelectionDisplayInteractionDelegate)
```

## Parameters

- `textInput` — The text input view that receives this interaction view.

- `delegate` — An optional delegate object to manage the selection UI views.
