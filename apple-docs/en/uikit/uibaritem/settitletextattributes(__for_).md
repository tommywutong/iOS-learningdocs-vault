---
title: 'setTitleTextAttributes(_:for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uibaritem/settitletextattributes(_:for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uibaritem/settitletextattributes(_:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uibaritem/settitletextattributes%28_%3Afor%3A%29.json'
content_hash: 'sha256:5e3cf67799b37845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIBarItem](../uibaritem.md)

# setTitleTextAttributes(_:for:)

<sub>Instance Method</sub>

Sets the title’s text attributes for a given control state.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setTitleTextAttributes(_ attributes: [NSAttributedString.Key : Any]?, for state: UIControl.State)
```

## Parameters

- `attributes` — A dictionary containing key-value pairs for text attributes. You can specify the font, text color, text shadow color, and text shadow offset using the keys listed in NSString UIKit Additions Reference.

- `state` — The control state for which you want to set the text attributes for the title.

## See Also

### Customizing appearance

- [- titleTextAttributesForState:](<titletextattributes(for_).md>) — Returns the title’s text attributes for a given control state.
