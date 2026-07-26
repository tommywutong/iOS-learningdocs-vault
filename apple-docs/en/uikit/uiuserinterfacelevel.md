---
title: UIUserInterfaceLevel
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiuserinterfacelevel
source_url: 'https://developer.apple.com/documentation/uikit/uiuserinterfacelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiuserinterfacelevel.json'
content_hash: 'sha256:42868c0750802558'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIUserInterfaceLevel

<sub>Enumeration</sub>

Constants that indicate the visual level for content in the window.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum UIUserInterfaceLevel
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Interface levels

- [UIUserInterfaceLevelUnspecified](uiuserinterfacelevel/unspecified.md) — An unspecified interface level.
- [UIUserInterfaceLevelBase](uiuserinterfacelevel/base.md) — The level for your window’s main content.
- [UIUserInterfaceLevelElevated](uiuserinterfacelevel/elevated.md) — The level for content visually above your window’s main content.

### Initializers

- [init(rawValue:)](<uiuserinterfacelevel/init(rawvalue_).md>)

## See Also

### Retrieving interface-related traits

- [userInterfaceStyle](uitraitcollection/userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [userInterfaceLevel](uitraitcollection/userinterfacelevel.md) — The elevation level of the interface.
- [layoutDirection](uitraitcollection/layoutdirection.md) — The layout direction associated with the current environment.
- [UITraitEnvironmentLayoutDirection](uitraitenvironmentlayoutdirection.md) — Constants that indicate the layout direction associated with the current environment.
- [resolvesNaturalAlignmentWithBaseWritingDirection](uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [accessibilityContrast](uitraitcollection/accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [UIAccessibilityContrast](uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](uitraitcollection/legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](uitraitcollection/activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
