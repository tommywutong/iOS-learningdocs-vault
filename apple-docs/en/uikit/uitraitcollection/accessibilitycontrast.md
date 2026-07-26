---
title: accessibilityContrast
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/accessibilitycontrast
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/accessibilitycontrast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/accessibilitycontrast.json'
content_hash: 'sha256:81feddef98c6f32c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# accessibilityContrast

<sub>Instance Property</sub>

The accessibility contrast associated with the current environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var accessibilityContrast: UIAccessibilityContrast { get }
```

## Discussion

Use this trait to determine whether the user requested a high contrast between foreground and background content. The user sets the contrast level in the Accessibility area in Settings.

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
- [UIAccessibilityContrast](../uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](../uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](../uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
