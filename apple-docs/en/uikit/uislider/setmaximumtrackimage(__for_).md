---
title: 'setMaximumTrackImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uislider/setmaximumtrackimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uislider/setmaximumtrackimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/setmaximumtrackimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:3829231ff7fb301c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# setMaximumTrackImage(_:for:)

<sub>Instance Method</sub>

Assigns a maximum track image to the specified control states.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setMaximumTrackImage(_ image: UIImage?, for state: UIControl.State)
```

## Parameters

- `image` — The maximum track image to associate with the specified states.

- `state` — The control state with which to associate the image.

## Discussion

Because the movement of the slider’s thumb changes the width of the area occupied by the maximum track image, the image width must change accordingly. To accommodate this requirement, specify track images as stretchable images that can grow or shrink to fill the available space. For information about how to create stretchable images, see [UIImage](../uiimage.md).

When you specify a custom maximum track image, the slider ignores the custom maximum track tint color, if any.

Sliders respond to user interaction with dynamic effects and appearance. If you use images to customize the appearance of the track, then the slider doesn’t apply the dynamic effects or alter the appearance.

> [!important] Important
> This method isn’t available when the user interface idiom is [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md) and [behavioralStyle](behavioralstyle.md) is [UIBehavioralStyleMac](../uibehavioralstyle/mac.md) — calling it while in this state throws an exception.

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
- [thumbTintColor](thumbtintcolor.md) — The color used to tint the default thumb images.
- [currentThumbImage](currentthumbimage.md) — The thumb image currently being used to render the slider.
- [- thumbImageForState:](<thumbimage(for_).md>) — Returns the thumb image associated with the specified control state.
- [- setThumbImage:forState:](<setthumbimage(__for_).md>) — Assigns a thumb image to the specified control states.
