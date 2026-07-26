---
title: backButtonAppearance
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uinavigationbarappearance/backbuttonappearance
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbarappearance/backbuttonappearance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbarappearance/backbuttonappearance.json'
content_hash: 'sha256:ae47a92e021730cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarAppearance](../uinavigationbarappearance.md)

# backButtonAppearance

<sub>Instance Property</sub>

The appearance attributes for the back button.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@NSCopying var backButtonAppearance: UIBarButtonItemAppearance { get set }
```

## Discussion

If you don’t change the value of this property, the navigation bar applies the attributes from the [buttonAppearance](buttonappearance.md) property.

## See Also

### Configuring the Back button

- [backIndicatorImage](backindicatorimage.md) — The image to display on the leading edge of the back button.
- [backIndicatorTransitionMaskImage](backindicatortransitionmaskimage.md) — The image for masking content flowing under the back indicator image during push and pop transitions.
- [- setBackIndicatorImage:transitionMaskImage:](<setbackindicatorimage(__transitionmaskimage_).md>) — Sets the back button indicator image and its transition mask.
