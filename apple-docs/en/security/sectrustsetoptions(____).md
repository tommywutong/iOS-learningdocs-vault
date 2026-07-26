---
title: 'SecTrustSetOptions(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/sectrustsetoptions(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/sectrustsetoptions(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustsetoptions%28_%3A_%3A%29.json'
content_hash: 'sha256:2aa4be4f0e1364f3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTrustSetOptions(_:_:)

<sub>Function</sub>

Sets option flags for customizing evaluation of a trust object.

<sub>macOS</sub>

```swift
func SecTrustSetOptions(_ trustRef: SecTrust, _ options: SecTrustOptionFlags) -> OSStatus
```

## Parameters

- `trustRef` — The trust object to modify.

- `options` — The new set of option flags. For a list of options, see [SecTrustOptionFlags](sectrustoptionflags.md).

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
