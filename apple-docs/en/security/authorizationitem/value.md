---
title: value
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationitem/value
source_url: 'https://developer.apple.com/documentation/security/authorizationitem/value'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationitem/value.json'
content_hash: 'sha256:17548df6ff35f290'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationItem](../authorizationitem.md)

# value

<sub>Instance Property</sub>

A pointer to information pertaining to the name field.

<sub>Mac Catalyst, macOS</sub>

```swift
var value: UnsafeMutableRawPointer?
```

## Discussion

If the `name` field is set to the value represented by the constant [kAuthorizationRightExecute](../kauthorizationrightexecute.md), then set the `value` field to the full POSIX pathname of the tool you want to execute. In most other cases, set this field to `NULL`.
