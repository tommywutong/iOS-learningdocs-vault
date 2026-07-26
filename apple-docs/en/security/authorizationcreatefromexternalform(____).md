---
title: 'AuthorizationCreateFromExternalForm(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationcreatefromexternalform(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationcreatefromexternalform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationcreatefromexternalform%28_%3A_%3A%29.json'
content_hash: 'sha256:8bc593a5fb2804db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationCreateFromExternalForm(_:_:)

<sub>Function</sub>

Internalizes the external representation of an authorization reference.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationCreateFromExternalForm(_ extForm: UnsafePointer<AuthorizationExternalForm>, _ authorization: UnsafeMutablePointer<AuthorizationRef?>) -> OSStatus
```

## Parameters

- `extForm` — A pointer to the external representation of the authorization reference you retrieve from the calling process.

- `authorization` — A pointer to an authorization reference. On return, this points to the local copy of the authorization reference. The Security Server allocates the authorization reference for you, so you do not need to call the function [AuthorizationCreate](<authorizationcreate(________).md>).

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

When passing an authorization reference between processes, use this function to internalize the external representation of the authorization reference you created using the function [AuthorizationMakeExternalForm](<authorizationmakeexternalform(____).md>).
