---
title: kCFURLFileSizeKey
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/kcfurlfilesizekey
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlfilesizekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlfilesizekey.json'
content_hash: 'sha256:8be1245e1ad4541a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLFileSizeKey

<sub>Global Variable</sub>

Key for the file’s size in bytes, returned as a `CFNumber` object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let kCFURLFileSizeKey: CFString!
```

## See Also

### Constants

- [kCFURLFileAllocatedSizeKey](kcfurlfileallocatedsizekey.md) — Key for the total size allocated on disk for the file, returned as an `CFNumber` object.
- [kCFURLIsAliasFileKey](kcfurlisaliasfilekey.md) — Key for determining whether the file is an alias, returned as a `CFBoolean` object.
- [kCFURLIsMountTriggerKey](kcfurlismounttriggerkey.md) — Key for determining whether the URL is a file system trigger directory, returned as a `CFBoolean` object. Traversing or opening a file system trigger directory causes an attempt to mount a file system on the directory.
- [kCFURLTotalFileAllocatedSizeKey](kcfurltotalfileallocatedsizekey.md) — Key for the total allocated size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.
- [kCFURLTotalFileSizeKey](kcfurltotalfilesizekey.md) — Key for the total displayable size of the file in bytes, returned as a `CFNumber` object. This includes the size of any file metadata.
