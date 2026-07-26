---
title: 'init(displayScale:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/init(displayscale:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/init(displayscale:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/init%28displayscale%3A%29.json'
content_hash: 'sha256:c296760f00837d63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# init(displayScale:)

<sub>Initializer</sub>

Creates a trait collection that contains only a specified display scale.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(displayScale scale: CGFloat)
```

## Parameters

- `scale` — The display scale for the new trait collection. Use `1.0` to specify a non-Retina display scale, and a value of `2.0` or greater to specify a Retina display scale.

## Return Value

A new trait collection containing only a specified display scale trait.

## See Also

### Creating a trait collection

- [- init](<init().md>) — Creates a trait collection whose traits are set to their default (unspecified) values.
- [+ traitCollectionWithUserInterfaceIdiom:](<init(userinterfaceidiom_).md>) — Creates a trait collection that contains only a specified interface idiom.
- [+ traitCollectionWithHorizontalSizeClass:](<init(horizontalsizeclass_).md>) — Creates a trait collection that contains only a specified horizontal size class.
- [+ traitCollectionWithVerticalSizeClass:](<init(verticalsizeclass_).md>) — Creates a trait collection that contains only a specified vertical size class.
- [+ traitCollectionWithUserInterfaceStyle:](<init(userinterfacestyle_).md>) — Creates a trait collection that contains only the specified user interface style trait.
- [+ traitCollectionWithAccessibilityContrast:](<init(accessibilitycontrast_).md>) — Creates a trait collection that contains only the specified accessibility contrast trait.
- [+ traitCollectionWithUserInterfaceLevel:](<init(userinterfacelevel_).md>) — Creates a trait collection that contains only the specified user interface level trait.
- [+ traitCollectionWithLegibilityWeight:](<init(legibilityweight_).md>) — Creates a trait collection that contains only the specified legibility weight trait.
- [+ traitCollectionWithForceTouchCapability:](<init(forcetouchcapability_).md>) — Creates a trait collection that contains only a specified force touch capability trait.
- [+ traitCollectionWithDisplayGamut:](<init(displaygamut_).md>) — Creates a trait collection that contains only the specified display gamut trait.
- [+ traitCollectionWithLayoutDirection:](<init(layoutdirection_).md>) — Creates a trait collection that contains only the specified layout direction trait.
- [+ traitCollectionWithPreferredContentSizeCategory:](<init(preferredcontentsizecategory_).md>) — Creates a trait collection that contains only the specified content size category trait.
- [+ traitCollectionWithActiveAppearance:](<init(activeappearance_).md>) — Creates a trait collection that contains only the specified active appearance trait.
- [+ traitCollectionWithToolbarItemPresentationSize:](<init(toolbaritempresentationsize_).md>) — Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [+ traitCollectionWithHDRHeadroomUsageLimit:](<init(hdrheadroomusagelimit_)-5zqph.md>)
