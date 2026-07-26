---
title: inputViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/inputviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/inputviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/inputviewcontroller.json'
content_hash: 'sha256:fa34b5a6cd78ad64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# inputViewController

<sub>Instance Property</sub>

The custom input view controller to use when the responder becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var inputViewController: UIInputViewController? { get }
```

## Discussion

This property is typically used to provide a view controller to replace the system-supplied keyboard that’s presented for [UITextField](../uitextfield.md) and [UITextView](../uitextview.md) objects.

The value of this read-only property is `nil`. If you want to provide a custom input view controller to replace the system keyboard in your app, redeclare this property as read-write in a [UIResponder](../uiresponder.md) subclass. You can then use this property to manage a custom input view controller. When the responder becomes the first responder, the responder infrastructure presents the specified input view controller automatically. Similarly, when the responder resigns its first responder status, the responder infrastructure automatically dismisses the specified input view controller.

## See Also

### Managing input views

- [inputView](inputview.md) — The custom input view to display when the responder becomes the first responder.
- [inputAccessoryView](inputaccessoryview.md) — The custom input accessory view to display when the responder becomes the first responder.
- [inputAccessoryViewController](inputaccessoryviewcontroller.md) — The custom input accessory view controller to display when the responder becomes the first responder.
- [- reloadInputViews](<reloadinputviews().md>) — Updates the custom input and accessory views when the object is the first responder.
