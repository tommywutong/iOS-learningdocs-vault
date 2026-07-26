---
title: CFURLPathStyle.cfurlhfsPathStyle
framework: Core Foundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（7.0 起废弃）, iPadOS 2.0+（7.0 起废弃）, tvOS 9.0+（9.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 2.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfurlpathstyle/cfurlhfspathstyle
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlpathstyle/cfurlhfspathstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlpathstyle/cfurlhfspathstyle.json'
content_hash: 'sha256:4424d2cefce1c19f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFURLPathStyle](../cfurlpathstyle.md)

# CFURLPathStyle.cfurlhfsPathStyle

<sub>Case</sub>

Indicates a HFS style path name. Components are colon delimited. A leading colon indicates a relative path, otherwise the first path component denotes the volume.

> [!warning] Deprecated
> Carbon File Manager is deprecated, use kCFURLPOSIXPathStyle where possible

<sub>tvOS, visionOS, watchOS</sub>

```swift
case cfurlhfsPathStyle
```

## See Also

### Constants

- [kCFURLPOSIXPathStyle](cfurlposixpathstyle.md) — Indicates a POSIX style path name. Components are slash delimited. A leading slash indicates an absolute path; a trailing slash is not significant.
- [kCFURLWindowsPathStyle](cfurlwindowspathstyle.md) — Indicates a Windows style path name.
