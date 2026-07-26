---
title: GetContextValue
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/getcontextvalue
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/getcontextvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/getcontextvalue.json'
content_hash: 'sha256:b07b15b27c82ed63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetContextValue

<sub>Instance Property</sub>

Reads a value collected during authorization.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const char *, enum AuthorizationContextFlags *, const struct AuthorizationValue **) GetContextValue;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `inKey` — A key indicating which value you want to retrieve. This key must correspond to one you specified when you used the [SetContextValue](setcontextvalue.md) function to store a context value.

- `outContextFlags` — On output points to a flag that indicates whether this value is available to the authorization client.

- `outValue` — On input, allocate a pointer to an [AuthorizationValue](../authorizationvalue.md) structure. On output, the structure contains the size of the data and a pointer to the data. Because your [AuthorizationValue](../authorizationvalue.md) structure does not own the data, you must not deallocate the structure or the data pointed to by the structure.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

Your plug-in authorization mechanism might collect data such as the user name and other authentication information during evaluation of authorization. You can use the [SetContextValue](setcontextvalue.md) function to have the Security Server store this data and the [GetContextValue](getcontextvalue.md) function to retrieve it.

The authorization engine sends you the entry point to the [GetContextValue](getcontextvalue.md) function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.

> [!important] Important
> Do not call this function after you have called the [SetResult](setresult.md) function. If you do so, the data retrieved by the `GetContextValue` function might not reflect the current value even though the function returns the [errAuthorizationSuccess](../errauthorizationsuccess.md) result code.
