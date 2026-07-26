---
title: userInterfaceLevel
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutabletraits-8l00o/userinterfacelevel
source_url: 'https://developer.apple.com/documentation/uikit/uimutabletraits-8l00o/userinterfacelevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutabletraits-8l00o/userinterfacelevel.json'
content_hash: 'sha256:af8ac73f2b3e815a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableTraits](../uimutabletraits-8l00o.md)

# userInterfaceLevel

<sub>Instance Property</sub>

The elevation level of the interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) UIUserInterfaceLevel userInterfaceLevel;
```

## Discussion

Levels create a visual separation between different parts of your UI. Window content typically appears at the [UIUserInterfaceLevelBase](../uiuserinterfacelevel/base.md) level. When you want parts of your UI to stand out from the underlying background, assign the [UIUserInterfaceLevelElevated](../uiuserinterfacelevel/elevated.md) level to them. For example, the system assigns the [UIUserInterfaceLevelElevated](../uiuserinterfacelevel/elevated.md) level to alerts and popovers.

## See Also

### Getting and setting trait values

- [accessibilityContrast](accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [displayGamut](displaygamut.md) — The gamut of the current display.
- [displayScale](displayscale.md) — The display scale of the trait collection.
- [forceTouchCapability](forcetouchcapability.md) — The Force Touch capability value of the trait collection.
- [horizontalSizeClass](horizontalsizeclass.md) — The horizontal size class of the trait collection.
- [imageDynamicRange](imagedynamicrange.md) — The image dynamic range associated with the current environment.
- [layoutDirection](layoutdirection.md) — The layout direction associated with the current environment.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [listEnvironment](listenvironment.md) — The style of the containing list in a collection view or table view.
- [preferredContentSizeCategory](preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [resolvesNaturalAlignmentWithBaseWritingDirection](resolvesnaturalalignmentwithbasewritingdirection.md) — The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [sceneCaptureState](scenecapturestate.md) — The scene capture state for the current environment.
- [splitViewControllerLayoutEnvironment](splitviewcontrollerlayoutenvironment.md) — The split view controller layout for the current environment.
- [tabAccessoryEnvironment](tabaccessoryenvironment.md) — The tab accessory environment for the current trait collection.
