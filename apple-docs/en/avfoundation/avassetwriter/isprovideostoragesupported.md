---
title: isProVideoStorageSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/isprovideostoragesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/isprovideostoragesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/isprovideostoragesupported.json'
content_hash: 'sha256:968b9c720565bd0d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# isProVideoStorageSupported

<sub>Instance Property</sub>

Indicates whether the receiver supports writing to pre-allocated storage on this device for high data rate video capture formats such as ProRes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isProVideoStorageSupported: Bool { get }
```

## Discussion

Check this value prior to setting the `usesProVideoStorage` property to avoid exceptions when pre-allocated storage is not supported.
