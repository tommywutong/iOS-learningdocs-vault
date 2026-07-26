---
title: FileProtectionType
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/fileprotectiontype
source_url: 'https://developer.apple.com/documentation/foundation/fileprotectiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/fileprotectiontype.json'
content_hash: 'sha256:9fc07a45956c1db6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# FileProtectionType

<sub>Structure</sub>

Protection level values that can be associated with a file attribute key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FileProtectionType
```

## Overview

These values are associated with the [NSFileProtectionKey](fileattributekey/protectionkey.md) key.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a File Protection Type

- [init(rawValue:)](<fileprotectiontype/init(rawvalue_).md>) — Creates a file protection type value.

### Working with Protection Levels

- [NSFileProtectionComplete](fileprotectiontype/complete.md) — The file is stored in an encrypted format on disk and cannot be read from or written to while the device is locked or booting.
- [NSFileProtectionCompleteUnlessOpen](fileprotectiontype/completeunlessopen.md) — The file is stored in an encrypted format on disk after it is closed.
- [NSFileProtectionCompleteUntilFirstUserAuthentication](fileprotectiontype/completeuntilfirstuserauthentication.md) — The file is stored in an encrypted format on disk and cannot be accessed until after the device has booted.
- [NSFileProtectionNone](fileprotectiontype/none.md) — The file has no special protections associated with it.

## See Also

### Supporting Types

- [DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDirectory](filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeKey](fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileAttributeType](fileattributetype.md) — Values representing a file’s type attribute.
- [URLFileProtection](urlfileprotection.md) — Protection-level values for a URL resource key.
