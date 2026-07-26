---
title: didChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uicontentsizecategory/didchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uicontentsizecategory/didchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uicontentsizecategory/didchangenotification.json'
content_hash: 'sha256:2350a1c88fecdb5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIContentSizeCategory](../uicontentsizecategory.md)

# didChangeNotification

<sub>Type Property</sub>

A notification that posts when the user changes the preferred content size setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated static let didChangeNotification: NSNotification.Name
```

## Discussion

This notification is sent when the value in the [preferredContentSizeCategory](../uiapplication/preferredcontentsizecategory.md) property changes. The `userInfo` dictionary of the notification contains the [UIContentSizeCategoryNewValueKey](newvalueuserinfokey.md) key, which reflects the new setting.

## See Also

### Managing the preferred content size

- [preferredContentSizeCategory](../uiapplication/preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [UIContentSizeCategory](../uicontentsizecategory.md) — Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryAdjusting](../uicontentsizecategoryadjusting.md) — A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [UIContentSizeCategoryNewValueKey](newvalueuserinfokey.md) — A key that reflects the new preferred content size.
