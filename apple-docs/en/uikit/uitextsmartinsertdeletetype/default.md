---
title: UITextSmartInsertDeleteType.default
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsmartinsertdeletetype/default
source_url: 'https://developer.apple.com/documentation/uikit/uitextsmartinsertdeletetype/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsmartinsertdeletetype/default.json'
content_hash: 'sha256:977a8738815fe9cb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSmartInsertDeleteType](../uitextsmartinsertdeletetype.md)

# UITextSmartInsertDeleteType.default

<sub>Case</sub>

Use the default behavior for inserting and deleting space characters.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
case `default`
```

## Discussion

This option selectively enables the automatic deletion of one or two neighboring spaces after a cut or delete, and the insertion of an extra space after a paste. For example, this option disables the behavior for email address and password keyboards.

## See Also

### Constants

- [UITextSmartInsertDeleteTypeNo](no.md) — Disable the insertion or deletion of extra spaces.
- [UITextSmartInsertDeleteTypeYes](yes.md) — Enable the insertion or deletion of extra spaces.
