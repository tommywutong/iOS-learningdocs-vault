---
title: textInput
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextselectiondisplayinteraction/textinput
source_url: 'https://developer.apple.com/documentation/uikit/uitextselectiondisplayinteraction/textinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextselectiondisplayinteraction/textinput.json'
content_hash: 'sha256:dbd4c27ba0565eb3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md)

# textInput

<sub>Instance Property</sub>

The text input object that manages the selection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var textInput: (any UITextInput)? { get }
```

## Discussion

Use this property to refer to the text input view that manages the text selection. You specify this view when you create the [UITextSelectionDisplayInteraction](../uitextselectiondisplayinteraction.md) object.
