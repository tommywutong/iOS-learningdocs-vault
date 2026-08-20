---
title: API Changes in Snow Leopard
apple_id: TP40007673
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2008-06-09'
source_url: https://developer.apple.com/library/archive/releasenotes/MacOSX/SnowLeopard_API_ReleaseNote/QuickLook.html
archived_at: '2026-07-18T02:58:45.520320Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [API Changes in Snow Leopard](API%20Changes%20in%20Snow%20Leopard.md)


[ADC Home](https://developer.apple.com/) >
[Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943) >
Release Notes >
OS X >
[API Changes in Snow Leopard Developer Preview](API%20Changes%20in%20Snow%20Leopard.md) >

# QuickLook Changes

## QuickLook

QLGenerator.hRemoved QLPreviewRequestSetWebContent()Added [QLPreviewPDFStyle](https://developer.apple.com/documentation/quicklook/qlpreviewpdfstyle)Added [QLPreviewRequestGetDocumentObject()](https://developer.apple.com/documentation/quicklook/1402696-qlpreviewrequestgetdocumentobjec)Added [QLPreviewRequestSetDocumentObject()](https://developer.apple.com/documentation/quicklook/1402611-qlpreviewrequestsetdocumentobjec)Added [QLPreviewRequestSetURLRepresentation()](https://developer.apple.com/documentation/quicklook/1402674-qlpreviewrequestseturlrepresenta)Added [QLThumbnailRequestGetDocumentObject()](https://developer.apple.com/documentation/quicklook/1402690-qlthumbnailrequestgetdocumentobj)Added [QLThumbnailRequestSetDocumentObject()](https://developer.apple.com/documentation/quicklook/1402619-qlthumbnailrequestsetdocumentobj)Added [QLThumbnailRequestSetImageAtURL()](https://developer.apple.com/documentation/quicklook/1402666-qlthumbnailrequestsetimageaturl)Added [QLThumbnailRequestSetThumbnailWithDataRepresentation()](https://developer.apple.com/documentation/quicklook/1402744-qlthumbnailrequestsetthumbnailwi)Added [QLThumbnailRequestSetThumbnailWithURLRepresentation()](https://developer.apple.com/documentation/quicklook/1402746-qlthumbnailrequestsetthumbnailwi)Added [kQLPreviewOptionCursorKey](https://developer.apple.com/documentation/quicklook/kqlpreviewoptioncursorkey)Added [kQLPreviewPDFPagesWithThumbnailsOnLeftStyle](https://developer.apple.com/documentation/quicklook/qlpreviewpdfstyle/kqlpreviewpdfpageswiththumbnailsonleftstyle)Added [kQLPreviewPDFPagesWithThumbnailsOnRightStyle](https://developer.apple.com/documentation/quicklook/qlpreviewpdfstyle/kqlpreviewpdfpageswiththumbnailsonrightstyle)Added [kQLPreviewPDFStandardStyle](https://developer.apple.com/documentation/quicklook/kqlpreviewpdfstandardstyle)Added [kQLPreviewPropertyBaseBundlePathKey](https://developer.apple.com/documentation/quicklook/kqlpreviewpropertybasebundlepathkey)Added [kQLPreviewPropertyCursorKey](https://developer.apple.com/documentation/quicklook/kqlpreviewpropertycursorkey)Added [kQLPreviewPropertyPDFStyleKey](https://developer.apple.com/documentation/quicklook/kqlpreviewpropertypdfstylekey)Added [#def kQLReturnHasMore](https://developer.apple.com/documentation/quicklook/kqlreturnhasmore)Added [#def kQLReturnMask](https://developer.apple.com/documentation/quicklook/kqlreturnmask)Added #def kQLReturnNoErrorAdded [kQLThumbnailPropertyBadgeImageKey](https://developer.apple.com/documentation/quicklook/kqlthumbnailpropertybadgeimagekey)Added [kQLThumbnailPropertyBaseBundlePathKey](https://developer.apple.com/documentation/quicklook/kqlthumbnailpropertybasebundlepathkey)Added [kQLThumbnailPropertyExtensionKey](https://developer.apple.com/documentation/quicklook/kqlthumbnailpropertyextensionkey)QLPreviewItem.hAdded [QLPreviewItem](https://developer.apple.com/documentation/quicklook/qlpreviewitem)Added [QLPreviewItem.previewItemDisplayState](https://developer.apple.com/documentation/quartz/qlpreviewitem/1419915-previewitemdisplaystate)Added [QLPreviewItem.previewItemTitle](https://developer.apple.com/documentation/quicklook/qlpreviewitem/1419911-previewitemtitle)Added [QLPreviewItem.previewItemURL](https://developer.apple.com/documentation/quartz/qlpreviewitem/1419913-previewitemurl)Added NSURL(QLPreviewConvenienceAdditions)QLPreviewPanel.hAdded [-[NSObject acceptsPreviewPanelControl:]](https://developer.apple.com/documentation/objectivec/nsobject/1504653-acceptspreviewpanelcontrol)Added [-[NSObject beginPreviewPanelControl:]](https://developer.apple.com/documentation/objectivec/nsobject/1504204-beginpreviewpanelcontrol)Added [-[NSObject endPreviewPanelControl:]](https://developer.apple.com/documentation/objectivec/nsobject/1505044-endpreviewpanelcontrol)Added [QLPreviewPanel](https://developer.apple.com/documentation/quartz/qlpreviewpanel)Added [QLPreviewPanel.currentController](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1505327-currentcontroller)Added [QLPreviewPanel.currentPreviewItem](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503578-currentpreviewitem)Added [QLPreviewPanel.currentPreviewItemIndex](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503428-currentpreviewitemindex)Added [QLPreviewPanel.dataSource](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503465-datasource)Added [QLPreviewPanel.delegate](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1504770-delegate)Added [QLPreviewPanel.displayState](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1505195-displaystate)Added [-[QLPreviewPanel enterFullScreenMode:withOptions:]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503434-enterfullscreenmode)Added [-[QLPreviewPanel exitFullScreenModeWithOptions:]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503669-exitfullscreenmodewithoptions)Added [QLPreviewPanel.inFullScreenMode](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503609-isinfullscreenmode)Added [-[QLPreviewPanel refreshCurrentPreviewItem]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1505151-refreshcurrentpreviewitem)Added [-[QLPreviewPanel reloadData]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1504075-reloaddata)Added [+[QLPreviewPanel sharedPreviewPanel]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503415-shared)Added [+[QLPreviewPanel sharedPreviewPanelExists]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1505319-sharedpreviewpanelexists)Added [-[QLPreviewPanel updateController]](https://developer.apple.com/documentation/quartz/qlpreviewpanel/1503825-updatecontroller)Added [QLPreviewPanelDelegate](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate)Added [-[QLPreviewPanelDelegate previewPanel:handleEvent:]](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate/1503889-previewpanel)Added [-[QLPreviewPanelDelegate previewPanel:sourceFrameOnScreenForPreviewItem:]](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate/1503423-previewpanel)Added [-[QLPreviewPanelDelegate previewPanel:transitionImageForPreviewItem:contentRect:]](https://developer.apple.com/documentation/quartz/qlpreviewpaneldelegate/1505277-previewpanel)Added NSObject(QLPreviewPanelController)Added numberOfPreviewItemsInPreviewPanelAdded previewPanel

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
