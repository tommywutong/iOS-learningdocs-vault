---
title: OS X v10.10.3 API Diffs
apple_id: TP40015182
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-04-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_10_3/frameworks/Quartz.html
archived_at: '2026-07-18T02:51:50.816982Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.10.3 API Diffs](OS%20X%20v10.10%20to%20OS%20X%20v10.10.3%20API%20Differences.md)


# Quartz Changes

## Quartz

IKCameraDeviceView.hModified [-[IKCameraDeviceView deleteSelectedItems:]](https://developer.apple.com/documentation/quartz/ikcameradeviceview/1504333-deleteselecteditems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)deleteSelectedItems:(id)sender ``` |
| To | ``` - (IBAction)deleteSelectedItems:(id)sender ``` |

Modified [-[IKCameraDeviceView downloadAllItems:]](https://developer.apple.com/documentation/quartz/ikcameradeviceview/1504326-downloadallitems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)downloadAllItems:(id)sender ``` |
| To | ``` - (IBAction)downloadAllItems:(id)sender ``` |

Modified [-[IKCameraDeviceView downloadSelectedItems:]](https://developer.apple.com/documentation/quartz/ikcameradeviceview/1504833-downloadselecteditems)

|  | Declaration |
| --- | --- |
| From | ``` - (void)downloadSelectedItems:(id)sender ``` |
| To | ``` - (IBAction)downloadSelectedItems:(id)sender ``` |

Modified [-[IKCameraDeviceView rotateLeft:]](https://developer.apple.com/documentation/quartz/ikcameradeviceview/1503662-rotateleft)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rotateLeft:(id)sender ``` |
| To | ``` - (IBAction)rotateLeft:(id)sender ``` |

Modified [-[IKCameraDeviceView rotateRight:]](https://developer.apple.com/documentation/quartz/ikcameradeviceview/1505123-rotateright)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rotateRight:(id)sender ``` |
| To | ``` - (IBAction)rotateRight:(id)sender ``` |

IKImageView.hModified [-[IKImageView crop:]](https://developer.apple.com/documentation/quartz/ikimageview/1503855-crop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)crop:(id)sender ``` |
| To | ``` - (IBAction)crop:(id)sender ``` |

Modified [-[IKImageView flipImageHorizontal:]](https://developer.apple.com/documentation/quartz/ikimageview/1505282-flipimagehorizontal)

|  | Declaration |
| --- | --- |
| From | ``` - (void)flipImageHorizontal:(id)sender ``` |
| To | ``` - (IBAction)flipImageHorizontal:(id)sender ``` |

Modified [-[IKImageView flipImageVertical:]](https://developer.apple.com/documentation/quartz/ikimageview/1503836-flipimagevertical)

|  | Declaration |
| --- | --- |
| From | ``` - (void)flipImageVertical:(id)sender ``` |
| To | ``` - (IBAction)flipImageVertical:(id)sender ``` |

Modified [-[IKImageView rotateImageLeft:]](https://developer.apple.com/documentation/quartz/ikimageview/1503769-rotateimageleft)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rotateImageLeft:(id)sender ``` |
| To | ``` - (IBAction)rotateImageLeft:(id)sender ``` |

Modified [-[IKImageView rotateImageRight:]](https://developer.apple.com/documentation/quartz/ikimageview/1503427-rotateimageright)

|  | Declaration |
| --- | --- |
| From | ``` - (void)rotateImageRight:(id)sender ``` |
| To | ``` - (IBAction)rotateImageRight:(id)sender ``` |

Modified [-[IKImageView zoomImageToActualSize:]](https://developer.apple.com/documentation/quartz/ikimageview/1504415-zoomimagetoactualsize)

|  | Declaration |
| --- | --- |
| From | ``` - (void)zoomImageToActualSize:(id)sender ``` |
| To | ``` - (IBAction)zoomImageToActualSize:(id)sender ``` |

Modified [-[IKImageView zoomImageToFit:]](https://developer.apple.com/documentation/quartz/ikimageview/1504450-zoomimagetofit)

|  | Declaration |
| --- | --- |
| From | ``` - (void)zoomImageToFit:(id)sender ``` |
| To | ``` - (IBAction)zoomImageToFit:(id)sender ``` |

Modified [-[IKImageView zoomIn:]](https://developer.apple.com/documentation/quartz/ikimageview/1503800-zoomin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)zoomIn:(id)sender ``` |
| To | ``` - (IBAction)zoomIn:(id)sender ``` |

Modified [-[IKImageView zoomOut:]](https://developer.apple.com/documentation/quartz/ikimageview/1503436-zoomout)

|  | Declaration |
| --- | --- |
| From | ``` - (void)zoomOut:(id)sender ``` |
| To | ``` - (IBAction)zoomOut:(id)sender ``` |

IKSlideshow.hAdded [IK_PhotosBundleIdentifier](https://developer.apple.com/documentation/quartz/ik_photosbundleidentifier)PDFView.hAdded [-[PDFView areaOfInterestForPoint:]](https://developer.apple.com/documentation/quartz/pdfview/1504304-areaofinterest)Added [kPDFImageArea](https://developer.apple.com/documentation/quartz/pdfareaofinterest/kpdfimagearea)Modified [PDFView](https://developer.apple.com/documentation/pdfkit/pdfview)

|  | Protocols |
| --- | --- |
| From | NSAnimationDelegate |
| To | NSAnimationDelegate, NSMenuDelegate |

Modified [-[PDFView goBack:]](https://developer.apple.com/documentation/quartz/pdfview/1504319-goback)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goBack:(id)sender ``` |
| To | ``` - (IBAction)goBack:(id)sender ``` |

Modified [-[PDFView goForward:]](https://developer.apple.com/documentation/pdfkit/pdfview/1505200-goforward)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goForward:(id)sender ``` |
| To | ``` - (IBAction)goForward:(id)sender ``` |

Modified [-[PDFView goToFirstPage:]](https://developer.apple.com/documentation/quartz/pdfview/1504797-gotofirstpage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goToFirstPage:(id)sender ``` |
| To | ``` - (IBAction)goToFirstPage:(id)sender ``` |

Modified [-[PDFView goToLastPage:]](https://developer.apple.com/documentation/pdfkit/pdfview/1503500-gotolastpage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goToLastPage:(id)sender ``` |
| To | ``` - (IBAction)goToLastPage:(id)sender ``` |

Modified [-[PDFView goToNextPage:]](https://developer.apple.com/documentation/pdfkit/pdfview/1503751-gotonextpage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goToNextPage:(id)sender ``` |
| To | ``` - (IBAction)goToNextPage:(id)sender ``` |

Modified [-[PDFView goToPreviousPage:]](https://developer.apple.com/documentation/pdfkit/pdfview/1503898-gotopreviouspage)

|  | Declaration |
| --- | --- |
| From | ``` - (void)goToPreviousPage:(id)sender ``` |
| To | ``` - (IBAction)goToPreviousPage:(id)sender ``` |

Modified [-[PDFView selectAll:]](https://developer.apple.com/documentation/pdfkit/pdfview/1504628-selectall)

|  | Declaration |
| --- | --- |
| From | ``` - (void)selectAll:(id)sender ``` |
| To | ``` - (IBAction)selectAll:(id)sender ``` |

Modified [-[PDFView takeBackgroundColorFrom:]](https://developer.apple.com/documentation/quartz/pdfview/1503462-takebackgroundcolorfrom)

|  | Declaration |
| --- | --- |
| From | ``` - (void)takeBackgroundColorFrom:(id)sender ``` |
| To | ``` - (IBAction)takeBackgroundColorFrom:(id)sender ``` |

Modified [-[PDFView zoomIn:]](https://developer.apple.com/documentation/pdfkit/pdfview/1504814-zoomin)

|  | Declaration |
| --- | --- |
| From | ``` - (void)zoomIn:(id)sender ``` |
| To | ``` - (IBAction)zoomIn:(id)sender ``` |

Modified [-[PDFView zoomOut:]](https://developer.apple.com/documentation/pdfkit/pdfview/1505129-zoomout)

|  | Declaration |
| --- | --- |
| From | ``` - (void)zoomOut:(id)sender ``` |
| To | ``` - (IBAction)zoomOut:(id)sender ``` |

QCView.hModified [-[QCView play:]](https://developer.apple.com/documentation/quartz/qcview/1436227-play)

|  | Declaration |
| --- | --- |
| From | ``` - (void)play:(id)sender ``` |
| To | ``` - (IBAction)play:(id)sender ``` |

Modified [-[QCView start:]](https://developer.apple.com/documentation/quartz/qcview/1436254-start)

|  | Declaration |
| --- | --- |
| From | ``` - (void)start:(id)sender ``` |
| To | ``` - (IBAction)start:(id)sender ``` |

Modified [-[QCView stop:]](https://developer.apple.com/documentation/quartz/qcview/1436244-stop)

|  | Declaration |
| --- | --- |
| From | ``` - (void)stop:(id)sender ``` |
| To | ``` - (IBAction)stop:(id)sender ``` |

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
