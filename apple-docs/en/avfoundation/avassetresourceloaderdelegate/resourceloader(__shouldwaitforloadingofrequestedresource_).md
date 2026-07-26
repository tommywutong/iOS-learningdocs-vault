---
title: 'resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader(_:shouldwaitforloadingofrequestedresource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetresourceloaderdelegate/resourceloader%28_%3Ashouldwaitforloadingofrequestedresource%3A%29.json'
content_hash: 'sha256:28afda6fdf2042cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetResourceLoaderDelegate](../avassetresourceloaderdelegate.md)

# resourceLoader(_:shouldWaitForLoadingOfRequestedResource:)

<sub>Instance Method</sub>

Asks the delegate if it wants to load the requested resource.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func resourceLoader(_ resourceLoader: AVAssetResourceLoader, shouldWaitForLoadingOfRequestedResource loadingRequest: AVAssetResourceLoadingRequest) -> Bool
```

## Parameters

- `resourceLoader` — The resource loader object that is making the request.

- `loadingRequest` — The loading request object that contains information about the requested resource.

## Return Value

[true](../../swift/true.md) if your delegate can load the resource specified by the `loadingRequest` parameter or [false](../../swift/false.md) if it cannot.

## Discussion

The resource loader object calls this method when assistance is required of your code to load the specified resource. For example, the resource loader might call this method to load decryption keys that have been specified using a custom URL scheme.

Returning [true](../../swift/true.md) from this method, implies only that the receiver will load, or at least attempt to load, the resource. In some implementations, the actual work of loading the resource might be initiated on another thread, running asynchronously to the resource loading delegate; whether the work begins immediately or merely soon is an implementation detail of the client application.

You can load the resource synchronously or asynchronously. In both cases, you must indicate success or failure of the operation by calling the [- finishLoadingWithResponse:data:redirect:](<../avassetresourceloadingrequest/finishloading(with_data_redirect_).md>) or [- finishLoadingWithError:](<../avassetresourceloadingrequest/finishloading(with_).md>) method of the request object when you finish. If you load the resource asynchronously, you must also store a strong reference to the object in the `loadingRequest` parameter before returning from this method.

If you return [false](../../swift/false.md) from this method, the resource loader treats the loading of the resource as having failed.

## See Also

### Processing resource requests

- [- resourceLoader:shouldWaitForRenewalOfRequestedResource:](<resourceloader(__shouldwaitforrenewalofrequestedresource_).md>) — Tells the delegate when assistance is required of the application to renew a resource.
- [- resourceLoader:didCancelLoadingRequest:](<resourceloader(__didcancel_)-3nl51.md>) — Informs the delegate that a prior loading request has been cancelled.
