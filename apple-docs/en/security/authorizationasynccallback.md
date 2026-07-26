---
title: AuthorizationAsyncCallback
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationasynccallback
source_url: 'https://developer.apple.com/documentation/security/authorizationasynccallback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationasynccallback.json'
content_hash: 'sha256:f0929faf669f1a6e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationAsyncCallback

<sub>Type Alias</sub>

A block used as a callback for the asynchronous version of copying authorization rights.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias AuthorizationAsyncCallback = (OSStatus, UnsafeMutablePointer<AuthorizationRights>?) -> Void
```

## Parameters

- `err` — A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md). This is equivalent to the return value from the [AuthorizationCopyRights](<authorizationcopyrights(__________).md>) function.

- `blockAuthorizedRights` — The authorized rights. This is equivalent to the authorizedRights parameter of the [AuthorizationCopyRights](<authorizationcopyrights(__________).md>) function. Free this object using the [AuthorizationFreeItemSet](<authorizationfreeitemset(__).md>) function when you are done with it.

## Discussion

Use a block of this type as the callback parameter to the [AuthorizationCopyRightsAsync](<authorizationcopyrightsasync(__________).md>) function.
