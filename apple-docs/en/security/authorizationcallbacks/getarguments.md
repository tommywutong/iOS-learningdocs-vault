---
title: GetArguments
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/getarguments
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/getarguments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/getarguments.json'
content_hash: 'sha256:2584b2b42a8ab64d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetArguments

<sub>Instance Property</sub>

Reads the arguments for this authorization mechanism from the authorization policy database.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const struct AuthorizationValueVector **) GetArguments;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `outArguments` — On input, allocate a pointer to an [AuthorizationValueVector](../authorizationvaluevector.md) structure. On output, the structure contains the number of arguments and a pointer to the data. Because your [AuthorizationValueVector](../authorizationvaluevector.md) structure does not own the data, you must not deallocate the structure or the data pointed to by the structure.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

The authorization policy database might contain arguments for each authentication mechanism. You can use this function to retrieve these arguments.

The authorization engine sends you the entry point to the [GetArguments](getarguments.md) function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.
