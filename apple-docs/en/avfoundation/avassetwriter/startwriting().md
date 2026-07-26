---
title: startWriting()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriter/startwriting()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/startwriting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/startwriting%28%29.json'
content_hash: 'sha256:1f7d0b062f402267'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# startWriting()

<sub>Instance Method</sub>

Tells the writer to start writing its output.

> [!warning] Deprecated
> Use start() instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startWriting() -> Bool
```

## Return Value

[true](../../swift/true.md) if writing starts successfully; otherwise [false](../../swift/false.md).

## Discussion

You must call this method after you configure the writer and add its inputs to prepare the object to write data. After you call this method, your app can start writing sessions by calling [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) and can write media samples using the methods that the asset writer’s inputs provide.

If writing fails to start, this method returns [false](../../swift/false.md). In this case, check the values of the [status](status-swift.property.md) and [error](error.md) properties to determine the reason for the failure.

## See Also

### Managing writing sessions

- [start()](<start().md>) — Prepares the writer to write media data to its output file.
- [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- cancelWriting](<cancelwriting().md>) — Cancels the creation of the output file.
- [- finishWriting](<finishwriting().md>) — Completes the writing of the output file. _(deprecated)_
