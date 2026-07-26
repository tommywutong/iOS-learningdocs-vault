---
title: 'init(userInterfaceStyle:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/init(userinterfacestyle:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/init(userinterfacestyle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/init%28userinterfacestyle%3A%29.json'
content_hash: 'sha256:e898045bb9237163'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# init(userInterfaceStyle:)

<sub>Initializer</sub>

Creates a trait collection that contains only the specified user interface style trait.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(userInterfaceStyle: UIUserInterfaceStyle)
```

## Parameters

- `userInterfaceStyle` — The interface style for the trait collection. For a list of possible values, see [UIUserInterfaceStyle](../uiuserinterfacestyle.md).

## Return Value

A new trait collection containing only the interface style trait.

## See Also

### Creating a trait collection

- [- init](<init().md>) — Creates a trait collection whose traits are set to their default (unspecified) values.
- [+ traitCollectionWithUserInterfaceIdiom:](<init(userinterfaceidiom_).md>) — Creates a trait collection that contains only a specified interface idiom.
- [+ traitCollectionWithHorizontalSizeClass:](<init(horizontalsizeclass_).md>) — Creates a trait collection that contains only a specified horizontal size class.
- [+ traitCollectionWithVerticalSizeClass:](<init(verticalsizeclass_).md>) — Creates a trait collection that contains only a specified vertical size class.
- [+ traitCollectionWithAccessibilityContrast:](<init(accessibilitycontrast_).md>) — Creates a trait collection that contains only the specified accessibility contrast trait.
- [+ traitCollectionWithUserInterfaceLevel:](<init(userinterfacelevel_).md>) — Creates a trait collection that contains only the specified user interface level trait.
- [+ traitCollectionWithLegibilityWeight:](<init(legibilityweight_).md>) — Creates a trait collection that contains only the specified legibility weight trait.
- [+ traitCollectionWithForceTouchCapability:](<init(forcetouchcapability_).md>) — Creates a trait collection that contains only a specified force touch capability trait.
- [+ traitCollectionWithDisplayScale:](<init(displayscale_).md>) — Creates a trait collection that contains only a specified display scale.
- [+ traitCollectionWithDisplayGamut:](<init(displaygamut_).md>) — Creates a trait collection that contains only the specified display gamut trait.
- [+ traitCollectionWithLayoutDirection:](<init(layoutdirection_).md>) — Creates a trait collection that contains only the specified layout direction trait.
- [+ traitCollectionWithPreferredContentSizeCategory:](<init(preferredcontentsizecategory_).md>) — Creates a trait collection that contains only the specified content size category trait.
- [+ traitCollectionWithActiveAppearance:](<init(activeappearance_).md>) — Creates a trait collection that contains only the specified active appearance trait.
- [+ traitCollectionWithToolbarItemPresentationSize:](<init(toolbaritempresentationsize_).md>) — Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [+ traitCollectionWithHDRHeadroomUsageLimit:](<init(hdrheadroomusagelimit_)-5zqph.md>)
