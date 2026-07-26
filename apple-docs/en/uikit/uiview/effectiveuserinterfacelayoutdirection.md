---
title: effectiveUserInterfaceLayoutDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/effectiveuserinterfacelayoutdirection
source_url: 'https://developer.apple.com/documentation/uikit/uiview/effectiveuserinterfacelayoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/effectiveuserinterfacelayoutdirection.json'
content_hash: 'sha256:da14aa3c13d52c8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# effectiveUserInterfaceLayoutDirection

<sub>Instance Property</sub>

The user interface layout direction appropriate for arranging the immediate content of the view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var effectiveUserInterfaceLayoutDirection: UIUserInterfaceLayoutDirection { get }
```

## Discussion

When a view’s immediate content is being arranged or drawn, you should always consult the value of this property. In addition, note that you can’t assume that the value propagates through the view’s subtree.

## See Also

### Adjusting the user interface

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view and all of its subviews.
- [semanticContentAttribute](semanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:](<userinterfacelayoutdirection(for_).md>) — Returns the user interface direction for the given semantic content attribute.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:relativeToLayoutDirection:](<userinterfacelayoutdirection(for_relativeto_).md>) — Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.
