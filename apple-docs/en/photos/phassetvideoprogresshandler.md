---
title: PHAssetVideoProgressHandler
framework: Photos
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetvideoprogresshandler
source_url: 'https://developer.apple.com/documentation/photos/phassetvideoprogresshandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetvideoprogresshandler.json'
content_hash: 'sha256:12b34a63ad5ba309'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetVideoProgressHandler

<sub>Type Alias</sub>

The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](phvideorequestoptions/progresshandler.md) property.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias PHAssetVideoProgressHandler = (Double, (any Error)?, UnsafeMutablePointer<ObjCBool>, [AnyHashable : Any]?) -> Void
```

## Discussion

If you request a video asset whose data is not on the local device, and you have enabled downloading with the [networkAccessAllowed](phvideorequestoptions/isnetworkaccessallowed.md) property, Photos calls your block periodically to report progress and allow canceling the download.

> [!note] Note
> Because Photos calls this block in an arbitrary serial queue, it may not execute on the main thread.

The block takes the following parameters:

- **progress** — A floating-point value indicating the progress of the download. A value of `0.0` indicates the download has just started, and a value of `1.0` indicates the download is complete.
- **error** — An `NSError` object describing an error that occurred when attempting to download the video, or `nil` if no errors have occurred.
- **stop** — A pointer to a Boolean value. To cancel the download, set `*stop` to `true` inside the block.
- **info** — A dictionary providing additional information about the status of the video request. See Image Result Info Keys for possible keys and values.

## See Also

### Fetching Video Data from iCloud

- [networkAccessAllowed](phvideorequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested video from iCloud.
- [progressHandler](phvideorequestoptions/progresshandler.md) — A block Photos calls periodically while downloading the video.
