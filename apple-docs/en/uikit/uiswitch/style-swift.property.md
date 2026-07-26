---
title: style
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswitch/style-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/style-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/style-swift.property.json'
content_hash: 'sha256:2975b2aa99a654af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISwitch](../uiswitch.md)

# style

<sub>Instance Property</sub>

The display style for the switch.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var style: UISwitch.Style { get }
```

## Discussion

This property returns the resolved style based on the user interface idiom, and never returns [UISwitchStyleAutomatic](style-swift.enum/automatic.md).

## See Also

### Setting the display style

- [Displaying a checkbox in your Mac app built with Mac Catalyst](../displaying-a-checkbox-in-your-mac-app-built-with-mac-catalyst.md) — Present a switch control as a Mac-style checkbox when your app runs in the Mac user interface idiom.
- [preferredStyle](preferredstyle.md) — The preferred display style for the switch.
- [Style](style-swift.enum.md) — Styles that determine the appearance of the switch.
- [title](title.md) — The title displayed next to a checkbox-style switch.
