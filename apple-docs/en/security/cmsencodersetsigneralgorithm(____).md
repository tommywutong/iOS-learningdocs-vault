---
title: 'CMSEncoderSetSignerAlgorithm(_:_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.11+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodersetsigneralgorithm(_:_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodersetsigneralgorithm(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodersetsigneralgorithm%28_%3A_%3A%29.json'
content_hash: 'sha256:cdcc4f4492a3096b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderSetSignerAlgorithm(_:_:)

<sub>Function</sub>

Sets the digest algorithm to use for the signer.

<sub>macOS</sub>

```swift
func CMSEncoderSetSignerAlgorithm(_ cmsEncoder: CMSEncoder, _ digestAlgorithm: CFString) -> OSStatus
```

## Parameters

- `cmsEncoder` — The CMSEncoder reference returned by the [CMSEncoderCreate](<cmsencodercreate(__).md>) function.

- `digestAlgorithm` — A string representing the digest algorithm to use.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).
