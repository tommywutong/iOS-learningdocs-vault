---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/modules/QuickLook.html
archived_at: '2026-07-18T02:52:38.195499Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# QuickLook Changes

## QuickLook

Added QLGeneratorInterfaceStruct.init()Added QLGeneratorInterfaceStruct.init(_reserved: UnsafeMutablePointer<Void>, QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>, CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)>, GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>, CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)>)Modified QLGeneratorInterfaceStruct [struct]

|  | Declaration |
| --- | --- |
| From | ``` struct QLGeneratorInterfaceStruct {     var _reserved: UnsafePointer<()>     var QueryInterface: CFunctionPointer<((UnsafePointer<()>, REFIID, UnsafePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafePointer<()>) -> ULONG)>     var Release: CFunctionPointer<((UnsafePointer<()>) -> ULONG)>     var GenerateThumbnailForURL: CFunctionPointer<((UnsafePointer<()>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>     var CancelThumbnailGeneration: CFunctionPointer<((UnsafePointer<()>, QLThumbnailRequest!) -> Void)>     var GeneratePreviewForURL: CFunctionPointer<((UnsafePointer<()>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>     var CancelPreviewGeneration: CFunctionPointer<((UnsafePointer<()>, QLPreviewRequest!) -> Void)> } ``` |
| To | ``` struct QLGeneratorInterfaceStruct {     var _reserved: UnsafeMutablePointer<Void>     var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>     var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>     var GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>     var CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)>     var GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>     var CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)>     init()     init(_reserved _reserved: UnsafeMutablePointer<Void>, QueryInterface QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)>, AddRef AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, Release Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)>, GenerateThumbnailForURL GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)>, CancelThumbnailGeneration CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)>, GeneratePreviewForURL GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)>, CancelPreviewGeneration CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)>) } ``` |

Modified QLGeneratorInterfaceStruct.AddRef

|  | Declaration |
| --- | --- |
| From | ``` var AddRef: CFunctionPointer<((UnsafePointer<()>) -> ULONG)> ``` |
| To | ``` var AddRef: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |

Modified QLGeneratorInterfaceStruct.CancelPreviewGeneration

|  | Declaration |
| --- | --- |
| From | ``` var CancelPreviewGeneration: CFunctionPointer<((UnsafePointer<()>, QLPreviewRequest!) -> Void)> ``` |
| To | ``` var CancelPreviewGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!) -> Void)> ``` |

Modified QLGeneratorInterfaceStruct.CancelThumbnailGeneration

|  | Declaration |
| --- | --- |
| From | ``` var CancelThumbnailGeneration: CFunctionPointer<((UnsafePointer<()>, QLThumbnailRequest!) -> Void)> ``` |
| To | ``` var CancelThumbnailGeneration: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!) -> Void)> ``` |

Modified QLGeneratorInterfaceStruct.GeneratePreviewForURL

|  | Declaration |
| --- | --- |
| From | ``` var GeneratePreviewForURL: CFunctionPointer<((UnsafePointer<()>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)> ``` |
| To | ``` var GeneratePreviewForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLPreviewRequest!, CFURL!, CFString!, CFDictionary!) -> OSStatus)> ``` |

Modified QLGeneratorInterfaceStruct.GenerateThumbnailForURL

|  | Declaration |
| --- | --- |
| From | ``` var GenerateThumbnailForURL: CFunctionPointer<((UnsafePointer<()>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)> ``` |
| To | ``` var GenerateThumbnailForURL: CFunctionPointer<((UnsafeMutablePointer<Void>, QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CGSize) -> OSStatus)> ``` |

Modified QLGeneratorInterfaceStruct.QueryInterface

|  | Declaration |
| --- | --- |
| From | ``` var QueryInterface: CFunctionPointer<((UnsafePointer<()>, REFIID, UnsafePointer<LPVOID>) -> HRESULT)> ``` |
| To | ``` var QueryInterface: CFunctionPointer<((UnsafeMutablePointer<Void>, REFIID, UnsafeMutablePointer<LPVOID>) -> HRESULT)> ``` |

Modified QLGeneratorInterfaceStruct.Release

|  | Declaration |
| --- | --- |
| From | ``` var Release: CFunctionPointer<((UnsafePointer<()>) -> ULONG)> ``` |
| To | ``` var Release: CFunctionPointer<((UnsafeMutablePointer<Void>) -> ULONG)> ``` |

Modified QLPreviewRequestCreatePDFContext(QLPreviewRequest!, UnsafePointer<CGRect>, CFDictionary!, CFDictionary!) -> Unmanaged<CGContext>!

|  | Declaration |
| --- | --- |
| From | ``` func QLPreviewRequestCreatePDFContext(_ preview: QLPreviewRequest!, _ mediaBox: ConstUnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |
| To | ``` func QLPreviewRequestCreatePDFContext(_ preview: QLPreviewRequest!, _ mediaBox: UnsafePointer<CGRect>, _ auxiliaryInfo: CFDictionary!, _ properties: CFDictionary!) -> Unmanaged<CGContext>! ``` |

Modified QLPreviewRequestGetDocumentObject(QLPreviewRequest!) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func QLPreviewRequestGetDocumentObject(_ preview: QLPreviewRequest!) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func QLPreviewRequestGetDocumentObject(_ preview: QLPreviewRequest!) -> UnsafePointer<Void> ``` | OS X 10.6 |

Modified QLPreviewRequestSetDocumentObject(QLPreviewRequest!, UnsafePointer<Void>, UnsafePointer<CFArrayCallBacks>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func QLPreviewRequestSetDocumentObject(_ preview: QLPreviewRequest!, _ object: ConstUnsafePointer<()>, _ callbacks: ConstUnsafePointer<CFArrayCallBacks>) ``` | OS X 10.10 |
| To | ``` func QLPreviewRequestSetDocumentObject(_ preview: QLPreviewRequest!, _ object: UnsafePointer<Void>, _ callbacks: UnsafePointer<CFArrayCallBacks>) ``` | OS X 10.6 |

Modified QLThumbnailCancel(QLThumbnail!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailCopyDocumentURL(QLThumbnail!) -> Unmanaged<CFURL>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailCopyImage(QLThumbnail!) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailCopyOptions(QLThumbnail!) -> Unmanaged<CFDictionary>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, dispatch_block_t!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailGetContentRect(QLThumbnail!) -> CGRect

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailGetMaximumSize(QLThumbnail!) -> CGSize

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.5 |

Modified QLThumbnailIsCancelled(QLThumbnail!) -> Boolean

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailRequestGetDocumentObject(QLThumbnailRequest!) -> UnsafePointer<Void>

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func QLThumbnailRequestGetDocumentObject(_ thumbnail: QLThumbnailRequest!) -> ConstUnsafePointer<()> ``` | OS X 10.10 |
| To | ``` func QLThumbnailRequestGetDocumentObject(_ thumbnail: QLThumbnailRequest!) -> UnsafePointer<Void> ``` | OS X 10.6 |

Modified QLThumbnailRequestSetDocumentObject(QLThumbnailRequest!, UnsafePointer<Void>, UnsafePointer<CFArrayCallBacks>)

|  | Declaration | Introduction |
| --- | --- | --- |
| From | ``` func QLThumbnailRequestSetDocumentObject(_ thumbnail: QLThumbnailRequest!, _ object: ConstUnsafePointer<()>, _ callbacks: ConstUnsafePointer<CFArrayCallBacks>) ``` | OS X 10.10 |
| To | ``` func QLThumbnailRequestSetDocumentObject(_ thumbnail: QLThumbnailRequest!, _ object: UnsafePointer<Void>, _ callbacks: UnsafePointer<CFArrayCallBacks>) ``` | OS X 10.6 |

Modified QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLPreviewOptionCursorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLPreviewPropertyBaseBundlePathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLPreviewPropertyCursorKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLPreviewPropertyPDFStyleKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLThumbnailPropertyBadgeImageKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLThumbnailPropertyBaseBundlePathKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

Modified kQLThumbnailPropertyExtensionKey

|  | Introduction |
| --- | --- |
| From | OS X 10.10 |
| To | OS X 10.6 |

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
