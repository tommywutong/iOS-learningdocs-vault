---
title: showsSecondaryOnlyButton
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/showssecondaryonlybutton
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/showssecondaryonlybutton'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/showssecondaryonlybutton.json'
content_hash: 'sha256:266a37dc7d1ecf2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# showsSecondaryOnlyButton

<sub>Instance Property</sub>

Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var showsSecondaryOnlyButton: Bool { get set }
```

## Discussion

This value only takes effect when the split view controller’s [style](style-swift.property.md) property is [UISplitViewControllerStyleTripleColumn](style-swift.enum/triplecolumn.md).

The default value of this property is [false](../../swift/false.md). If you set the value to [true](../../swift/true.md), the secondary view controller shows a button that lets a user toggle the display mode to and from [UISplitViewControllerDisplayModeSecondaryOnly](displaymode-swift.enum/secondaryonly.md).

## See Also

### Managing the display mode

- [preferredDisplayMode](preferreddisplaymode.md) — The preferred arrangement of the split view interface.
- [displayMode](displaymode-swift.property.md) — The current arrangement of the split view interface.
- [displayModeButtonItem](displaymodebuttonitem.md) — A button that changes the display mode of the split view controller.
- [presentsWithGesture](presentswithgesture.md) — Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [DisplayMode](displaymode-swift.enum.md) — Constants that describe the possible arrangements for a split view interface.
- [displayModeButtonVisibility](displaymodebuttonvisibility-swift.property.md) — A setting that determines whether the display mode button is visible in the interface.
- [DisplayModeButtonVisibility](displaymodebuttonvisibility-swift.enum.md) — Constants that determine the visibility of the display mode button.
