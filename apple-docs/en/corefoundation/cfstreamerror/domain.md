---
title: domain
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/corefoundation/cfstreamerror/domain
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstreamerror/domain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstreamerror/domain.json'
content_hash: 'sha256:f24d735eb746e5cc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFStreamError](../cfstreamerror.md)

# domain

<sub>Instance Property</sub>

The error domain that should be used to interpret the error. See [CFStreamErrorDomain](../cfstreamerrordomain.md) for possible values.

> [!warning] Deprecated
> Use [CFReadStreamCopyError](<../cfreadstreamcopyerror(__).md>) and [CFWriteStreamCopyError](<../cfwritestreamcopyerror(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var domain: CFIndex
```
