---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_Globals_c.html
archived_at: '2026-07-18T02:59:14.098726Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Virtual%20Sphere%20Sample%20Code%201.1-Globals.h.md)[Previous](Rotation%20Controllers%20demo%201.0.1-Rotation%20Programs%20Doc.txt.md)

# Virtual Sphere Sample Code 1.1/Globals.c

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* Globals.c
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1991-1993 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __GLOBALS__
#include "Globals.h"
#endif

#ifndef __DIALOGS__
#include <Dialogs.h>
#endif

#ifndef __SEGLOAD__
#include <SegLoad.h>
#endif

# include "Sample.h"

/* Declare globals used in menus */
short       gObjectDisplayed;           /* Which object is being draw currently */              
short       gRenderingStyle;            /* iLineDrawing, iFlatShading, iFlatShadingWithOutline */               
Boolean     gDoBackfacedPolygonRemoval;
Boolean     gDoubleBuffer;
Boolean     gDrawInColor;


/*=================================================================================================
/* DebugMessage
/*
/* Show a debugging message either to the debugger or in a dialog box
/* depending if the code is compiled for debugging (qDebug flag).
/*-------------------------------------------------------------------------------------------------*/
pascal void DebugMessage (Str255 message)
{
    if (qDebug) {
        DebugStr (message);
    } else {
        MessageAlert (message);
    }
}

/*=================================================================================================
/* EnableDisableItem
/*
/* Single routine to call EnableItem or DisableItem
/*-------------------------------------------------------------------------------------------------*/
pascal void EnableDisableItem (MenuHandle theMenu, short item, Boolean enable)
{
    if (enable) {
        EnableItem (theMenu, item);
    } else {
        DisableItem (theMenu, item);
    }
}

/*=================================================================================================
/* LocalToGlobalRect
/*
/* Returns a rect in global coordinate
/* Note the implicit dependency on the ordering of fields within a Rect
/*-------------------------------------------------------------------------------------------------*/
pascal void LocalToGlobalRect (Rect *globalRect)
{
    LocalToGlobal ((Point *) &(globalRect->top));
    LocalToGlobal ((Point *) &(globalRect->bottom));
}

/*=================================================================================================
/* MessageAlert
/*
/* Put up a message in an alert
/* Routine must be universal code
/*-------------------------------------------------------------------------------------------------*/
#ifdef applec
#pragma push                    /* MPW: save compiler flags         */
#pragma processor 68000         /* Generate 68000 instructions only */
#endif
pascal void MessageAlert (Str255 message)
{
    #ifdef THINK_C              /* THINK C: Generate 68020 instructionsÉ */
    #pragma options(!mc68020)   /* ÉNOT!  Silly way of saying 68000      */
    #endif                      /* instructions only.  Note this pragma  */
                                /* is defined only until end of routine. */
    SetCursor(&qd.arrow);
    ParamText (message, "", "", "");
    SysBeep (10);
    (void) Alert (rMessageAlert, nil);
}
#ifdef applec
#pragma pop                     /* MPW: restore compiler flags */
#endif

/*=================================================================================================
/* MessageAlertAndQuit
/*
/* Put up a message in an alert then quit out of application
/* Routine must be universal code
/*-------------------------------------------------------------------------------------------------*/
#ifdef applec
#pragma push                /* make sure error dialogs can be executed on all machines */
#pragma processor 68000
#endif
pascal void MessageAlertAndQuit (Str255 message)
{
    MessageAlert (message);
    ExitToShell();
}
#ifdef applec
#pragma pop
#endif

/*=================================================================================================
/* ScreenDepth
/*
/* Return the maximum monitor depth in the enclosing globalRect
/*-------------------------------------------------------------------------------------------------*/
pascal short ScreenDepth (const Rect *globalRect)
{
    GDHandle maxGDevice;
    maxGDevice = GetMaxDevice (globalRect);
    return ((**(**maxGDevice).gdPMap).pixelSize);
}
```

[Next](Virtual%20Sphere%20Sample%20Code%201.1-Globals.h.md)[Previous](Rotation%20Controllers%20demo%201.0.1-Rotation%20Programs%20Doc.txt.md)

