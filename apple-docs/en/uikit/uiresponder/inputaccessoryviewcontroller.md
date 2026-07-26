---
title: inputAccessoryViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/inputaccessoryviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/inputaccessoryviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/inputaccessoryviewcontroller.json'
content_hash: 'sha256:bc1d8ed5b53fdff8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# inputAccessoryViewController

<sub>Instance Property</sub>

The custom input accessory view controller to display when the responder becomes the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var inputAccessoryViewController: UIInputViewController? { get }
```

## Discussion

This property is typically used to attach an accessory view controller to the system-supplied keyboard that’s presented for [UITextField](../uitextfield.md) and [UITextView](../uitextview.md) objects.

The value of this read-only property is `nil`. If you want to attach custom controls to a system-supplied input view controller (such as the system keyboard) or to a custom input view (one you provide in the [inputViewController](inputviewcontroller.md) property), redeclare this property as read-write in a [UIResponder](../uiresponder.md) subclass. You can then use this property to manage a custom accessory view. When the responder becomes the first responder, the responder infrastructure attaches the accessory view to the appropriate input view before displaying it.

## See Also

### Managing input views

- [inputView](inputview.md) — The custom input view to display when the responder becomes the first responder.
- [inputViewController](inputviewcontroller.md) — The custom input view controller to use when the responder becomes the first responder.
- [inputAccessoryView](inputaccessoryview.md) — The custom input accessory view to display when the responder becomes the first responder.
- [- reloadInputViews](<reloadinputviews().md>) — Updates the custom input and accessory views when the object is the first responder.
