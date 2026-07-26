---
title: 'SecPolicyCreateWithProperties(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secpolicycreatewithproperties(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/secpolicycreatewithproperties(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicycreatewithproperties%28_%3A_%3A%29.json'
content_hash: 'sha256:3642c631d4abd598'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyCreateWithProperties(_:_:)

<sub>Function</sub>

Returns a policy object based on an object identifier for the policy type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecPolicyCreateWithProperties(_ policyIdentifier: CFTypeRef, _ properties: CFDictionary?) -> SecPolicy?
```

## Parameters

- `policyIdentifier` — The identifier for the desired policy type.

- `properties` — A properties dictionary. See [Security Policy Keys](security-policy-keys.md) for a list of valid property names to use as keys in this dictionary.

## Return Value

A new policy, or `NULL` if the policy could not be created.
