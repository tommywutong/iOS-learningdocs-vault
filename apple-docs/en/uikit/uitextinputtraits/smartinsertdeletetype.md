---
title: smartInsertDeleteType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/smartinsertdeletetype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/smartinsertdeletetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/smartinsertdeletetype.json'
content_hash: 'sha256:c7204cdbc4840cff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# smartInsertDeleteType

<sub>Instance Property</sub>

The configuration state for the smart insertion and deletion of space characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var smartInsertDeleteType: UITextSmartInsertDeleteType { get set }
```

## Discussion

Use this property to configure whether UIKit may insert an extra space after a paste operation or delete one or two spaces after a cut or delete operation. The default value of this property is [UITextSmartInsertDeleteTypeDefault](../uitextsmartinsertdeletetype/default.md), which selectively enables the behavior based on the keyboard type.

## See Also

### Configuring the autoformatting behaviors

- [smartQuotesType](smartquotestype.md) — The configuration state for smart quotes.
- [UITextSmartQuotesType](../uitextsmartquotestype.md) — Constants that indicate whether to enable or disable smart quotes.
- [smartDashesType](smartdashestype.md) — The configuration state for smart dashes.
- [UITextSmartDashesType](../uitextsmartdashestype.md) — Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [UITextSmartInsertDeleteType](../uitextsmartinsertdeletetype.md) — Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.
