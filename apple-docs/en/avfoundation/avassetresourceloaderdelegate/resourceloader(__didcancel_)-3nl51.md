---
title: 'resourceLoader(_:didCancel:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:didcancel:)-3nl51'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:didcancel:)-3nl51'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader%28_%3Adidcancel%3A%29-3nl51.json'
content_hash: 'sha256:bb0004ddca74ad83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)

# resourceLoader(_:didCancel:)

<sub>Instance Method</sub>

Informs the delegate that a prior loading request has been cancelled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, didCancel loadingRequest: AVAssetResourceLoadingRequest)
```

## Parameters

- `resourceLoader` — The resource loader.

- `loadingRequest` — The loading request that has been cancelled.

## Discussion

Previously issued loading requests can be cancelled when data from the resource is no longer required or when a loading request is superseded by new requests for data from the same resource.

For example, if to complete a seek operation it becomes necessary to load a range of bytes that’s different from a range previously requested, the prior request may be cancelled while the delegate is still handling it.

## See Also

### Processing resource requests

- [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<resourceloader(__shouldwaitforloadingofrequestedresource_).md>) — Asks the delegate if it wants to load the requested resource.
- [- resourceLoader:shouldWaitForRenewalOfRequestedResource:](<resourceloader(__shouldwaitforrenewalofrequestedresource_).md>) — Tells the delegate when assistance is required of the application to renew a resource.
