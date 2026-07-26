---
title: 'setDividerImage(_:forLeftSegmentState:rightSegmentState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uistepper/setdividerimage(_:forleftsegmentstate:rightsegmentstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uistepper/setdividerimage(_:forleftsegmentstate:rightsegmentstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistepper/setdividerimage%28_%3Aforleftsegmentstate%3Arightsegmentstate%3A%29.json'
content_hash: 'sha256:696dd1bb4c25a4fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStepper](../uistepper.md)

# setDividerImage(_:forLeftSegmentState:rightSegmentState:)

<sub>Instance Method</sub>

Sets the image to use for the given combination of left and right states.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func setDividerImage(_ image: UIImage?, forLeftSegmentState leftState: UIControl.State, rightSegmentState rightState: UIControl.State)
```

## Parameters

- `image` — The divider image to use.

- `leftState` — The state of the left side of the control.

- `rightState` — The state of the right side of the control.

## See Also

### Customizing appearance

- [- backgroundImageForState:](<backgroundimage(for_).md>) — Returns the background image associated with the specified control state.
- [- setBackgroundImage:forState:](<setbackgroundimage(__for_).md>) — Sets the background image for the control when it’s in the specified state.
- [- decrementImageForState:](<decrementimage(for_).md>) — Returns the image used for the decrement glyph of the control.
- [- setDecrementImage:forState:](<setdecrementimage(__for_).md>) — Sets the image to use for the decrement glyph of the control.
- [- dividerImageForLeftSegmentState:rightSegmentState:](<dividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image for the given combination of left and right states.
- [- incrementImageForState:](<incrementimage(for_).md>) — Returns the image used for the increment glyph of the control.
- [- setIncrementImage:forState:](<setincrementimage(__for_).md>) — Sets the image to use for the increment glyph of the control.
