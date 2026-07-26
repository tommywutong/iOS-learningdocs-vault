---
title: maximumTrackTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uislider/maximumtracktintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uislider/maximumtracktintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uislider/maximumtracktintcolor.json'
content_hash: 'sha256:923883ae1a3a708e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISlider](../uislider.md)

# maximumTrackTintColor

<sub>Instance Property</sub>

The color used to tint the default maximum track images.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var maximumTrackTintColor: UIColor? { get set }
```

## Discussion

Setting this property resets the maximum track images back to the slider’s default images; any custom images are released by the slider. Setting this property to `nil` resets the tint color to the default and removes any custom maximum track images.

> [!important] Important
> This property isn’t available when the user interface idiom is [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md) and [behavioralStyle](behavioralstyle.md) is [UIBehavioralStyleMac](../uibehavioralstyle/mac.md) — setting it while in this state throws an exception.

## See Also

### Changing the slider’s appearance

- [minimumValueImage](minimumvalueimage.md) — The image that represents the slider’s minimum value.
- [maximumValueImage](maximumvalueimage.md) — The image representing the slider’s maximum value.
- [minimumTrackTintColor](minimumtracktintcolor.md) — The color used to tint the default minimum track images.
- [currentMinimumTrackImage](currentminimumtrackimage.md) — The minimum track image currently being used to render the slider.
- [- minimumTrackImageForState:](<minimumtrackimage(for_).md>) — Returns the minimum track image associated with the specified control state.
- [- setMinimumTrackImage:forState:](<setminimumtrackimage(__for_).md>) — Assigns a minimum track image to the specified control states.
- [currentMaximumTrackImage](currentmaximumtrackimage.md) — Contains the maximum track image currently being used to render the slider.
- [- maximumTrackImageForState:](<maximumtrackimage(for_).md>) — Returns the maximum track image associated with the specified control state.
- [- setMaximumTrackImage:forState:](<setmaximumtrackimage(__for_).md>) — Assigns a maximum track image to the specified control states.
- [thumbTintColor](thumbtintcolor.md) — The color used to tint the default thumb images.
- [currentThumbImage](currentthumbimage.md) — The thumb image currently being used to render the slider.
- [- thumbImageForState:](<thumbimage(for_).md>) — Returns the thumb image associated with the specified control state.
- [- setThumbImage:forState:](<setthumbimage(__for_).md>) — Assigns a thumb image to the specified control states.
