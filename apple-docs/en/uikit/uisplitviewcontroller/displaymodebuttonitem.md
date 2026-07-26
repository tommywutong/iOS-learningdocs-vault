---
title: displayModeButtonItem
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/displaymodebuttonitem
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/displaymodebuttonitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/displaymodebuttonitem.json'
content_hash: 'sha256:b496539b6452b571'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# displayModeButtonItem

<sub>Instance Property</sub>

A button that changes the display mode of the split view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var displayModeButtonItem: UIBarButtonItem { get }
```

## Return Value

A preconfigured bar button item that changes the display mode.

## Discussion

You use this property in classic split view interfaces only. This button doesn’t affect column-style split view interfaces.

When a user taps this button, the display mode changes to the value last returned by the delegate’s [- targetDisplayModeForActionInSplitViewController:](<../uisplitviewcontrollerdelegate/targetdisplaymodeforaction(in_).md>) method. Use that method to determine what mode to apply next based on the current configuration of the split view controller.

Don’t change the configuration of the returned button. The split view controller updates the button’s configuration and appearance automatically based on the current display mode and the information the delegate object provides.

You must incorporate this button into your user interface yourself.

## See Also

### Managing the display mode

- [preferredDisplayMode](preferreddisplaymode.md) — The preferred arrangement of the split view interface.
- [displayMode](displaymode-swift.property.md) — The current arrangement of the split view interface.
- [presentsWithGesture](presentswithgesture.md) — Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.
- [showsSecondaryOnlyButton](showssecondaryonlybutton.md) — Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [DisplayMode](displaymode-swift.enum.md) — Constants that describe the possible arrangements for a split view interface.
- [displayModeButtonVisibility](displaymodebuttonvisibility-swift.property.md) — A setting that determines whether the display mode button is visible in the interface.
- [DisplayModeButtonVisibility](displaymodebuttonvisibility-swift.enum.md) — Constants that determine the visibility of the display mode button.
