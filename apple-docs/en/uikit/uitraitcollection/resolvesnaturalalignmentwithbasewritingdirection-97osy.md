---
title: resolvesNaturalAlignmentWithBaseWritingDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-97osy.json'
content_hash: 'sha256:1a9c2aca3ceef24b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# resolvesNaturalAlignmentWithBaseWritingDirection

<sub>Instance Property</sub>

Specifies the behavior for resolving `NSTextAlignment.natural` to the visual alignment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) BOOL resolvesNaturalAlignmentWithBaseWritingDirection;
```

## Discussion

When set to `true`, the resolved visual alignment is determined by the resolved base writing direction; otherwise, it is using the user’s preferred language.

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
- [accessibilityContrast](accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [UIAccessibilityContrast](../uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](../uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](../uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
