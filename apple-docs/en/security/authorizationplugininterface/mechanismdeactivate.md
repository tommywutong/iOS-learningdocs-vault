---
title: MechanismDeactivate
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationplugininterface/mechanismdeactivate
source_url: 'https://developer.apple.com/documentation/security/authorizationplugininterface/mechanismdeactivate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationplugininterface/mechanismdeactivate.json'
content_hash: 'sha256:31bd0cb0541188ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationPluginInterface](../authorizationplugininterface.md)

# MechanismDeactivate

<sub>Instance Property</sub>

Deactivates an authorization mechanism.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(void *) MechanismDeactivate;
```

## Parameters

- `inMechanism` — An authorization mechanism reference that you returned when your [MechanismCreate](mechanismcreate.md) function was called to create the mechanism.

## Return Value

A result code. Return [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) if the function completes successfully and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

## Discussion

The authorization engine calls the [MechanismDeactivate](mechanismdeactivate.md) function of each active mechanism when you call the [RequestInterrupt](../authorizationcallbacks/requestinterrupt.md) function. To deactivate your mechanism, you must stop any processing that is currently underway; for example, you should terminate any threads or UI processes that you initiated.

After you have terminated all processing, you must call the [DidDeactivate](../authorizationcallbacks/diddeactivate.md) function; the authorization engine waits for you to call this function before it resumes operation.
