---
title: backgroundViewClass
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（9.0 起废弃）, iPadOS 5.0+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/backgroundviewclass
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/backgroundviewclass'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/backgroundviewclass.json'
content_hash: 'sha256:13cd567f35a67127'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# backgroundViewClass

<sub>Instance Property</sub>

The class to use for displaying the popover background content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var backgroundViewClass: AnyClass? { get set }
```

## Discussion

The default value of this property is `nil`, which indicates that the popover controller should use the default popover appearance. Setting this property to a value other than `nil` causes the popover controller to use the specified class to draw the popover’s background content. The class you specify must be a subclass of [UIPopoverBackgroundView](../uipopoverbackgroundview.md).

## See Also

### Customizing the popover appearance

- [popoverLayoutMargins](layoutmargins.md) — The margins that define the portion of the screen in which it is permissible to display the popover. _(deprecated)_
- [backgroundColor](backgroundcolor.md) — The color of the popover’s backdrop view. _(deprecated)_
