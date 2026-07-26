---
title: 'cancelDataRequest(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresourcemanager/canceldatarequest(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcemanager/canceldatarequest(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcemanager/canceldatarequest%28_%3A%29.json'
content_hash: 'sha256:832dfff1e6f21647'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceManager](../phassetresourcemanager.md)

# cancelDataRequest(_:)

<sub>Instance Method</sub>

Cancels an asynchronous request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelDataRequest(_ requestID: PHAssetResourceDataRequestID)
```

## Parameters

- `requestID` — The numeric identifier of the request to be canceled.

## Discussion

When you perform an asynchronous request for asset resource data using the [- requestDataForAssetResource:options:dataReceivedHandler:completionHandler:](<requestdata(for_options_datareceivedhandler_completionhandler_).md>) method, the image manager returns a numeric identifier for the request. To cancel the request before it completes, provide this identifier when calling the [- cancelDataRequest:](<canceldatarequest(__).md>) method.

## See Also

### Requesting Resources

- [- requestDataForAssetResource:options:dataReceivedHandler:completionHandler:](<requestdata(for_options_datareceivedhandler_completionhandler_).md>) — Requests the underlying data for the specified asset resource, to be delivered asynchronously.
- [- writeDataForAssetResource:toFile:options:completionHandler:](<writedata(for_tofile_options_completionhandler_).md>) — Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.
