---
title: 'init(displayGamut:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitraitcollection/init(displaygamut:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/init(displaygamut:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/init%28displaygamut%3A%29.json'
content_hash: 'sha256:341ebfa6b07f6c02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# init(displayGamut:)

<sub>Initializer</sub>

Creates a trait collection that contains only the specified display gamut trait.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(displayGamut: UIDisplayGamut)
```

## Parameters

- `displayGamut` — The display gamut for the new trait collection. For a list of possible values, see [UIDisplayGamut](../uidisplaygamut.md).

## Return Value

A new trait collection containing only the gamut value.

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
- [+ traitCollectionWithDisplayScale:](<init(displayscale_).md>) — Creates a trait collection that contains only a specified display scale.
- [+ traitCollectionWithLayoutDirection:](<init(layoutdirection_).md>) — Creates a trait collection that contains only the specified layout direction trait.
- [+ traitCollectionWithPreferredContentSizeCategory:](<init(preferredcontentsizecategory_).md>) — Creates a trait collection that contains only the specified content size category trait.
- [+ traitCollectionWithActiveAppearance:](<init(activeappearance_).md>) — Creates a trait collection that contains only the specified active appearance trait.
- [+ traitCollectionWithToolbarItemPresentationSize:](<init(toolbaritempresentationsize_).md>) — Creates a trait collection that contains only the specified toolbar item presentation size trait.
- [+ traitCollectionWithHDRHeadroomUsageLimit:](<init(hdrheadroomusagelimit_)-5zqph.md>)
