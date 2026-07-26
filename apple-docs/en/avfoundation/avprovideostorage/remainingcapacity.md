---
title: remainingCapacity
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage/remainingcapacity
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/remainingcapacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/remainingcapacity.json'
content_hash: 'sha256:3ec5894ad02e3f86'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# remainingCapacity

<sub>Instance Property</sub>

Current size of Pro Video Storage in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var remainingCapacity: Int { get }
```

## Return Value

0 if Pro Video Storage is not configured or -1 if there was a failure while extracting information from it.

## Discussion

The remaining capacity decreases as recordings are captured.

## See Also

### Inspecting capacity

- [initialCapacity](initialcapacity.md) — Initial size of Pro Video Storage in bytes. _(beta)_
- [- replenishCapacityWithCompletionHandler:](<replenishcapacity(completionhandler_).md>) — Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app. _(beta)_
