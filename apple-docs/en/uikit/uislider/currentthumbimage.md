---
title: currentThumbImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/currentthumbimage
source_url: 'https://developer.apple.com/documentation/uikit/uislider/currentthumbimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/currentthumbimage.json'
content_hash: 'sha256:8202142cd3e92d73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# currentThumbImage

<sub>Instance Property</sub>

The thumb image currently being used to render the slider.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var currentThumbImage: UIImage? { get }
```

## Discussion

Sliders can have different thumb images for different control states. The active control state determines which thumb image is stored in this property. To get the thumb image for a different control state, use the [- thumbImageForState:](<thumbimage(for_).md>) method.

If no custom thumb images have been set using the [- setThumbImage:forState:](<setthumbimage(__for_).md>) method, this property is `nil`. In that situation, the slider uses the default thumb image for drawing.

## See Also

### Changing the slider’s appearance

- [minimumValueImage](minimumvalueimage.md) — The image that represents the slider’s minimum value.
- [maximumValueImage](maximumvalueimage.md) — The image representing the slider’s maximum value.
- [minimumTrackTintColor](minimumtracktintcolor.md) — The color used to tint the default minimum track images.
- [currentMinimumTrackImage](currentminimumtrackimage.md) — The minimum track image currently being used to render the slider.
- [- minimumTrackImageForState:](<minimumtrackimage(for_).md>) — Returns the minimum track image associated with the specified control state.
- [- setMinimumTrackImage:forState:](<setminimumtrackimage(__for_).md>) — Assigns a minimum track image to the specified control states.
- [maximumTrackTintColor](maximumtracktintcolor.md) — The color used to tint the default maximum track images.
- [currentMaximumTrackImage](currentmaximumtrackimage.md) — Contains the maximum track image currently being used to render the slider.
- [- maximumTrackImageForState:](<maximumtrackimage(for_).md>) — Returns the maximum track image associated with the specified control state.
- [- setMaximumTrackImage:forState:](<setmaximumtrackimage(__for_).md>) — Assigns a maximum track image to the specified control states.
- [thumbTintColor](thumbtintcolor.md) — The color used to tint the default thumb images.
- [- thumbImageForState:](<thumbimage(for_).md>) — Returns the thumb image associated with the specified control state.
- [- setThumbImage:forState:](<setthumbimage(__for_).md>) — Assigns a thumb image to the specified control states.
