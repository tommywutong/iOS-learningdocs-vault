---
title: 'resourceLoader(_:didCancel:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:didcancel:)-1wqin'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:didcancel:)-1wqin'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader%28_%3Adidcancel%3A%29-1wqin.json'
content_hash: 'sha256:5d9e020dfec4a475'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)

# resourceLoader(_:didCancel:)

<sub>Instance Method</sub>

Informs the delegate that a prior authentication challenge has been cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel authenticationChallenge: URLAuthenticationChallenge)
```

## Parameters

- `resourceLoader` — The resource loader.

- `authenticationChallenge` — The authentication challenge that has been cancelled.

## See Also

### Processing authentication challenges

- [- resourceLoader:shouldWaitForResponseToAuthenticationChallenge:](<resourceloader(__shouldwaitforresponseto_).md>) — Tells the delegate that assistance is required of the application to respond to an authentication challenge.
