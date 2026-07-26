---
title: delegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinteraction/delegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextinteraction/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinteraction/delegate.json'
content_hash: 'sha256:04c951660968eece'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInteraction](../uitextinteraction.md)

# delegate

<sub>Instance Property</sub>

The object that receives events from the text interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var delegate: (any UITextInteractionDelegate)? { get set }
```

## See Also

### Handling text input and interaction events

- [textInput](textinput.md) — The object that interacts with the text input system.
- [UITextInteractionDelegate](../uitextinteractiondelegate.md) — An interface that an object implements to receive information about text interaction events.
