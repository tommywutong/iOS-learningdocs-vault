---
title: preferredCornerRadius
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/preferredcornerradius-358tc
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferredcornerradius-358tc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/preferredcornerradius-358tc.json'
content_hash: 'sha256:8891f50c391a24f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# preferredCornerRadius

<sub>Instance Property</sub>

The corner radius that the sheet attempts to present with.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat preferredCornerRadius;
```

## Discussion

The default value is [UISheetPresentationControllerAutomaticDimension](../uisheetpresentationcontrollerautomaticdimension.md). This property only has an effect when the sheet is at the front of its sheet stack.

## See Also

### Managing the appearance

- [prefersGrabberVisible](prefersgrabbervisible.md) — A Boolean value that determines whether the sheet shows a grabber at the top.
- [prefersPageSizing](preferspagesizing.md) — A Boolean value that indicates whether the sheet sizes itself for readable content.
- [prefersEdgeAttachedInCompactHeight](prefersedgeattachedincompactheight.md) — A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [widthFollowsPreferredContentSizeWhenEdgeAttached](widthfollowspreferredcontentsizewhenedgeattached.md) — A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [UISheetPresentationControllerAutomaticDimension](../uisheetpresentationcontrollerautomaticdimension.md) — The default value to apply to a dimension.
