---
title: currentMaximumTrackImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/currentmaximumtrackimage
source_url: 'https://developer.apple.com/documentation/uikit/uislider/currentmaximumtrackimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/currentmaximumtrackimage.json'
content_hash: 'sha256:96f09be57e27219b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# currentMaximumTrackImage

<sub>Instance Property</sub>

Contains the maximum track image currently being used to render the slider.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var currentMaximumTrackImage: UIImage? { get }
```

## Discussion

Sliders can have different track images for different control states. The active control state determines which maximum track image is stored in this property. To get the maximum track image for a different control state, use the [- maximumTrackImageForState:](<maximumtrackimage(for_).md>) method.

If no custom track images have been set using the [- setMaximumTrackImage:forState:](<setmaximumtrackimage(__for_).md>) method, this property contains the value `nil`. In that situation, the slider uses the default maximum track image for drawing.

## See Also

### Changing the slider’s appearance

- [minimumValueImage](minimumvalueimage.md) — The image that represents the slider’s minimum value.
- [maximumValueImage](maximumvalueimage.md) — The image representing the slider’s maximum value.
- [minimumTrackTintColor](minimumtracktintcolor.md) — The color used to tint the default minimum track images.
- [currentMinimumTrackImage](currentminimumtrackimage.md) — The minimum track image currently being used to render the slider.
- [- minimumTrackImageForState:](<minimumtrackimage(for_).md>) — Returns the minimum track image associated with the specified control state.
- [- setMinimumTrackImage:forState:](<setminimumtrackimage(__for_).md>) — Assigns a minimum track image to the specified control states.
- [maximumTrackTintColor](maximumtracktintcolor.md) — The color used to tint the default maximum track images.
- [- maximumTrackImageForState:](<maximumtrackimage(for_).md>) — Returns the maximum track image associated with the specified control state.
- [- setMaximumTrackImage:forState:](<setmaximumtrackimage(__for_).md>) — Assigns a maximum track image to the specified control states.
- [thumbTintColor](thumbtintcolor.md) — The color used to tint the default thumb images.
- [currentThumbImage](currentthumbimage.md) — The thumb image currently being used to render the slider.
- [- thumbImageForState:](<thumbimage(for_).md>) — Returns the thumb image associated with the specified control state.
- [- setThumbImage:forState:](<setthumbimage(__for_).md>) — Assigns a thumb image to the specified control states.
