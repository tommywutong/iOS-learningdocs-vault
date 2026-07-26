---
title: 'writeData(for:toFile:options:completionHandler:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresourcemanager/writedata(for:tofile:options:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcemanager/writedata(for:tofile:options:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcemanager/writedata%28for%3Atofile%3Aoptions%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:fdbab619b69d251b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceManager](../phassetresourcemanager.md)

# writeData(for:toFile:options:completionHandler:)

<sub>Instance Method</sub>

Requests the underlying data for the specified asset resource, to be asynchronously written to a local file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeData(for resource: PHAssetResource, toFile fileURL: URL, options: PHAssetResourceRequestOptions?, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func writeData(for resource: PHAssetResource, toFile fileURL: URL, options: PHAssetResourceRequestOptions?) async throws
```

## Parameters

- `resource` — The asset resource for which to request data.

- `fileURL` — A URL identifying the local filename at which to write the asset resource’s data.

- `options` — Options specifying how Photos should handle the request and notify your app of progress. For details, see [PHAssetResourceRequestOptions](../phassetresourcerequestoptions.md).

- `completionHandler` — A block that photos calls after the request has been fulfilled or has failed. The block takes a single parameter: - **error** — If the request has failed, an `NSError` object describing the failure; otherwise `nil`.

## Discussion

When you call this method, Photos begins asynchronously reading the underlying data for the asset resource. Depending on the options you specify and the current state of the asset, Photos may download asset data from the network.

While reading (or downloading) asset resource data, Photos progressively writes the data into the specified file. After writing all of the data, or if an error prevents reading all of the data, Photos calls your `completionHandler` block.

> [!note] Note
> Photos calls your `completionHandler` block on an arbitrary serial queue. To update the UI in response to these events, dispatch to the main queue.

## See Also

### Requesting Resources

- [- requestDataForAssetResource:options:dataReceivedHandler:completionHandler:](<requestdata(for_options_datareceivedhandler_completionhandler_).md>) — Requests the underlying data for the specified asset resource, to be delivered asynchronously.
- [- cancelDataRequest:](<canceldatarequest(__).md>) — Cancels an asynchronous request.
