---
title: start()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriter/start()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/start()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/start%28%29.json'
content_hash: 'sha256:fa1b22b06d605338'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# start()

<sub>Instance Method</sub>

Prepares the writer to write media data to its output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func start() throws
```

## Discussion

> [!danger] Throws
> An error if reading fails to start.

## See Also

### Managing writing sessions

- [- startWriting](<startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- cancelWriting](<cancelwriting().md>) — Cancels the creation of the output file.
- [- finishWriting](<finishwriting().md>) — Completes the writing of the output file. _(deprecated)_
