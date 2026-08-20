---
title: couldNotResolveDataRef (-2000) returned from DataHSetDataRef and OpenADataHandler
apple_id: DTS10001664
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qa2001/qa1116.html
archived_at: '2026-07-18T02:38:14.496967Z'
---
> 导航：[总目录](../../../README.md) · [qa](../../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [Legacy Documents](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/LegacyTechnologies/idxQuickTime-date.html) >

# Legacy Documentclose button

__Important:__ This document is part of the Legacy section of the ADC Reference Library. This information should not be used for new development.

Current information on this Reference Library topic can be found here:

- [QuickTime > QuickTime Component Creation](https://developer.apple.com/referencelibrary/QuickTime/idxQuickTimeComponentCreation-date.html)

|  |
| --- |
| Technical Q&A QA1116couldNotResolveDataRef (-2000) returned from DataHSetDataRef and OpenADataHandler |

|  |  |  |
| --- | --- | --- |
| ---   Q: I'm currently working on implementing the MovieExportFromProceduresToDataRef function for an export component, but I've run into couldNotResolveDataRef errors using `DataHSetDataRef` and `OpenADataHandler` APIs.  In the DataHSetDataRef case, I manually iterate over all the Data Handler components using FindNextComponent until I find a handler for the dataRefType I'm passed in (I'm currently only concerned with 'alis' references). I open it using OpenComponent and call DataHSetDataRef. This results in a couldNotResolveDataRef (-2000) error.  After looking though some QuickTime documentation I encountered OpenADataHandler. This seemed like a much better, more convenient way to do what I needed. I removed all my previous code in favor of this single API, but it returns the same couldNotResolveDataRef error.  Is there something else I can do to get DataHSetDataRef to work? Is OpenADataHandler the correct API?  A: DataHSetDataRef assigns a data reference to the data handler component you're working with, this reference is used to identify and locate a movie's container.  The 'alis' Data Handler Components internal implementation of DataHSetDataRef performs a MatchAlias to find the file referenced. If the file does not yet exist, MatchAlias will return a file not found error ('fnfErr') but will also return a valid FSSpec.  The error returned from DataHSetDataRef in this case is couldNotResolveDataRef, exactly what is being seen. The data reference is good, even though the call returned an error.  OpenADataHandler on the other hand is a 'convenience' function which finds, opens, and sets up a data handler component in a single call. It's internal implementation uses the sequence of GetDataHandler, OpenAComponent and SetDataRef calls. However, it checks the result of DataHSetDataRef and fails if the result is not 'noErr', again returning couldNotResolveDataRef.  Therefore, you currently cannot replace the GetDataHandler, OpenAComponent, SetDataRef sequence of calls (see Listing 1) with the simpler OpenADataHandler call for the writing case. If the file already exists you will not encounter this problem.  Notice the result from DataHSetDataRef is ignored in the code because the file might not exist.   |  | | --- | | ``` Component   dh; DataHandler theDataHandler;  dh = GetDataHandler((Handle)inAlias, inDataRefType, kDataHCanRead | kDataHCanWrite); if (NULL == dh) {     err = cantFindHandler;     goto bail; }  err = OpenAComponent(dh, &theDataHandler); if (err) goto bail;  // Ignore error from this call, as the file may not already exist DataHSetDataRef(theDataHandler, (Handle)inAlias); ``` | | __Listing 1__. Finding and Opening a Data Handler |   Additionally, developers should be aware that component manager functions are often unable to make the best choice when there are several different data handlers available for data references of a specific type. Developers should always use either GetDataHandler or OpenADataHandler (note the case discussed above) APIs when attempting to find and/or open a Data Handler Component. Using FindNextComponent may get you something you didn't really want.  For example, when looking for an 'alis' Data Handler you could find the "Apple Alias Data Handler for CDi Disks" or the "Apple Alias Data Handler" or the "Streaming file data handler." All three have the same Type and SubType but serve different purposes.  Additional information:  [QuickTime Data Handler Documentation](https://developer.apple.com/documentation/quicktime/qtdevdocs/RM/rmDataHandlerComp.htm)  [Using Data Handler Components](https://developer.apple.com/documentation/quicktime/qtdevdocs/REF/refDataHandlerComp.7.htm)  [GetDataHandler Reference](https://developer.apple.com/documentation/quicktime/qtdevdocs/APIREF/SOURCESI/getdatahandler.htm)  [OpenADataHandler Reference](https://developer.apple.com/documentation/quicktime/qtdevdocs/APIREF/SOURCESII/openadatahandler.htm)   ---  [Feb 07 2002] |

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
