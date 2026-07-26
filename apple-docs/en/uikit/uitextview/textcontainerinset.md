---
title: textContainerInset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextview/textcontainerinset
source_url: 'https://developer.apple.com/documentation/uikit/uitextview/textcontainerinset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextview/textcontainerinset.json'
content_hash: 'sha256:7f277ee9379d2b2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextView](../uitextview.md)

# textContainerInset

<sub>Instance Property</sub>

The inset of the text container’s layout area within the text view’s content area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var textContainerInset: UIEdgeInsets { get set }
```

## Discussion

This property provides text margins for text laid out in the text view. By default the value of this property is `(8, 0, 8, 0)`.

## See Also

### Configuring layout attributes

- [usesStandardTextScaling](usesstandardtextscaling.md) — A Boolean value that determines the rendering scale of the text.
- [sizingRule](../uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
