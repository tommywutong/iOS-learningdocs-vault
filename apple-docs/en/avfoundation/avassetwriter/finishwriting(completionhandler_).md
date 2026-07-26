---
title: 'finishWriting(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/finishwriting(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/finishwriting(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/finishwriting%28completionhandler%3A%29.json'
content_hash: 'sha256:7581c759749de62f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# finishWriting(completionHandler:)

<sub>Instance Method</sub>

Marks all unfinished inputs as finished and completes the writing of the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finishWriting(completionHandler handler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func finishWriting() async
```

## Parameters

- `handler` — A completion handler the system invokes when it finishes writing. Determine the success or failure of the writing session by querying the asset writer’s [status](status-swift.property.md) property value.

## Discussion

To ensure the asset writer finishes writing all samples, call this method only after all calls to [- appendSampleBuffer:](<../avassetwriterinput/append(__).md>) or [- appendPixelBuffer:withPresentationTime:](<../avassetwriterinputpixelbufferadaptor/append(__withpresentationtime_).md>) return.

## See Also

### Managing writing sessions

- [start()](<start().md>) — Prepares the writer to write media data to its output file.
- [- startWriting](<startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- cancelWriting](<cancelwriting().md>) — Cancels the creation of the output file.
- [- finishWriting](<finishwriting().md>) — Completes the writing of the output file. _(deprecated)_
