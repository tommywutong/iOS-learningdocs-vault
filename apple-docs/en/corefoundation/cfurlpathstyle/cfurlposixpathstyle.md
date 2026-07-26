---
title: CFURLPathStyle.cfurlposixPathStyle
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlpathstyle/cfurlposixpathstyle
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/cfurlposixpathstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlpathstyle/cfurlposixpathstyle.json'
content_hash: 'sha256:8ee452af48796d9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLPathStyle](../cfurlpathstyle.md)

# CFURLPathStyle.cfurlposixPathStyle

<sub>Case</sub>

Indicates a POSIX style path name. Components are slash delimited. A leading slash indicates an absolute path; a trailing slash is not significant.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cfurlposixPathStyle
```

## See Also

### Constants

- [kCFURLHFSPathStyle](cfurlhfspathstyle.md) — Indicates a HFS style path name. Components are colon delimited. A leading colon indicates a relative path, otherwise the first path component denotes the volume. _(deprecated)_
- [kCFURLWindowsPathStyle](cfurlwindowspathstyle.md) — Indicates a Windows style path name.
