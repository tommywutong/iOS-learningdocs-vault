---
title: 'setBackgroundImage(_:for:barMetrics:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setbackgroundimage(_:for:barmetrics:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setbackgroundimage(_:for:barmetrics:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setbackgroundimage%28_%3Afor%3Abarmetrics%3A%29.json'
content_hash: 'sha256:4b46513ad9a0c41a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setBackgroundImage(_:for:barMetrics:)

<sub>Instance Method</sub>

Sets the image to use for the background in a given position and with given metrics.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setBackgroundImage(_ backgroundImage: UIImage?, for barPosition: UIBarPosition, barMetrics: UIBarMetrics)
```

## Parameters

- `backgroundImage` — The image to use for the search bar background in the position specified by `barPosition` and with the metrics specified by `barMetrics`.

- `barPosition` — A bar position constant.

- `barMetrics` — A bar metrics constant.

## See Also

### Customizing the search bar appearance

- [backgroundImage](backgroundimage.md) — The background image for the search bar.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- setImage:forSearchBarIcon:state:](<setimage(__for_state_).md>) — Sets the image for a given search bar icon type and control state.
- [- positionAdjustmentForSearchBarIcon:](<positionadjustment(for_).md>) — Returns the position adjustment for a given icon.
- [- setPositionAdjustment:forSearchBarIcon:](<setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [inputAccessoryView](inputaccessoryview.md) — A custom input accessory view for the keyboard of the search bar.
- [- searchFieldBackgroundImageForState:](<searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [- setSearchFieldBackgroundImage:forState:](<setsearchfieldbackgroundimage(__for_).md>) — Sets the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](searchtextpositionadjustment.md) — The offset of the text within the search text field background.
