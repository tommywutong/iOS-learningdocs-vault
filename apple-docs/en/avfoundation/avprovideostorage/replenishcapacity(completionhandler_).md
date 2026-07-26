---
title: 'replenishCapacity(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avprovideostorage/replenishcapacity(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avprovideostorage/replenishcapacity(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avprovideostorage/replenishcapacity%28completionhandler%3A%29.json'
content_hash: 'sha256:d6735f8b404c75c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVProVideoStorage](../avprovideostorage.md)

# replenishCapacity(completionHandler:)

<sub>Instance Method</sub>

Performs a best-effort attempt to restore Pro Video Storage to the initial capacity specified by the user in Settings app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func replenishCapacity(completionHandler: (@Sendable (Int, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func replenishCapacity() async throws -> Int
```

## Parameters

- `completionHandler` — The completion handler is called on an arbitrary dispatch queue when the replenish operation finishes. The `remainingCapacity` parameter reflects the new size in bytes, which may be less than [initialCapacity](initialcapacity.md). If the operation fails, the `error` parameter is set and `remainingCapacity` is unchanged or -1 if there was a failure retrieving the value.

## Discussion

If there is enough readily available free space on the file system, Pro Video Storage will be resized to [initialCapacity](initialcapacity.md). Otherwise, this method will attempt to resize it near that value.

Pro Video Storage is busy when the replenish operation starts and is no longer busy when the completion handler is called.

## See Also

### Inspecting capacity

- [initialCapacity](initialcapacity.md) — Initial size of Pro Video Storage in bytes. _(beta)_
- [remainingCapacity](remainingcapacity.md) — Current size of Pro Video Storage in bytes. _(beta)_
