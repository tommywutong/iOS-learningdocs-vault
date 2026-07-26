---
title: UITextSmartInsertDeleteType
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsmartinsertdeletetype
source_url: 'https://developer.apple.com/documentation/uikit/uitextsmartinsertdeletetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsmartinsertdeletetype.json'
content_hash: 'sha256:7283980ec7cee007'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UITextSmartInsertDeleteType

<sub>Enumeration</sub>

Constants that specify whether to automatically insert extra spaces after a paste operation or to delete them after a cut or delete operation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum UITextSmartInsertDeleteType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [UITextSmartInsertDeleteTypeDefault](uitextsmartinsertdeletetype/default.md) — Use the default behavior for inserting and deleting space characters.
- [UITextSmartInsertDeleteTypeNo](uitextsmartinsertdeletetype/no.md) — Disable the insertion or deletion of extra spaces.
- [UITextSmartInsertDeleteTypeYes](uitextsmartinsertdeletetype/yes.md) — Enable the insertion or deletion of extra spaces.

### Initializers

- [init(rawValue:)](<uitextsmartinsertdeletetype/init(rawvalue_).md>)

## See Also

### Configuring the autoformatting behaviors

- [smartQuotesType](uitextinputtraits/smartquotestype.md) — The configuration state for smart quotes.
- [UITextSmartQuotesType](uitextsmartquotestype.md) — Constants that indicate whether to enable or disable smart quotes.
- [smartDashesType](uitextinputtraits/smartdashestype.md) — The configuration state for smart dashes.
- [UITextSmartDashesType](uitextsmartdashestype.md) — Constants that specify the automatic conversion behavior between hyphens and en or em dashes.
- [smartInsertDeleteType](uitextinputtraits/smartinsertdeletetype.md) — The configuration state for the smart insertion and deletion of space characters.
