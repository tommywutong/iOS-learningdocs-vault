---
title: MechanismInvoke
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationplugininterface/mechanisminvoke
source_url: 'https://developer.apple.com/documentation/security/authorizationplugininterface/mechanisminvoke'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationplugininterface/mechanisminvoke.json'
content_hash: 'sha256:f4c5fec6b4847522'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationPluginInterface](../authorizationplugininterface.md)

# MechanismInvoke

<sub>Instance Property</sub>

Invokes an authorization mechanism to perform an authorization operation.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(void *) MechanismInvoke;
```

## Parameters

- `inMechanism` — An authorization mechanism reference that you returned when your [MechanismCreate](mechanismcreate.md) function was called to create the mechanism.

## Return Value

A result code. Return [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) if the function completes successfully and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error) if any error occurs.

## Discussion

When the authorization engine calls your `MechanismInvoke` function, you should perform the authorization operation indicated by the mechanism reference. You can use the functions [GetArguments](../authorizationcallbacks/getarguments.md), [GetContextValue](../authorizationcallbacks/getcontextvalue.md), and [GetHintValue](../authorizationcallbacks/gethintvalue.md) to get more information, if any, about the authorization.
