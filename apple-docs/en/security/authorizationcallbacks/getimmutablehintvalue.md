---
title: GetImmutableHintValue
framework: Security
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationcallbacks/getimmutablehintvalue
source_url: 'https://developer.apple.com/documentation/security/authorizationcallbacks/getimmutablehintvalue'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcallbacks/getimmutablehintvalue.json'
content_hash: 'sha256:ccb65bee2b307ff5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationCallbacks](../authorizationcallbacks.md)

# GetImmutableHintValue

<sub>Instance Property</sub>

Reads an immutable value stored by the plug-in authorization mechanism.

<sub>Mac Catalyst, macOS</sub>

```objc
int (*)(struct __OpaqueAuthorizationEngine *, const char *, const struct AuthorizationValue **) GetImmutableHintValue;
```

## Parameters

- `inEngine` — An opaque handle that is passed to your plug-in when the authorization engine calls your [MechanismCreate](../authorizationplugininterface/mechanismcreate.md) function.

- `inKey` — A key indicating which value you want to retrieve. This key must correspond to one you specified when you used the [SetHintValue](sethintvalue.md) function to store a hint value.

- `outValue` — On input, allocate a pointer to an [AuthorizationValue](../authorizationvalue.md) structure. On output, the structure contains the size of the data and a pointer to the data. Because your [AuthorizationValue](../authorizationvalue.md) structure does not own the data, you must not deallocate the structure or the data pointed to by the structure.

## Return Value

A result code. Possible results are [errAuthorizationSuccess](../errauthorizationsuccess.md) (no error) and [errAuthorizationInternal](../errauthorizationinternal.md) (Security Server internal error).

## Discussion

This function behaves like [GetHintValue](gethintvalue.md), except that the hint is immutable.
