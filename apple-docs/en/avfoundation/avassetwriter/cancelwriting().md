---
title: cancelWriting()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/cancelwriting()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/cancelwriting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/cancelwriting%28%29.json'
content_hash: 'sha256:90aca5fbb6eb3c27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# cancelWriting()

<sub>Instance Method</sub>

Cancels the creation of the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func cancelWriting()
```

## Discussion

If the asset writer is in [AVAssetWriterStatusFailed](status-swift.enum/failed.md) or [AVAssetWriterStatusCompleted](status-swift.enum/completed.md) state, calling this method has no effect. Otherwise, invoking it blocks the calling thread until the asset writer finishes canceling the writing session.

If the asset writer created an output file during the writing process, calling this method deletes the file.

## See Also

### Managing writing sessions

- [start()](<start().md>) — Prepares the writer to write media data to its output file.
- [- startWriting](<startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- finishWriting](<finishwriting().md>) — Completes the writing of the output file. _(deprecated)_
