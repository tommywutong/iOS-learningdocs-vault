---
title: 'setImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/setimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/setimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/setimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:a670559e50eb9a42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setImage(_:for:)

<sub>Instance Method</sub>

Sets the image to use for the specified state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setImage(_ image: UIImage?, for state: UIControl.State)
```

## Parameters

- `image` — The image to use for the specified state.

- `state` — The state that uses the specified image. The values are described in [State](../uicontrol/state-swift.struct.md).

## Discussion

At a minimum, always set an image for the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state when associating images to a button. If you don’t specify an image for the other states, the button uses the image associated with [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md). If you don’t specify an image for the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) state, the button uses a system value.

> [!important] Important
> When the user interface idiom is [UIUserInterfaceIdiomMac](../uiuserinterfaceidiom/mac.md) and [behavioralStyle](behavioralstyle.md) is [UIBehavioralStyleMac](../uibehavioralstyle/mac.md), your app throws an exception if you use this method to set the image for any state other than [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md).

## See Also

### Managing images and tint color

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image used for a button state.
- [- imageForState:](<image(for_).md>) — Returns the image used for a button state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image to use for the specified button state.
- [- preferredSymbolConfigurationForImageInState:](<preferredsymbolconfigurationforimage(in_).md>) — Returns the preferred symbol configuration for a button state.
- [- setPreferredSymbolConfiguration:forImageInState:](<setpreferredsymbolconfiguration(__forimagein_).md>) — Sets the preferred symbol configuration for a button state.
- [tintColor](tintcolor.md) — The tint color to apply to the button title and image.
