---
title: Importing image data from memory
apple_id: DTS10002026
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2011-07-11'
source_url: https://developer.apple.com/library/archive/qa/qtmtb/qtmtb56.html
archived_at: '2026-07-18T02:38:49.492083Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



[ADC Home](https://developer.apple.com/) > [Reference Library](https://developer.apple.com/library/archive/referencelibrary/index.html) > [Technical Q&As](https://developer.apple.com/library/archive/technicalqas/index.html) > [QuickTime](https://developer.apple.com/library/archive/technicalqas/QuickTime/index.html) > [Import & Export](https://developer.apple.com/library/archive/technicalqas/QuickTime/idxImportExport-date.html) >

|  |
| --- |
| Technical Q&A QTMTB56Importing image data from memory |

|  |
| --- |
| ---   Q: How do I use the graphics importer API's to read image data which resides not in a file but in memory?  A: Create a handle data reference for your data, and use the `GetGraphicsImporterForDataRef` function to locate a graphics importer component for the handle data reference.  However, if you just make a "plain" handle data reference, it doesn't contain any information about the file type or file name, so QuickTime has to perform a slow search through the available graphics importers, asking each if it recognizes the data - there's no other way. As well as being slow, this will miss some file formats that can't be detected by validation. If you have the file name, you should add the file name to the handle data reference. If you know the file type and/or MIME type, you should add that as well. For information and code showing how to add these types of data to your handle data reference, refer to [Technote 1195, "Tagging Handle Data References in QuickTime 4."](https://developer.apple.com/library/archive/technotes/tn/tn1195.html)  Here's a code snippet showing how to use the graphics importer API's to read image data that resides not in a file but in memory. You simply pass to this function in the `imageDataH` parameter a handle to your data, followed by any file name, file type and/or mime type and initialization data you may have (again, refer to [Technote 1195](https://developer.apple.com/library/archive/technotes/tn/tn1195.html) for additional information). Next, we create a handle data reference for the memory-based data. Then, we pass this handle data reference to the `GetGraphicsImporterForDataRef` function, which returns us a graphics importer component for the data:   ``` void MyGetGraphicsImporterForHandle(Handle         imageDataH,                                    Str255         fileName,                                    OSType        fileType,                                    StringPtr    mimeTypeString,                                    Ptr            initDataPtr,                                    Size        initDataByteCount                                     ) {      OSErr                 err;      Handle             dataRef = nil;      ComponentInstance    gi=0;       /* first create the handle data reference - refer to          TechNote 1195 for the details */      dataRef = myCreateHandleDataRef( imageDataH,                                       fileName,                                       fileType,                                       mimeTypeString,                                       initDataPtr,                                       initDataByteCount                                      );      if (dataRef != nil)      {          /* now get the appropriate graphics importer component             for this image */          err = GetGraphicsImporterForDataRef( dataRef,                                               HandleDataHandlerSubType,                                               &gi );          /* it's now safe to dispose of the data reference */          DisposeHandle(dataRef);          if (err == noErr)          {           /* ...now that we have the graphics importer component for this           image, we can call any of the graphics importer routines to           manipulate the image... */            /* close the graphics importer component instance when we are           done */              CloseComponent(gi);          }      }  }   Handle myCreateHandleDataRef(                     Handle             dataHandle,                     Str255             fileName,                     OSType             fileType,                     StringPtr          mimeTypeString,                     Ptr                initDataPtr,                     Size               initDataByteCount                      )     {      OSErr        err;      Handle    dataRef = nil;      Str31        tempName;      long        atoms[3];      StringPtr    name;       // First create a data reference handle for our data     err = PtrToHand( &dataHandle, &dataRef, sizeof(Handle));     if (err) goto bail;      // If this is QuickTime 3 or later, we can add     // the filename to the data ref to help importer     // finding process. Find uses the extension.      name = fileName;     if (name == nil)     {         tempName[0] = 0;         name = tempName;     }      // Only add the file name if we are also adding a     // file type, MIME type or initialization data     if ((fileType) || (mimeTypeString) || (initDataPtr))     {         err = PtrAndHand(name, dataRef, name[0]+1);         if (err) goto bail;     }      // If this is QuickTime 4, the handle data handler     // can also be told the filetype and/or     // MIME type by adding data ref extensions. These     // help the importer finding process.     // NOTE: If you add either of these, you MUST add     // a filename first -- even if it is an empty Pascal     // string. Under QuickTime 3, any data ref extensions     // will be ignored.      // to add file type, you add a classic atom followed     // by the MacOS filetype for the kind of file      if (fileType)     {         atoms[0] = EndianU32_NtoB(sizeof(long) * 3);         atoms[1] = EndianU32_NtoB(kDataRefExtensionMacOSFileType);         atoms[2] = EndianU32_NtoB(fileType);          err = PtrAndHand(atoms, dataRef, sizeof(long) * 3);         if (err) goto bail;     }       // to add MIME type information, add a classic atom followed by     // a Pascal string holding the MIME type      if (mimeTypeString)     {         atoms[0] = EndianU32_NtoB(sizeof(long) * 2 + mimeTypeString[0]+1);         atoms[1] = EndianU32_NtoB(kDataRefExtensionMIMEType);          err = PtrAndHand(atoms, dataRef, sizeof(long) * 2);         if (err) goto bail;          err = PtrAndHand(mimeTypeString, dataRef, mimeTypeString[0]+1);         if (err) goto bail;     }      // add any initialization data, but only if a dataHandle was     // not already specified (any initialization data is ignored     // in this case)     if((dataHandle == nil) && (initDataPtr))     {          atoms[0] = EndianU32_NtoB(sizeof(long) * 2 + initDataByteCount);         atoms[1] = EndianU32_NtoB(kDataRefExtensionInitializationData);          err = PtrAndHand(atoms, dataRef, sizeof(long) * 2);         if (err) goto bail;          err = PtrAndHand(initDataPtr, dataRef, initDataByteCount);         if (err) goto bail;     }      return dataRef;  bail:     if (dataRef)     {         // make sure and dispose the data reference handle         // once we are done with it         DisposeHandle(dataRef);     }      return nil; } ```   Note that you can dispose the handle data reference (`dataRef`) immediately after calling `GetGraphicsImporterForDataRef` if you like -- but you must not dispose the actual image data handle (`imageDataH`) until after you either close the graphics importer component instance or change its data source.  Alternately, you can use the `GraphicsImportSetDataHandle` function to specify the handle that the graphics data resides in. However, this requires you to open the appropriate graphics importer component yourself (and that you know the format of data). Here's a short code snippet showing how it's done. In this example, you simply pass in the data type along with a handle to your data:   ``` void MyGetGraphicsImporterForHandle(OSType dataType, Handle imageDataHandle)  {     OSErr               err;     ComponentInstance    ci=0;       /* get the appropriate graphics importer component for this image */     err = OpenADefaultComponent(GraphicsImporterComponentType, dataType, &ci);     if (err == noErr)     {         ComponentResult result;          /* now specify the handle in which the graphics data resides.            NOTE: For PICTs, imageDataHandle must include the standard 512            byte header. */          result = GraphicsImportSetDataHandle(ci, imageDataHandle);          /* ...now we can call any of the graphics importer routines to            manipulate the image...*/          /* make sure and close the component when we are done */         err = CloseComponent(ci);     }   } ```  [Apr 03 2000] |

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
