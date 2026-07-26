---
title: makeSampleCursorAtLastSampleInDecodeOrder()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 10.10+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassettrack/makesamplecursoratlastsampleindecodeorder()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/makesamplecursoratlastsampleindecodeorder()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/makesamplecursoratlastsampleindecodeorder%28%29.json'
content_hash: 'sha256:1148d9cbc6c54f13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# makeSampleCursorAtLastSampleInDecodeOrder()

<sub>Instance Method</sub>

Creates a sample cursor and positions it at the track’s last media sample in decode order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func makeSampleCursorAtLastSampleInDecodeOrder() -> AVSampleCursor?
```

## Return Value

An instance of [AVSampleCursor](../avsamplecursor.md).

## See Also

### Creating sample cursors

- [- makeSampleCursorWithPresentationTimeStamp:](<makesamplecursor(presentationtimestamp_).md>) — Creates a sample cursor and positions it at or near the specified presentation timestamp.
- [- makeSampleCursorAtFirstSampleInDecodeOrder](<makesamplecursoratfirstsampleindecodeorder().md>) — Creates a sample cursor and positions it at the track’s first media sample in decode order.
