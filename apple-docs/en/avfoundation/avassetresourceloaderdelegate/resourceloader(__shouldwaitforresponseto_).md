---
title: 'resourceLoader(_:shouldWaitForResponseTo:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforresponseto:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforresponseto:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader%28_%3Ashouldwaitforresponseto%3A%29.json'
content_hash: 'sha256:ba794524029b4075'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)

# resourceLoader(_:shouldWaitForResponseTo:)

<sub>Instance Method</sub>

Tells the delegate that assistance is required of the application to respond to an authentication challenge.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForResponseTo authenticationChallenge: URLAuthenticationChallenge) -> Bool
```

## Parameters

- `resourceLoader` — The resource loader.

- `authenticationChallenge` — The authentication challenge.

## Return Value

[true](../../swift/true.md) if the resource loader should wait for a response to the authentication challenge; otherwise [false](../../swift/false.md).

## Discussion

Delegates receive this message when assistance is required of the application to respond to an authentication challenge.

Return [true](../../swift/true.md) if you expect a response either subsequently or immediately to the authenticationChallenger object’s sender.

If you intend to respond to the authentication challenge after your handling of `resourceLoader:shouldWaitForResponseToAuthenticationChallenge:` returns, you must retain the authenticationChallenge until after your response has been made.

## See Also

### Processing authentication challenges

- [- resourceLoader:didCancelAuthenticationChallenge:](<resourceloader(__didcancel_)-1wqin.md>) — Informs the delegate that a prior authentication challenge has been cancelled.
