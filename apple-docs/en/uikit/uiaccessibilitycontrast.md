---
title: UIAccessibilityContrast
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiaccessibilitycontrast
source_url: 'https://developer.apple.com/documentation/uikit/uiaccessibilitycontrast'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiaccessibilitycontrast.json'
content_hash: 'sha256:793b3cfeed8cea60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIAccessibilityContrast

<sub>Enumeration</sub>

Constants that indicate the accessibility contrast setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UIAccessibilityContrast
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Contrast settings

- [UIAccessibilityContrastUnspecified](uiaccessibilitycontrast/unspecified.md) — An unspecified contrast.
- [UIAccessibilityContrastNormal](uiaccessibilitycontrast/normal.md) — A normal contrast level.
- [UIAccessibilityContrastHigh](uiaccessibilitycontrast/high.md) — A high contrast level.

### Initializers

- [init(_:)](<uiaccessibilitycontrast/init(__).md>) — Creates an accessibility contrast from the specified SwiftUI color scheme contrast.
- [init(rawValue:)](<uiaccessibilitycontrast/init(rawvalue_).md>)

## See Also

### Retrieving interface-related traits

- [userInterfaceStyle](uitraitcollection/userinterfacestyle.md) — The style associated with the user interface.
- [UIUserInterfaceStyle](uiuserinterfacestyle.md) — Constants that indicate the interface style for the app.
- [userInterfaceIdiom](uitraitcollection/userinterfaceidiom.md) — The user interface idiom of the trait collection.
- [UIUserInterfaceIdiom](uiuserinterfaceidiom.md) — Constants that indicate the interface type for the device or an object that has a trait environment, such as a view and view controller.
- [userInterfaceLevel](uitraitcollection/userinterfacelevel.md) — The elevation level of the interface.
- [UIUserInterfaceLevel](uiuserinterfacelevel.md) — Constants that indicate the visual level for content in the window.
- [layoutDirection](uitraitcollection/layoutdirection.md) — The layout direction associated with the current environment.
- [UITraitEnvironmentLayoutDirection](uitraitenvironmentlayoutdirection.md) — Constants that indicate the layout direction associated with the current environment.
- [resolvesNaturalAlignmentWithBaseWritingDirection](uitraitcollection/resolvesnaturalalignmentwithbasewritingdirection-58wlh.md)
- [accessibilityContrast](uitraitcollection/accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [legibilityWeight](uitraitcollection/legibilityweight.md) — The font weight to apply to text.
- [UILegibilityWeight](uilegibilityweight.md) — Constants that indicate the weight to apply to text in your interface.
- [activeAppearance](uitraitcollection/activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [UIUserInterfaceActiveAppearance](uiuserinterfaceactiveappearance.md) — Constants that indicate whether the user interface has an active appearance.
- [toolbarItemPresentationSize](uitraitcollection/toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
