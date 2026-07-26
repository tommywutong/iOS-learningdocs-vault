---
title: FileManager.SearchPathDomainMask
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/searchpathdomainmask
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/searchpathdomainmask'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/searchpathdomainmask.json'
content_hash: 'sha256:a71f1da008d5c028'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.SearchPathDomainMask

<sub>Structure</sub>

Domain constants specifying base locations to use when you search for significant directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SearchPathDomainMask
```

## Overview

These constants are used by the [- URLsForDirectory:inDomains:](<urls(for_in_).md>) and [- URLForDirectory:inDomain:appropriateForURL:create:error:](<url(for_in_appropriatefor_create_).md>) methods of FileManager.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Creating a Search Path Domain Mask

- [init(rawValue:)](<searchpathdomainmask/init(rawvalue_).md>) — Creates a search path domain mask.

### Specifying Search Path Domains

- [NSUserDomainMask](searchpathdomainmask/userdomainmask.md) — The user’s home directory—the place to install user’s personal items (`~`).
- [NSLocalDomainMask](searchpathdomainmask/localdomainmask.md) — The place to install items available to everyone on this machine.
- [NSNetworkDomainMask](searchpathdomainmask/networkdomainmask.md) — The place to install items available on the network (`/Network`).
- [NSSystemDomainMask](searchpathdomainmask/systemdomainmask.md) — A directory for system files provided by Apple (`/System`) .
- [NSAllDomainsMask](searchpathdomainmask/alldomainsmask.md) — All domains.

## See Also

### Supporting Types

- [DirectoryEnumerationOptions](directoryenumerationoptions.md) — Options for enumerating the contents of directories.
- [SearchPathDirectory](searchpathdirectory.md) — The location of significant directories.
- [FileAttributeKey](../fileattributekey.md) — Keys in dictionaries used to get and set file attributes.
- [FileAttributeType](../fileattributetype.md) — Values representing a file’s type attribute.
- [FileProtectionType](../fileprotectiontype.md) — Protection level values that can be associated with a file attribute key.
- [URLFileProtection](../urlfileprotection.md) — Protection-level values for a URL resource key.
