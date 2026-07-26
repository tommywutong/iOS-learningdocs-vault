---
title: overrideUserInterfaceStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiview/overrideuserinterfacestyle
source_url: 'https://developer.apple.com/documentation/uikit/uiview/overrideuserinterfacestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/overrideuserinterfacestyle.json'
content_hash: 'sha256:2d2206b80c399831'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# overrideUserInterfaceStyle

<sub>Instance Property</sub>

The user interface style adopted by the view and all of its subviews.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var overrideUserInterfaceStyle: UIUserInterfaceStyle { get set }
```

## Discussion

Use this property to force the view to always adopt a light or dark interface style. The default value of this property is [UIUserInterfaceStyleUnspecified](../uiuserinterfacestyle/unspecified.md), which causes the view to inherit the interface style from a parent view or view controller. If you assign a different value, the new style applies to the view and all of the subviews owned by the same view controller. (If the view hierarchy contains the root view of an embedded child view controller, the child view controller and its views do not inherit the interface style.) If the view is a [UIWindow](../uiwindow.md) object, the new style applies to everything in the window, including the root view controller and all presented content.

## See Also

### Adjusting the user interface

- [semanticContentAttribute](semanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [effectiveUserInterfaceLayoutDirection](effectiveuserinterfacelayoutdirection.md) — The user interface layout direction appropriate for arranging the immediate content of the view.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:](<userinterfacelayoutdirection(for_).md>) — Returns the user interface direction for the given semantic content attribute.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:relativeToLayoutDirection:](<userinterfacelayoutdirection(for_relativeto_).md>) — Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.
