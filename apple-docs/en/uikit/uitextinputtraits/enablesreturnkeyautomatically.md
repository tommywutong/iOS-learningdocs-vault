---
title: enablesReturnKeyAutomatically
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/enablesreturnkeyautomatically
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/enablesreturnkeyautomatically'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/enablesreturnkeyautomatically.json'
content_hash: 'sha256:3cd6a2db42e8b2fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# enablesReturnKeyAutomatically

<sub>Instance Property</sub>

A Boolean value that indicates whether the system automatically enables the Return key when the user enters text.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var enablesReturnKeyAutomatically: Bool { get set }
```

## Discussion

The default value for this property is [false](../../swift/false.md). If you set it to [true](../../swift/true.md), the keyboard disables the Return key when the text entry area contains no text. As soon as the user enters some text, the Return key is automatically enabled.

## See Also

### Managing the keyboard behavior

- [secureTextEntry](issecuretextentry.md) — A Boolean value that indicates whether a text object disables copying, and in some cases, prevents recording/broadcasting and also hides the text.
