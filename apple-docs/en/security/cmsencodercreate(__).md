---
title: 'CMSEncoderCreate(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/security/cmsencodercreate(_:)'
source_url: 'https://developer.apple.com/documentation/security/cmsencodercreate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/cmsencodercreate%28_%3A%29.json'
content_hash: 'sha256:7a54df40db13e595'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# CMSEncoderCreate(_:)

<sub>Function</sub>

Creates a CMSEncoder reference.

<sub>macOS</sub>

```swift
func CMSEncoderCreate(_ cmsEncoderOut: UnsafeMutablePointer<CMSEncoder?>) -> OSStatus
```

## Parameters

- `cmsEncoderOut` — On return, points to a CMSEncoder reference. You must use the `CFRelease` function to free this reference when you are finished using it.

## Return Value

A result code. See [Security Framework Result Codes](security-framework-result-codes.md).

## Discussion

This is the first function in a sequence of encoder functions that you call to sign or encrypt a message. The other functions in the sequence require you to pass in the CMSEncoder reference returned by this function. In many cases, you can call the [CMSEncode](cmsencode.md) function alone instead of this sequence of encoder functions.
