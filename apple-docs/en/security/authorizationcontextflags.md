---
title: AuthorizationContextFlags
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcontextflags
source_url: 'https://developer.apple.com/documentation/security/authorizationcontextflags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcontextflags.json'
content_hash: 'sha256:4840973b7f338ab0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationContextFlags

<sub>Enumeration</sub>

The flags that specify whether authentication data should be made available to the authorization client.

<sub>Mac Catalyst, macOS</sub>

```objc
enum AuthorizationContextFlags : UInt32;
```

## Topics

### Constants

- [kAuthorizationContextFlagExtractable](authorizationcontextflags/kauthorizationcontextflagextractable.md) — It is possible for the authorization client to use the [AuthorizationCopyInfo](<authorizationcopyinfo(______).md>) function to obtain the value.
- [kAuthorizationContextFlagVolatile](authorizationcontextflags/kauthorizationcontextflagvolatile.md) — The value is not saved for the authorization client.
- [kAuthorizationContextFlagSticky](authorizationcontextflags/kauthorizationcontextflagsticky.md) — This data persists through an interrupted or failed evaluation.
