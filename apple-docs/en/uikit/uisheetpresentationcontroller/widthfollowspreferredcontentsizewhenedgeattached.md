---
title: widthFollowsPreferredContentSizeWhenEdgeAttached
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached.json'
content_hash: 'sha256:37534d0d02dd4297'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# widthFollowsPreferredContentSizeWhenEdgeAttached

<sub>Instance Property</sub>

A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var widthFollowsPreferredContentSizeWhenEdgeAttached: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md), which means the sheet’s width equals the width of its container’s safe area. Set this value to [true](../../swift/true.md) to use your view controller’s [preferredContentSize](../uiviewcontroller/preferredcontentsize.md) to determine the width of the sheet instead.

This property doesn’t have an effect when the sheet is in a compact-width and regular-height size class, or when [prefersEdgeAttachedInCompactHeight](prefersedgeattachedincompactheight.md) is [false](../../swift/false.md).

## See Also

### Managing the appearance

- [prefersGrabberVisible](prefersgrabbervisible.md) — A Boolean value that determines whether the sheet shows a grabber at the top.
- [prefersPageSizing](preferspagesizing.md) — A Boolean value that indicates whether the sheet sizes itself for readable content.
- [prefersEdgeAttachedInCompactHeight](prefersedgeattachedincompactheight.md) — A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [preferredCornerRadius](preferredcornerradius-3mb5.md) — The corner radius that the sheet attempts to present with.
