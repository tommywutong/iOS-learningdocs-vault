---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/ResourceConstants_h.html
archived_at: '2026-07-18T02:59:27.420887Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UAEClientCommand.cp.md)[Previous](MAEGestalt.cp.md)

# ResourceConstants.h

```
//  ResourceConstants.h file
//  Copyright © 1991-92 by Apple Computer, Inc.  All rights reserved. 
//  Kent Sandvik DTS
//  This file contains resource types which are needed in both the
//  source code and the resource files. 
//
//  <1>     khs     1.0     First final version


#ifndef __RESOURCECONSTANTS__
#define __RESOURCECONSTANTS__

//  Signature and Type
#define kSignature              'FOOB'          // application signature
#define kFileType               'FOOD'          // file type code used for document files created by this application
#define kStationery             'fOOD'          // Stationery file type 


//  Bundle Constants
#define kBundleID               128
#define kApplicationID          128
#define kDocumentID             129
#define kStationeryID           130


//  Menus and command
#define mExamine                10
#define cFindAEGestalt          1001            // also command number
#define cCreateReport           1002            // also command number

#define cAEProvideGestaltInfo   1003            // AE Server command number


//  Views
#define kMainWindow             1002            // the main document window

#define kHorizontalOffset       20              //  Common view placement constants
#define kVerticalOffset         20
#define kHorizontStart          28
#define kVerticalStart          15


// AppleEvents
#define kGestaltAEEvents        1201            // 'aedt' resource constant
#define kMacAppClass            'maca'          // AE class
#define kAEGetConfig            'mgtc'          // AE command
#define kAEConfig               'conf'          // AE descriptor
#define typeConfig              'tcnf'          // AE descriptor type

#endif
```

[Next](UAEClientCommand.cp.md)[Previous](MAEGestalt.cp.md)

