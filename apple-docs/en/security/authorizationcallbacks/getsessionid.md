---
title: GetSessionId
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/getsessionid
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/getsessionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/getsessionid.json'
content_hash: 'sha256:aedc33fd0596ab63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetSessionId

<sub>Instance Property</sub>

Reads the session ID.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, void **) GetSessionId;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `outSessionId` — On output, points to the session ID.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

The session ID is a unique value provided by the authorization engine for a given authorization session. Normally, all the mechanisms in your plug-in are called in turn for a given authorization session and there is no need to ask for the session ID. However, if you were to launch an authorization daemon (for example) that caches data from different authorization sessions and then uses that data later, you might need to keep track of which session a given data item came from. The session ID is available for your use if you wish to implement such a system.

The authorization engine sends you the entry point to the [GetSessionId](getsessionid.md) function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.
