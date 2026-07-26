---
title: 'resourceLoader(_:shouldWaitForRenewalOfRequestedResource:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforrenewalofrequestedresource:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforrenewalofrequestedresource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader%28_%3Ashouldwaitforrenewalofrequestedresource%3A%29.json'
content_hash: 'sha256:4b3a26dedc4e77e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)

# resourceLoader(_:shouldWaitForRenewalOfRequestedResource:)

<sub>Instance Method</sub>

Tells the delegate when assistance is required of the application to renew a resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForRenewalOfRequestedResource renewalRequest: AVAssetResourceRenewalRequest) -> Bool
```

## Parameters

- `resourceLoader` — The resource loader.

- `renewalRequest` — An instance of `AVAssetResourceRenewalRequest` that provides information about the requested resource.

## Return Value

[true](../../swift/true.md) if the delegate can renew the resource; otherwise [false](../../swift/false.md).

## Discussion

Delegates receive this message when assistance is required to renew a resource previously loaded by [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<resourceloader(__shouldwaitforloadingofrequestedresource_).md>). For example, this method is invoked to for decryption keys that require renewal, as indicated in a response to a prior invocation of [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<resourceloader(__shouldwaitforloadingofrequestedresource_).md>).

If the result is [true](../../swift/true.md), the resource loader expects invocation, either subsequently or immediately, of either the `AVAssetResourceRenewalRequest` method `finishLoading` or `finishLoadingWithError:`. If you intend to finish loading the resource after your handling of this message returns, you must retain the `renewalRequest` until after loading is finished.

If the result is [false](../../swift/false.md), the resource loader treats the loading of the resource as having failed.

> [!note] Note
> If the delegate’s implementation of -[- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<resourceloader(__shouldwaitforloadingofrequestedresource_).md>) returns [true](../../swift/true.md) without finishing the loading request immediately, it may be invoked again with another loading request before the prior request is finished; therefore in such cases the delegate should be prepared to manage multiple loading requests.

## See Also

### Processing resource requests

- [- resourceLoader:shouldWaitForLoadingOfRequestedResource:](<resourceloader(__shouldwaitforloadingofrequestedresource_).md>) — Asks the delegate if it wants to load the requested resource.
- [- resourceLoader:didCancelLoadingRequest:](<resourceloader(__didcancel_)-3nl51.md>) — Informs the delegate that a prior loading request has been cancelled.
