---
title: JPEG Sample
apple_id: DTS10000324
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JPEG_Sample/Listings/Headers_Global_h.html
archived_at: '2026-07-18T03:13:10.824045Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JPEG Sample](JPEG%20Sample.md)


[Next](Headers-Proto.h.md)[Previous](Headers-App.h.md)

# Headers/Global.h

```c
/*************************************************************************************
#
#       Global.h
#
#       This file contains the global definitions
#
#       Author(s):  Michael Marinkovich & Guillermo Ortiz
#                   marink@apple.com
#
#       Modification History: 
#
#           4/3/96      MWM     Initial coding                   
#
#       Copyright © 1992-96 Apple Computer, Inc., All Rights Reserved
#
#
#       You may incorporate this sample code into your applications without
#       restriction, though the sample code has been provided "AS IS" and the
#       responsibility for its operation is 100% yours.  However, what you are
#       not permitted to do is to redistribute the source as "DSC Sample Code"
#       after having made changes. If you're going to re-distribute the source,
#       we require that you make it clear in the source that the code was
#       descended from Apple Sample Code, but that you've made changes.
#
*************************************************************************************/

#include <Drag.h>

AEEventHandlerUPP   gAEOpenAppUPP;                  // hold on to these UPP's so we
AEEventHandlerUPP   gAEQuitAppUPP;                  // can ensure they are disposed of
AEEventHandlerUPP   gAEOpenDocUPP;                  // properly when we quit
AEEventHandlerUPP   gAEPrintDocUPP;
Boolean             gHasDMTwo;                      // is DM 2.0 available?
Boolean             gInBackground = false;          // are we in the background?
Boolean             gDone = false;                  // app is done flag     
Boolean             gHasDrag;                       // we have Drag Manager?
Boolean             gHasAbout;                      // do we have an about box showing?
short               gWindCount;                     // window counter for new windows
```

[Next](Headers-Proto.h.md)[Previous](Headers-App.h.md)

