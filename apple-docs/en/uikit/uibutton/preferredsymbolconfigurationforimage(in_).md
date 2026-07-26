---
title: 'preferredSymbolConfigurationForImage(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/preferredsymbolconfigurationforimage(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/preferredsymbolconfigurationforimage(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/preferredsymbolconfigurationforimage%28in%3A%29.json'
content_hash: 'sha256:6d46333d10f41938'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# preferredSymbolConfigurationForImage(in:)

<sub>Instance Method</sub>

Returns the preferred symbol configuration for a button state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func preferredSymbolConfigurationForImage(in state: UIControl.State) -> UIImage.SymbolConfiguration?
```

## Parameters

- `state` — The state that uses the symbol configuration. Possible values are described in [State](../uicontrol/state-swift.struct.md).

## See Also

### Managing images and tint color

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image used for a button state.
- [- imageForState:](<image(for_).md>) — Returns the image used for a button state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image to use for the specified button state.
- [- setImage:forState:](<setimage(__for_).md>) — Sets the image to use for the specified state.
- [- setPreferredSymbolConfiguration:forImageInState:](<setpreferredsymbolconfiguration(__forimagein_).md>) — Sets the preferred symbol configuration for a button state.
- [tintColor](tintcolor.md) — The tint color to apply to the button title and image.
