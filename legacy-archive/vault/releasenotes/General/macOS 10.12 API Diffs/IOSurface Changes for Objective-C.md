---
title: macOS 10.12 API Diffs
apple_id: TP40017105
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOS10_12/Objective-C/IOSurface.html
archived_at: '2026-07-18T02:50:39.781360Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [macOS 10.12 API Diffs](OS%20X%2010.11.4%20to%20macOS%2010.12%20API%20Differences.md)


# IOSurface Changes for Objective-C

### IOSurface

#### IOSurfaceAPI.h

Added [IOSurfaceAllowsPixelSizeCasting()](https://developer.apple.com/documentation/iosurface/1642028-iosurfaceallowspixelsizecasting)Added [kIOSurfacePixelSizeCastingAllowed](https://developer.apple.com/documentation/iosurface/kiosurfacepixelsizecastingallowed)

#### IOSurfaceBase.h

Added #def IOSFC_CLASS_AVAILABLEAdded #def IOSFC_SWIFT_NAME

#### IOSurfaceObjC.h (Added)

Added [IOSurface](https://developer.apple.com/documentation/iosurface/iosurface)Added [-[IOSurface allAttachments]](https://developer.apple.com/documentation/iosurface/iosurface/2092487-allattachments)Added [IOSurface.allocationSize](https://developer.apple.com/documentation/iosurface/iosurface/2092534-allocationsize)Added [IOSurface.allowsPixelSizeCasting](https://developer.apple.com/documentation/iosurface/iosurface/2092536-allowspixelsizecasting)Added [-[IOSurface attachmentForKey:]](https://developer.apple.com/documentation/iosurface/iosurface/2092535-attachmentforkey)Added [IOSurface.baseAddress](https://developer.apple.com/documentation/iosurface/iosurface/2092525-baseaddress)Added [-[IOSurface baseAddressOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092494-baseaddressofplane)Added [IOSurface.bytesPerElement](https://developer.apple.com/documentation/iosurface/iosurface/2092503-bytesperelement)Added [-[IOSurface bytesPerElementOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092511-bytesperelementofplaneatindex)Added [IOSurface.bytesPerRow](https://developer.apple.com/documentation/iosurface/iosurface/2092502-bytesperrow)Added [-[IOSurface bytesPerRowOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092497-bytesperrowofplaneatindex)Added [-[IOSurface decrementUseCount]](https://developer.apple.com/documentation/iosurface/iosurface/2092538-decrementusecount)Added [IOSurface.elementHeight](https://developer.apple.com/documentation/iosurface/iosurface/2092539-elementheight)Added [-[IOSurface elementHeightOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092515-elementheightofplaneatindex)Added [IOSurface.elementWidth](https://developer.apple.com/documentation/iosurface/iosurface/2092514-elementwidth)Added [-[IOSurface elementWidthOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092498-elementwidthofplaneatindex)Added [IOSurface.height](https://developer.apple.com/documentation/iosurface/iosurface/2092501-height)Added [-[IOSurface heightOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092493-heightofplane)Added [-[IOSurface incrementUseCount]](https://developer.apple.com/documentation/iosurface/iosurface/2092506-incrementusecount)Added [-[IOSurface initWithProperties:]](https://developer.apple.com/documentation/iosurface/iosurface/2092523-init)Added [IOSurface.isInUse](https://developer.apple.com/documentation/iosurface/iosurface/2092504-isinuse)Added [IOSurface.localUseCount](https://developer.apple.com/documentation/iosurface/iosurface/2092529-localusecount)Added [-[IOSurface lockWithOptions:seed:]](https://developer.apple.com/documentation/iosurface/iosurface/2092522-lock)Added [IOSurface.pixelFormat](https://developer.apple.com/documentation/iosurface/iosurface/2092537-pixelformat)Added [IOSurface.planeCount](https://developer.apple.com/documentation/iosurface/iosurface/2092508-planecount)Added [-[IOSurface removeAllAttachments]](https://developer.apple.com/documentation/iosurface/iosurface/2092490-removeallattachments)Added [-[IOSurface removeAttachmentForKey:]](https://developer.apple.com/documentation/iosurface/iosurface/2092541-removeattachmentforkey)Added [IOSurface.seed](https://developer.apple.com/documentation/iosurface/iosurface/2092533-seed)Added [-[IOSurface setAllAttachments:]](https://developer.apple.com/documentation/iosurface/iosurface/2092532-setallattachments)Added [-[IOSurface setAttachment:forKey:]](https://developer.apple.com/documentation/iosurface/iosurface/2092540-setattachment)Added [-[IOSurface unlockWithOptions:seed:]](https://developer.apple.com/documentation/iosurface/iosurface/2092530-unlockwithoptions)Added [IOSurface.width](https://developer.apple.com/documentation/iosurface/iosurface/2092516-width)Added [-[IOSurface widthOfPlaneAtIndex:]](https://developer.apple.com/documentation/iosurface/iosurface/2092520-widthofplane)Added [IOSurfacePropertyAllocSizeKey](https://developer.apple.com/documentation/iosurface/iosurfacepropertyallocsizekey)Added [IOSurfacePropertyKey](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey)Added [IOSurfacePropertyKeyBytesPerElement](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeybytesperelement)Added [IOSurfacePropertyKeyBytesPerRow](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092519-bytesperrow)Added [IOSurfacePropertyKeyCacheMode](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092528-cachemode)Added [IOSurfacePropertyKeyElementHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyelementheight)Added [IOSurfacePropertyKeyElementWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092507-elementwidth)Added [IOSurfacePropertyKeyHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyheight)Added [IOSurfacePropertyKeyOffset](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyoffset)Added [IOSurfacePropertyKeyPixelFormat](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeypixelformat)Added [IOSurfacePropertyKeyPixelSizeCastingAllowed](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeypixelsizecastingallowed)Added [IOSurfacePropertyKeyPlaneBase](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanebase)Added [IOSurfacePropertyKeyPlaneBytesPerElement](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanebytesperelement)Added [IOSurfacePropertyKeyPlaneBytesPerRow](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanebytesperrow)Added [IOSurfacePropertyKeyPlaneElementHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092492-planeelementheight)Added [IOSurfacePropertyKeyPlaneElementWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplaneelementwidth)Added [IOSurfacePropertyKeyPlaneHeight](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092500-planeheight)Added [IOSurfacePropertyKeyPlaneInfo](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplaneinfo)Added [IOSurfacePropertyKeyPlaneOffset](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092491-planeoffset)Added [IOSurfacePropertyKeyPlaneSize](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092499-planesize)Added [IOSurfacePropertyKeyPlaneWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykeyplanewidth)Added [IOSurfacePropertyKeyWidth](https://developer.apple.com/documentation/iosurface/iosurfacepropertykey/2092509-width)

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
