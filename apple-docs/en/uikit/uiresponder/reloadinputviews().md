---
title: reloadInputViews()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiresponder/reloadinputviews()
source_url: 'https://developer.apple.com/documentation/uikit/uiresponder/reloadinputviews()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiresponder/reloadinputviews%28%29.json'
content_hash: 'sha256:f22909a38fc3cd99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIResponder](../uiresponder.md)

# reloadInputViews()

<sub>Instance Method</sub>

Updates the custom input and accessory views when the object is the first responder.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func reloadInputViews()
```

## Discussion

You can use this method to refresh the custom input view or input accessory view associated with the current object when it’s the first responder. The views are replaced immediately, without animating them into place. If the current object isn’t the first responder, this method has no effect.

## See Also

### Managing input views

- [inputView](inputview.md) — The custom input view to display when the responder becomes the first responder.
- [inputViewController](inputviewcontroller.md) — The custom input view controller to use when the responder becomes the first responder.
- [inputAccessoryView](inputaccessoryview.md) — The custom input accessory view to display when the responder becomes the first responder.
- [inputAccessoryViewController](inputaccessoryviewcontroller.md) — The custom input accessory view controller to display when the responder becomes the first responder.
