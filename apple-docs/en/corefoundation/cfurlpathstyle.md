---
title: CFURLPathStyle
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlpathstyle
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlpathstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlpathstyle.json'
content_hash: 'sha256:3860d73b05068768'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLPathStyle

<sub>Enumeration</sub>

Options you can use to determine how CFURL functions parse a file system path name.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFURLPathStyle
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFURLPOSIXPathStyle](cfurlpathstyle/cfurlposixpathstyle.md) — Indicates a POSIX style path name. Components are slash delimited. A leading slash indicates an absolute path; a trailing slash is not significant.
- [kCFURLHFSPathStyle](cfurlpathstyle/cfurlhfspathstyle.md) — Indicates a HFS style path name. Components are colon delimited. A leading colon indicates a relative path, otherwise the first path component denotes the volume. _(deprecated)_
- [kCFURLWindowsPathStyle](cfurlpathstyle/cfurlwindowspathstyle.md) — Indicates a Windows style path name.

### Initializers

- [init(rawValue:)](<cfurlpathstyle/init(rawvalue_).md>)

## See Also

### Miscellaneous

- [CFURLComponentType](cfurlcomponenttype.md) — The types of components in a URL.
