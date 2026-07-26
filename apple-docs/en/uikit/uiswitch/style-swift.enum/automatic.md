---
title: UISwitch.Style.automatic
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiswitch/style-swift.enum/automatic
source_url: 'https://developer.apple.com/documentation/uikit/uiswitch/style-swift.enum/automatic'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiswitch/style-swift.enum/automatic.json'
content_hash: 'sha256:2b979db0a048d500'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UISwitch](../../uiswitch.md) · [Style](../style-swift.enum.md)

# UISwitch.Style.automatic

<sub>Case</sub>

A style indicating that the system chooses the appearance of the switch according to the current user interface idiom.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case automatic
```

## Discussion

The system chooses the [UISwitchStyleCheckbox](checkbox.md) style when the user interface idiom is [UIUserInterfaceIdiomMac](../../uiuserinterfaceidiom/mac.md); otherwise, it chooses the [UISwitchStyleSliding](sliding.md) style.

## See Also

### Styles

- [UISwitchStyleCheckbox](checkbox.md) — A style indicating that the switch appears as a Mac-style checkbox.
- [UISwitchStyleSliding](sliding.md) — A style indicating that the switch appears as an on/off slider.
