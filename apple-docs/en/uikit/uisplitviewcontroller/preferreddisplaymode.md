---
title: preferredDisplayMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/preferreddisplaymode
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/preferreddisplaymode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/preferreddisplaymode.json'
content_hash: 'sha256:0ad64123e0d1861b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# preferredDisplayMode

<sub>Instance Property</sub>

The preferred arrangement of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredDisplayMode: UISplitViewController.DisplayMode { get set }
```

## Discussion

Use this property to specify the display mode that you prefer to use. The split view controller makes every effort to adopt the interface you specify, but may use a different type of interface if there isn’t enough space to support your preferred choice. If changing the value of this property leads to an actual change in the current display mode, the split view controller updates [displayMode](displaymode-swift.property.md). The resulting change is animated if you made the change in an animation block.

Setting the value of this property to [UISplitViewControllerDisplayModeAutomatic](displaymode-swift.enum/automatic.md) causes the split view controller to choose the most appropriate display mode for the currently available space. The default value of this property is [UISplitViewControllerDisplayModeAutomatic](displaymode-swift.enum/automatic.md).

A split view controller’s split behavior affects its possible display mode. The preferred display mode is interpreted to match the current [splitBehavior](splitbehavior-swift.property.md). For example, if you set the preferred display mode to [UISplitViewControllerDisplayModeTwoBesideSecondary](displaymode-swift.enum/twobesidesecondary.md), the actual [displayMode](displaymode-swift.property.md) is interpreted as [UISplitViewControllerDisplayModeTwoOverSecondary](displaymode-swift.enum/twooversecondary.md) for [UISplitViewControllerSplitBehaviorOverlay](splitbehavior-swift.enum/overlay.md), and as [UISplitViewControllerDisplayModeTwoDisplaceSecondary](displaymode-swift.enum/twodisplacesecondary.md) for [UISplitViewControllerSplitBehaviorDisplace](splitbehavior-swift.enum/displace.md).

If [presentsWithGesture](presentswithgesture.md) is [false](../../swift/false.md), the value of this property is strictly respected.

## See Also

### Managing the display mode

- [displayMode](displaymode-swift.property.md) — The current arrangement of the split view interface.
- [displayModeButtonItem](displaymodebuttonitem.md) — A button that changes the display mode of the split view controller.
- [presentsWithGesture](presentswithgesture.md) — Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [showsSecondaryOnlyButton](showssecondaryonlybutton.md) — Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [DisplayMode](displaymode-swift.enum.md) — Constants that describe the possible arrangements for a split view interface.
- [displayModeButtonVisibility](displaymodebuttonvisibility-swift.property.md) — A setting that determines whether the display mode button is visible in the interface.
- [DisplayModeButtonVisibility](displaymodebuttonvisibility-swift.enum.md) — Constants that determine the visibility of the display mode button.
