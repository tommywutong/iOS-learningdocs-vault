---
title: 'rangeOfAudioTimeRangeAttributes(intersecting:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/rangeofaudiotimerangeattributes(intersecting:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/rangeofaudiotimerangeattributes(intersecting:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/rangeofaudiotimerangeattributes%28intersecting%3A%29.json'
content_hash: 'sha256:0afc6cdf01d204fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# rangeOfAudioTimeRangeAttributes(intersecting:)

<sub>Instance Method</sub>

Returns the range of the attributed string that is within the given time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func rangeOfAudioTimeRangeAttributes(intersecting timeRange: CMTimeRange) -> Range<AttributedString.Index>?
```

## Parameters

- `timeRange` — An audio time range.

## Return Value

The range of the string’s intersecting text, or `nil` if the string has no intersecting text.

## Discussion

The method compares the given time range against the [TimeRangeAttribute](../attributescopes/speechattributes/timerangeattribute.md) attributes of the string. The time ranges in the string should be in ascending order, but not necessarily contiguous, and the string can include runs without a time range attribute.

You can use this method to help update an attributed string that tracks the volatile or finalized results of a `SpeechTranscriber` or `DictationTranscriber` module.
