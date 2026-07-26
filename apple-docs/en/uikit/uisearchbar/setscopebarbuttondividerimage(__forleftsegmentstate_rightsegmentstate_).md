---
title: 'setScopeBarButtonDividerImage(_:forLeftSegmentState:rightSegmentState:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setscopebarbuttondividerimage(_:forleftsegmentstate:rightsegmentstate:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setscopebarbuttondividerimage(_:forleftsegmentstate:rightsegmentstate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setscopebarbuttondividerimage%28_%3Aforleftsegmentstate%3Arightsegmentstate%3A%29.json'
content_hash: 'sha256:ff27b62060887c29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setScopeBarButtonDividerImage(_:forLeftSegmentState:rightSegmentState:)

<sub>Instance Method</sub>

Sets the divider image to use for a given combination of left and right segment states.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setScopeBarButtonDividerImage(_ dividerImage: UIImage?, forLeftSegmentState leftState: UIControl.State, rightSegmentState rightState: UIControl.State)
```

## Parameters

- `dividerImage` — The divider image to use for the combination of `leftState` and `rightState`.

- `leftState` — The state of the left segment for which to set the divider image. The state may be [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) or [UIControlStateSelected](../uicontrol/state-swift.struct/selected.md).

- `rightState` — The state of the right segment for which to set the divider image. The state may be [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) or [UIControlStateSelected](../uicontrol/state-swift.struct/selected.md).

## Discussion

To customize the segmented control appearance you need to provide divider images to go between two unselected segments (`leftSegmentState:UIControlStateNormal rightSegmentState:UIControlStateNormal`), selected on the left and unselected on the right (`leftSegmentState:UIControlStateSelected rightSegmentState:UIControlStateNormal`), and unselected on the left and selected on the right (`leftSegmentState:UIControlStateNormal rightSegmentState:UIControlStateSelected`).

## See Also

### Customizing the scope bar appearance

- [scopeBarBackgroundImage](scopebarbackgroundimage.md) — The background image for the scope bar.
- [- scopeBarButtonBackgroundImageForState:](<scopebarbuttonbackgroundimage(for_).md>) — Returns the background image for the scope bar button in a given state.
- [- setScopeBarButtonBackgroundImage:forState:](<setscopebarbuttonbackgroundimage(__for_).md>) — Sets the background image for the scope bar button in a given state.
- [- scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:](<scopebarbuttondividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image to use for a given combination of left and right segment states.
- [- scopeBarButtonTitleTextAttributesForState:](<scopebarbuttontitletextattributes(for_).md>) — Returns the text attributes for the search bar’s button’s title string for a given state.
- [- setScopeBarButtonTitleTextAttributes:forState:](<setscopebarbuttontitletextattributes(__for_).md>) — Sets the text attributes for the search bar’ button’s title string for a given state.
