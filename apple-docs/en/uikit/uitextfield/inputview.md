---
title: inputView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/inputview
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/inputview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/inputview.json'
content_hash: 'sha256:7307e8129d0359b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# inputView

<sub>Instance Property</sub>

The custom input view to display when the text field becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var inputView: UIView? { get set }
```

## Discussion

If the value in this property is `nil`, the text field displays the standard system keyboard when it becomes first responder. Assigning a custom view to this property causes that view to be presented instead.

The default value of this property is `nil`.

## See Also

### Replacing the system input views

- [inputAccessoryView](inputaccessoryview.md) — The custom accessory view to display when the text field becomes the first responder.
