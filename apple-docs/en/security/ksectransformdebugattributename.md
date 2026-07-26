---
title: kSecTransformDebugAttributeName
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [macOS 10.7+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/ksectransformdebugattributename
source_url: 'https://developer.apple.com/documentation/security/ksectransformdebugattributename'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/ksectransformdebugattributename.json'
content_hash: 'sha256:0d194284645aeb47'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kSecTransformDebugAttributeName

<sub>Global Variable</sub>

A write stream that should receive debug data.

> [!warning] Deprecated
> SecTransform is no longer supported

<sub>macOS</sub>

```swift
let kSecTransformDebugAttributeName: CFString
```

## Discussion

Set this attribute to a [CFWriteStream](../corefoundation/cfwritestream.md). This signals the transform to write debugging information to the stream. If you set this attribute to [kCFBooleanTrue](../corefoundation/kcfbooleantrue.md), debug data is written to `stderr` instead.
