---
title: URLFileProtection
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlfileprotection
source_url: 'https://developer.apple.com/documentation/foundation/urlfileprotection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlfileprotection.json'
content_hash: 'sha256:9545f813d3093eb0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# URLFileProtection

<sub>Structure</sub>

Protection-level values for a URL resource key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct URLFileProtection
```

## Overview

These are values for the [URLResourceKey](urlresourcekey.md) key [NSURLFileProtectionKey](urlresourcekey/fileprotectionkey.md).

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a URL File Protection Type

- [init(rawValue:)](<urlfileprotection/init(rawvalue_).md>) — Creates a URL file protection type value.

### Protection levels

- [NSURLFileProtectionComplete](urlfileprotection/complete.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access for reading or writing to while the device is locked or booting.
- [NSURLFileProtectionCompleteUnlessOpen](urlfileprotection/completeunlessopen.md) — An option that instructs the system to store the file in an encrypted format on-disk after it closes.
- [NSURLFileProtectionCompleteUntilFirstUserAuthentication](urlfileprotection/completeuntilfirstuserauthentication.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can’t access until after the device boots.
- [NSURLFileProtectionCompleteWhenUserInactive](urlfileprotection/completewhenuserinactive.md) — An option that instructs the system to store the file in an encrypted format on-disk that your app can access only after device unlock and before expiration.
- [NSURLFileProtectionNone](urlfileprotection/none.md) — An option that indicates the file has no special protections associated with it.

## See Also

### Supporting Types

- [DirectoryEnumerationOptions](filemanager/directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDirectory](filemanager/searchpathdirectory.md) — The location of significant directories.
- [SearchPathDomainMask](filemanager/searchpathdomainmask.md) — Domain constants specifying base locations to use when you search for significant directories.
- [FileAttributeKey](fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileAttributeType](fileattributetype.md) — Values representing a file’s type attribute.
- [FileProtectionType](fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
