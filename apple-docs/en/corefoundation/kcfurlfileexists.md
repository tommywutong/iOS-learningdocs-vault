---
title: kCFURLFileExists
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/kcfurlfileexists
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlfileexists'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlfileexists.json'
content_hash: 'sha256:52649f98d0e2e242'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLFileExists

<sub>Global Variable</sub>

A `CFBoolean` object indicating whether the file referred to by a URL exists.

> [!warning] Deprecated
> Use CFURLResourceIsReachable instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
let kCFURLFileExists: CFString!
```

## See Also

### Constants

- [kCFURLFileDirectoryContents](kcfurlfiledirectorycontents.md) — A `CFArray` object holding `CFURL` objects for the contents of a directory referred to by a URL. _(deprecated)_
- [kCFURLFileLength](kcfurlfilelength.md) — A `CFNumber` object holding the file’s length in bytes. _(deprecated)_
- [kCFURLFileLastModificationTime](kcfurlfilelastmodificationtime.md) — A `CFDate` object holding the file’s modification time. _(deprecated)_
- [kCFURLFilePOSIXMode](kcfurlfileposixmode.md) — A `CFNumber` holding the file’s POSIX mode as given in `/usr/include/sys/stat.h`. _(deprecated)_
- [kCFURLFileOwnerID](kcfurlfileownerid.md) — A `CFNumber` holding the file owner’s UID. _(deprecated)_
