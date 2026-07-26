---
title: completeUnlessOpen
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileprotectiontype/completeunlessopen
source_url: 'https://developer.apple.com/documentation/foundation/fileprotectiontype/completeunlessopen'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileprotectiontype/completeunlessopen.json'
content_hash: 'sha256:26b3e14b3dce64d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileProtectionType](../fileprotectiontype.md)

# completeUnlessOpen

<sub>Type Property</sub>

The file is stored in an encrypted format on disk after it is closed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let completeUnlessOpen: FileProtectionType
```

## Discussion

Files with this type of protection can be created while the device is locked, but once closed, cannot be opened again until the device is unlocked. If the file is opened when unlocked, you may continue to access the file normally, even if the user locks the device. There is a small performance penalty when the file is created and opened, though not when being written to or read from. This can be mitigated by changing the file protection to [NSFileProtectionComplete](complete.md) when the device is unlocked.

## See Also

### Working with Protection Levels

- [NSFileProtectionComplete](complete.md) — The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.
- [NSFileProtectionCompleteUntilFirstUserAuthentication](completeuntilfirstuserauthentication.md) — The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.
- [NSFileProtectionNone](none.md) — The file has no special protections associated with it.
