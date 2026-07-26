---
title: 'AuthorizationCopyInfo(_:_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationcopyinfo(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationcopyinfo(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcopyinfo%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:c666b01d166196f9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationCopyInfo(_:_:_:)

<sub>Function</sub>

Retrieves supporting data such as the user name and other information gathered during evaluation of authorization.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationCopyInfo(_ authorization: AuthorizationRef, _ tag: AuthorizationString?, _ info: UnsafeMutablePointer<UnsafeMutablePointer<AuthorizationItemSet>?>) -> OSStatus
```

## Parameters

- `authorization` — An authorization reference referring to the authorization session.

- `tag` — An [AuthorizationString](authorizationstring.md) specifying the type of data the Security Server should return. Pass `nil` to retrieve all available information.

- `info` — A pointer to an authorization set the Security Server creates. On return, this set contains side-band authorization data. When this set is no longer needed, free the memory associated with it by calling the function [AuthorizationFreeItemSet](<authorizationfreeitemset(__).md>).

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

An authorization plug-in can store the results of an authentication operation by calling the [SetContextValue](authorizationcallbacks/setcontextvalue.md) function. You can use the [AuthorizationCopyInfo](<authorizationcopyinfo(______).md>) function to retrieve this information.
