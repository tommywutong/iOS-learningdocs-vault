---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Swift/QuickLook.html
archived_at: '2026-07-18T02:53:41.662386Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# QuickLook Changes for Swift

### QuickLook

Removed QLGeneratorInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>, CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)>, GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>, CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)>)Removed QLPreviewPDFStyle.valueAdded QLGeneratorInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)!, CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)!, GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)!, CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)!)Added QLPreviewPDFStyle.init(rawValue: UInt32)Added QLPreviewPDFStyle.rawValueModified [QLGeneratorInterfaceStruct [struct]](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct QLGeneratorInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>     var CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)>     var GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>     var CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, GenerateThumbnailForURL GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>, CancelThumbnailGeneration CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)>, GeneratePreviewForURL GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>, CancelPreviewGeneration CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)>) } ``` |
| To | ``` struct QLGeneratorInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)!     var CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)!     var GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)!     var CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, GenerateThumbnailForURL GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)!, CancelThumbnailGeneration CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)!, GeneratePreviewForURL GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)!, CancelPreviewGeneration CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)!) } ``` |

Modified [QLGeneratorInterfaceStruct.AddRef](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402726-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [QLGeneratorInterfaceStruct.CancelPreviewGeneration](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402692-cancelpreviewgeneration)

|  | Declaration |
| --- | --- |
| From | ``` var CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)> ``` |
| To | ``` var CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)! ``` |

Modified [QLGeneratorInterfaceStruct.CancelThumbnailGeneration](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402763-cancelthumbnailgeneration)

|  | Declaration |
| --- | --- |
| From | ``` var CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)> ``` |
| To | ``` var CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)! ``` |

Modified [QLGeneratorInterfaceStruct.GeneratePreviewForURL](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402715-generatepreviewforurl)

|  | Declaration |
| --- | --- |
| From | ``` var GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)> ``` |
| To | ``` var GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)! ``` |

Modified [QLGeneratorInterfaceStruct.GenerateThumbnailForURL](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402767-generatethumbnailforurl)

|  | Declaration |
| --- | --- |
| From | ``` var GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)> ``` |
| To | ``` var GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)! ``` |

Modified [QLGeneratorInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402724-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |

Modified [QLGeneratorInterfaceStruct.Release](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402641-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |
| To | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |

Modified [QLPreviewPDFStyle [struct]](https://developer.apple.com/documentation/quicklook/qlpreviewpdfstyle)

|  | Declaration | Protocols |
| --- | --- | --- |
| From | ``` struct QLPreviewPDFStyle {     init(_ value: UInt32)     var value: UInt32 } ``` | -- |
| To | ``` struct QLPreviewPDFStyle : RawRepresentable {     init(_ rawValue: UInt32)     init(rawValue rawValue: UInt32)     var rawValue: UInt32 } ``` | RawRepresentable |

Modified [QLPreviewRequestCreateContext(_: QLPreviewRequest!, _: CGSize, _: Bool, _: CFDictionary!) -> Unmanaged<CGContext>!](https://developer.apple.com/documentation/quicklook/1402613-qlpreviewrequestcreatecontext)

|  | Declaration |
| --- | --- |
| From | ``` func QLPreviewRequestCreateContext(_ preview: QLPreviewRequest!, _ size: CGSize, _ isBitmap: Boolean, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |
| To | ``` func QLPreviewRequestCreateContext(_ preview: QLPreviewRequest!, _ size: CGSize, _ isBitmap: Bool, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |

Modified [QLPreviewRequestIsCancelled(_: QLPreviewRequest!) -> Bool](https://developer.apple.com/documentation/quicklook/1402748-qlpreviewrequestiscancelled)

|  | Declaration |
| --- | --- |
| From | ``` func QLPreviewRequestIsCancelled(_ preview: QLPreviewRequest!) -> Boolean ``` |
| To | ``` func QLPreviewRequestIsCancelled(_ preview: QLPreviewRequest!) -> Bool ``` |

Modified [QLThumbnailIsCancelled(_: QLThumbnail!) -> Bool](https://developer.apple.com/documentation/quicklook/1402740-qlthumbnailiscancelled)

|  | Declaration |
| --- | --- |
| From | ``` func QLThumbnailIsCancelled(_ thumbnail: QLThumbnail!) -> Boolean ``` |
| To | ``` func QLThumbnailIsCancelled(_ thumbnail: QLThumbnail!) -> Bool ``` |

Modified [QLThumbnailRequestCreateContext(_: QLThumbnailRequest!, _: CGSize, _: Bool, _: CFDictionary!) -> Unmanaged<CGContext>!](https://developer.apple.com/documentation/quicklook/1402694-qlthumbnailrequestcreatecontext)

|  | Declaration |
| --- | --- |
| From | ``` func QLThumbnailRequestCreateContext(_ thumbnail: QLThumbnailRequest!, _ size: CGSize, _ isBitmap: Boolean, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |
| To | ``` func QLThumbnailRequestCreateContext(_ thumbnail: QLThumbnailRequest!, _ size: CGSize, _ isBitmap: Bool, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |

Modified [QLThumbnailRequestIsCancelled(_: QLThumbnailRequest!) -> Bool](https://developer.apple.com/documentation/quicklook/1402676-qlthumbnailrequestiscancelled)

|  | Declaration |
| --- | --- |
| From | ``` func QLThumbnailRequestIsCancelled(_ thumbnail: QLThumbnailRequest!) -> Boolean ``` |
| To | ``` func QLThumbnailRequestIsCancelled(_ thumbnail: QLThumbnailRequest!) -> Bool ``` |

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
