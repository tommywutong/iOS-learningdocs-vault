---
title: displayMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymode-swift.property.json'
content_hash: 'sha256:b78d355126db7d4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# displayMode

<sub>Instance Property</sub>

The current arrangement of the split view interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var displayMode: UISplitViewController.DisplayMode { get }
```

## Discussion

This property reflects the arrangement of the child view controllers in a split view interface. The value in this property is never set to [UISplitViewControllerDisplayModeAutomatic](displaymode-swift.enum/automatic.md). To change the current display mode, change the value of the [preferredDisplayMode](preferreddisplaymode.md) property. If you just want to change which columns are shown, consider using [- showColumn:](<show(__).md>) or [- hideColumn:](<hide(__).md>) and the split view controller will determine how to update the display mode to display the desired columns.

When [collapsed](iscollapsed.md) is [true](../../swift/true.md), the value of this property is ignored. A collapsed split view interface contains only one view controller, so the display mode is superfluous.

## See Also

### Managing the display mode

- [preferredDisplayMode](preferreddisplaymode.md) — The preferred arrangement of the split view interface.
- [displayModeButtonItem](displaymodebuttonitem.md) — A button that changes the display mode of the split view controller.
- [presentsWithGesture](presentswithgesture.md) — Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [showsSecondaryOnlyButton](showssecondaryonlybutton.md) — Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [DisplayMode](displaymode-swift.enum.md) — Constants that describe the possible arrangements for a split view interface.
- [displayModeButtonVisibility](displaymodebuttonvisibility-swift.property.md) — A setting that determines whether the display mode button is visible in the interface.
- [DisplayModeButtonVisibility](displaymodebuttonvisibility-swift.enum.md) — Constants that determine the visibility of the display mode button.
