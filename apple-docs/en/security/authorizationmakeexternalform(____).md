---
title: 'AuthorizationMakeExternalForm(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationmakeexternalform(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationmakeexternalform(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationmakeexternalform%28_%3A_%3A%29.json'
content_hash: 'sha256:17efc91b43baecde'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationMakeExternalForm(_:_:)

<sub>Function</sub>

Creates an external representation of an authorization reference.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationMakeExternalForm(_ authorization: AuthorizationRef, _ extForm: UnsafeMutablePointer<AuthorizationExternalForm>) -> OSStatus
```

## Parameters

- `authorization` — An authorization reference referring to the authorization session.

- `extForm` — A pointer to an external authorization reference. On return, this points to the external representation of the authorization reference.

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

This function creates an external representation of an authorization reference so that you can transmit it between processes. Authorizations are bound by session, process, and time limits, so you cannot store the authorization reference for another process to use. Instead, you must create an external representation of the authorization reference and pass it securely to the other process. Use the function [AuthorizationCreateFromExternalForm](<authorizationcreatefromexternalform(____).md>) to internalize the external representation of the authorization reference.

If it is necessary for your application to perform some privileged operations, it is good programming practice to isolate all of the privileged operations in a separate process, referred to as a _helper tool_ (see [Authorization Services Programming Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/authorization_concepts/01introduction/introduction.html#//apple_ref/doc/uid/TP30000995) for details). In this case, you must pass your authorization reference to the helper tool so that Authorization Services can tell that the helper tool is operating on behalf of your application. Doing so allows the authorization dialog to show your application’s path rather than the path to the helper tool and it allows the system to determine whether the authorization dialog should have keyboard focus.
