---
title: 'legibleOutput(_:didOutputAttributedStrings:nativeSampleBuffers:forItemTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/legibleoutput(_:didoutputattributedstrings:nativesamplebuffers:foritemtime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/legibleoutput(_:didoutputattributedstrings:nativesamplebuffers:foritemtime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutputpushdelegate/legibleoutput%28_%3Adidoutputattributedstrings%3Anativesamplebuffers%3Aforitemtime%3A%29.json'
content_hash: 'sha256:bf4b9ed4908d040a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutputPushDelegate](../avplayeritemlegibleoutputpushdelegate.md)

# legibleOutput(_:didOutputAttributedStrings:nativeSampleBuffers:forItemTime:)

<sub>Instance Method</sub>

Asks the delegate to process the delivery of new textual samples.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func legibleOutput(_ output: AVPlayerItemLegibleOutput, didOutputAttributedStrings strings: [NSAttributedString], nativeSampleBuffers nativeSamples: [Any], forItemTime itemTime: CMTime)
```

## Parameters

- `output` — The [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md) source instance.

- `strings` — An array of [NSAttributedString](../../foundation/nsattributedstring.md) objects, each containing both the run of text and the descriptive markup.

- `nativeSamples` — An array of [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) objects, for media subtypes included in the array passed to the `output` object’s [- initWithMediaSubtypesForNativeRepresentation:](<../avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation_).md>) method.

- `itemTime` — The item time at which the strings should be presented.

## Discussion

For each media subtype in the array passed in to the `output` object’s  [- initWithMediaSubtypesForNativeRepresentation:](<../avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation_).md>) method, the delegate receives sample buffers carrying data in its native format via the `nativeSamples` parameter if there is media data of that subtype in the media resource.

For all other media subtypes present in the media resource, the delegate receives attributed strings in a common format via the `strings` parameter.  See [CMTextMarkup](../../coremedia/cmtextmarkup.md) for the string attributes keys and values that are used in the attributed strings.
