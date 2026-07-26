---
title: backgroundImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/backgroundimage
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/backgroundimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/backgroundimage.json'
content_hash: 'sha256:f16d67847060a324'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# backgroundImage

<sub>Instance Property</sub>

The background image for the search bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var backgroundImage: UIImage? { get set }
```

## Discussion

Images that are 1 point wide or stretchable images are stretched, otherwise the image is tiled.

## See Also

### Customizing the search bar appearance

- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- setImage:forSearchBarIcon:state:](<setimage(__for_state_).md>) — Sets the image for a given search bar icon type and control state.
- [- positionAdjustmentForSearchBarIcon:](<positionadjustment(for_).md>) — Returns the position adjustment for a given icon.
- [- setPositionAdjustment:forSearchBarIcon:](<setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [inputAccessoryView](inputaccessoryview.md) — A custom input accessory view for the keyboard of the search bar.
- [- searchFieldBackgroundImageForState:](<searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [- setSearchFieldBackgroundImage:forState:](<setsearchfieldbackgroundimage(__for_).md>) — Sets the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](searchtextpositionadjustment.md) — The offset of the text within the search text field background.
