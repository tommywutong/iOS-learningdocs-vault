---
title: displayScale
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uimutabletraits-8l00o/displayscale
source_url: 'https://developer.apple.com/documentation/uikit/uimutabletraits-8l00o/displayscale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimutabletraits-8l00o/displayscale.json'
content_hash: 'sha256:114d66327bc94717'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMutableTraits](../uimutabletraits-8l00o.md)

# displayScale

<sub>Instance Property</sub>

The display scale of the trait collection.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic) CGFloat displayScale;
```

## Discussion

A value of `1.0` indicates a non-Retina display, `2.0` indicates a Retina display, and `3.0` indicates a Super Retina display. The default display scale for a trait collection is `0.0` (indicating unspecified).

## See Also

### Getting and setting trait values

- [accessibilityContrast](accessibilitycontrast.md) — The accessibility contrast associated with the current environment.
- [activeAppearance](activeappearance.md) — A property that indicates whether the user interface has an active appearance.
- [displayGamut](displaygamut.md) — The gamut of the current display.
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
- [toolbarItemPresentationSize](toolbaritempresentationsize.md) — The presentation size of a toolbar item in an AppKit toolbar.
