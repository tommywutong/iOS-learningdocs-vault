---
title: MechanismDestroy
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationplugininterface/mechanismdestroy
source_url: 'https://developer.apple.com/documentation/security/authorizationplugininterface/mechanismdestroy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationplugininterface/mechanismdestroy.json'
content_hash: 'sha256:33914d30b6745346'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationPluginInterface](../authorizationplugininterface.md)

# MechanismDestroy

<sub>Instance Property</sub>

Destroys an authorization mechanism.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(void *) MechanismDestroy;
```

## Parameters

- `inMechanism` — An authorization mechanism reference that you returned when your [MechanismCreate](mechanismcreate.md) function was called to create the mechanism.

## Return Value

A result code. Return [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) if the function completes successfully and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

## Discussion

When the authorization engine calls your [MechanismDestroy](mechanismdestroy.md) function, you must release all resources owned by your mechanism and do any other cleanup necessary (such as deleting temporary files).
