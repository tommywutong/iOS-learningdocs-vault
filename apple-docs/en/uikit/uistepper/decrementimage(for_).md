---
title: 'decrementImage(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistepper/decrementimage(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/decrementimage(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/decrementimage%28for%3A%29.json'
content_hash: 'sha256:e43d4256dd7eeeec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# decrementImage(for:)

<sub>Instance Method</sub>

Returns the image used for the decrement glyph of the control.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func decrementImage(for state: UIControl.State) -> UIImage?
```

## Parameters

- `state` — The control state in which the image is displayed.

## Return Value

The image used for the decrement glyph of the control.

## See Also

### Customizing appearance

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image associated with the specified control state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image for the control when it’s in the specified state.
- [- setDecrementImage:forState:](<setdecrementimage(__for_).md>) — Sets the image to use for the decrement glyph of the control.
- [- dividerImageForLeftSegmentState:rightSegmentState:](<dividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image for the given combination of left and right states.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the image to use for the given combination of left and right states.
- [- incrementImageForState:](<incrementimage(for_).md>) — Returns the image used for the increment glyph of the control.
- [- setIncrementImage:forState:](<setincrementimage(__for_).md>) — Sets the image to use for the increment glyph of the control.
