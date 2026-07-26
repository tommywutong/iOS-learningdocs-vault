---
title: newValueUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategory/newvalueuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategory/newvalueuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategory/newvalueuserinfokey.json'
content_hash: 'sha256:57a7c2bdd8957e77'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentSizeCategory](../uicontentsizecategory.md)

# newValueUserInfoKey

<sub>Type Property</sub>

A key that reflects the new preferred content size.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let newValueUserInfoKey: String
```

## Discussion

This key’s value is an [NSString](../../foundation/nsstring.md) object that reflects the new value of the [preferredContentSizeCategory](../uiapplication/preferredcontentsizecategory.md) property.

## See Also

### Managing the preferred content size

- [preferredContentSizeCategory](../uiapplication/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [UIContentSizeCategory](../uicontentsizecategory.md) — Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryAdjusting](../uicontentsizecategoryadjusting.md) — A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [UIContentSizeCategoryDidChangeNotification](didchangenotification.md) — A notification that posts when the user changes the preferred content size setting.
