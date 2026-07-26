---
title: 'positionAdjustment(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uisearchbar/positionadjustment(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/positionadjustment(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/positionadjustment%28for%3A%29.json'
content_hash: 'sha256:a7eaa4b667f0ea4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# positionAdjustment(for:)

<sub>Instance Method</sub>

Returns the position adjustment for a given icon.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func positionAdjustment(for icon: UISearchBar.Icon) -> UIOffset
```

## Parameters

- `icon` — An icon identifier constant.

## Return Value

The position adjustment for the icon identified by `icon`.

## Discussion

The offset is used to adjust the position of an icon within the search text field.

## See Also

### Customizing the search bar appearance

- [backgroundImage](backgroundimage.md) — The background image for the search bar.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- setImage:forSearchBarIcon:state:](<setimage(__for_state_).md>) — Sets the image for a given search bar icon type and control state.
- [- setPositionAdjustment:forSearchBarIcon:](<setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [inputAccessoryView](inputaccessoryview.md) — A custom input accessory view for the keyboard of the search bar.
- [- searchFieldBackgroundImageForState:](<searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [- setSearchFieldBackgroundImage:forState:](<setsearchfieldbackgroundimage(__for_).md>) — Sets the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](searchtextpositionadjustment.md) — The offset of the text within the search text field background.
