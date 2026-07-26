---
title: maximumValueImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/maximumvalueimage
source_url: 'https://developer.apple.com/documentation/uikit/uislider/maximumvalueimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/maximumvalueimage.json'
content_hash: 'sha256:cfa24d1d524f21c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# maximumValueImage

<sub>Instance Property</sub>

The image representing the slider’s maximum value.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumValueImage: UIImage? { get set }
```

## Discussion

The image you specify must fit within the bounding rectangle returned by the [- maximumValueImageRectForBounds:](<maximumvalueimagerect(forbounds_).md>) method. If it doesn’t, the slider scales the image to fit. In addition, the slider lengthens or shortens its track as needed to accommodate the image in its bounding rectangle.

Because _maximum_ is a semantic concept, in a right-to-left interface, the slider automatically flips the image placement, always placing it at the trailing end of the slider’s track.

The default value of this property is `nil`.

> [!important] Important
> This property isn’t available when the user interface idiom is [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md) and [behavioralStyle](behavioralstyle.md) is [UIBehavioralStyleMac](../uibehavioralstyle/mac.md) — setting it while in this state throws an exception.

## See Also

### Changing the slider’s appearance

- [minimumValueImage](minimumvalueimage.md) — The image that represents the slider’s minimum value.
- [minimumTrackTintColor](minimumtracktintcolor.md) — The color used to tint the default minimum track images.
- [currentMinimumTrackImage](currentminimumtrackimage.md) — The minimum track image currently being used to render the slider.
- [- minimumTrackImageForState:](<minimumtrackimage(for_).md>) — Returns the minimum track image associated with the specified control state.
- [- setMinimumTrackImage:forState:](<setminimumtrackimage(__for_).md>) — Assigns a minimum track image to the specified control states.
- [maximumTrackTintColor](maximumtracktintcolor.md) — The color used to tint the default maximum track images.
- [currentMaximumTrackImage](currentmaximumtrackimage.md) — Contains the maximum track image currently being used to render the slider.
- [- maximumTrackImageForState:](<maximumtrackimage(for_).md>) — Returns the maximum track image associated with the specified control state.
- [- setMaximumTrackImage:forState:](<setmaximumtrackimage(__for_).md>) — Assigns a maximum track image to the specified control states.
- [thumbTintColor](thumbtintcolor.md) — The color used to tint the default thumb images.
- [currentThumbImage](currentthumbimage.md) — The thumb image currently being used to render the slider.
- [- thumbImageForState:](<thumbimage(for_).md>) — Returns the thumb image associated with the specified control state.
- [- setThumbImage:forState:](<setthumbimage(__for_).md>) — Assigns a thumb image to the specified control states.
