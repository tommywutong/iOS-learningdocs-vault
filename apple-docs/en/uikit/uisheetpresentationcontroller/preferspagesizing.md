---
title: prefersPageSizing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/preferspagesizing
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/preferspagesizing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/preferspagesizing.json'
content_hash: 'sha256:46d04c8f4cf55f4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# prefersPageSizing

<sub>Instance Property</sub>

A Boolean value that indicates whether the sheet sizes itself for readable content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var prefersPageSizing: Bool { get set }
```

## Discussion

The default value is [true](../../swift/true.md). The default value indicates the sheet uses [UIModalPresentationPageSheet](../uimodalpresentationstyle/pagesheet.md) behavior, in which the sheet width follows the readable width.

When the value is set to [false](../../swift/false.md), the sheet uses [UIModalPresentationFormSheet](../uimodalpresentationstyle/formsheet.md) behavior, in which the sheet size follows the presented view controller’s [preferredContentSize](../uiviewcontroller/preferredcontentsize.md).

## See Also

### Managing the appearance

- [prefersGrabberVisible](prefersgrabbervisible.md) — A Boolean value that determines whether the sheet shows a grabber at the top.
- [prefersEdgeAttachedInCompactHeight](prefersedgeattachedincompactheight.md) — A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [widthFollowsPreferredContentSizeWhenEdgeAttached](widthfollowspreferredcontentsizewhenedgeattached.md) — A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [preferredCornerRadius](preferredcornerradius-3mb5.md) — The corner radius that the sheet attempts to present with.
