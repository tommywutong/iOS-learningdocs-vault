---
title: inputView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiinputviewcontroller/inputview
source_url: 'https://developer.apple.com/documentation/uikit/uiinputviewcontroller/inputview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiinputviewcontroller/inputview.json'
content_hash: 'sha256:d7a5bfd08083cc1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIInputViewController](../uiinputviewcontroller.md)

# inputView

<sub>Instance Property</sub>

The primary view for the input view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var inputView: UIInputView? { get set }
```

## Discussion

When you use an input view controller subclass as the primary view controller for a custom keyboard, this property’s [UIInputView](../uiinputview.md) object is initially empty. To display your keyboard’s user interface, add controls and views to the [inputView](inputview.md) property.
