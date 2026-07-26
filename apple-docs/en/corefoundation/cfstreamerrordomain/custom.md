---
title: CFStreamErrorDomain.custom
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfstreamerrordomain/custom
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamerrordomain/custom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamerrordomain/custom.json'
content_hash: 'sha256:18ca6d67c32c3542'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamErrorDomain](../cfstreamerrordomain.md)

# CFStreamErrorDomain.custom

<sub>Case</sub>

The error code is a custom error code.

> [!warning] Deprecated
> These constants are returned by [CFReadStreamGetError](<../cfreadstreamgeterror(__).md>) and [CFWriteStreamGetError](<../cfwritestreamgeterror(__).md>); use [CFReadStreamCopyError](<../cfreadstreamcopyerror(__).md>) and [CFWriteStreamCopyError](<../cfwritestreamcopyerror(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case custom
```

## See Also

### Constants

- [kCFStreamErrorDomainPOSIX](posix.md) — The error code is an error code defined in `errno.h`.
- [kCFStreamErrorDomainMacOSStatus](macosstatus.md) — The error is an OSStatus value defined in `MacErrors.h`.
