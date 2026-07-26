---
title: inputDelegate
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/inputdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/inputdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/inputdelegate.json'
content_hash: 'sha256:35155814150dbbea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# inputDelegate

<sub>Instance Property</sub>

An input delegate that receives a notification when text changes or when the selection changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var inputDelegate: (any UITextInputDelegate)? { get set }
```

## Discussion

The text input system automatically assigns a delegate to this property at runtime. It is the responsibility of the view that adopts the [UITextInput](../uitextinput.md) protocol to notify the input delegate at the appropriate junctures.

## See Also

### Handling text input

- [UITextInputDelegate](../uitextinputdelegate.md) — An intermediary between a document and the text input system.
