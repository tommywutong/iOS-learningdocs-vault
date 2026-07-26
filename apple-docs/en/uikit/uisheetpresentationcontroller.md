---
title: UISheetPresentationController
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller.json'
content_hash: 'sha256:4ed9c60bee3f1eb6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISheetPresentationController

<sub>Class</sub>

A presentation controller that manages the appearance and behavior of a sheet.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor class UISheetPresentationController
```

## Overview

[UISheetPresentationController](uisheetpresentationcontroller.md) lets you present your view controller as a sheet. Before you present your view controller, configure the sheet presentation controller in its [sheetPresentationController](uiviewcontroller/sheetpresentationcontroller.md) property with the behavior and appearance you want for your sheet.

```swift
// In a subclass of UIViewController, customize and present the sheet.
func showMyViewControllerInACustomizedSheet() {
    let viewControllerToPresent = MyViewController()
    if let sheet = viewControllerToPresent.sheetPresentationController {
        sheet.detents = [.medium(), .large()]
        sheet.largestUndimmedDetentIdentifier = .medium
        sheet.prefersScrollingExpandsWhenScrolledToEdge = false
        sheet.prefersEdgeAttachedInCompactHeight = true
        sheet.widthFollowsPreferredContentSizeWhenEdgeAttached = true
    }
    present(viewControllerToPresent, animated: true, completion: nil)
}
```

Sheet presentation controllers specify a sheet’s size based on a _detent_, a height where a sheet naturally rests. Detents allow a sheet to resize from one edge of its fully expanded frame while the other three edges remain fixed. You specify the detents that a sheet supports using [detents](uisheetpresentationcontroller/detents.md), and monitor its most recently selected detent using [selectedDetentIdentifier](uisheetpresentationcontroller/selecteddetentidentifier.md).

> [!note] Related Sessions from WWDC21
> Session 10063: [Customize and Resize Sheets in UIKit](https://developer.apple.com/wwdc21/10063)
>
> Session 10068: [What’s new in UIKit](https://developer.apple.com/videos/play/wwdc2022/10068)

## Relationships

- **Inherits From**: [UIPresentationController](uipresentationcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIAppearanceContainer](uiappearancecontainer.md), [UIContentContainer](uicontentcontainer.md), [UIFocusEnvironment](uifocusenvironment.md), [UITraitChangeObservable](uitraitchangeobservable-67e94.md), [UITraitEnvironment](uitraitenvironment.md)

## Topics

### Specifying the height

- [detents](uisheetpresentationcontroller/detents.md) — The array of heights where a sheet can rest.
- [selectedDetentIdentifier](uisheetpresentationcontroller/selecteddetentidentifier.md) — The identifier of the most recently selected detent.
- [Detent](uisheetpresentationcontroller/detent.md) — An object that represents a height where a sheet naturally rests.

### Managing the delegate

- [delegate](uisheetpresentationcontroller/delegate.md) — The delegate of the sheet presentation controller.
- [UISheetPresentationControllerDelegate](uisheetpresentationcontrollerdelegate.md) — The interface that an object implements to respond to size changes in a sheet presentation controller.

### Managing user interaction

- [largestUndimmedDetentIdentifier](uisheetpresentationcontroller/largestundimmeddetentidentifier.md) — The largest detent that doesn’t dim the view underneath the sheet.
- [prefersScrollingExpandsWhenScrolledToEdge](uisheetpresentationcontroller/prefersscrollingexpandswhenscrolledtoedge.md) — A Boolean value that determines whether scrolling expands the sheet to a larger detent.

### Managing the appearance

- [prefersGrabberVisible](uisheetpresentationcontroller/prefersgrabbervisible.md) — A Boolean value that determines whether the sheet shows a grabber at the top.
- [prefersPageSizing](uisheetpresentationcontroller/preferspagesizing.md) — A Boolean value that indicates whether the sheet sizes itself for readable content.
- [prefersEdgeAttachedInCompactHeight](uisheetpresentationcontroller/prefersedgeattachedincompactheight.md) — A Boolean value that determines whether the sheet attaches to the bottom edge of the screen in a compact-height size class.
- [widthFollowsPreferredContentSizeWhenEdgeAttached](uisheetpresentationcontroller/widthfollowspreferredcontentsizewhenedgeattached.md) — A Boolean value that determines whether the sheet’s width matches its view controller’s preferred content size.
- [preferredCornerRadius](uisheetpresentationcontroller/preferredcornerradius-3mb5.md) — The corner radius that the sheet attempts to present with.

### Customizing the position

- [sourceView](uisheetpresentationcontroller/sourceview.md) — The view that the sheet centers itself over.

### Working with custom detents

- [- invalidateDetents](<uisheetpresentationcontroller/invalidatedetents().md>) — Notifies the sheet to re-evaluate its detent value in the next layout pass.

### Animating changes to the sheet

- [- animateChanges:](<uisheetpresentationcontroller/animatechanges(__).md>) — Animates the UI changes to the sheet’s properties.

## See Also

### Presentation management

- [Disabling the pull-down gesture for a sheet](disabling-the-pull-down-gesture-for-a-sheet.md) — Ensure a positive user experience when presenting a view controller as a sheet.
- [UIPresentationController](uipresentationcontroller.md) — An object that manages the transition animations and the presentation of view controllers onscreen.
