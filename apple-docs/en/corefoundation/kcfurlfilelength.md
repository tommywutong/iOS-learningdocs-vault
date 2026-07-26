---
title: kCFURLFileLength
framework: Core Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/kcfurlfilelength
source_url: 'https://developer.apple.com/documentation/corefoundation/kcfurlfilelength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/kcfurlfilelength.json'
content_hash: 'sha256:8910bb94eda89414'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# kCFURLFileLength

<sub>Global Variable</sub>

A `CFNumber` object holding the file’s length in bytes.

> [!warning] Deprecated
> Use CFURLCopyResourcePropertyForKey with kCFURLFileSizeKey instead.

<sub>tvOS, visionOS, watchOS</sub>

```swift
let kCFURLFileLength: CFString!
```

## See Also

### Constants

- [kCFURLFileExists](kcfurlfileexists.md) — A `CFBoolean` object indicating whether the file referred to by a URL exists. _(deprecated)_
- [kCFURLFileDirectoryContents](kcfurlfiledirectorycontents.md) — A `CFArray` object holding `CFURL` objects for the contents of a directory referred to by a URL. _(deprecated)_
- [kCFURLFileLastModificationTime](kcfurlfilelastmodificationtime.md) — A `CFDate` object holding the file’s modification time. _(deprecated)_
- [kCFURLFilePOSIXMode](kcfurlfileposixmode.md) — A `CFNumber` holding the file’s POSIX mode as given in `/usr/include/sys/stat.h`. _(deprecated)_
- [kCFURLFileOwnerID](kcfurlfileownerid.md) — A `CFNumber` holding the file owner’s UID. _(deprecated)_
