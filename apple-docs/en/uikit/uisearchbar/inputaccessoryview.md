---
title: inputAccessoryView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisearchbar/inputaccessoryview
source_url: 'https://developer.apple.com/documentation/uikit/uisearchbar/inputaccessoryview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisearchbar/inputaccessoryview.json'
content_hash: 'sha256:f384f02dc4a37cf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISearchBar](../uisearchbar.md)

# inputAccessoryView

<sub>Instance Property</sub>

A custom input accessory view for the keyboard of the search bar.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var inputAccessoryView: UIView? { get set }
```

## Discussion

The default value is `nil`. When non-`nil`, this property represents a custom input accessory view that will be placed onto the search bar’s system-supplied keyboard.

## See Also

### Customizing the search bar appearance

- [backgroundImage](backgroundimage.md) — The background image for the search bar.
- [- backgroundImageForBarPosition:barMetrics:](<backgroundimage(for_barmetrics_).md>) — Returns the image used for the background in a given position and with given metrics.
- [- setBackgroundImage:forBarPosition:barMetrics:](<setbackgroundimage(__for_barmetrics_).md>) — Sets the image to use for the background in a given position and with given metrics.
- [- imageForSearchBarIcon:state:](<image(for_state_).md>) — Returns the image for a given search bar icon type and control state.
- [- setImage:forSearchBarIcon:state:](<setimage(__for_state_).md>) — Sets the image for a given search bar icon type and control state.
- [- positionAdjustmentForSearchBarIcon:](<positionadjustment(for_).md>) — Returns the position adjustment for a given icon.
- [- setPositionAdjustment:forSearchBarIcon:](<setpositionadjustment(__for_).md>) — Returns the position adjustment for a given icon.
- [- searchFieldBackgroundImageForState:](<searchfieldbackgroundimage(for_).md>) — Returns the search text field image for a given state.
- [- setSearchFieldBackgroundImage:forState:](<setsearchfieldbackgroundimage(__for_).md>) — Sets the search text field image for a given state.
- [searchFieldBackgroundPositionAdjustment](searchfieldbackgroundpositionadjustment.md) — The offset of the search text field background in the search bar.
- [searchTextPositionAdjustment](searchtextpositionadjustment.md) — The offset of the text within the search text field background.
