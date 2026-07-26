---
title: isSecureTextEntry
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/issecuretextentry
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/issecuretextentry'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/issecuretextentry.json'
content_hash: 'sha256:e36196b71a06f3c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# isSecureTextEntry

<sub>Instance Property</sub>

A Boolean value that indicates whether a text object disables copying, and in some cases, prevents recording/broadcasting and also hides the text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var isSecureTextEntry: Bool { get set }
```

## Discussion

This property is set to [false](../../swift/false.md) by default. Setting this property to [true](../../swift/true.md) in any view that conforms to [UITextInputTraits](../uitextinputtraits.md) disables the user’s ability to copy the text in the view and, in some cases, also disables the user’s ability to record and broadcast the text in the view.

Setting this property to [true](../../swift/true.md) in a [UITextField](../uitextfield.md) object additionally enables a password-style experience, in which the text being entered is obscured.

## See Also

### Managing the keyboard behavior

- [enablesReturnKeyAutomatically](enablesreturnkeyautomatically.md) — A Boolean value that indicates whether the system automatically enables the Return key when the user enters text.
