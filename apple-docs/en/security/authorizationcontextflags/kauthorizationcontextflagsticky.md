---
title: kAuthorizationContextFlagSticky
framework: Security
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcontextflags/kauthorizationcontextflagsticky
source_url: 'https://developer.apple.com/documentation/security/authorizationcontextflags/kauthorizationcontextflagsticky'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcontextflags/kauthorizationcontextflagsticky.json'
content_hash: 'sha256:0e16160d0f8dab87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationContextFlags](../authorizationcontextflags.md)

# kAuthorizationContextFlagSticky

<sub>Enumeration Case</sub>

This data persists through an interrupted or failed evaluation.

<sub>Mac Catalyst, macOS</sub>

```objc
kAuthorizationContextFlagSticky
```

## Discussion

This flag can be used to propagate an error condition from a downstream plug-in to an upstream one. It is not remembered in the authorization reference (see [Authorization Services](../authorization-services.md)).
