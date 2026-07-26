---
title: finishWriting()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [tvOS 9.0+（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriter/finishwriting()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriter/finishwriting()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriter/finishwriting%28%29.json'
content_hash: 'sha256:310d1ef96c415f6c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriter](../avassetwriter.md)

# finishWriting()

<sub>Instance Method</sub>

Completes the writing of the output file.

> [!warning] Deprecated
> Use [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) instead.

<sub>tvOS</sub>

```swift
func finishWriting() -> Bool
```

## Return Value

[true](../../swift/true.md) if writing can be finished, otherwise [false](../../swift/false.md).

## See Also

### Managing writing sessions

- [start()](<start().md>) — Prepares the writer to write media data to its output file.
- [- startWriting](<startwriting().md>) — Tells the writer to start writing its output. _(deprecated)_
- [- startSessionAtSourceTime:](<startsession(atsourcetime_).md>) — Starts an asset-writing session.
- [- endSessionAtSourceTime:](<endsession(atsourcetime_).md>) — Finishes an asset-writing session.
- [- finishWritingWithCompletionHandler:](<finishwriting(completionhandler_).md>) — Marks all unfinished inputs as finished and completes the writing of the output file.
- [- cancelWriting](<cancelwriting().md>) — Cancels the creation of the output file.
