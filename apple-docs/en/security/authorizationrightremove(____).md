---
title: 'AuthorizationRightRemove(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/authorizationrightremove(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/authorizationrightremove(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationrightremove%28_%3A_%3A%29.json'
content_hash: 'sha256:5a43ed5f3190f285'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationRightRemove(_:_:)

<sub>Function</sub>

Removes a right from the policy database.

<sub>Mac Catalyst, macOS</sub>

```swift
func AuthorizationRightRemove(_ authRef: AuthorizationRef, _ rightName: UnsafePointer<CChar>) -> OSStatus
```

## Parameters

- `authRef` — A valid authorization reference used to authorize modifications.

- `rightName` — An ASCII character string representing the right name. This function does not accept wildcard right names.

## Return Value

A result code. See [Authorization Services Result Codes](authorization-services-result-codes.md).

## Discussion

The right you remove must be an explicit right with no wildcards. Wildcard rights are for use by system administrators for site configuration.
