---
title: CFURLComponentType
framework: Core Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfurlcomponenttype
source_url: 'https://developer.apple.com/documentation/corefoundation/cfurlcomponenttype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfurlcomponenttype.json'
content_hash: 'sha256:3ee028d1185feec1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFURLComponentType

<sub>Enumeration</sub>

The types of components in a URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CFURLComponentType
```

## Overview

These constants are used by the [CFURLGetByteRangeForComponent](<cfurlgetbyterangeforcomponent(______).md>) function.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [kCFURLComponentScheme](cfurlcomponenttype/scheme.md) — The URL’s scheme.
- [kCFURLComponentNetLocation](cfurlcomponenttype/netlocation.md) — The URL’s network location.
- [kCFURLComponentPath](cfurlcomponenttype/path.md) — The URL’s path component.
- [kCFURLComponentResourceSpecifier](cfurlcomponenttype/resourcespecifier.md) — The URL’s resource specifier.
- [kCFURLComponentUser](cfurlcomponenttype/user.md) — The URL’s user.
- [kCFURLComponentPassword](cfurlcomponenttype/password.md) — The user’s password.
- [kCFURLComponentUserInfo](cfurlcomponenttype/userinfo.md) — The user’s information.
- [kCFURLComponentHost](cfurlcomponenttype/host.md) — The URL’s host.
- [kCFURLComponentPort](cfurlcomponenttype/port.md) — The URL’s port.
- [kCFURLComponentParameterString](cfurlcomponenttype/parameterstring.md) — The URL’s parameter string.
- [kCFURLComponentQuery](cfurlcomponenttype/query.md) — The URL’s query.
- [kCFURLComponentFragment](cfurlcomponenttype/fragment.md) — The URL’s fragment.

### Initializers

- [init(rawValue:)](<cfurlcomponenttype/init(rawvalue_).md>)

## See Also

### Miscellaneous

- [CFURLPathStyle](cfurlpathstyle.md) — Options you can use to determine how CFURL functions parse a file system path name.
