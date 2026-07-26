---
title: inputAccessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextfield/inputaccessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uitextfield/inputaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextfield/inputaccessoryview.json'
content_hash: 'sha256:f5428df36484d0bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextField](../uitextfield.md)

# inputAccessoryView

<sub>Instance Property</sub>

The custom accessory view to display when the text field becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var inputAccessoryView: UIView? { get set }
```

## Discussion

The default value of this property is `nil`. Assigning a view to this property causes that view to be displayed above the standard system keyboard (or above the custom input view if one is provided) when the text field becomes the first responder. For example, you could use this property to attach a custom toolbar to the keyboard.

## See Also

### Replacing the system input views

- [inputView](inputview.md) — The custom input view to display when the text field becomes the first responder.
