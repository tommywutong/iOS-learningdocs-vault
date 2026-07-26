---
title: 'setScopeBarButtonTitleTextAttributes(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setscopebarbuttontitletextattributes(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setscopebarbuttontitletextattributes(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setscopebarbuttontitletextattributes%28_%3Afor%3A%29.json'
content_hash: 'sha256:55cba910b031698b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setScopeBarButtonTitleTextAttributes(_:for:)

<sub>Instance Method</sub>

Sets the text attributes for the search bar’ button’s title string for a given state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setScopeBarButtonTitleTextAttributes(_ attributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

## Parameters

- `attributes` — A dictionary containing key-value pairs specifying the text attributes to use for `state`. You may specify the font, text color, text shadow color, and text shadow offset, using the keys found in NSString UIKit Additions Reference.

- `state` — A control state.

## See Also

### Customizing the scope bar appearance

- [scopeBarBackgroundImage](scopebarbackgroundimage.md) — The background image for the scope bar.
- [- scopeBarButtonBackgroundImageForState:](<scopebarbuttonbackgroundimage(for_).md>) — Returns the background image for the scope bar button in a given state.
- [- setScopeBarButtonBackgroundImage:forState:](<setscopebarbuttonbackgroundimage(__for_).md>) — Sets the background image for the scope bar button in a given state.
- [- scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:](<scopebarbuttondividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image to use for a given combination of left and right segment states.
- [- setScopeBarButtonDividerImage:forLeftSegmentState:rightSegmentState:](<setscopebarbuttondividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the divider image to use for a given combination of left and right segment states.
- [- scopeBarButtonTitleTextAttributesForState:](<scopebarbuttontitletextattributes(for_).md>) — Returns the text attributes for the search bar’s button’s title string for a given state.
