---
title: SecPolicyCreateBasicX509()
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/secpolicycreatebasicx509()
source_url: 'https://developer.apple.com/documentation/security/secpolicycreatebasicx509()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicycreatebasicx509%28%29.json'
content_hash: 'sha256:f2dbabc98b1f55e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyCreateBasicX509()

<sub>Function</sub>

Returns a policy object for the default X.509 policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecPolicyCreateBasicX509() -> SecPolicy
```

## Return Value

The policy object. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to release the object when you are finished with it.
