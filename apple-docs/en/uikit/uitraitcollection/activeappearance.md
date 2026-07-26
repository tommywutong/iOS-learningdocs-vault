---
title: activeAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/activeappearance
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/activeappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/activeappearance.json'
content_hash: 'sha256:a3cb7b4609dfd7de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# activeAppearance

<sub>Instance Property</sub>

A property that indicates whether the user interface has an active appearance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var activeAppearance: UIUserInterfaceActiveAppearance { get }
```

## Discussion

The active appearance varies by platform and window management mode. On macOS, Stage Manager on iPad, and Windowed mode on iPad, the value is `.active` when at least one window is in the foreground and `.inactive` when no windows are in the foreground. On iOS and Full Screen mode on iPad, the value reflects whether the app itself is in the foreground (`.active`) or not (`.inactive`).

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
- [UIUserInterfaceActiveAppearance](../uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
