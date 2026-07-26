---
title: smartQuotesType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextinputtraits/smartquotestype
source_url: 'https://developer.apple.com/documentation/uikit/uitextinputtraits/smartquotestype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextinputtraits/smartquotestype.json'
content_hash: 'sha256:fb1ebbcad404f584'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextInputTraits](../uitextinputtraits.md)

# smartQuotesType

<sub>Instance Property</sub>

The configuration state for smart quotes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional var smartQuotesType: UITextSmartQuotesType { get set }
```

## Discussion

Use this property to configure whether UIKit replaces straight apostrophes and quotation marks with region-specific glyphs. The default value of this property is [UITextSmartQuotesTypeDefault](../uitextsmartquotestype/default.md), which selectively enables smart quotes based on the keyboard type.

## See Also

### Configuring the autoformatting behaviors

- [UITextSmartQuotesType](../uitextsmartquotestype.md) — Constants that indicate whether to enable or disable smart quotes.
- [smartDashesType](smartdashestype.md) — The configuration state for smart dashes.
- [UITextSmartDashesType](../uitextsmartdashestype.md) — Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [smartInsertDeleteType](smartinsertdeletetype.md) — The configuration state for the smart insertion and deletion of space characters.
- [UITextSmartInsertDeleteType](../uitextsmartinsertdeletetype.md) — Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.
