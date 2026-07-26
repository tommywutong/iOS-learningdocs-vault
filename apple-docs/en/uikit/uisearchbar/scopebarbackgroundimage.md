---
title: scopeBarBackgroundImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/scopebarbackgroundimage
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/scopebarbackgroundimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/scopebarbackgroundimage.json'
content_hash: 'sha256:b698edb2082638ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# scopeBarBackgroundImage

<sub>Instance Property</sub>

The background image for the scope bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var scopeBarBackgroundImage: UIImage? { get set }
```

## Discussion

Images that are 1 point wide or stretchable images are stretched, otherwise the image is tiled.

## See Also

### Related Documentation

- [backgroundImage](backgroundimage.md) — The background image for the search bar.

### Customizing the scope bar appearance

- [- scopeBarButtonBackgroundImageForState:](<scopebarbuttonbackgroundimage(for_).md>) — Returns the background image for the scope bar button in a given state.
- [- setScopeBarButtonBackgroundImage:forState:](<setscopebarbuttonbackgroundimage(__for_).md>) — Sets the background image for the scope bar button in a given state.
- [- scopeBarButtonDividerImageForLeftSegmentState:rightSegmentState:](<scopebarbuttondividerimage(forleftsegmentstate_rightsegmentstate_).md>) — Returns the divider image to use for a given combination of left and right segment states.
- [- setScopeBarButtonDividerImage:forLeftSegmentState:rightSegmentState:](<setscopebarbuttondividerimage(__forleftsegmentstate_rightsegmentstate_).md>) — Sets the divider image to use for a given combination of left and right segment states.
- [- scopeBarButtonTitleTextAttributesForState:](<scopebarbuttontitletextattributes(for_).md>) — Returns the text attributes for the search bar’s button’s title string for a given state.
- [- setScopeBarButtonTitleTextAttributes:forState:](<setscopebarbuttontitletextattributes(__for_).md>) — Sets the text attributes for the search bar’ button’s title string for a given state.
