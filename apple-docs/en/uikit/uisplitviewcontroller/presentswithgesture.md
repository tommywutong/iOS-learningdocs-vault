---
title: presentsWithGesture
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.1+, iPadOS 5.1+, Mac Catalyst 13.1+, tvOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisplitviewcontroller/presentswithgesture
source_url: 'https://developer.apple.com/documentation/uikit/uisplitviewcontroller/presentswithgesture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisplitviewcontroller/presentswithgesture.json'
content_hash: 'sha256:154ae77a2c626eb6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISplitViewController](../uisplitviewcontroller.md)

# presentsWithGesture

<sub>Instance Property</sub>

Specifies whether a hidden view controller can be presented and dismissed using a swipe gesture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var presentsWithGesture: Bool { get set }
```

## Discussion

When this property is [true](../../swift/true.md), the split view controller installs a gesture recognizer for changing the current display mode. In a column-style split view interface, the gesture is interactive.

In a classic split view interface, the gesture recognizer applies the display mode returned by the delegate’s [- targetDisplayModeForActionInSplitViewController:](<../uisplitviewcontrollerdelegate/targetdisplaymodeforaction(in_).md>) method. If that method returns the [UISplitViewControllerDisplayModeAutomatic](displaymode-swift.enum/automatic.md) mode, the split view controller applies the most appropriate display mode given its current configuration and size class.

When this property is [false](../../swift/false.md), the split view controller doesn’t install a gesture recognizer for changing the display mode. The split view controller also doesn’t display a button to change the display mode.

The default value of this property is [true](../../swift/true.md).

## See Also

### Managing the display mode

- [preferredDisplayMode](preferreddisplaymode.md) — The preferred arrangement of the split view interface.
- [displayMode](displaymode-swift.property.md) — The current arrangement of the split view interface.
- [displayModeButtonItem](displaymodebuttonitem.md) — A button that changes the display mode of the split view controller.
- [showsSecondaryOnlyButton](showssecondaryonlybutton.md) — Specifies whether the secondary view controller shows a button to toggle to and from the secondary-only display mode.
- [DisplayMode](displaymode-swift.enum.md) — Constants that describe the possible arrangements for a split view interface.
- [displayModeButtonVisibility](displaymodebuttonvisibility-swift.property.md) — A setting that determines whether the display mode button is visible in the interface.
- [DisplayModeButtonVisibility](displaymodebuttonvisibility-swift.enum.md) — Constants that determine the visibility of the display mode button.
