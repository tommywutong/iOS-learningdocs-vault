---
title: initialCapacity
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avprovideostorage/initialcapacity
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/initialcapacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/initialcapacity.json'
content_hash: 'sha256:8c2956d66290edf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# initialCapacity

<sub>Instance Property</sub>

Initial size of Pro Video Storage in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var initialCapacity: Int { get }
```

## Return Value

0 if Pro Video Storage is not configured or -1 if there was a failure while extracting information from it.

## Discussion

The initial capacity is defined by the user via the Settings app.

## See Also

### Inspecting capacity

- [remainingCapacity](remainingcapacity.md) — Current size of Pro Video Storage in bytes. _(beta)_
- [- replenishCapacityWithCompletionHandler:](<replenishcapacity(completionhandler_).md>) — Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app. _(beta)_
