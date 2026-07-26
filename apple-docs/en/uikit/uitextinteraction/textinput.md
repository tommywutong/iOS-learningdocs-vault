---
title: textInput
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinteraction/textinput
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteraction/textinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteraction/textinput.json'
content_hash: 'sha256:46508084d5b32543'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInteraction](../uitextinteraction.md)

# textInput

<sub>Instance Property</sub>

The object that interacts with the text input system.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var textInput: (any UIResponder & UITextInput)? { get set }
```

## Discussion

The object that you assign to [textInput](textinput.md) can be different than the view that contains the text interaction. For example, you may want the gestures for the text interaction to work on a container view, such as a scroll view, while managing the text selection behavior in a contained view, such as the one drawing the text.

## See Also

### Handling text input and interaction events

- [delegate](delegate.md) — The object that receives events from the text interaction.
- [UITextInteractionDelegate](../uitextinteractiondelegate.md) — An interface that an object implements to receive information about text interaction events.
