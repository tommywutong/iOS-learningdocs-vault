---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Swift/QuickLook.html
archived_at: '2026-07-18T02:51:33.571667Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# QuickLook Changes for Swift

### QuickLook

Removed QLGeneratorInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)!, CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)!, GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)!, CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)!)Added [QLGeneratorInterfaceStruct.init(_reserved: UnsafeMutableRawPointer!, QueryInterface: ( (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef: ( (UnsafeMutableRawPointer?) -> ULONG)!, Release: ( (UnsafeMutableRawPointer?) -> ULONG)!, GenerateThumbnailForURL: ( (UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)!, CancelThumbnailGeneration: ( (UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Swift.Void)!, GeneratePreviewForURL: ( (UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)!, CancelPreviewGeneration: ( (UnsafeMutableRawPointer?, QLPreviewRequest?) -> Swift.Void)!)](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1792090-init)Modified [QLGeneratorInterfaceStruct [struct]](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct)

|  | Declaration |
| --- | --- |
| From | ``` struct QLGeneratorInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!     var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!     var Release: ((UnsafeMutablePointer<Void>) -> ULONG)!     var GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)!     var CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)!     var GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)!     var CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)!     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)!, AddRef AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)!, Release Release: ((UnsafeMutablePointer<Void>) -> ULONG)!, GenerateThumbnailForURL GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)!, CancelThumbnailGeneration CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)!, GeneratePreviewForURL GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)!, CancelPreviewGeneration CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)!) } ``` |
| To | ``` struct QLGeneratorInterfaceStruct {     var _reserved: UnsafeMutableRawPointer!     var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!     var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)!     var Release: ((UnsafeMutableRawPointer?) -> ULONG)!     var GenerateThumbnailForURL: ((UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)!     var CancelThumbnailGeneration: ((UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Swift.Void)!     var GeneratePreviewForURL: ((UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)!     var CancelPreviewGeneration: ((UnsafeMutableRawPointer?, QLPreviewRequest?) -> Swift.Void)!     init()     init(_reserved _reserved: UnsafeMutableRawPointer!, QueryInterface QueryInterface: (@escaping (UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)!, AddRef AddRef: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, Release Release: (@escaping (UnsafeMutableRawPointer?) -> ULONG)!, GenerateThumbnailForURL GenerateThumbnailForURL: (@escaping (UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)!, CancelThumbnailGeneration CancelThumbnailGeneration: (@escaping (UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Swift.Void)!, GeneratePreviewForURL GeneratePreviewForURL: (@escaping (UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)!, CancelPreviewGeneration CancelPreviewGeneration: (@escaping (UnsafeMutableRawPointer?, QLPreviewRequest?) -> Swift.Void)!) } ``` |

Modified [QLGeneratorInterfaceStruct.AddRef](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402726-addref)

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var AddRef: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [QLGeneratorInterfaceStruct.CancelPreviewGeneration](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402692-cancelpreviewgeneration)

|  | Declaration |
| --- | --- |
| From | ``` var CancelPreviewGeneration: ((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)! ``` |
| To | ``` var CancelPreviewGeneration: ((UnsafeMutableRawPointer?, QLPreviewRequest?) -> Swift.Void)! ``` |

Modified [QLGeneratorInterfaceStruct.CancelThumbnailGeneration](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402763-cancelthumbnailgeneration)

|  | Declaration |
| --- | --- |
| From | ``` var CancelThumbnailGeneration: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)! ``` |
| To | ``` var CancelThumbnailGeneration: ((UnsafeMutableRawPointer?, QLThumbnailRequest?) -> Swift.Void)! ``` |

Modified [QLGeneratorInterfaceStruct.GeneratePreviewForURL](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402715-generatepreviewforurl)

|  | Declaration |
| --- | --- |
| From | ``` var GeneratePreviewForURL: ((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)! ``` |
| To | ``` var GeneratePreviewForURL: ((UnsafeMutableRawPointer?, QLPreviewRequest?, CFURL?, CFString?, CFDictionary?) -> OSStatus)! ``` |

Modified [QLGeneratorInterfaceStruct.GenerateThumbnailForURL](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402767-generatethumbnailforurl)

|  | Declaration |
| --- | --- |
| From | ``` var GenerateThumbnailForURL: ((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)! ``` |
| To | ``` var GenerateThumbnailForURL: ((UnsafeMutableRawPointer?, QLThumbnailRequest?, CFURL?, CFString?, CFDictionary?, CGSize) -> OSStatus)! ``` |

Modified [QLGeneratorInterfaceStruct.QueryInterface](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402724-queryinterface)

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: ((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)! ``` |
| To | ``` var QueryInterface: ((UnsafeMutableRawPointer?, REFIID, UnsafeMutablePointer<LPVOID?>?) -> HRESULT)! ``` |

Modified [QLGeneratorInterfaceStruct.Release](https://developer.apple.com/documentation/quicklook/qlgeneratorinterfacestruct/1402641-release)

|  | Declaration |
| --- | --- |
| From | ``` var Release: ((UnsafeMutablePointer<Void>) -> ULONG)! ``` |
| To | ``` var Release: ((UnsafeMutableRawPointer?) -> ULONG)! ``` |

Modified [QLPreviewRequestCreatePDFContext(_: QLPreviewRequest!, _: UnsafePointer<CGRect>!, _: CFDictionary!, _: CFDictionary!) -> Unmanaged<CGContext>!](https://developer.apple.com/documentation/quicklook/1402759-qlpreviewrequestcreatepdfcontext)

|  | Declaration |
| --- | --- |
| From | ``` func QLPreviewRequestCreatePDFContext(_ preview: QLPreviewRequest!, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |
| To | ``` func QLPreviewRequestCreatePDFContext(_ preview: QLPreviewRequest!, _ mediaBox: UnsafePointer<CGRect>!, _ auxiliaryInfo: CFDictionary!, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |

Modified [QLPreviewRequestGetDocumentObject(_: QLPreviewRequest!) -> UnsafeRawPointer!](https://developer.apple.com/documentation/quicklook/1402696-qlpreviewrequestgetdocumentobjec)

|  | Declaration |
| --- | --- |
| From | ``` func QLPreviewRequestGetDocumentObject(_ preview: QLPreviewRequest!) -> UnsafePointer<Void> ``` |
| To | ``` func QLPreviewRequestGetDocumentObject(_ preview: QLPreviewRequest!) -> UnsafeRawPointer! ``` |

Modified [QLPreviewRequestSetDocumentObject(_: QLPreviewRequest!, _: UnsafeRawPointer!, _: UnsafePointer<CFArrayCallBacks>!)](https://developer.apple.com/documentation/quicklook/1402611-qlpreviewrequestsetdocumentobjec)

|  | Declaration |
| --- | --- |
| From | ``` func QLPreviewRequestSetDocumentObject(_ preview: QLPreviewRequest!, _ object: UnsafePointer<Void>, _ callbacks: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func QLPreviewRequestSetDocumentObject(_ preview: QLPreviewRequest!, _ object: UnsafeRawPointer!, _ callbacks: UnsafePointer<CFArrayCallBacks>!) ``` |

Modified [QLThumbnailDispatchAsync(_: QLThumbnail!, _: DispatchQueue!, _: ( () -> Swift.Void)!)](https://developer.apple.com/documentation/quicklook/1402703-qlthumbnaildispatchasync)

|  | Declaration |
| --- | --- |
| From | ``` func QLThumbnailDispatchAsync(_ thumbnail: QLThumbnail!, _ queue: dispatch_queue_t!, _ completion: dispatch_block_t!) ``` |
| To | ``` func QLThumbnailDispatchAsync(_ thumbnail: QLThumbnail!, _ queue: DispatchQueue!, _ completion: (@escaping () -> Swift.Void)!) ``` |

Modified [QLThumbnailRequestGetDocumentObject(_: QLThumbnailRequest!) -> UnsafeRawPointer!](https://developer.apple.com/documentation/quicklook/1402690-qlthumbnailrequestgetdocumentobj)

|  | Declaration |
| --- | --- |
| From | ``` func QLThumbnailRequestGetDocumentObject(_ thumbnail: QLThumbnailRequest!) -> UnsafePointer<Void> ``` |
| To | ``` func QLThumbnailRequestGetDocumentObject(_ thumbnail: QLThumbnailRequest!) -> UnsafeRawPointer! ``` |

Modified [QLThumbnailRequestSetDocumentObject(_: QLThumbnailRequest!, _: UnsafeRawPointer!, _: UnsafePointer<CFArrayCallBacks>!)](https://developer.apple.com/documentation/quicklook/1402619-qlthumbnailrequestsetdocumentobj)

|  | Declaration |
| --- | --- |
| From | ``` func QLThumbnailRequestSetDocumentObject(_ thumbnail: QLThumbnailRequest!, _ object: UnsafePointer<Void>, _ callbacks: UnsafePointer<CFArrayCallBacks>) ``` |
| To | ``` func QLThumbnailRequestSetDocumentObject(_ thumbnail: QLThumbnailRequest!, _ object: UnsafeRawPointer!, _ callbacks: UnsafePointer<CFArrayCallBacks>!) ``` |

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
