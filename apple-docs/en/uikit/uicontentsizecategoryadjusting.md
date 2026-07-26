---
title: UIContentSizeCategoryAdjusting
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategoryadjusting
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategoryadjusting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategoryadjusting.json'
content_hash: 'sha256:eb1b033cd58cdeab'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIContentSizeCategoryAdjusting

<sub>Protocol</sub>

A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIContentSizeCategoryAdjusting : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [UILabel](uilabel.md), [UISearchTextField](uisearchtextfield.md), [UITextField](uitextfield.md), [UITextView](uitextview.md)

## Topics

### Adjusting the size of fonts

- [adjustsFontForContentSizeCategory](uicontentsizecategoryadjusting/adjustsfontforcontentsizecategory.md) — A Boolean that indicates whether the object automatically updates its font when the device’s content size category changes.

## See Also

### Managing the preferred content size

- [preferredContentSizeCategory](uiapplication/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [UIContentSizeCategory](uicontentsizecategory.md) — Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryDidChangeNotification](uicontentsizecategory/didchangenotification.md) — A notification that posts when the user changes the preferred content size setting.
- [UIContentSizeCategoryNewValueKey](uicontentsizecategory/newvalueuserinfokey.md) — A key that reflects the new preferred content size.
