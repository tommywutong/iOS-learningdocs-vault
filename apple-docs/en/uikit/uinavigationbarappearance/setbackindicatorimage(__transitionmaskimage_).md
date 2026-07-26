---
title: 'setBackIndicatorImage(_:transitionMaskImage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uinavigationbarappearance/setbackindicatorimage(_:transitionmaskimage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uinavigationbarappearance/setbackindicatorimage(_:transitionmaskimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uinavigationbarappearance/setbackindicatorimage%28_%3Atransitionmaskimage%3A%29.json'
content_hash: 'sha256:20720e95370fd725'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UINavigationBarAppearance](../uinavigationbarappearance.md)

# setBackIndicatorImage(_:transitionMaskImage:)

<sub>Instance Method</sub>

Sets the back button indicator image and its transition mask.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackIndicatorImage(_ backIndicatorImage: UIImage?, transitionMaskImage backIndicatorTransitionMaskImage: UIImage?)
```

## Parameters

- `backIndicatorImage` — The image to display on the leading edge of the back button.

- `backIndicatorTransitionMaskImage` — The image for masking content flowing under the back indicator image during push and pop transitions.

## Discussion

If you specify `nil` for either [backIndicatorImage](backindicatorimage.md) or [backIndicatorTransitionMaskImage](backindicatortransitionmaskimage.md), this method resets both images to their default values.

## See Also

### Configuring the Back button

- [backButtonAppearance](backbuttonappearance.md) — The appearance attributes for the back button.
- [backIndicatorImage](backindicatorimage.md) — The image to display on the leading edge of the back button.
- [backIndicatorTransitionMaskImage](backindicatortransitionmaskimage.md) — The image for masking content flowing under the back indicator image during push and pop transitions.
