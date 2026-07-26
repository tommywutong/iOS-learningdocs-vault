---
title: 'userInterfaceLayoutDirection(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/userinterfacelayoutdirection(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/userinterfacelayoutdirection(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/userinterfacelayoutdirection%28for%3A%29.json'
content_hash: 'sha256:aad7e40a2e026029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# userInterfaceLayoutDirection(for:)

<sub>Type Method</sub>

Returns the user interface direction for the given semantic content attribute.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func userInterfaceLayoutDirection(for attribute: UISemanticContentAttribute) -> UIUserInterfaceLayoutDirection
```

## Parameters

- `attribute` — The semantic content attribute for a view.

## Return Value

The user interface layout direction (left-to-right or right-to-left).

## Discussion

When creating a view that contains subviews, you can use this method to determine whether the subviews should be flipped, and lay out the views in the appropriate order.

## See Also

### Adjusting the user interface

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view and all of its subviews.
- [semanticContentAttribute](semanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [effectiveUserInterfaceLayoutDirection](effectiveuserinterfacelayoutdirection.md) — The user interface layout direction appropriate for arranging the immediate content of the view.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:relativeToLayoutDirection:](<userinterfacelayoutdirection(for_relativeto_).md>) — Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.
