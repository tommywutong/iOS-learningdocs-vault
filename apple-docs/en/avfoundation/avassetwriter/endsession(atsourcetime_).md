---
title: 'endSession(atSourceTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriter/endsession(atsourcetime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/endsession(atsourcetime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/endsession%28atsourcetime%3A%29.json'
content_hash: 'sha256:497b9de7513390b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# endSession(atSourceTime:)

<sub>Instance Method</sub>

Finishes an asset-writing session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func endSession(atSourceTime endTime: CMTime)
```

## Parameters

- `endTime` — The ending asset time for the session, in the timeline of the source samples.

## Discussion

Call this method to complete a session that you started with [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>).

The end time defines the moment on the timeline of source samples at which the session ends. In the case of the QuickTime movie file format, each sample-writing session’s start and end time pair corresponds to a period of movie time into which a writer inserts samples. The writer adds samples with timestamps that are later than the session end time to the written file but they aren’t presented during playback. For example, if the first session has duration `D1 = endTime - startTime`, the writer inserts it into the written file at time `0` through `D1`; the second session would insert into the written file at time `D1` through `D1 + D2`, and so on. It’s legal to have a session with no samples; this causes the creation of an empty edit of the prescribed duration.

If you don’t explicitly call this method, the system invokes it automatically when you call [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>). In that case, the session’s effective end time is the timestamp of the last sample you append.

> [!note] Note
> An asset writer doesn’t support multiple sample-writing sessions. It’s an error to call [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) a second time after calling [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>).

## See Also

### Managing writing sessions

- [start()](<start().md>) — Prepares the writer to write media data to its output file.
- [- startWriting](<startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- cancelWriting](<cancelwriting().md>) — Cancels the creation of the output file.
- [- finishWriting](<finishwriting().md>) — Completes the writing of the output file. _(deprecated)_
