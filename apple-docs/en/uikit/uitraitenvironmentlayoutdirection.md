---
title: UITraitEnvironmentLayoutDirection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitraitenvironmentlayoutdirection
source_url: 'https://developer.apple.com/documentation/uikit/uitraitenvironmentlayoutdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitenvironmentlayoutdirection.json'
content_hash: 'sha256:70f4b6600e16dcfa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITraitEnvironmentLayoutDirection

<sub>Enumeration</sub>

Constants that indicate the layout direction associated with the current environment.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITraitEnvironmentLayoutDirection
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITraitEnvironmentLayoutDirectionUnspecified](uitraitenvironmentlayoutdirection/unspecified.md) — An unknown layout direction.
- [UITraitEnvironmentLayoutDirectionLeftToRight](uitraitenvironmentlayoutdirection/lefttoright.md) — A left-to-right layout direction.
- [UITraitEnvironmentLayoutDirectionRightToLeft](uitraitenvironmentlayoutdirection/righttoleft.md) — A right-to-left layout direction.

### Initializers

- [init(_:)](<uitraitenvironmentlayoutdirection/init(__).md>) — Creates a trait environment layout direction from the specified SwiftUI layout direction.
- [init(rawValue:)](<uitraitenvironmentlayoutdirection/init(rawvalue_).md>)

## See Also

### Retrieving interface-related traits

- [userInterfaceStyle](uitraitcollection/userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [userInterfaceLevel](uitraitcollection/userinterfacelevel.md) — The elevation level of the interface.
- [UIUserInterfaceLevel](uiuserinterfacelevel.md) — Constants that indicate the visual level for content in the window.
- [layoutDirection](uitraitcollection/layoutdirection.md) — The layout direction associated with the current environment.
- [resolvesNaturalAlignmentWithBaseWritingDirection](uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [accessibilityContrast](uitraitcollection/accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [UIAccessibilityContrast](uiaccessibilitycontrast.md) — Constants that indicate the accessibility contrast setting.
- [legibilityWeight](uitraitcollection/legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](uitraitcollection/activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
