---
title: smartDashesType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/smartdashestype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/smartdashestype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/smartdashestype.json'
content_hash: 'sha256:85cd05c11f7a0662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# smartDashesType

<sub>Instance Property</sub>

The configuration state for smart dashes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var smartDashesType: UITextSmartDashesType { get set }
```

## Discussion

Use this property to configure whether UIKit converts two hyphens into an en-dash and three hyphens into an em-dash automatically. The default value of this property is [UITextSmartDashesTypeDefault](../uitextsmartdashestype/default.md), which selectively enables smart dashes based on the keyboard type.

## See Also

### Configuring the autoformatting behaviors

- [smartQuotesType](smartquotestype.md) — The configuration state for smart quotes.
- [UITextSmartQuotesType](../uitextsmartquotestype.md) — Constants that indicate whether to enable or disable smart quotes.
- [UITextSmartDashesType](../uitextsmartdashestype.md) — Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [smartInsertDeleteType](smartinsertdeletetype.md) — The configuration state for the smart insertion and deletion of space characters.
- [UITextSmartInsertDeleteType](../uitextsmartinsertdeletetype.md) — Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.
