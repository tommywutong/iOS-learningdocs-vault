---
title: GetLAContext
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.13+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/getlacontext
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/getlacontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/getlacontext.json'
content_hash: 'sha256:24d7d7495794520d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetLAContext

<sub>Instance Property</sub>

Constructs a local authentication context.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const void **) GetLAContext;
```

## Parameters

- `inEngine` — An opaque handle that’s passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `outValue` — A pointer the function uses to return the [LAContext](../../localauthentication/lacontext.md) instance.

## Discussion

If a PIN is available, you can use the context for token operations that would normally require a PIN.

You can also use this context for keychain item accesses, for example using the [SecItemCopyMatching](<../secitemcopymatching(____).md>) function, that include the [kSecUseAuthenticationContext](../ksecuseauthenticationcontext.md) key in the query dictionary.

The caller owns the returned context and is responsible for releasing it.

> [!important] Important
> This function is only available when the callback [version](version.md) is 2 or higher.
