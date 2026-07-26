---
title: CFFileSecurityClearOptions
framework: Core Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cffilesecurityclearoptions
source_url: 'https://developer.apple.com/documentation/corefoundation/cffilesecurityclearoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cffilesecurityclearoptions.json'
content_hash: 'sha256:a984d7f6802682fd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFFileSecurityClearOptions

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CFFileSecurityClearOptions
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Constants

- [kCFFileSecurityClearAccessControlList](cffilesecurityclearoptions/accesscontrollist.md) — Clear the access control list.
- [kCFFileSecurityClearGroup](cffilesecurityclearoptions/group.md) — Clear the (POSIX) group ID.
- [kCFFileSecurityClearGroupUUID](cffilesecurityclearoptions/groupuuid.md) — Clear the group UUID (for the access control list).
- [kCFFileSecurityClearMode](cffilesecurityclearoptions/mode.md) — Clear the file’s mode (POSIX permissions).
- [kCFFileSecurityClearOwner](cffilesecurityclearoptions/owner.md) — Clear the (POSIX) owner ID.
- [kCFFileSecurityClearOwnerUUID](cffilesecurityclearoptions/owneruuid.md) — Clear the owner UUID (for the access control list).

### Initializers

- [init(rawValue:)](<cffilesecurityclearoptions/init(rawvalue_).md>)

## See Also

### Enumerations

- [CFISO8601DateFormatOptions](cfiso8601dateformatoptions.md)
- [CFRunLoopRunResult](cfrunlooprunresult.md)
- [CFURLEnumeratorOptions](cfurlenumeratoroptions.md) — Options for controlling enumerator behavior.
- [CFURLEnumeratorResult](cfurlenumeratorresult.md) — Result codes from the [CFURLEnumeratorGetNextURL](<cfurlenumeratorgetnexturl(______).md>) function.
- [CGRectEdge](cgrectedge.md)
