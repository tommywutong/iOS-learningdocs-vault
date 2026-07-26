---
title: 'SecTransformCreateReadTransformWithReadStream(_:)'
framework: Security
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.7+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/security/sectransformcreatereadtransformwithreadstream(_:)'
source_url: 'https://developer.apple.com/documentation/security/sectransformcreatereadtransformwithreadstream(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectransformcreatereadtransformwithreadstream%28_%3A%29.json'
content_hash: 'sha256:7f8a64b4eaac8d19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecTransformCreateReadTransformWithReadStream(_:)

<sub>Function</sub>

Creates a read transform from a read stream reference.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
func SecTransformCreateReadTransformWithReadStream(_ inputStream: CFReadStream) -> SecTransform
```

## Parameters

- `inputStream` — The stream that is to be opened and read from when the chain executes.

## Return Value

A pointer to a new transform. In Objective-C, call the [CFRelease](../corefoundation/cfrelease.md) function to free this object’s memory when you are done with it.
