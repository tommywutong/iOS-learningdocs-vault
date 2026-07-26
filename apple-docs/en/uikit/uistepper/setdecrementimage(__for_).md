---
title: 'setDecrementImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistepper/setdecrementimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/setdecrementimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/setdecrementimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:71c8daa677979a00'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# setDecrementImage(_:for:)

<sub>Instance Method</sub>

Sets the image to use for the decrement glyph of the control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setDecrementImage(_ image: UIImage?, for state: UIControl.State)
```

## Parameters

- `image` — The image to use for the decrement glyph.

- `state` — The control state in which you want to display the image.

## Discussion

The image you specify is used as a template image to create the final control. If you don’t specify a custom image, a minus (`-`) glyph is used.

## See Also

### Customizing appearance

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image associated with the specified control state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image for the control when it’s in the specified state.
- [- decrementImageForState:](<decrementimage(for_).md>) — Returns the image used for the decrement glyph of the control.
- [- dividerImageForLeftSegmentState:rightSegmentState:](<dividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image for the given combination of left and right states.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the image to use for the given combination of left and right states.
- [- incrementImageForState:](<incrementimage(for_).md>) — Returns the image used for the increment glyph of the control.
- [- setIncrementImage:forState:](<setincrementimage(__for_).md>) — Sets the image to use for the increment glyph of the control.
