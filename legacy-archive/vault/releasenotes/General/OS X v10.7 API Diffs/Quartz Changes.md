---
title: OS X v10.7 API Diffs
apple_id: TP40010630
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2011-06-06'
source_url: https://developer.apple.com/library/archive/releasenotes/General/MacOSXLionAPIDiffs/Quartz.html
archived_at: '2026-07-18T02:54:38.772682Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.7 API Diffs](OS%20X%20v10.6%20to%20v10.7%20API%20Diffs.md)


# Quartz Changes

## Quartz

|  | Framework Architectures |
| --- | --- |
| From | i386,ppc,x86_64 |
| To | i386,x86_64 |

IKImageBrowserView.hModified [IKImageBrowserView](https://developer.apple.com/documentation/quartz/ikimagebrowserview)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSDraggingSource |

ImageKitDeprecated.hRemoved IKImagePickerRemoved -[IKImagePicker beginImagePickerSheetForWindow:withDelegate:didEndSelector:contextInfo:]Removed -[IKImagePicker beginImagePickerWithDelegate:didEndSelector:contextInfo:]Removed +[IKImagePicker imagePicker]Removed -[NSObject imageBrowser:cellAtIndex:]Removed -[NSObject imageBrowser:moveCellsAtIndexes:toIndex:]Removed -[NSObject imageBrowser:removeCellsAtIndexes:]Removed -[NSObject imageBrowser:writeCellsAtIndexes:toPasteboard:]Removed -[NSObject numberOfCellsInImageBrowser:]Removed IKImageBrowserCellLayerTypeBackgroundRemoved IKImageBrowserCellLayerTypeForegroundRemoved IKImageBrowserCellLayerTypePlaceHolderRemoved IKImageBrowserCellLayerTypeSelectionRemoved #def IKImagePickerAllowsEditingKeyRemoved #def IKImagePickerAllowsFileChoosingKeyRemoved #def IKImagePickerAllowsVideoCaptureKeyRemoved #def IKImagePickerCropAreaSizeKeyRemoved #def IKImagePickerImageTransformsKeyRemoved #def IKImagePickerInformationalTextKeyRemoved #def IKImagePickerOutputImageMaxSizeKeyRemoved #def IKImagePickerShowEffectsKeyRemoved #def IKImagePickerShowRecentPictureKeyRemoved #def IKImagePickerUpdateRecentPictureKeyRemoved NSObject(IKImageBrowserDataSourceDeprecated)Added DEPRECATED_ATTRIBUTE (no architecture available)PDFAction.hModified [PDFAction](https://developer.apple.com/documentation/pdfkit/pdfaction)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotation.hModified [PDFAnnotation](https://developer.apple.com/documentation/pdfkit/pdfannotation)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationButtonWidget.hAdded [-[PDFAnnotationButtonWidget setAllowsToggleToOff:]](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget/1412944-setallowstoggletooff)Modified [PDFAnnotationButtonWidget](https://developer.apple.com/documentation/quartz/pdfannotationbuttonwidget)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationChoiceWidget.hModified [PDFAnnotationChoiceWidget](https://developer.apple.com/documentation/quartz/pdfannotationchoicewidget)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationCircle.hModified [PDFAnnotationCircle](https://developer.apple.com/documentation/quartz/pdfannotationcircle)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationFreeText.hModified [PDFAnnotationFreeText](https://developer.apple.com/documentation/quartz/pdfannotationfreetext)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationInk.hModified [PDFAnnotationInk](https://developer.apple.com/documentation/quartz/pdfannotationink)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationLine.hModified [PDFAnnotationLine](https://developer.apple.com/documentation/quartz/pdfannotationline)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationLink.hModified [PDFAnnotationLink](https://developer.apple.com/documentation/quartz/pdfannotationlink)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationMarkup.hModified [PDFAnnotationMarkup](https://developer.apple.com/documentation/quartz/pdfannotationmarkup)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationPopup.hModified [PDFAnnotationPopup](https://developer.apple.com/documentation/quartz/pdfannotationpopup)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationSquare.hModified [PDFAnnotationSquare](https://developer.apple.com/documentation/quartz/pdfannotationsquare)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationStamp.hModified [PDFAnnotationStamp](https://developer.apple.com/documentation/quartz/pdfannotationstamp)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationText.hModified [PDFAnnotationText](https://developer.apple.com/documentation/quartz/pdfannotationtext)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFAnnotationTextWidget.hModified [PDFAnnotationTextWidget](https://developer.apple.com/documentation/quartz/pdfannotationtextwidget)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFBorder.hRemoved [-[PDFBorder horizontalCornerRadius]](https://developer.apple.com/documentation/quartz/pdfborder/1806517-horizontalcornerradius)Removed [-[PDFBorder setHorizontalCornerRadius:]](https://developer.apple.com/documentation/pdfkit/pdfborder/1806522-sethorizontalcornerradius)Removed [-[PDFBorder setVerticalCornerRadius:]](https://developer.apple.com/documentation/pdfkit/pdfborder/1806538-setverticalcornerradius)Removed [-[PDFBorder verticalCornerRadius]](https://developer.apple.com/documentation/quartz/pdfborder/1806532-verticalcornerradius)Modified [PDFBorder](https://developer.apple.com/documentation/pdfkit/pdfborder)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFDestination.hAdded -[PDFDestination setZoom:]Added [-[PDFDestination zoom]](https://developer.apple.com/documentation/pdfkit/pdfdestination/1504094-zoom)PDFDocument.hAdded [-[PDFDocument printOperationForPrintInfo:scalingMode:autoRotate:]](https://developer.apple.com/documentation/quartz/pdfdocument/1436075-printoperationforprintinfo)Modified [PDFDocument](https://developer.apple.com/documentation/quartz/pdfdocument)

|  | Protocols |
| --- | --- |
| From | _none_ |
| To | NSCopying |

PDFSelection.hAdded [-[PDFSelection numberOfTextRangesOnPage:]](https://developer.apple.com/documentation/pdfkit/pdfselection/1389579-numberoftextrangesonpage)Added [-[PDFSelection rangeAtIndex:onPage:]](https://developer.apple.com/documentation/pdfkit/pdfselection/1389587-rangeatindex)PDFView.hAdded [-[PDFView interpolationQuality]](https://developer.apple.com/documentation/pdfkit/pdfview/1503789-interpolationquality)Added -[PDFView setInterpolationQuality:]Added [PDFInterpolationQuality](https://developer.apple.com/documentation/pdfkit/pdfinterpolationquality)Added [kPDFInterpolationQualityHigh](https://developer.apple.com/documentation/pdfkit/pdfinterpolationquality/high)Added [kPDFInterpolationQualityLow](https://developer.apple.com/documentation/pdfkit/pdfinterpolationquality/low)Added [kPDFInterpolationQualityNone](https://developer.apple.com/documentation/pdfkit/pdfinterpolationquality/none)QCPatchController.hAdded [QCPatchController](https://developer.apple.com/documentation/quartz/qcpatchcontroller)QCPlugIn.hAdded [QCPlugInAttributeCategoriesKey](https://developer.apple.com/documentation/quartz/qcpluginattributecategorieskey)Added [QCPlugInAttributeExamplesKey](https://developer.apple.com/documentation/quartz/qcpluginattributeexampleskey)QCPlugInViewController.hAdded -[QCPlugIn NS_RETURNS_RETAINED] (no architecture available)QLPreviewView.hAdded [QLPreviewView](https://developer.apple.com/documentation/quartz/qlpreviewview)Added [QLPreviewView.autostarts](https://developer.apple.com/documentation/quartz/qlpreviewview/1503689-autostarts)Added [-[QLPreviewView close]](https://developer.apple.com/documentation/quartz/qlpreviewview/1503506-close)Added [QLPreviewView.displayState](https://developer.apple.com/documentation/quartz/qlpreviewview/1503408-displaystate)Added [-[QLPreviewView initWithFrame:]](https://developer.apple.com/documentation/quartz/qlpreviewview/1503812-initwithframe)Added [-[QLPreviewView initWithFrame:style:]](https://developer.apple.com/documentation/quartz/qlpreviewview/1504541-initwithframe)Added [QLPreviewView.previewItem](https://developer.apple.com/documentation/quartz/qlpreviewview/1504747-previewitem)Added [-[QLPreviewView refreshPreviewItem]](https://developer.apple.com/documentation/quartz/qlpreviewview/1504399-refreshpreviewitem)Added [QLPreviewView.shouldCloseWithWindow](https://developer.apple.com/documentation/quartz/qlpreviewview/1503457-shouldclosewithwindow)Added [QLPreviewViewStyle](https://developer.apple.com/documentation/quartz/qlpreviewviewstyle)Added [QLPreviewViewStyleCompact](https://developer.apple.com/documentation/quartz/qlpreviewviewstyle/compact)Added [QLPreviewViewStyleNormal](https://developer.apple.com/documentation/quartz/qlpreviewviewstyle/qlpreviewviewstylenormal)

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
