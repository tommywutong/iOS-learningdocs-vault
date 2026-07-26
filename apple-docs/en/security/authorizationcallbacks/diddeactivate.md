---
title: DidDeactivate
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/diddeactivate
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/diddeactivate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/diddeactivate.json'
content_hash: 'sha256:2b125e42a6ce113e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# DidDeactivate

<sub>Instance Property</sub>

Reports the successful deactivation of an authorization mechanism.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *) DidDeactivate;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

Call this function after deactivating your authorization mechanism in response to a call to your [MechanismDeactivate](../authorizationplugininterface/mechanismdeactivate.md) function. The authorization engine waits for confirmation that all mechanisms have deactivated before continuing.

The authorization engine sends you the entry point to the [DidDeactivate](diddeactivate.md) function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.
