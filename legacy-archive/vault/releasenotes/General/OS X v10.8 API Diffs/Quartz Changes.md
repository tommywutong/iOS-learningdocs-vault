---
title: OS X v10.8 API Diffs
apple_id: TP40011748
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2012-07-23'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_8/Quartz.html
archived_at: '2026-07-18T02:54:06.090710Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.8 API Diffs](OS%20X%20v10.7%20to%20OS%20X%20v10.8%20API%20Differences.md)


# Quartz Changes

## Quartz

IKPictureTaker.hRemoved [NSInteger](https://developer.apple.com/documentation/objectivec/nsinteger) (no architecture available)IKScannerDeviceView.hAdded [-[IKScannerDeviceViewDelegate scannerDeviceView:didScanToBandData:scanInfo:error:]](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate/1503867-scannerdeviceview)Added [-[IKScannerDeviceViewDelegate scannerDeviceView:didScanToURL:error:]](https://developer.apple.com/documentation/quartz/ikscannerdeviceviewdelegate/1504768-scannerdeviceview)ImageKitDeprecated.hModified [IKPictureTakerCropAreaSizeKey](https://developer.apple.com/documentation/quartz/ikpicturetakercropareasizekey)

|  | Header |
| --- | --- |
| From | IKPictureTaker.h |
| To | ImageKitDeprecated.h |

PDFAnnotationTextWidget.hAdded [-[PDFAnnotationTextWidget attributedStringValue]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504145-attributedstringvalue)Added [-[PDFAnnotationTextWidget setAttributedStringValue:]](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget/1504779-setattributedstringvalue)PDFLayerView.hAdded PDFLayerViewAdded PDFLayerView.displayBoxAdded PDFLayerView.documentAdded -[PDFLayerView idealSizeForContent]QuartzFilterManager.hAdded [globalUpdateOK](https://developer.apple.com/documentation/quartz/globalupdateok)

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
