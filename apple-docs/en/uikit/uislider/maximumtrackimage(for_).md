---
title: 'maximumTrackImage(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uislider/maximumtrackimage(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uislider/maximumtrackimage(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/maximumtrackimage%28for%3A%29.json'
content_hash: 'sha256:a7914daf21042e66'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# maximumTrackImage(for:)

<sub>Instance Method</sub>

Returns the maximum track image associated with the specified control state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func maximumTrackImage(for state: UIControl.State) -> UIImage?
```

## Parameters

- `state` — The control state whose maximum track image you want to use. Specify a single control state value for this parameter.

## Return Value

The maximum track image associated with the specified state, or `nil` if an appropriate image could not be retrieved. This method might return `nil` if you specify multiple control states in the `state` parameter. For a description of track images, see [Customize the slider’s appearance](../uislider.md#Customize-the-sliders-appearance).

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
- [- setMaximumTrackImage:forState:](<setmaximumtrackimage(__for_).md>) — Assigns a maximum track image to the specified control states.
- [thumbTintColor](thumbtintcolor.md) — The color used to tint the default thumb images.
- [currentThumbImage](currentthumbimage.md) — The thumb image currently being used to render the slider.
- [- thumbImageForState:](<thumbimage(for_).md>) — Returns the thumb image associated with the specified control state.
- [- setThumbImage:forState:](<setthumbimage(__for_).md>) — Assigns a thumb image to the specified control states.
