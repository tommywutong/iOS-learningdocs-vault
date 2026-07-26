---
title: valueLength
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationitem/valuelength
source_url: 'https://developer.apple.com/documentation/security/authorizationitem/valuelength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationitem/valuelength.json'
content_hash: 'sha256:05a43a5bf2736304'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationItem](../authorizationitem.md)

# valueLength

<sub>Instance Property</sub>

The number of bytes in the value field.

<sub>Mac Catalyst, macOS</sub>

```swift
var valueLength: Int
```

## Discussion

Set this field to `0` if you set the `value` field to `NULL`.
