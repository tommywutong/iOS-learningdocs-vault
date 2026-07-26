---
title: backgroundColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（9.0 起废弃）, iPadOS 7.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/backgroundcolor
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/backgroundcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/backgroundcolor.json'
content_hash: 'sha256:a4a475142b3d6f62'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# backgroundColor

<sub>Instance Property</sub>

The color of the popover’s backdrop view.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@NSCopying var backgroundColor: UIColor? { get set }
```

## Discussion

Use this property to customize the background color of your popover. Changing the value of this property while the popover is visible triggers an animated changeover to the new color. The default value of this property is `nil`, which corresponds to the default background color.

## See Also

### Customizing the popover appearance

- [popoverLayoutMargins](layoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover. _(deprecated)_
- [popoverBackgroundViewClass](backgroundviewclass.md) — The class to use for displaying the popover background content. _(deprecated)_
