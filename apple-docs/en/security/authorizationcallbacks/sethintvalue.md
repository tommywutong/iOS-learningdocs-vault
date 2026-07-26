---
title: SetHintValue
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/sethintvalue
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/sethintvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/sethintvalue.json'
content_hash: 'sha256:cf511bc0ade8faa0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# SetHintValue

<sub>Instance Property</sub>

Stores data needed during authorization as a key-value pair.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const char *, const struct AuthorizationValue *) SetHintValue;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `inKey` — A key identifying the value you are storing. For standard values such as a time stamp, use the keys listed in `DirectoryService/DirServicesConst.h`. If you need to define a new key, make sure the key is unique. For example, you can use your company name as a prefix for the key name.

- `inValue` — A pointer to an [AuthorizationValue](../authorizationvalue.md) structure that contains the size of the data and a pointer to the data. Both the structure and the data are copied to storage maintained by the authorization engine.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

Your plug-in authorization mechanism can save and retrieve auxiliary information—called hints—for use by subsequent mechanisms that are part of the same authorization. You use the `SetHintValue` function to have the Security Server store this data and the [GetHintValue](gethintvalue.md) function to retrieve it. Hints are not preserved as part of the authorization result; once all mechanisms have approved the authorization or any mechanism has denied it, the security engine disposes of the hints.

The authorization engine sends you the entry point to the `SetHintValue` function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.

> [!important] Important
> Do not call this function after you have called the [SetResult](setresult.md) function. If you do so, the function does not set the hint data, even though the function returns the [errAuthorizationSuccess](../errauthorizationsuccess.md) result code.
