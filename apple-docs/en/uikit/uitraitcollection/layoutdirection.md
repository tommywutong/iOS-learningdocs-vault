---
title: layoutDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/layoutdirection
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/layoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/layoutdirection.json'
content_hash: 'sha256:3eb1e19c938e9c1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# layoutDirection

<sub>Instance Property</sub>

The layout direction associated with the current environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var layoutDirection: UITraitEnvironmentLayoutDirection { get }
```

## Discussion

Use this trait to determine whether the underlying environment uses a left-to-right or right-to-left orientation.

## See Also

### Retrieving interface-related traits

- [userInterfaceStyle](userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](../uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](../uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [userInterfaceLevel](userinterfacelevel.md) — The elevation level of the interface.
- [UIUserInterfaceLevel](../uiuserinterfacelevel.md) — Constants that indicate the visual level for content in the window.
- [UITraitEnvironmentLayoutDirection](../uitraitenvironmentlayoutdirection.md) — Constants that indicate the layout direction associated with the current environment.
- [resolvesNaturalAlignmentWithBaseWritingDirection](resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [accessibilityContrast](accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [UIAccessibilityContrast](../uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](../uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](../uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
