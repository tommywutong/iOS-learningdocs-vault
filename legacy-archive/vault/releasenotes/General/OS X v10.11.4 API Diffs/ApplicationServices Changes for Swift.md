---
title: OS X v10.11.4 API Diffs
apple_id: TP40016680
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11_4/Swift/ApplicationServices.html
archived_at: '2026-07-18T02:53:50.223416Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11.4 API Diffs](OS%20X%20v10.11.4%20API%20Diffs.md)


# ApplicationServices Changes for Swift

### ApplicationServices

Added [AppParameters.init(theMsgEvent: AppParameters.__Unnamed_struct_theMsgEvent, eventRefCon: UInt32, messageLength: UInt32)](https://developer.apple.com/documentation/applicationservices/appparameters/1461815-init)Added [AppParameters.theMsgEvent](https://developer.apple.com/documentation/applicationservices/appparameters/1462322-themsgevent)Added [ATSFontFilter.filter](https://developer.apple.com/documentation/applicationservices/atsfontfilter/1459868-filter)Added [ATSFontFilter.init(version: UInt32, filterSelector: ATSFontFilterSelector, filter: ATSFontFilter.__Unnamed_union_filter)](https://developer.apple.com/documentation/applicationservices/atsfontfilter/1463749-init)Added [FMFilter.filter](https://developer.apple.com/documentation/applicationservices/fmfilter/1461915-filter)Added [FMFilter.init(format: UInt32, selector: FMFilterSelector, filter: FMFilter.__Unnamed_union_filter)](https://developer.apple.com/documentation/applicationservices/fmfilter/1461528-init)Added [ATSFontRef](https://developer.apple.com/documentation/coretext/atsfontref)Added [ATSFONTREF_DEFINED](https://developer.apple.com/documentation/applicationservices/atsfontref_defined)Modified [AppParameters [struct]](https://developer.apple.com/documentation/applicationservices/appparameters)

|  | Declaration |
| --- | --- |
| From | ``` struct AppParameters {     var eventRefCon: UInt32     var messageLength: UInt32     init() } ``` |
| To | ``` struct AppParameters {     struct __Unnamed_struct_theMsgEvent {         var what: UInt16         var message: UInt32         var when: UInt32         var `where`: Point         var modifiers: UInt16         init()         init(what what: UInt16, message message: UInt32, when when: UInt32, where where: Point, modifiers modifiers: UInt16)     }     var theMsgEvent: AppParameters.__Unnamed_struct_theMsgEvent     var eventRefCon: UInt32     var messageLength: UInt32     init()     init(theMsgEvent theMsgEvent: AppParameters.__Unnamed_struct_theMsgEvent, eventRefCon eventRefCon: UInt32, messageLength messageLength: UInt32) } ``` |

Modified [ATSFontFilter [struct]](https://developer.apple.com/documentation/applicationservices/atsfontfilter)

|  | Declaration |
| --- | --- |
| From | ``` struct ATSFontFilter {     var version: UInt32     var filterSelector: ATSFontFilterSelector     init() } ``` |
| To | ``` struct ATSFontFilter {     struct __Unnamed_union_filter {         var generationFilter: ATSGeneration         var fontFamilyFilter: ATSFontFamilyRef         var fontFamilyApplierFunctionFilter: ATSFontFamilyApplierFunction!         var fontApplierFunctionFilter: ATSFontApplierFunction!         var fontFileRefFilter: UnsafePointer<FSRef>         init(generationFilter generationFilter: ATSGeneration)         init(fontFamilyFilter fontFamilyFilter: ATSFontFamilyRef)         init(fontFamilyApplierFunctionFilter fontFamilyApplierFunctionFilter: ATSFontFamilyApplierFunction!)         init(fontApplierFunctionFilter fontApplierFunctionFilter: ATSFontApplierFunction!)         init(fontFileRefFilter fontFileRefFilter: UnsafePointer<FSRef>)         init()     }     var version: UInt32     var filterSelector: ATSFontFilterSelector     var filter: ATSFontFilter.__Unnamed_union_filter     init()     init(version version: UInt32, filterSelector filterSelector: ATSFontFilterSelector, filter filter: ATSFontFilter.__Unnamed_union_filter) } ``` |

Modified [AXObserver](https://developer.apple.com/documentation/applicationservices/axobserverref)

|  | Name | Declaration |
| --- | --- | --- |
| From | AXObserverRef | ``` typealias AXObserverRef = AXObserver ``` |
| To | AXObserver | ``` class AXObserver { } ``` |

Modified [AXUIElement](https://developer.apple.com/documentation/applicationservices/axuielement)

|  | Name | Declaration |
| --- | --- | --- |
| From | AXUIElementRef | ``` typealias AXUIElementRef = AXUIElement ``` |
| To | AXUIElement | ``` class AXUIElement { } ``` |

Modified [AXValue](https://developer.apple.com/documentation/applicationservices/axvalue)

|  | Name | Declaration |
| --- | --- | --- |
| From | AXValueRef | ``` typealias AXValueRef = AXValue ``` |
| To | AXValue | ``` class AXValue { } ``` |

Modified [ColorSyncCMM](https://developer.apple.com/documentation/colorsync/colorsynccmmref)

|  | Name | Declaration |
| --- | --- | --- |
| From | ColorSyncCMMRef | ``` typealias ColorSyncCMMRef = ColorSyncCMM ``` |
| To | ColorSyncCMM | ``` class ColorSyncCMM { } ``` |

Modified [ColorSyncMutableProfile](https://developer.apple.com/documentation/colorsync/colorsyncmutableprofileref)

|  | Name | Declaration |
| --- | --- | --- |
| From | ColorSyncMutableProfileRef | ``` typealias ColorSyncMutableProfileRef = ColorSyncMutableProfile ``` |
| To | ColorSyncMutableProfile | ``` class ColorSyncMutableProfile { } ``` |

Modified [ColorSyncProfile](https://developer.apple.com/documentation/colorsync/colorsyncprofileref)

|  | Name | Declaration |
| --- | --- | --- |
| From | ColorSyncProfileRef | ``` typealias ColorSyncProfileRef = ColorSyncProfile ``` |
| To | ColorSyncProfile | ``` class ColorSyncProfile { } ``` |

Modified [ColorSyncTransform](https://developer.apple.com/documentation/colorsync/colorsynctransformref)

|  | Name | Declaration |
| --- | --- | --- |
| From | ColorSyncTransformRef | ``` typealias ColorSyncTransformRef = ColorSyncTransform ``` |
| To | ColorSyncTransform | ``` class ColorSyncTransform { } ``` |

Modified [FMFilter [struct]](https://developer.apple.com/documentation/applicationservices/fmfilter)

|  | Declaration |
| --- | --- |
| From | ``` struct FMFilter {     var format: UInt32     var selector: FMFilterSelector     init() } ``` |
| To | ``` struct FMFilter {     struct __Unnamed_union_filter {         var fontTechnologyFilter: FourCharCode         var fontContainerFilter: ATSFSSpec         var generationFilter: FMGeneration         var fontFamilyCallbackFilter: FMFontFamilyCallbackFilterUPP!         var fontCallbackFilter: FMFontCallbackFilterUPP!         var fontDirectoryFilter: FMFontDirectoryFilter         var fontFileRefFilter: UnsafePointer<FSRef>         init(fontTechnologyFilter fontTechnologyFilter: FourCharCode)         init(fontContainerFilter fontContainerFilter: ATSFSSpec)         init(generationFilter generationFilter: FMGeneration)         init(fontFamilyCallbackFilter fontFamilyCallbackFilter: FMFontFamilyCallbackFilterUPP!)         init(fontCallbackFilter fontCallbackFilter: FMFontCallbackFilterUPP!)         init(fontDirectoryFilter fontDirectoryFilter: FMFontDirectoryFilter)         init(fontFileRefFilter fontFileRefFilter: UnsafePointer<FSRef>)         init()     }     var format: UInt32     var selector: FMFilterSelector     var filter: FMFilter.__Unnamed_union_filter     init()     init(format format: UInt32, selector selector: FMFilterSelector, filter filter: FMFilter.__Unnamed_union_filter) } ``` |

Modified [HIMutableShape](https://developer.apple.com/documentation/applicationservices/himutableshaperef)

|  | Name | Declaration |
| --- | --- | --- |
| From | HIMutableShapeRef | ``` typealias HIMutableShapeRef = HIMutableShape ``` |
| To | HIMutableShape | ``` class HIMutableShape { } ``` |

Modified [HIShape](https://developer.apple.com/documentation/applicationservices/hishape)

|  | Name | Declaration |
| --- | --- | --- |
| From | HIShapeRef | ``` typealias HIShapeRef = HIShape ``` |
| To | HIShape | ``` class HIShape { } ``` |

Modified [ICMapEntry [struct]](https://developer.apple.com/documentation/applicationservices/icmapentry)

|  | Declaration |
| --- | --- |
| From | ``` struct ICMapEntry {     var totalLength: Int16     var fixedLength: ICFixedLength     var version: Int16     var fileType: OSType     var fileCreator: OSType     var postCreator: OSType     var flags: ICMapEntryFlags     var `extension`: Str255     var creatorAppName: Str255     var postAppName: Str255     var MIMEType: Str255     var entryName: Str255     init()     init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, `extension` `extension`: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) } ``` |
| To | ``` struct ICMapEntry {     var totalLength: Int16     var fixedLength: ICFixedLength     var version: Int16     var fileType: OSType     var fileCreator: OSType     var postCreator: OSType     var flags: ICMapEntryFlags     var `extension`: Str255     var creatorAppName: Str255     var postAppName: Str255     var MIMEType: Str255     var entryName: Str255     init()     init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, extension extension: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) } ``` |

Modified [ICMapEntry.init(totalLength: Int16, fixedLength: ICFixedLength, version: Int16, fileType: OSType, fileCreator: OSType, postCreator: OSType, flags: ICMapEntryFlags, extension: Str255, creatorAppName: Str255, postAppName: Str255, MIMEType: Str255, entryName: Str255)](https://developer.apple.com/documentation/applicationservices/icmapentry/1463249-init)

|  | Declaration |
| --- | --- |
| From | ``` init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, `extension` `extension`: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) ``` |
| To | ``` init(totalLength totalLength: Int16, fixedLength fixedLength: ICFixedLength, version version: Int16, fileType fileType: OSType, fileCreator fileCreator: OSType, postCreator postCreator: OSType, flags flags: ICMapEntryFlags, extension extension: Str255, creatorAppName creatorAppName: Str255, postAppName postAppName: Str255, MIMEType MIMEType: Str255, entryName entryName: Str255) ``` |

Modified [Pasteboard](https://developer.apple.com/documentation/applicationservices/pasteboard)

|  | Name | Declaration |
| --- | --- | --- |
| From | PasteboardRef | ``` typealias PasteboardRef = Pasteboard ``` |
| To | Pasteboard | ``` class Pasteboard { } ``` |

Modified [Translation](https://developer.apple.com/documentation/applicationservices/translationref)

|  | Name | Declaration |
| --- | --- | --- |
| From | TranslationRef | ``` typealias TranslationRef = Translation ``` |
| To | Translation | ``` class Translation { } ``` |

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
