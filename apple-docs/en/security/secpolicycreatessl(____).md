---
title: 'SecPolicyCreateSSL(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secpolicycreatessl(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secpolicycreatessl(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicycreatessl%28_%3A_%3A%29.json'
content_hash: 'sha256:1efcfe1f1f19049b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyCreateSSL(_:_:)

<sub>Function</sub>

Returns a policy object for evaluating SSL certificate chains.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecPolicyCreateSSL(_ server: Bool, _ hostname: CFString?) -> SecPolicy
```

## Parameters

- `server` — Specify `true` on the client side to return a policy for SSL server certificates.

- `hostname` — If you specify a value for this parameter, the policy will require the specified value to match the host name in the leaf certificate.

## Return Value

The policy object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release the object when you are finished with it.
