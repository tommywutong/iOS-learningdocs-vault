---
title: UILetterformAwareAdjusting
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiletterformawareadjusting
source_url: 'https://developer.apple.com/documentation/uikit/uiletterformawareadjusting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiletterformawareadjusting.json'
content_hash: 'sha256:8e797fb4b49f66ca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UILetterformAwareAdjusting

<sub>Protocol</sub>

The typographic bounds-sizing behavior to handle text with fonts that contain oversize characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UILetterformAwareAdjusting : NSObjectProtocol
```

## Overview

In [UILabel](uilabel.md), [UITextField](uitextfield.md), or a nonscrollable [UITextView](uitextview.md), [- sizeThatFits:](<uiview/sizethatfits(__).md>) and [intrinsicContentSize](uiview/intrinsiccontentsize.md) increase the height calculated for tall scripts when you present text that contains oversize characters in a font that you create with  [+ preferredFontForTextStyle:](<uifont/preferredfont(fortextstyle_).md>). Even with the increase, some extreme ascenders and descenders may extend beyond the view’s bounds and appear to be clipped. For nontext-style fonts, [- sizeThatFits:](<uiview/sizethatfits(__).md>) and [intrinsicContentSize](uiview/intrinsiccontentsize.md) don’t increase the calculated height for oversize characters. This is the default, standard behavior. Set [sizingRule](uiletterformawareadjusting/sizingrule.md) to [UILetterformAwareSizingRuleTypographic](uiletterformawaresizingrule/typographic.md) to use this behavior explicitly.

To adjust the boundary calculations in [- sizeThatFits:](<uiview/sizethatfits(__).md>) and [intrinsicContentSize](uiview/intrinsiccontentsize.md) to account for oversize characters, set [sizingRule](uiletterformawareadjusting/sizingrule.md) to [UILetterformAwareSizingRuleOversize](uiletterformawaresizingrule/oversize.md). Note that the larger bounds to accommodate oversize characters may negatively impact typographic alignment, such as vertical edge alignment, vertical edge-to-edge spacing, or vertical centering.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UILabel](uilabel.md), [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Specifying text-sizing behavior

- [sizingRule](uiletterformawareadjusting/sizingrule.md) — The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
- [UILetterformAwareSizingRule](uiletterformawaresizingrule.md) — Constants that specify typographic bounds-sizing behavior to handle text in fonts with oversize characters.
