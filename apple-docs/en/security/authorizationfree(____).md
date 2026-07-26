---
title: 'AuthorizationFree(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationfree(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationfree(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationfree%28_%3A_%3A%29.json'
content_hash: 'sha256:cd5c34d9862325aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationFree(_:_:)

<sub>Function</sub>

Frees the memory associated with an authorization reference.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationFree(_ authorization: AuthorizationRef, _ flags: AuthorizationFlags) -> OSStatus
```

## Parameters

- `authorization` — The authorization reference to free.

- `flags` — A bit mask. In most cases, pass the constant [kAuthorizationFlagDefaults](authorizationflags/kauthorizationflagdefaults.md). To remove all shared and non-shared authorizations, pass the constant [kAuthorizationFlagDestroyRights](authorizationflags/destroyrights.md).

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

Call this function when your application no longer needs the authorization reference you created using the function [AuthorizationCreate](<authorizationcreate(________).md>).
