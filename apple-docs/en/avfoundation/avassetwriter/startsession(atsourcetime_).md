---
title: 'startSession(atSourceTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/startsession(atsourcetime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/startsession(atsourcetime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/startsession%28atsourcetime%3A%29.json'
content_hash: 'sha256:0365b6718ad57c68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# startSession(atSourceTime:)

<sub>Instance Method</sub>

Starts an asset-writing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startSession(atSourceTime startTime: CMTime)
```

## Parameters

- `startTime` — The starting asset time for the sample-writing session, in the timeline of the source samples.

## Discussion

You must call this method after you call [- startWriting](<startwriting().md>), but before you append sample data to asset writer inputs.

Each writing session has a start time that, where allowed by the file format you’re writing, defines the mapping from the timeline of source samples to the timeline of the written file. In the case of the QuickTime movie file format, the first session begins at movie time `0`, so a sample you append with timestamp `T` plays at movie time (`T-startTime`). The writer adds samples with timestamps earlier than the start time to the output file, but they don’t display during playback. If the earliest sample for an input has a timestamp later than the start time, the system inserts an empty edit to preserve synchronization between tracks of the output asset.

To end a session, call [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>)or [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>)

> [!note] Note
> An asset writer doesn’t support multiple sample-writing sessions. It’s an error to call [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) a second time after calling [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>).

## See Also

### Managing writing sessions

- [start()](<start().md>) — Prepares the writer to write media data to its output file.
- [- startWriting](<startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- cancelWriting](<cancelwriting().md>) — Cancels the creation of the output file.
- [- finishWriting](<finishwriting().md>) — Completes the writing of the output file. _(deprecated)_
