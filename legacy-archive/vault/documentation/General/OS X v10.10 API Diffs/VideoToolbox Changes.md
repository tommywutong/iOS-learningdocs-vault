---
title: OS X v10.10 API Diffs
apple_id: TP40014444
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2014-10-16'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/APIDiffsMacOSX10_10SeedDiff/frameworks/VideoToolbox.html
archived_at: '2026-07-15T07:34:47.552754Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OS X v10.10 API Diffs](OS%20X%20v10.9%20to%20OS%20X%20v10.10%20API%20Differences.md)


# VideoToolbox Changes

## VideoToolbox

VTCompressionProperties.hAdded [kVTCompressionPropertyKey_MultiPassStorage](https://developer.apple.com/documentation/videotoolbox/kvtcompressionpropertykey_multipassstorage)VTCompressionSession.hAdded [VTCompressionSessionBeginPass()](https://developer.apple.com/documentation/videotoolbox/1428289-vtcompressionsessionbeginpass)Added [VTCompressionSessionEndPass()](https://developer.apple.com/documentation/videotoolbox/1428313-vtcompressionsessionendpass)Added [VTCompressionSessionGetTimeRangesForNextPass()](https://developer.apple.com/documentation/videotoolbox/1428311-vtcompressionsessiongettimerange)Added [VTCompressionSessionOptionFlags](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionoptionflags)Added [kVTCompressionSessionBeginFinalPass](https://developer.apple.com/documentation/videotoolbox/vtcompressionsessionoptionflags/1428299-beginfinalpass)VTDecompressionProperties.hAdded [kVTDecompressionPropertyKey_RealTime](https://developer.apple.com/documentation/videotoolbox/kvtdecompressionpropertykey_realtime)VTErrors.hAdded [kVTCouldNotFindTemporalFilterErr](https://developer.apple.com/documentation/videotoolbox/kvtcouldnotfindtemporalfiltererr)Added [kVTDecodeInfo_ImageBufferModifiable](https://developer.apple.com/documentation/videotoolbox/vtdecodeinfoflags/kvtdecodeinfo_imagebuffermodifiable)Added [kVTFrameSiloInvalidTimeRangeErr](https://developer.apple.com/documentation/videotoolbox/kvtframesiloinvalidtimerangeerr)Added [kVTFrameSiloInvalidTimeStampErr](https://developer.apple.com/documentation/videotoolbox/1490398-error_code_constants/kvtframesiloinvalidtimestamperr)Added [kVTMultiPassStorageIdentifierMismatchErr](https://developer.apple.com/documentation/videotoolbox/kvtmultipassstorageidentifiermismatcherr)Added [kVTMultiPassStorageInvalidErr](https://developer.apple.com/documentation/videotoolbox/kvtmultipassstorageinvaliderr)Added [kVTPixelTransferNotPermittedErr](https://developer.apple.com/documentation/videotoolbox/kvtpixeltransfernotpermittederr)VTFrameSilo.h (Added)Added [VTFrameSiloAddSampleBuffer()](https://developer.apple.com/documentation/videotoolbox/1474240-vtframesiloaddsamplebuffer)Added [VTFrameSiloCallBlockForEachSampleBuffer()](https://developer.apple.com/documentation/videotoolbox/1474252-vtframesilocallblockforeachsampl)Added [VTFrameSiloCallFunctionForEachSampleBuffer()](https://developer.apple.com/documentation/videotoolbox/1474246-vtframesilocallfunctionforeachsa)Added [VTFrameSiloCreate()](https://developer.apple.com/documentation/videotoolbox/1474250-vtframesilocreate)Added [VTFrameSiloGetProgressOfCurrentPass()](https://developer.apple.com/documentation/videotoolbox/1474248-vtframesilogetprogressofcurrentp)Added [VTFrameSiloGetTypeID()](https://developer.apple.com/documentation/videotoolbox/1474242-vtframesilogettypeid)Added [VTFrameSiloRef](https://developer.apple.com/documentation/videotoolbox/vtframesiloref)Added [VTFrameSiloSetTimeRangesForNextPass()](https://developer.apple.com/documentation/videotoolbox/1474238-vtframesilosettimerangesfornextp)VTMultiPassStorage.h (Added)Added [VTMultiPassStorageClose()](https://developer.apple.com/documentation/videotoolbox/1536110-vtmultipassstorageclose)Added [VTMultiPassStorageCreate()](https://developer.apple.com/documentation/videotoolbox/1536088-vtmultipassstoragecreate)Added [VTMultiPassStorageGetTypeID()](https://developer.apple.com/documentation/videotoolbox/1536166-vtmultipassstoragegettypeid)Added [VTMultiPassStorageRef](https://developer.apple.com/documentation/videotoolbox/vtmultipassstorageref)Added [kVTMultiPassStorageCreationOption_DoNotDelete](https://developer.apple.com/documentation/videotoolbox/kvtmultipassstoragecreationoption_donotdelete)VTProfessionalVideoWorkflow.hAdded [VTRegisterProfessionalVideoWorkflowVideoEncoders()](https://developer.apple.com/documentation/videotoolbox/1437858-vtregisterprofessionalvideoworkf)

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
