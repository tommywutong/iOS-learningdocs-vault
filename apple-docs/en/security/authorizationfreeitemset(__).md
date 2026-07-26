---
title: 'AuthorizationFreeItemSet(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationfreeitemset(_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationfreeitemset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationfreeitemset%28_%3A%29.json'
content_hash: 'sha256:772c1f25ac19f932'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationFreeItemSet(_:)

<sub>Function</sub>

Frees the memory associated with a set of authorization items.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationFreeItemSet(_ set: UnsafeMutablePointer<AuthorizationItemSet>) -> OSStatus
```

## Parameters

- `set` — A pointer to the authorization set to free.

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

When your application no longer needs the authorization item sets created by the Security Server in the [AuthorizationCopyRights](<authorizationcopyrights(__________).md>) and [AuthorizationCopyInfo](<authorizationcopyinfo(______).md>) functions, call this function to free it.
