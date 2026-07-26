---
title: 'setScopeBarButtonBackgroundImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setscopebarbuttonbackgroundimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setscopebarbuttonbackgroundimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setscopebarbuttonbackgroundimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:7f8c70ab72ced616'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setScopeBarButtonBackgroundImage(_:for:)

<sub>Instance Method</sub>

Sets the background image for the scope bar button in a given state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setScopeBarButtonBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State)
```

## Parameters

- `backgroundImage` — The background image for the scope bar button in `state`.

- `state` — A control state.

## Discussion

For more details, see [- scopeBarButtonBackgroundImageForState:](<scopebarbuttonbackgroundimage(for_).md>).

## See Also

### Customizing the scope bar appearance

- [scopeBarBackgroundImage](scopebarbackgroundimage.md) — The background image for the scope bar.
- [- scopeBarButtonBackgroundImageForState:](<scopebarbuttonbackgroundimage(for_).md>) — Returns the background image for the scope bar button in a given state.
- [- scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:](<scopebarbuttondividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image to use for a given combination of left and right segment states.
- [- setScopeBarButtonDividerImage:forLeftSegmentState:rightSegmentState:](<setscopebarbuttondividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the divider image to use for a given combination of left and right segment states.
- [- scopeBarButtonTitleTextAttributesForState:](<scopebarbuttontitletextattributes(for_).md>) — Returns the text attributes for the search bar’s button’s title string for a given state.
- [- setScopeBarButtonTitleTextAttributes:forState:](<setscopebarbuttontitletextattributes(__for_).md>) — Sets the text attributes for the search bar’ button’s title string for a given state.
