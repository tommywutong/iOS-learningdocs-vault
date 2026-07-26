---
title: inputView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/inputview
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/inputview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/inputview.json'
content_hash: 'sha256:15010176f3dbab67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# inputView

<sub>Instance Property</sub>

The custom input view to display when the responder becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var inputView: UIView? { get }
```

## Discussion

This property is typically used to provide a view to replace the system-supplied keyboard that’s presented for [UITextField](../uitextfield.md) and [UITextView](../uitextview.md) objects.

The value of this read-only property is `nil`. A responder object that requires a custom view to gather input from the user should redeclare this property as read-write and use it to manage its custom input view. When the responder becomes the first responder, the responder infrastructure presents the specified input view automatically. Similarly, when the responder resigns its first responder status, the responder infrastructure automatically dismisses the specified input view.

## See Also

### Managing input views

- [inputViewController](inputviewcontroller.md) — The custom input view controller to use when the responder becomes the first responder.
- [inputAccessoryView](inputaccessoryview.md) — The custom input accessory view to display when the responder becomes the first responder.
- [inputAccessoryViewController](inputaccessoryviewcontroller.md) — The custom input accessory view controller to display when the responder becomes the first responder.
- [- reloadInputViews](<reloadinputviews().md>) — Updates the custom input and accessory views when the object is the first responder.
