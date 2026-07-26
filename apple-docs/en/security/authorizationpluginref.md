---
title: AuthorizationPluginRef
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationpluginref
source_url: 'https://developer.apple.com/documentation/security/authorizationpluginref'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationpluginref.json'
content_hash: 'sha256:9028569c608d2d8f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationPluginRef

<sub>Type Alias</sub>

A handle passed by the plug-in to the authorization engine when the plug-in is initiated.

<sub>Mac Catalyst, macOS</sub>

```objc
typedef void * AuthorizationPluginRef;
```

## Discussion

Your [AuthorizationPluginCreate](authorizationplugincreate.md) function assigns this value and returns it to the authorization engine. The authorization engine passes this reference back to you in any subsequent calls to your [MechanismCreate](authorizationplugininterface/mechanismcreate.md) and [PluginDestroy](authorizationplugininterface/plugindestroy.md) functions.
