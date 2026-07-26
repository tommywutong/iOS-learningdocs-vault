---
title: 'insertMediaTimeRange(_:into:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.12+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmutablemovietrack/insertmediatimerange(_:into:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/insertmediatimerange(_:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/insertmediatimerange%28_%3Ainto%3A%29.json'
content_hash: 'sha256:716456f203bcf1dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# insertMediaTimeRange(_:into:)

<sub>Instance Method</sub>

Inserts a reference to a media time range into a track.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func insertMediaTimeRange(_ mediaTimeRange: CMTimeRange, into trackTimeRange: CMTimeRange) -> Bool
```

## Parameters

- `mediaTimeRange` — The presentation time range of the media to be inserted.

- `trackTimeRange` — The time range of the track into which the media is to be inserted.

## Return Value

A Boolean value that indicates whether the insertion was successful.

## Discussion

Use this method after appending samples or sample references to a track’s media. To specify that the media time range be played at its natural rate, pass `mediaTimeRange.duration == trackTimeRange.duration`; otherwise, the ratio between these is used to determine the playback rate. Pass [invalid](../../coremedia/cmtime/invalid.md) for `trackTimeRange.start` to indicate that the segment should be appended to the end of the track.

## See Also

### Appending sample data

- [append(_:)](<append(__).md>) — Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.
- [- appendSampleBuffer:decodeTime:presentationTime:error:](<append(__decodetime_presentationtime_).md>) — Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables. _(deprecated)_
