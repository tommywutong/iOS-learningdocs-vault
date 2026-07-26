---
title: 'SecPolicyCopyProperties(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secpolicycopyproperties(_:)'
source_url: 'https://developer.apple.com/documentation/security/secpolicycopyproperties(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicycopyproperties%28_%3A%29.json'
content_hash: 'sha256:56d438c84eeb6722'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyCopyProperties(_:)

<sub>Function</sub>

Returns a dictionary containing a policy’s properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecPolicyCopyProperties(_ policyRef: SecPolicy) -> CFDictionary?
```

## Parameters

- `policyRef` — The policy from which properties should be copied.

## Return Value

A dictionary with the policy’s properties. See [Security Policy Keys](security-policy-keys.md) for a list of valid keys. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free the dictionary’s memory when you are done with it.
