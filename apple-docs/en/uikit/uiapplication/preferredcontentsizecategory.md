---
title: preferredContentSizeCategory
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiapplication/preferredcontentsizecategory
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/preferredcontentsizecategory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/preferredcontentsizecategory.json'
content_hash: 'sha256:b0e252a25109c139'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# preferredContentSizeCategory

<sub>Instance Property</sub>

The font sizing option preferred by the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredContentSizeCategory: UIContentSizeCategory { get }
```

## Discussion

Users can request that apps display fonts in a size that is larger or smaller than the normal font size defined by the system. For example, a user with a visual impairment might request a larger default font size to make it easier to read text. Font objects returned by the system automatically scale based on the user’s preference. You can use the value of this property to request a font object of the appropriate size.

When the value of this property changes, the app object sends a [UIContentSizeCategoryDidChangeNotification](../uicontentsizecategory/didchangenotification.md) notification so that observers can respond accordingly.

For a list of possible values, see `Content Size Category Constants` and `Accessibility Content Size Category Constants`.

## See Also

### Managing the preferred content size

- [UIContentSizeCategory](../uicontentsizecategory.md) — Constants that indicate the preferred size of your content.
- [UIContentSizeCategoryAdjusting](../uicontentsizecategoryadjusting.md) — A collection of methods that give controls an easy way to adopt automatic adjustment to content category changes.
- [UIContentSizeCategoryDidChangeNotification](../uicontentsizecategory/didchangenotification.md) — A notification that posts when the user changes the preferred content size setting.
- [UIContentSizeCategoryNewValueKey](../uicontentsizecategory/newvalueuserinfokey.md) — A key that reflects the new preferred content size.
