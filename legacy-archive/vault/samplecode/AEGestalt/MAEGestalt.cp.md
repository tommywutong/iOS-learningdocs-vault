---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/MAEGestalt_cp.html
archived_at: '2026-07-18T02:59:27.359690Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](ResourceConstants.h.md)[Previous](IncludeFiles.h.md)

# MAEGestalt.cp

```c
//  MAEGestalt.cp
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This is the main-main file, it all starts here...
//
//  <1>     khs     1.0     First final version


// INCLUDES

#ifndef __AEGESTALT__
#include "UAEGestalt.h"
#endif


// T H E   M A I N  P R O G R A M

#pragma processor 68000
#pragma segment Main


// the application object 
TAEApplication* gAEApplication = NULL;

void main()
{
    // essential toolbox and utilities initialization
    InitToolBox();

    // make sure we can run
    if (ValidateConfiguration(gConfiguration) && gConfiguration.hasColorQD && gConfiguration.hasAppleEventMgr)
    {
        // we made it! Continue with remainder of initialization 
        // initialize MacApp; 8 calls to MoreMasters        
        InitUMacApp(8);
        // initialize the TDialog view handling
        InitUDialog();

        // construct a new TAEApplication object, allocation errors are checked for.
        gAEApplication = new TAEApplication;
        gAEApplication->IAEApplication(kFileType, kSignature);

        // run the application, when it's done - exit.
        gAEApplication->Run();
    }
    else
        StdAlert(phUnsupportedConfiguration);
}
```

[Next](ResourceConstants.h.md)[Previous](IncludeFiles.h.md)

