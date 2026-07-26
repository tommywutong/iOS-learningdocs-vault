---
title: userInterfaceLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/userinterfacelevel
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/userinterfacelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/userinterfacelevel.json'
content_hash: 'sha256:5683f11198d7517e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# userInterfaceLevel

<sub>Instance Property</sub>

The elevation level of the interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var userInterfaceLevel: UIUserInterfaceLevel { get }
```

## Discussion

Levels create a visual separation between different parts of your UI. Window content typically appears at the [UIUserInterfaceLevelBase](../uiuserinterfacelevel/base.md) level. When you want parts of your UI to stand out from the underlying background, assign the [UIUserInterfaceLevelElevated](../uiuserinterfacelevel/elevated.md) level to them. For example, the system assigns the [UIUserInterfaceLevelElevated](../uiuserinterfacelevel/elevated.md) level to alerts and popovers.

## See Also

### Retrieving interface-related traits

- [userInterfaceStyle](userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](../uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
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
- [toolbarItemPresentationSize](toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
