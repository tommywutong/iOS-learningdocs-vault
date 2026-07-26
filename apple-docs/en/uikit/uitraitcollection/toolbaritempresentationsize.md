---
title: toolbarItemPresentationSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 16.0+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/toolbaritempresentationsize
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/toolbaritempresentationsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/toolbaritempresentationsize.json'
content_hash: 'sha256:6d28c24ad66afd1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# toolbarItemPresentationSize

<sub>Instance Property</sub>

The presentation size of a toolbar item in an AppKit toolbar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var toolbarItemPresentationSize: UINSToolbarItemPresentationSize { get }
```

## Discussion

[NSToolbar](../../appkit/nstoolbar.md) supports various display modes that affect the amount of space available for displaying toolbar items. If you use [NSUIViewToolbarItem](../nsuiviewtoolbaritem.md) to host a [UIView](../uiview.md) in an [NSToolbar](../../appkit/nstoolbar.md) when you build your app with Mac Catalyst, that view receives information about its expected size through this trait. Use this trait to make any necessary adjustments to your custom view when the trait collection changes, such as when the toolbar switches to a new display mode.

The default value of this trait is [UINSToolbarItemPresentationSizeUnspecified](../uinstoolbaritempresentationsize/unspecified.md) when an [NSToolbar](../../appkit/nstoolbar.md) doesn’t host the view.

## See Also

### Retrieving interface-related traits

- [userInterfaceStyle](userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](../uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [userInterfaceLevel](userinterfacelevel.md) — The elevation level of the interface.
- [UIUserInterfaceLevel](../uiuserinterfacelevel.md) — Constants that indicate the visual level for content in the window.
- [layoutDirection](layoutdirection.md) — The layout direction associated with the current environment.
- [UITraitEnvironmentLayoutDirection](../uitraitenvironmentlayoutdirection.md) — Constants that indicate the layout direction associated with the current environment.
- [resolvesNaturalAlignmentWithBaseWritingDirection](resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [accessibilityContrast](accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [UIAccessibilityContrast](../uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](../uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](../uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
