---
title: SetContextValue
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/setcontextvalue
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/setcontextvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/setcontextvalue.json'
content_hash: 'sha256:2c8ab55fce76a151'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# SetContextValue

<sub>Instance Property</sub>

Stores data collected during authorization as a key-value pair.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const char *, enum AuthorizationContextFlags, const struct AuthorizationValue *) SetContextValue;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `inKey` — A key identifying the value you are storing. For standard values such as user names, use the keys listed in `DirectoryService/DirServicesConst.h`. If you need to define a new key, use reverse domain notation (such as `com.apple.ifoo`) and make sure the key is unique. For example, you can use your company name as a prefix for the key name.

- `inContextFlags` — A flag that indicates whether this value should be available to the authorization client.

- `inValue` — A pointer to an [AuthorizationValue](../authorizationvalue.md) structure that contains the size of the context data and a pointer to the data. Both the structure and the data are copied to the context maintained by the Security Server.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

Your plug-in authorization mechanism collects data such as the user name and other authentication information during evaluation of authorization. You can use this function to have the Security Server store this data and the [GetContextValue](getcontextvalue.md) function to retrieve it.

When you store this context data, you flag it to indicate whether the authorization client can obtain the value with the [AuthorizationCopyInfo](<../authorizationcopyinfo(______).md>) function. If data is set to be extractable ([kAuthorizationContextFlagExtractable](../authorizationcontextflags/kauthorizationcontextflagextractable.md)), it is possible for the authorization client to use the [AuthorizationCopyInfo](<../authorizationcopyinfo(______).md>) function to obtain the value. If data is marked as volatile ([kAuthorizationContextFlagVolatile](../authorizationcontextflags/kauthorizationcontextflagvolatile.md)), the value is not available to the client. In any case, sensitive data such as a user’s password is not provided to the client.

The authorization engine sends you the entry point to the `SetContextValue` function in an [AuthorizationCallbacks](../authorizationcallbacks.md) structure when you call the [AuthorizationPluginCreate](../authorizationplugincreate.md) function.

> [!important] Important
> Do not call this function after you have called the [SetResult](setresult.md) function. If you do so, the function does not set the context data, even though the function returns the [errAuthorizationSuccess](../errauthorizationsuccess.md) result code.
