---
title: GetHintValue
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/gethintvalue
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/gethintvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/gethintvalue.json'
content_hash: 'sha256:9a8096122bae4e08'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetHintValue

<sub>Instance Property</sub>

Reads a value stored by the plug-in authorization mechanism.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const char *, const struct AuthorizationValue **) GetHintValue;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `inKey` — A key indicating which value you want to retrieve. This key must correspond to one you specified when you used the [SetHintValue](sethintvalue.md) function to store a hint value.

- `outValue` — On input, allocate a pointer to an [AuthorizationValue](../authorizationvalue.md) structure. On output, the structure contains the size of the data and a pointer to the data. Because your [AuthorizationValue](../authorizationvalue.md) structure does not own the data, you must not deallocate the structure or the data pointed to by the structure.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

Your plug-in authorization mechanism can save and retrieve auxiliary information—called hints—for use by subsequent mechanisms that are part of the same authorization. You use the [SetHintValue](sethintvalue.md) function to have the Security Server store this data and the `GetHintValue` function to retrieve it. Hints are not preserved as part of the authorization result; once all mechanisms have approved the authorization or any mechanism has denied it, the security engine disposes of the hints.

The authorization engine sends you the entry point to the `GetHintValue` function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.

> [!important] Important
> Do not call this function after you have called the [SetResult](setresult.md) function. If you do so, the data retrieved by the `GetHintValue` function might not reflect the current value even though the function returns the [errAuthorizationSuccess](../errauthorizationsuccess.md) result code.
