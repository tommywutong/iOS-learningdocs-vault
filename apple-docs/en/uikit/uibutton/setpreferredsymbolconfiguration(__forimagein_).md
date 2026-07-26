---
title: 'setPreferredSymbolConfiguration(_:forImageIn:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/setpreferredsymbolconfiguration(_:forimagein:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/setpreferredsymbolconfiguration(_:forimagein:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/setpreferredsymbolconfiguration%28_%3Aforimagein%3A%29.json'
content_hash: 'sha256:3b8c02e2c2588734'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setPreferredSymbolConfiguration(_:forImageIn:)

<sub>Instance Method</sub>

Sets the preferred symbol configuration for a button state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setPreferredSymbolConfiguration(_ configuration: UIImage.SymbolConfiguration?, forImageIn state: UIControl.State)
```

## Parameters

- `configuration` — The image symbol configuration for the specified state.

- `state` — The state that uses the specified image symbol configuration. Possible values are described in [State](../uicontrol/state-swift.struct.md).

## See Also

### Managing images and tint color

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image used for a button state.
- [- imageForState:](<image(for_).md>) — Returns the image used for a button state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image to use for the specified button state.
- [- setImage:forState:](<setimage(__for_).md>) — Sets the image to use for the specified state.
- [- preferredSymbolConfigurationForImageInState:](<preferredsymbolconfigurationforimage(in_).md>) — Returns the preferred symbol configuration for a button state.
- [tintColor](tintcolor.md) — The tint color to apply to the button title and image.
