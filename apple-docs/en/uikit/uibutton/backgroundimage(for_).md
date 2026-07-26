---
title: 'backgroundImage(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/backgroundimage(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/backgroundimage(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/backgroundimage%28for%3A%29.json'
content_hash: 'sha256:2e79300411cbd4e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# backgroundImage(for:)

<sub>Instance Method</sub>

Returns the background image used for a button state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func backgroundImage(for state: UIControl.State) -> UIImage?
```

## Parameters

- `state` — The state that uses the background image. Possible values are described in [State](../uicontrol/state-swift.struct.md).

## Return Value

The background image used for the specified state.

## See Also

### Managing images and tint color

- [- imageForState:](<image(for_).md>) — Returns the image used for a button state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image to use for the specified button state.
- [- setImage:forState:](<setimage(__for_).md>) — Sets the image to use for the specified state.
- [- preferredSymbolConfigurationForImageInState:](<preferredsymbolconfigurationforimage(in_).md>) — Returns the preferred symbol configuration for a button state.
- [- setPreferredSymbolConfiguration:forImageInState:](<setpreferredsymbolconfiguration(__forimagein_).md>) — Sets the preferred symbol configuration for a button state.
- [tintColor](tintcolor.md) — The tint color to apply to the button title and image.
