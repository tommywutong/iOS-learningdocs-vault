---
title: 'userInterfaceLayoutDirection(for:relativeTo:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiview/userinterfacelayoutdirection(for:relativeto:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiview/userinterfacelayoutdirection(for:relativeto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiview/userinterfacelayoutdirection%28for%3Arelativeto%3A%29.json'
content_hash: 'sha256:ee71a90eaa2edffb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIView](../uiview.md)

# userInterfaceLayoutDirection(for:relativeTo:)

<sub>Type Method</sub>

Returns the layout direction implied by the specified semantic content attribute, relative to the specified layout direction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func userInterfaceLayoutDirection(for semanticContentAttribute: UISemanticContentAttribute, relativeTo layoutDirection: UIUserInterfaceLayoutDirection) -> UIUserInterfaceLayoutDirection
```

## Parameters

- `semanticContentAttribute` — The semantic content attribute for a view.

- `layoutDirection` — The user interface layout direction ([UIUserInterfaceLayoutDirectionLeftToRight](../uiuserinterfacelayoutdirection/lefttoright.md) or [UIUserInterfaceLayoutDirectionRightToLeft](../uiuserinterfacelayoutdirection/righttoleft.md)).

## Return Value

The layout direction implied by the semantic content attribute and relative to the layout direction.

## Discussion

For example, when this method is passed a layout direction of [UIUserInterfaceLayoutDirectionRightToLeft](../uiuserinterfacelayoutdirection/righttoleft.md) and a semantic content attribute of [UISemanticContentAttributePlayback](../uisemanticcontentattribute/playback.md), it returns [UIUserInterfaceLayoutDirectionLeftToRight](../uiuserinterfacelayoutdirection/lefttoright.md). Although layout and drawing code can use this method to determine how to arrange elements, it might be easier to query the container view’s [effectiveUserInterfaceLayoutDirection](effectiveuserinterfacelayoutdirection.md) property instead.

## See Also

### Adjusting the user interface

- [overrideUserInterfaceStyle](overrideuserinterfacestyle.md) — The user interface style adopted by the view and all of its subviews.
- [semanticContentAttribute](semanticcontentattribute.md) — A semantic description of the view’s contents, used to determine whether the view should be flipped when switching between left-to-right and right-to-left layouts.
- [effectiveUserInterfaceLayoutDirection](effectiveuserinterfacelayoutdirection.md) — The user interface layout direction appropriate for arranging the immediate content of the view.
- [+ userInterfaceLayoutDirectionForSemanticContentAttribute:](<userinterfacelayoutdirection(for_).md>) — Returns the user interface direction for the given semantic content attribute.
