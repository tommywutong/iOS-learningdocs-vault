---
title: tintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uibutton/tintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uibutton/tintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibutton/tintcolor.json'
content_hash: 'sha256:4aedb3eb04a8b322'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIButton](../uibutton.md)

# tintColor

<sub>Instance Property</sub>

The tint color to apply to the button title and image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var tintColor: UIColor! { get set }
```

## Discussion

All subclasses of [UIView](../uiview.md) derive their behavior for [tintColor](../uiview/tintcolor.md) from the base class. See the discussion of [tintColor](../uiview/tintcolor.md) at the [UIView](../uiview.md) level for more information.

This property has no default effect for buttons with type [UIButtonTypeCustom](buttontype-swift.enum/custom.md). For custom buttons, you must implement any behavior related to [tintColor](tintcolor.md) yourself.

## See Also

### Managing images and tint color

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image used for a button state.
- [- imageForState:](<image(for_).md>) — Returns the image used for a button state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image to use for the specified button state.
- [- setImage:forState:](<setimage(__for_).md>) — Sets the image to use for the specified state.
- [- preferredSymbolConfigurationForImageInState:](<preferredsymbolconfigurationforimage(in_).md>) — Returns the preferred symbol configuration for a button state.
- [- setPreferredSymbolConfiguration:forImageInState:](<setpreferredsymbolconfiguration(__forimagein_).md>) — Sets the preferred symbol configuration for a button state.
