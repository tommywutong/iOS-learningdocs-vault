---
title: completeUntilFirstUserAuthentication
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication
source_url: 'https://developer.apple.com/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileprotectiontype/completeuntilfirstuserauthentication.json'
content_hash: 'sha256:9053f7ccd333bf52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileProtectionType](../fileprotectiontype.md)

# completeUntilFirstUserAuthentication

<sub>Type Property</sub>

The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let completeUntilFirstUserAuthentication: FileProtectionType
```

## Discussion

After the user unlocks the device for the first time, your app can access the file and continue to access it even if the user subsequently locks the device.

## See Also

### Working with Protection Levels

- [NSFileProtectionComplete](complete.md) — The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.
- [NSFileProtectionCompleteUnlessOpen](completeunlessopen.md) — The file is stored in an encrypted format on disk after it is closed.
- [NSFileProtectionNone](none.md) — The file has no special protections associated with it.
