---
title: 'dividerImage(forLeftSegmentState:rightSegmentState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistepper/dividerimage(forleftsegmentstate:rightsegmentstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/dividerimage(forleftsegmentstate:rightsegmentstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/dividerimage%28forleftsegmentstate%3Arightsegmentstate%3A%29.json'
content_hash: 'sha256:e9522ddb799642f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# dividerImage(forLeftSegmentState:rightSegmentState:)

<sub>Instance Method</sub>

Returns the divider image for the given combination of left and right states.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dividerImage(forLeftSegmentState state: UIControl.State, rightSegmentState state: UIControl.State) -> UIImage?
```

## Return Value

The image used for the specified combination of left and right states.

## See Also

### Customizing appearance

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image associated with the specified control state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image for the control when it’s in the specified state.
- [- decrementImageForState:](<decrementimage(for_).md>) — Returns the image used for the decrement glyph of the control.
- [- setDecrementImage:forState:](<setdecrementimage(__for_).md>) — Sets the image to use for the decrement glyph of the control.
- [- setDividerImage:forLeftSegmentState:rightSegmentState:](<setdividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the image to use for the given combination of left and right states.
- [- incrementImageForState:](<incrementimage(for_).md>) — Returns the image used for the increment glyph of the control.
- [- setIncrementImage:forState:](<setincrementimage(__for_).md>) — Sets the image to use for the increment glyph of the control.
