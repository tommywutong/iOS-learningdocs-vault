---
title: 'append(_:decodeTime:presentationTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avmutablemovietrack/append(_:decodetime:presentationtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmutablemovietrack/append(_:decodetime:presentationtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmutablemovietrack/append%28_%3Adecodetime%3Apresentationtime%3A%29.json'
content_hash: 'sha256:83bd893a4f0d336f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMutableMovieTrack](../avmutablemovietrack.md)

# append(_:decodeTime:presentationTime:)

<sub>Instance Method</sub>

Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.

> [!warning] Deprecated
> Use append(_:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS, watchOS</sub>

```swift
func append(_ sampleBuffer: CMSampleBuffer, decodeTime outDecodeTime: UnsafeMutablePointer<CMTime>?, presentationTime outPresentationTime: UnsafeMutablePointer<CMTime>?) throws
```

## Parameters

- `sampleBuffer` — The sample buffer to be appended.

- `outDecodeTime` — A pointer to a [CMTime](../../coremedia/cmtime.md) structure to receive the decode time in the media of the first sample appended from the sample buffer. Pass `NULL` if the information is not needed.

- `outPresentationTime` — A pointer to a [CMTime](../../coremedia/cmtime.md) structure to receive the presentation time in the media of the first sample appended from the sample buffer. Pass `NULL` if the information is not needed.

## Discussion

If the sample buffer carries sample data, the sample data is written to the container specified by the track property [mediaDataStorage](mediadatastorage.md) if non-nil, or by the movie property [defaultMediaDataStorage](../avmutablemovie/defaultmediadatastorage.md) if non-nil, and sample references are appended to the track’s media. If both media data storage properties are `nil`, the method will fail and return `NO`.

If the sample buffer carries sample references only, sample data will not be written and sample references to the samples in their original container are appended to the track’s media as necessary.

> [!note] Note
> In a track’s media, the first sample’s decode timestamp must be zero. For an audio track, each sample buffer’s duration is used as the sample decode duration. For other track types, the difference between a sample’s decode timestamp and the following sample’s decode timestamp is used as the first sample’s decode duration, so as to preserve the relative timing.

To make the new samples appear in the track’s timeline, invoke [- insertMediaTimeRange:intoTimeRange:](<insertmediatimerange(__into_).md>). Retrieve the [mediaPresentationTimeRange](../avmovietrack/mediapresentationtimerange.md) property before and after appending a sequence of samples, using [CMTimeRangeGetEnd(_:)](<../../coremedia/cmtimerangegetend(__).md>) on each to calculate the media time range for [- insertMediaTimeRange:intoTimeRange:](<insertmediatimerange(__into_).md>).

It’s safe for multiple threads to call this method on different tracks at the same time.

## See Also

### Appending sample data

- [append(_:)](<append(__).md>) — Appends sample data to a media file and adds sample references for the added data to a track’s media sample tables.
- [- insertMediaTimeRange:intoTimeRange:](<insertmediatimerange(__into_).md>) — Inserts a reference to a media time range into a track.
