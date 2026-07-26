---
title: preferredStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswitch/preferredstyle
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/preferredstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/preferredstyle.json'
content_hash: 'sha256:7542d7ddb092db6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# preferredStyle

<sub>Instance Property</sub>

The preferred display style for the switch.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredStyle: UISwitch.Style { get set }
```

## Discussion

Use this property to specify the display style that you prefer. If the style changes, the switch may generate a layout pass to update the display.

The default style is [UISwitchStyleAutomatic](style-swift.enum/automatic.md). For a list of styles, see [Style](style-swift.enum.md).

## See Also

### Setting the display style

- [Displaying a checkbox in your Mac app built with Mac Catalyst](../displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md) — Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [style](style-swift.property.md) — The display style for the switch.
- [Style](style-swift.enum.md) — Styles that determine the appearance of the switch.
- [title](title.md) — The title displayed next to a checkbox-style switch.
