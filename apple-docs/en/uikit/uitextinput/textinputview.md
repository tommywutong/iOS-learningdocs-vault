---
title: textInputView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinput/textinputview
source_url: 'https://developer.apple.com/documentation/uikit/uitextinput/textinputview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinput/textinputview.json'
content_hash: 'sha256:0204d0b7601a4c99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInput](../uitextinput.md)

# textInputView

<sub>Instance Property</sub>

An affiliated view that provides a coordinate system for all geometric values in the protocol.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var textInputView: UIView { get }
```

## Discussion

The view that both draws the text and provides a coordinate system for all geometric values in this protocol. (This is typically an instance of the [UITextInput](../uitextinput.md)-adopting class.) If this property is unimplemented, the first view in the responder chain is selected.
