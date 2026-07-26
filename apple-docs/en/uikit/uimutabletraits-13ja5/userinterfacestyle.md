---
title: userInterfaceStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutabletraits-13ja5/userinterfacestyle
source_url: 'https://developer.apple.com/documentation/uikit/uimutabletraits-13ja5/userinterfacestyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutabletraits-13ja5/userinterfacestyle.json'
content_hash: 'sha256:5c90ab83e0481953'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableTraits](../uimutabletraits-13ja5.md)

# userInterfaceStyle

<sub>Instance Property</sub>

The style associated with the user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var userInterfaceStyle: UIUserInterfaceStyle { get set }
```

## Discussion

Use this trait to determine whether your interface should be configured with a dark or light appearance. The default value of this trait is set to the corresponding appearance setting on the user’s device.

## See Also

### Getting and setting trait values

- [accessibilityContrast](accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [displayGamut](displaygamut.md) — The gamut of the current display.
- [displayScale](displayscale.md) — The display scale of the trait collection.
- [forceTouchCapability](forcetouchcapability.md) — The Force Touch capability value of the trait collection.
- [headroomUsageLimit](headroomusagelimit.md) — The HDR headroom usage limit associated with the current environment.
- [horizontalSizeClass](horizontalsizeclass.md) — The horizontal size class of the trait collection.
- [imageDynamicRange](imagedynamicrange.md) — The image dynamic range associated with the current environment.
- [layoutDirection](layoutdirection.md) — The layout direction associated with the current environment.
- [legibilityWeight](legibilityweight.md) — The font weight to apply to text.
- [listEnvironment](listenvironment.md) — The style of the containing list in a collection view or table view.
- [preferredContentSizeCategory](preferredcontentsizecategory.md) — The font sizing option preferred by the user.
- [resolvesNaturalAlignmentWithBaseWritingDirection](resolvesnaturalalignmentwithbasewritingdirection.md) — The setting for whether the system resolves natural alignment with base writing direction for the current environment.
- [sceneCaptureState](scenecapturestate.md) — The scene capture state for the current environment.
- [splitViewControllerLayoutEnvironment](splitviewcontrollerlayoutenvironment.md) — The split view controller layout for the current environment.
