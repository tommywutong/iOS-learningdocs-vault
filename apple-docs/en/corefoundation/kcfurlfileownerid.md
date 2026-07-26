---
title: kCFURLFileOwnerID
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/kcfurlfileownerid
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlfileownerid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlfileownerid.json'
content_hash: 'sha256:9351c72b44bc8ab2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLFileOwnerID

<sub>Global Variable</sub>

A `CFNumber` holding the file owner’s UID.

> [!warning] Deprecated
> Use CFURLCopyResourcePropertyForKey with kCFURLFileSecurityKey and then the CFFileSecurity API instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
let kCFURLFileOwnerID: CFString!
```

## See Also

### Constants

- [kCFURLFileExists](kcfurlfileexists.md) — A `CFBoolean` object indicating whether the file referred to by a URL exists. _(deprecated)_
- [kCFURLFileDirectoryContents](kcfurlfiledirectorycontents.md) — A `CFArray` object holding `CFURL` objects for the contents of a directory referred to by a URL. _(deprecated)_
- [kCFURLFileLength](kcfurlfilelength.md) — A `CFNumber` object holding the file’s length in bytes. _(deprecated)_
- [kCFURLFileLastModificationTime](kcfurlfilelastmodificationtime.md) — A `CFDate` object holding the file’s modification time. _(deprecated)_
- [kCFURLFilePOSIXMode](kcfurlfileposixmode.md) — A `CFNumber` holding the file’s POSIX mode as given in `/usr/include/sys/stat.h`. _(deprecated)_
