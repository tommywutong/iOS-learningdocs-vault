---
title: AuthorizationEngineRef
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationengineref
source_url: 'https://developer.apple.com/documentation/security/authorizationengineref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationengineref.json'
content_hash: 'sha256:dbc24cd6747a066e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationEngineRef

<sub>Type Alias</sub>

Handle passed from the authorization engine to an instance of a mechanism in a plug-in.

<sub>Mac Catalyst, macOS</sub>

```objc
typedef struct __OpaqueAuthorizationEngine * AuthorizationEngineRef;
```

## Discussion

The authorization engine passes one of these opaque handles to your plug-in when it calls your [MechanismCreate](authorizationplugininterface/mechanismcreate.md) function. Your mechanism must pass this handle back to the authorization engine when you call one of the engine’s callback functions, as defined in the [AuthorizationCallbacks](authorizationcallbacks.md) structure.
