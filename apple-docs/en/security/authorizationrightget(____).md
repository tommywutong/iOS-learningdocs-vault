---
title: 'AuthorizationRightGet(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationrightget(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationrightget(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationrightget%28_%3A_%3A%29.json'
content_hash: 'sha256:3d8988d1e5135d41'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationRightGet(_:_:)

<sub>Function</sub>

Retrieves a right definition as a dictionary.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationRightGet(_ rightName: UnsafePointer<CChar>, _ rightDefinition: UnsafeMutablePointer<CFDictionary?>?) -> OSStatus
```

## Parameters

- `rightName` — An ASCII character string representing the right name. Wildcard right names are valid.

- `rightDefinition` — A reference to a dictionary. On return, this points to a dictionary of keys that define the right. Passing `nil` checks if the right is defined. You should release the memory used by the returned dictionary.

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

You do not need an authorization reference to use this function because the policy database is world readable.
