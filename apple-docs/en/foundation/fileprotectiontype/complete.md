---
title: complete
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileprotectiontype/complete
source_url: 'https://developer.apple.com/documentation/foundation/fileprotectiontype/complete'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileprotectiontype/complete.json'
content_hash: 'sha256:2bb9be0301dee5dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileProtectionType](../fileprotectiontype.md)

# complete

<sub>Type Property</sub>

The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let complete: FileProtectionType
```

## See Also

### Working with Protection Levels

- [NSFileProtectionCompleteUnlessOpen](completeunlessopen.md) — The file is stored in an encrypted format on disk after it is closed.
- [NSFileProtectionCompleteUntilFirstUserAuthentication](completeuntilfirstuserauthentication.md) — The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.
- [NSFileProtectionNone](none.md) — The file has no special protections associated with it.
