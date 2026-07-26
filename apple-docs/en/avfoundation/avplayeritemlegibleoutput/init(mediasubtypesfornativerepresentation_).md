---
title: 'init(mediaSubtypesForNativeRepresentation:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput/init%28mediasubtypesfornativerepresentation%3A%29.json'
content_hash: 'sha256:1da235c08d7746c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemLegibleOutput](../avplayeritemlegibleoutput.md)

# init(mediaSubtypesForNativeRepresentation:)

<sub>Initializer</sub>

Creates an initialized legible-output object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(mediaSubtypesForNativeRepresentation subtypes: [NSNumber])
```

## Parameters

- `subtypes` — An [NSArray](../../foundation/nsarray.md) of [NSNumber](../../foundation/nsnumber.md) FourCC codes.

## Return Value

An initialized instance of `AVPlayerItemLegibleOutput`.

## Discussion

When creating an instance you add media subtype FourCC codes as `NSNumber` objects to the `subtypes` array to elect to receive that type as a [CMSampleBuffer](../../coremedia/cmsamplebuffer.md) instead of an attributed string. FourCC codes are converted to `NSNumber` objects as shown:

```objc
@[ [NSNumber numberWithUnsignedInt:'tx3g'] ]
```

Initializing an `AVPlayerItemLegibleOutput` using the `init` method (which is preferred) is equivalent to calling this method with an empty `subtypes` array, which means that all legible data, regardless of media subtype, is delivered using [NSAttributedString](../../foundation/nsattributedstring.md) instances in a common format.

If a media subtype for which there is no legible data in the current player item is included in the media `subtypes` array, no error occurs.  An `AVPlayerItemLegibleOutput` instance doesn’t vend closed caption data as a [CMSampleBuffer](../../coremedia/cmsamplebuffer.md), so it is an error to include `'c608'` in the media subtypes array.

> [!note] Note
> The preferred method of creating an `AVPlayerItemLegibleOutput` object is to use the [init](../1805461-init.md) method.
