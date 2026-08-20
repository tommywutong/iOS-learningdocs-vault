---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/modules/QuickLook.html
archived_at: '2026-07-15T07:34:56.759908Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# QuickLook Changes

## QuickLook (Added)

Added QLGeneratorInterfaceStruct [struct]Added QLGeneratorInterfaceStruct.AddRefAdded QLGeneratorInterfaceStruct.CancelPreviewGenerationAdded QLGeneratorInterfaceStruct.CancelThumbnailGenerationAdded QLGeneratorInterfaceStruct.GeneratePreviewForURLAdded QLGeneratorInterfaceStruct.GenerateThumbnailForURLAdded QLGeneratorInterfaceStruct.QueryInterfaceAdded QLGeneratorInterfaceStruct.ReleaseAdded QLPreviewPDFStyle [struct]Added QLPreviewPDFStyle.init(_: UInt32)Added QLPreviewPDFStyle.valueAdded QLPreviewRequestCopyContentUTI(QLPreviewRequest!) -> Unmanaged<CFString>!Added QLPreviewRequestCopyOptions(QLPreviewRequest!) -> Unmanaged<CFDictionary>!Added QLPreviewRequestCopyURL(QLPreviewRequest!) -> Unmanaged<CFURL>!Added QLPreviewRequestCreateContext(QLPreviewRequest!, CGSize, Boolean, CFDictionary!) -> Unmanaged<CGContext>!Added QLPreviewRequestCreatePDFContext(QLPreviewRequest!, UnsafePointer<CGRect>, CFDictionary!, CFDictionary!) -> Unmanaged<CGContext>!Added QLPreviewRequestFlushContext(QLPreviewRequest!, CGContext!)Added QLPreviewRequestGetDocumentObject(QLPreviewRequest!) -> UnsafePointer<Void>Added QLPreviewRequestGetGeneratorBundle(QLPreviewRequest!) -> Unmanaged<CFBundle>!Added QLPreviewRequestGetTypeID() -> CFTypeIDAdded QLPreviewRequestIsCancelled(QLPreviewRequest!) -> BooleanAdded QLPreviewRequestRefAdded QLPreviewRequestSetDataRepresentation(QLPreviewRequest!, CFData!, CFString!, CFDictionary!)Added QLPreviewRequestSetDocumentObject(QLPreviewRequest!, UnsafePointer<Void>, UnsafePointer<CFArrayCallBacks>)Added QLPreviewRequestSetURLRepresentation(QLPreviewRequest!, CFURL!, CFString!, CFDictionary!)Added QLThumbnailCancel(QLThumbnail!)Added QLThumbnailCopyDocumentURL(QLThumbnail!) -> Unmanaged<CFURL>!Added QLThumbnailCopyImage(QLThumbnail!) -> Unmanaged<CGImage>!Added QLThumbnailCopyOptions(QLThumbnail!) -> Unmanaged<CFDictionary>!Added QLThumbnailCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<QLThumbnail>!Added QLThumbnailDispatchAsync(QLThumbnail!, dispatch_queue_t!, dispatch_block_t!)Added QLThumbnailGetContentRect(QLThumbnail!) -> CGRectAdded QLThumbnailGetMaximumSize(QLThumbnail!) -> CGSizeAdded QLThumbnailGetTypeID() -> CFTypeIDAdded QLThumbnailImageCreate(CFAllocator!, CFURL!, CGSize, CFDictionary!) -> Unmanaged<CGImage>!Added QLThumbnailIsCancelled(QLThumbnail!) -> BooleanAdded QLThumbnailRefAdded QLThumbnailRequestCopyContentUTI(QLThumbnailRequest!) -> Unmanaged<CFString>!Added QLThumbnailRequestCopyOptions(QLThumbnailRequest!) -> Unmanaged<CFDictionary>!Added QLThumbnailRequestCopyURL(QLThumbnailRequest!) -> Unmanaged<CFURL>!Added QLThumbnailRequestCreateContext(QLThumbnailRequest!, CGSize, Boolean, CFDictionary!) -> Unmanaged<CGContext>!Added QLThumbnailRequestFlushContext(QLThumbnailRequest!, CGContext!)Added QLThumbnailRequestGetDocumentObject(QLThumbnailRequest!) -> UnsafePointer<Void>Added QLThumbnailRequestGetGeneratorBundle(QLThumbnailRequest!) -> Unmanaged<CFBundle>!Added QLThumbnailRequestGetMaximumSize(QLThumbnailRequest!) -> CGSizeAdded QLThumbnailRequestGetTypeID() -> CFTypeIDAdded QLThumbnailRequestIsCancelled(QLThumbnailRequest!) -> BooleanAdded QLThumbnailRequestRefAdded QLThumbnailRequestSetDocumentObject(QLThumbnailRequest!, UnsafePointer<Void>, UnsafePointer<CFArrayCallBacks>)Added QLThumbnailRequestSetImage(QLThumbnailRequest!, CGImage!, CFDictionary!)Added QLThumbnailRequestSetImageAtURL(QLThumbnailRequest!, CFURL!, CFDictionary!)Added QLThumbnailRequestSetImageWithData(QLThumbnailRequest!, CFData!, CFDictionary!)Added QLThumbnailRequestSetThumbnailWithDataRepresentation(QLThumbnailRequest!, CFData!, CFString!, CFDictionary!, CFDictionary!)Added QLThumbnailRequestSetThumbnailWithURLRepresentation(QLThumbnailRequest!, CFURL!, CFString!, CFDictionary!, CFDictionary!)Added QUICKLOOK_VERSIONAdded kQLPreviewContentIDSchemeAdded kQLPreviewOptionCursorKeyAdded kQLPreviewPDFPagesWithThumbnailsOnLeftStyleAdded kQLPreviewPDFPagesWithThumbnailsOnRightStyleAdded kQLPreviewPDFStandardStyleAdded kQLPreviewPropertyAttachmentDataKeyAdded kQLPreviewPropertyAttachmentsKeyAdded kQLPreviewPropertyBaseBundlePathKeyAdded kQLPreviewPropertyCursorKeyAdded kQLPreviewPropertyDisplayNameKeyAdded kQLPreviewPropertyHeightKeyAdded kQLPreviewPropertyMIMETypeKeyAdded kQLPreviewPropertyPDFStyleKeyAdded kQLPreviewPropertyStringEncodingKeyAdded kQLPreviewPropertyTextEncodingNameKeyAdded kQLPreviewPropertyWidthKeyAdded kQLReturnMaskAdded kQLThumbnailOptionIconModeKeyAdded kQLThumbnailOptionScaleFactorKeyAdded kQLThumbnailPropertyBadgeImageKeyAdded kQLThumbnailPropertyBaseBundlePathKeyAdded kQLThumbnailPropertyExtensionKey

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
