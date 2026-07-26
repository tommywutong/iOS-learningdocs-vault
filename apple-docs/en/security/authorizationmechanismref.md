---
title: AuthorizationMechanismRef
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationmechanismref
source_url: 'https://developer.apple.com/documentation/security/authorizationmechanismref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationmechanismref.json'
content_hash: 'sha256:9470b08df66e0989'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationMechanismRef

<sub>Type Alias</sub>

A handle passed by the plug-in to the authorization engine when creating an instance of a mechanism.

<sub>Mac Catalyst, macOS</sub>

```objc
typedef void * AuthorizationMechanismRef;
```

## Discussion

Your [MechanismCreate](authorizationplugininterface/mechanismcreate.md) function assigns this value and returns it to the authorization engine. The authorization engine passes this reference back to you in any subsequent calls to your [MechanismInvoke](authorizationplugininterface/mechanisminvoke.md), [MechanismDeactivate](authorizationplugininterface/mechanismdeactivate.md), and [MechanismDestroy](authorizationplugininterface/mechanismdestroy.md) functions.
