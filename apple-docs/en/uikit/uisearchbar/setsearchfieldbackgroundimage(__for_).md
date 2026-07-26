---
title: 'setSearchFieldBackgroundImage(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/setsearchfieldbackgroundimage(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/setsearchfieldbackgroundimage(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/setsearchfieldbackgroundimage%28_%3Afor%3A%29.json'
content_hash: 'sha256:f83b716c8f1edf3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# setSearchFieldBackgroundImage(_:for:)

<sub>Instance Method</sub>

Sets the search text field image for a given state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setSearchFieldBackgroundImage(_ backgroundImage: UIImage?, for state: UIControl.State)
```

## Parameters

- `backgroundImage` — The search text field image to use for `state`.

- `state` — A control state. Valid states are [UIControlStateNormal](../uicontrol/state-swift.struct/normal.md) and [UIControlStateDisabled](../uicontrol/state-swift.struct/disabled.md).

## See Also

### Customizing the search bar appearance

- [backgroundImage](backgroundimage.md) — The background image for the search bar.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- setImage:forSearchBarIcon:state:](<setimage(__for_state_).md>) — Sets the image for a given search bar icon type and control state.
- [- positionAdjustmentForSearchBarIcon:](<positionadjustment(for_).md>) — Returns the position adjustment for a given icon.
- [- setPositionAdjustment:forSearchBarIcon:](<setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [inputAccessoryView](inputaccessoryview.md) — A custom input accessory view for the keyboard of the search bar.
- [- searchFieldBackgroundImageForState:](<searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](searchtextpositionadjustment.md) — The offset of the text within the search text field background.
