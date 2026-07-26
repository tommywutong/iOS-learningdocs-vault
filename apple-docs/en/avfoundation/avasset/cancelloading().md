---
title: cancelLoading()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasset/cancelloading()
source_url: 'https://developer.apple.com/documentation/avfoundation/avasset/cancelloading()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasset/cancelloading%28%29.json'
content_hash: 'sha256:93bbe01c640d7789'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsset](../avasset.md)

# cancelLoading()

<sub>Instance Method</sub>

Cancels all pending requests to asynchronously load property values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cancelLoading()
```

## Discussion

Calling this method cancels pending requests to load an asset’s property values. Call this method only when you’re done using an asset and you want to cancel any outstanding requests. Deallocating an asset implicitly calls this method if loading requests are still pending.
