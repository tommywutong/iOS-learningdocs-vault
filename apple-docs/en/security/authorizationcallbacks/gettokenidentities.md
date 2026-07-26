---
title: GetTokenIdentities
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/gettokenidentities
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/gettokenidentities'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/gettokenidentities.json'
content_hash: 'sha256:d20e5a60443f686a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetTokenIdentities

<sub>Instance Property</sub>

Returns an array of identities available on tokens.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const void *, const struct __CFArray **) GetTokenIdentities;
```

## Parameters

- `inEngine` — An opaque handle that’s passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `context` — A local authentication context returned by the [GetLAContext](getlacontext.md) call.

- `outValue` — A pointer the function uses to return an array of identities, each of which consists of two array elements: a [SecIdentity](../secidentity.md) instance and a text description of the identity.

## Discussion

The caller owns the returned array and is responsible for releasing it.

> [!important] Important
> This function is only available when the callback [version](version.md) is 2 or higher.
