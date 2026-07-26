---
title: 'setBackgroundImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibutton/setbackgroundimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/setbackgroundimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/setbackgroundimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:b2671f9fc047c9f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# setBackgroundImage(_:for:)

<sub>Instance Method</sub>

Sets the background image to use for the specified button state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundImage(_ image: UIImage?, for state: UIControl.State)
```

## Parameters

- `image` — The background image to use for the specified state.

- `state` — The state that uses the specified image. The values are described in [State](../uicontrol/state-swift.struct.md).

## Discussion

In general, if a property is not specified for a state, the default is to use the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) value. If the [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) value is not set, then the property defaults to a system value. Therefore, at a minimum, you should set the value for the normal state.

## See Also

### Managing images and tint color

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image used for a button state.
- [- imageForState:](<image(for_).md>) — Returns the image used for a button state.
- [- setImage:forState:](<setimage(__for_).md>) — Sets the image to use for the specified state.
- [- preferredSymbolConfigurationForImageInState:](<preferredsymbolconfigurationforimage(in_).md>) — Returns the preferred symbol configuration for a button state.
- [- setPreferredSymbolConfiguration:forImageInState:](<setpreferredsymbolconfiguration(__forimagein_).md>) — Sets the preferred symbol configuration for a button state.
- [tintColor](tintcolor.md) — The tint color to apply to the button title and image.
