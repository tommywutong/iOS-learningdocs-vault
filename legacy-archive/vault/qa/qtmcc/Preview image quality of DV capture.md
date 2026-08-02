---
title: Preview image quality of DV capture
apple_id: DTS10001955
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-12'
source_url: https://developer.apple.com/library/archive/qa/qtmcc/qtmcc12.html
archived_at: '2026-07-18T02:38:47.053708Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Movie Creation](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxMovieCreation-date.html) >

|  |
| --- |
| Technical Q&A QTMCC12Preview image quality of DV capture |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ---   Q: The preview display of QuickTime movies captured using a DV camera over FireWire are not particularly sharp. Is there anything I can do to sharpen the images?  A: To save CPU processing time, the QuickTime DV image decompressor component usually draws DV movies using only a quarter of the original DV data, resulting in poor rendering focus. You can improve the rendering focus by using the `SetMoviePlayHints` and `SetMediaPlayHints` functions along with the `hintsHighQuality` flag to render the movie in full resolution during playback. When this flag is set, image quality takes precedence over frame rate (but note that rendering at the highest quality takes much more time and memory than rendering at a lesser quality). You can also order QuickTime Player (Pro version) to render in full resolution using the __Get Info__ panel in the __Movie__ menu. Check the “High Quality Enabled” box of Video Track.  Similarly, you can use the `SGSetChannelPlayFlags` function along with the `channelPlayHighQuality` flag during movie capture to instruct the channel component to play the channel’s data at the highest possible quality:     |  | | --- | | ``` err = SGSetChannelPlayFlags(theVch, channelPlayHighQuality); ``` |    This flag has no effect under QuickTime 3, but it does not return an error either. Note that once you’ve set high-quality mode in this manner, the mode will remain in effect during both preview and record operations. While recording, you should reset the mode to normal playback to avoid dropping frames:     |  | | --- | | ``` err = SGSetChannelPlayFlags(theVch, channelPlayNormal); ``` |    The DV decompressor in QuickTime 4 allows you to request single-field processing if you are decoding in high quality. This is useful to eliminate field aliasing when displaying still images. The parameter is passed in to the DV decompressor using the `requestedSingleField` parameter in the `CodecDecompressParams` structure. When doing low-quality DV decode, only one field is being used.  If you are using the ICM directly you can request a single field to be displayed by calling `SetDSequenceFlags`:     |  | | --- | | ``` err = SetDSequenceFlags( decompressionSequence, codecDSequenceSingleField,                          codecDSequenceSingleField ); ``` |    If you are using the Movie Toolbox you can request a single field to be displayed by calling `SetMediaPlayHints`:     |  | | --- | | ``` SetMediaPlayHints( GetTrackMedia( videoTrack ), hintsSingleField,                    hintsSingleField ); ``` |    For more information, see [Rendering High Quality Movies](https://developer.apple.com/quicktime/icefloe/dispatch011.html) on the QuickTime developer web site. [Oct 25 2000] |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
