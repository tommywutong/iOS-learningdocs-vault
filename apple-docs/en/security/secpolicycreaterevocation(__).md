---
title: 'SecPolicyCreateRevocation(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/secpolicycreaterevocation(_:)'
source_url: 'https://developer.apple.com/documentation/security/secpolicycreaterevocation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/secpolicycreaterevocation%28_%3A%29.json'
content_hash: 'sha256:f7d2bf735d8fdee8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecPolicyCreateRevocation(_:)

<sub>Function</sub>

Returns a policy object for checking revocation of certificates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func SecPolicyCreateRevocation(_ revocationFlags: CFOptionFlags) -> SecPolicy?
```

## Parameters

- `revocationFlags` — Flags that specify revocation checking options. See [Revocation Policy Constants](revocation-policy-constants.md) for a list of possible values.

## Return Value

A policy object or `nil` on failure.

## Discussion

It’s usually not necessary to create a revocation policy yourself unless you wish to override default system behavior, for example to force a particular method, or to disable revocation checking entirely.
