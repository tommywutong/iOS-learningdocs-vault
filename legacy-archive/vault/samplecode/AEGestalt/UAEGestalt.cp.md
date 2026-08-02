---
title: AEGestalt
apple_id: DTS10000203
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEGestalt/Listings/UAEGestalt_cp.html
archived_at: '2026-07-18T02:59:27.698789Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEGestalt](AEGestalt.md)


[Next](UAEGestalt.h.md)[Previous](UAEDocument.h.md)

# UAEGestalt.cp

```c
//  UAEGestalt.cp 
//  Copyright © 1991-92 by Apple Computer, Inc. All rights reserved.
//  Kent Sandvik DTS
//  This file contains the basic TAEApplication member functions
//
//  <1>     khs     1.0     First final version


// INCLUDES 

#ifndef __UAEGESTALT__
#include "UAEGestalt.h"                                     
#endif

// TAEApplication
//  Empty constructor - for avoiding ptabs in global data space

#undef Inherited
#define Inherited TApplication

#pragma segment ARes
DefineClass(TAEApplication, TApplication);

TAEApplication::TAEApplication()
{
}

//  Initialize the Application object

#pragma segment AInit
void TAEApplication::IAEApplication(OSType fileType,
                                           OSType creator)
{
    Inherited::IApplication(fileType, creator);

    // so the linker doesn't dead strip class info 
    macroDontDeadStrip(TLabelView);
    macroDontDeadStrip(TInformationView);
    macroDontDeadStrip(TGrayFill);

    // register adorner types
    RegisterStdType("TGrayFill", 'gray');
}


//  Create a new TDocument from the class
#pragma segment AOpen
TDocument* TAEApplication::DoMakeDocument(CommandNumber/* itsCmdNumber */,
                                                 TFile*/* itsFile */ )
{
    TAEDocument * aAEDocument = new TAEDocument;
    aAEDocument->IAEDocument();
    return aAEDocument;
}


//  Handle incoming AppleEvents calls, in our case to the TAEServerCommand
#pragma segment ASelCommand
void TAEApplication::DoAppleCommand(CommandNumber theNumber,
                                           const AppleEvent& message,
                                           const AppleEvent& reply)
{
    switch (theNumber)
    {
            // case Gestalt server AE, create a command from the AE, and post it!
        case cAEProvideGestaltInfo:
           {
            TAEServerCommand * aCommand = new TAEServerCommand;
            aCommand->InitializeFromAppleEvent(theNumber, this, kCantUndo, kDoesNotCauseChange, NULL, message, reply);
            this->PostCommand(aCommand);
            break;
            }

        default:
            Inherited::DoAppleCommand(theNumber, message, reply);
            break;
    }
}


// Show our cute About Box with Jeff trying to destroy my portable back home
#pragma segment ARes
void TAEApplication::DoAboutBox()
{
    CreateAboutBox();
}
```

[Next](UAEGestalt.h.md)[Previous](UAEDocument.h.md)

