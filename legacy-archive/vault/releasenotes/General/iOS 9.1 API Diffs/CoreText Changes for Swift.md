---
title: iOS 9.1 API Diffs
apple_id: TP40016573
resource_type: Release Note
platform: iOS
topic: General
technology: null
published: '2015-10-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/iOS91APIDiffs/Swift/CoreText.html
archived_at: '2026-07-18T02:57:07.747352Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [iOS 9.1 API Diffs](iOS%209.0%20to%20iOS%209.1%20API%20Differences.md)


# CoreText Changes for Swift

### CoreText

Added BslnFormatUnion.fmt0PartAdded BslnFormatUnion.fmt1PartAdded BslnFormatUnion.fmt2PartAdded BslnFormatUnion.fmt3PartAdded BslnFormatUnion.init(fmt0Part: BslnFormat0Part)Added BslnFormatUnion.init(fmt1Part: BslnFormat1Part)Added BslnFormatUnion.init(fmt2Part: BslnFormat2Part)Added BslnFormatUnion.init(fmt3Part: BslnFormat3Part)Added KernFormatSpecificHeader.indexArrayAdded KernFormatSpecificHeader.init(indexArray: KernIndexArrayHeader)Added KernFormatSpecificHeader.init(orderedList: KernOrderedListHeader)Added KernFormatSpecificHeader.init(simpleArray: KernSimpleArrayHeader)Added KernFormatSpecificHeader.init(stateTable: KernStateHeader)Added KernFormatSpecificHeader.orderedListAdded KernFormatSpecificHeader.simpleArrayAdded KernFormatSpecificHeader.stateTableAdded KerxFormatSpecificHeader.controlPointAdded KerxFormatSpecificHeader.indexArrayAdded KerxFormatSpecificHeader.init(controlPoint: KerxControlPointHeader)Added KerxFormatSpecificHeader.init(indexArray: KerxIndexArrayHeader)Added KerxFormatSpecificHeader.init(orderedList: KerxOrderedListHeader)Added KerxFormatSpecificHeader.init(simpleArray: KerxSimpleArrayHeader)Added KerxFormatSpecificHeader.init(stateTable: KerxStateHeader)Added KerxFormatSpecificHeader.orderedListAdded KerxFormatSpecificHeader.simpleArrayAdded KerxFormatSpecificHeader.stateTableAdded MortSpecificSubtable.contextualAdded MortSpecificSubtable.init(contextual: MortContextualSubtable)Added MortSpecificSubtable.init(insertion: MortInsertionSubtable)Added MortSpecificSubtable.init(ligature: MortLigatureSubtable)Added MortSpecificSubtable.init(rearrangement: MortRearrangementSubtable)Added MortSpecificSubtable.init(swash: MortSwashSubtable)Added MortSpecificSubtable.insertionAdded MortSpecificSubtable.ligatureAdded MortSpecificSubtable.rearrangementAdded MortSpecificSubtable.swashAdded MorxSpecificSubtable.contextualAdded MorxSpecificSubtable.init(contextual: MorxContextualSubtable)Added MorxSpecificSubtable.init(insertion: MorxInsertionSubtable)Added MorxSpecificSubtable.init(ligature: MorxLigatureSubtable)Added MorxSpecificSubtable.init(rearrangement: MorxRearrangementSubtable)Added MorxSpecificSubtable.init(swash: MortSwashSubtable)Added MorxSpecificSubtable.insertionAdded MorxSpecificSubtable.ligatureAdded MorxSpecificSubtable.rearrangementAdded MorxSpecificSubtable.swashAdded SFNTLookupFormatSpecificHeader.init(segment: SFNTLookupSegmentHeader)Added SFNTLookupFormatSpecificHeader.init(single: SFNTLookupSingleHeader)Added SFNTLookupFormatSpecificHeader.init(theArray: SFNTLookupArrayHeader)Added SFNTLookupFormatSpecificHeader.init(trimmedArray: SFNTLookupTrimmedArrayHeader)Added SFNTLookupFormatSpecificHeader.segmentAdded SFNTLookupFormatSpecificHeader.singleAdded SFNTLookupFormatSpecificHeader.theArrayAdded SFNTLookupFormatSpecificHeader.trimmedArrayModified BslnFormatUnion [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct BslnFormatUnion {     init() } ``` |
| To | ``` struct BslnFormatUnion {     var fmt0Part: BslnFormat0Part     var fmt1Part: BslnFormat1Part     var fmt2Part: BslnFormat2Part     var fmt3Part: BslnFormat3Part     init(fmt0Part fmt0Part: BslnFormat0Part)     init(fmt1Part fmt1Part: BslnFormat1Part)     init(fmt2Part fmt2Part: BslnFormat2Part)     init(fmt3Part fmt3Part: BslnFormat3Part)     init() } ``` |

Modified [CTCharacterCollection [enum]](https://developer.apple.com/documentation/coretext/ctcharactercollection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontDescriptorMatchingState [enum]](https://developer.apple.com/documentation/coretext/ctfontdescriptormatchingstate)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontFormat [enum]](https://developer.apple.com/documentation/coretext/ctfontformat)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontManagerAutoActivationSetting [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagerautoactivationsetting)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontManagerError [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagererror)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontManagerScope [enum]](https://developer.apple.com/documentation/coretext/ctfontmanagerscope)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontOrientation [enum]](https://developer.apple.com/documentation/coretext/ctfontorientation)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFontUIFontType [enum]](https://developer.apple.com/documentation/coretext/ctfontuifonttype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFramePathFillRule [enum]](https://developer.apple.com/documentation/coretext/ctframepathfillrule)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTFrameProgression [enum]](https://developer.apple.com/documentation/coretext/ctframeprogression)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTLineBreakMode [enum]](https://developer.apple.com/documentation/coretext/ctlinebreakmode)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTLineTruncationType [enum]](https://developer.apple.com/documentation/coretext/ctlinetruncationtype)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTParagraphStyleSpecifier [enum]](https://developer.apple.com/documentation/coretext/ctparagraphstylespecifier)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTRubyAlignment [enum]](https://developer.apple.com/documentation/coretext/ctrubyalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTRubyOverhang [enum]](https://developer.apple.com/documentation/coretext/ctrubyoverhang)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTRubyPosition [enum]](https://developer.apple.com/documentation/coretext/ctrubyposition)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTTextAlignment [enum]](https://developer.apple.com/documentation/coretext/cttextalignment)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified [CTWritingDirection [enum]](https://developer.apple.com/documentation/coretext/ctwritingdirection)

|  | Protocols |
| --- | --- |
| From | Equatable, Hashable, RawRepresentable |
| To | -- |

Modified KernFormatSpecificHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KernFormatSpecificHeader {     init() } ``` |
| To | ``` struct KernFormatSpecificHeader {     var orderedList: KernOrderedListHeader     var stateTable: KernStateHeader     var simpleArray: KernSimpleArrayHeader     var indexArray: KernIndexArrayHeader     init(orderedList orderedList: KernOrderedListHeader)     init(stateTable stateTable: KernStateHeader)     init(simpleArray simpleArray: KernSimpleArrayHeader)     init(indexArray indexArray: KernIndexArrayHeader)     init() } ``` |

Modified KerxFormatSpecificHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct KerxFormatSpecificHeader {     init() } ``` |
| To | ``` struct KerxFormatSpecificHeader {     var orderedList: KerxOrderedListHeader     var stateTable: KerxStateHeader     var simpleArray: KerxSimpleArrayHeader     var indexArray: KerxIndexArrayHeader     var controlPoint: KerxControlPointHeader     init(orderedList orderedList: KerxOrderedListHeader)     init(stateTable stateTable: KerxStateHeader)     init(simpleArray simpleArray: KerxSimpleArrayHeader)     init(indexArray indexArray: KerxIndexArrayHeader)     init(controlPoint controlPoint: KerxControlPointHeader)     init() } ``` |

Modified MortSpecificSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MortSpecificSubtable {     init() } ``` |
| To | ``` struct MortSpecificSubtable {     var rearrangement: MortRearrangementSubtable     var contextual: MortContextualSubtable     var ligature: MortLigatureSubtable     var swash: MortSwashSubtable     var insertion: MortInsertionSubtable     init(rearrangement rearrangement: MortRearrangementSubtable)     init(contextual contextual: MortContextualSubtable)     init(ligature ligature: MortLigatureSubtable)     init(swash swash: MortSwashSubtable)     init(insertion insertion: MortInsertionSubtable)     init() } ``` |

Modified MorxSpecificSubtable [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct MorxSpecificSubtable {     init() } ``` |
| To | ``` struct MorxSpecificSubtable {     var rearrangement: MorxRearrangementSubtable     var contextual: MorxContextualSubtable     var ligature: MorxLigatureSubtable     var swash: MortSwashSubtable     var insertion: MorxInsertionSubtable     init(rearrangement rearrangement: MorxRearrangementSubtable)     init(contextual contextual: MorxContextualSubtable)     init(ligature ligature: MorxLigatureSubtable)     init(swash swash: MortSwashSubtable)     init(insertion insertion: MorxInsertionSubtable)     init() } ``` |

Modified SFNTLookupFormatSpecificHeader [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct SFNTLookupFormatSpecificHeader {     init() } ``` |
| To | ``` struct SFNTLookupFormatSpecificHeader {     var theArray: SFNTLookupArrayHeader     var segment: SFNTLookupSegmentHeader     var single: SFNTLookupSingleHeader     var trimmedArray: SFNTLookupTrimmedArrayHeader     init(theArray theArray: SFNTLookupArrayHeader)     init(segment segment: SFNTLookupSegmentHeader)     init(single single: SFNTLookupSingleHeader)     init(trimmedArray trimmedArray: SFNTLookupTrimmedArrayHeader)     init() } ``` |

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
