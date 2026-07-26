---
title: 'init(traitsFrom:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（17.0 起废弃）, iPadOS 8.0+（17.0 起废弃）, Mac Catalyst 13.1+（17.0 起废弃）, tvOS（17.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uitraitcollection/init(traitsfrom:)'
source_url: 'https://developer.apple.com/documentation/uikit/uitraitcollection/init(traitsfrom:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitraitcollection/init%28traitsfrom%3A%29.json'
content_hash: 'sha256:a716de8620f926bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITraitCollection](../uitraitcollection.md)

# init(traitsFrom:)

<sub>Initializer</sub>

Creates a trait collection that consists of traits merged from a specified array of trait collections.

> [!warning] Deprecated
> Use [init(mutations:)](<init(mutations_).md>) or [modifyingTraits(_:)](<modifyingtraits(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(traitsFrom traitCollections: [UITraitCollection])
```

## Parameters

- `traitCollections` — An array of [UITraitCollection](../uitraitcollection.md) objects.

## Return Value

A new trait collection consisting of traits merged from a specified `traitCollections` array.

## Discussion

This method takes an array of one or more trait collections and merges them to create a new trait collection. If the array contains more than one element, the highest-indexed element that contains a given trait is used for that trait. For example, the following code snippet creates a trait collection with a _compact_ horizontal size class, because the second element in the array overrides the first for that trait:

```objc
UITraitCollection *newHorizontalSizeClass1 = [UITraitCollection traitCollectionWithHorizontalSizeClass: UIUserInterfaceSizeClassRegular];
UITraitCollection *newHorizontalSizeClass2 = [UITraitCollection traitCollectionWithHorizontalSizeClass: UIUserInterfaceSizeClassCompact];
NSArray *traitArray = [NSArray arrayWithObjects: newHorizontalSizeClass1, newHorizontalSizeClass2, nil];
UITraitCollection *combinedTraits = [UITraitCollection traitCollectionWithTraitsFromCollections: traitArray];
```

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
- [+ traitCollectionWithDisplayGamut:](<init(displaygamut_).md>) — Creates a trait collection that contains only the specified display gamut trait.
- [+ traitCollectionWithLayoutDirection:](<init(layoutdirection_).md>) — Creates a trait collection that contains only the specified layout direction trait.
- [+ traitCollectionWithPreferredContentSizeCategory:](<init(preferredcontentsizecategory_).md>) — Creates a trait collection that contains only the specified content size category trait.
- [+ traitCollectionWithActiveAppearance:](<init(activeappearance_).md>) — Creates a trait collection that contains only the specified active appearance trait.
- [+ traitCollectionWithToolbarItemPresentationSize:](<init(toolbaritempresentationsize_).md>) — Creates a trait collection that contains only the specified toolbar item presentation size trait.
