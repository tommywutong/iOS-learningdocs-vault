---
title: semanticContentAttribute
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/semanticcontentattribute
source_url: 'https://developer.apple.com/documentation/uikit/uiview/semanticcontentattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/semanticcontentattribute.json'
content_hash: 'sha256:6c9d354292a3b466'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# semanticContentAttribute

<sub>Instance Property</sub>

A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var semanticContentAttribute: UISemanticContentAttribute { get set }
```

## Discussion

Some views should not flip when switching between left-to-right and right-to-left layouts. For example, the view is part of the playback controls or represents physical directions (up, down, left, right) that don’t change. Instead of thinking about whether or not a view should change its orientation, select the semantic content attribute that best describes your view.

When creating a view that contains subviews, you can use the [+ userInterfaceLayoutDirectionForSemanticContentAttribute:](<userinterfacelayoutdirection(for_).md>) class method to determine whether the subviews should be flipped, and lay out the views in the appropriate order.

For a list of possible values, see [UISemanticContentAttribute](../uisemanticcontentattribute.md).

## See Also

### Adjusting the user interface

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view and all of its subviews.
- [effectiveUserInterfaceLayoutDirection](effectiveuserinterfacelayoutdirection.md) — The user interface layout direction appropriate for arranging the immediate content of the view.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:](<userinterfacelayoutdirection(for_).md>) — Returns the user interface direction for the given semantic content attribute.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:relativeToLayoutDirection:](<userinterfacelayoutdirection(for_relativeto_).md>) — Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.
