---
title: 'setImage(_:for:state:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setimage(_:for:state:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setimage(_:for:state:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setimage%28_%3Afor%3Astate%3A%29.json'
content_hash: 'sha256:695f9a4f4e2536fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setImage(_:for:state:)

<sub>Instance Method</sub>

Sets the image for a given search bar icon type and control state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setImage(_ iconImage: UIImage?, for icon: UISearchBar.Icon, state: UIControl.State)
```

## Parameters

- `iconImage` — The image to use for the search bar icon identified by `icon` in the state identified by `state`.

- `icon` — An icon identifier constant.

- `state` — A control state. Valid states are [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) and [UIControlStateDisabled](../uicontrol/state-swift.struct/disabled.md).

## See Also

### Customizing the search bar appearance

- [backgroundImage](backgroundimage.md) — The background image for the search bar.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- positionAdjustmentForSearchBarIcon:](<positionadjustment(for_).md>) — Returns the position adjustment for a given icon.
- [- setPositionAdjustment:forSearchBarIcon:](<setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [inputAccessoryView](inputaccessoryview.md) — A custom input accessory view for the keyboard of the search bar.
- [- searchFieldBackgroundImageForState:](<searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [- setSearchFieldBackgroundImage:forState:](<setsearchfieldbackgroundimage(__for_).md>) — Sets the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](searchtextpositionadjustment.md) — The offset of the text within the search text field background.
