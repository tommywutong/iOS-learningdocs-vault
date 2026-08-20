---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_Globals_h.html
archived_at: '2026-07-18T02:59:14.156461Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Virtual%20Sphere%20Sample%20Code%201.1-Graphics3D.c.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-Globals.c.md)

# Virtual Sphere Sample Code 1.1/Globals.h

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* Globals.h
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1991-1993 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __GLOBALS__
#define __GLOBALS__


/*=================================================================================================
/* LightSpeed C dependencies
/*-------------------------------------------------------------------------------------------------*/
#ifdef THINK_C

/* Set flag for compiling a version using FPU or not */ 
#if __option (mc68020)
    #if __option (mc68881)
        #define qUseFPUand020   true
    #endif
#endif

#endif THINK_C


/*=================================================================================================
/* MPW C dependencies
/*-------------------------------------------------------------------------------------------------*/
#ifdef applec

/* Set flag for compiling a version using FPU or not */ 
#ifdef  mc68020
    #ifdef mc68881
        #define qUseFPUand020   true
    #else
        #define qUseFPUand020   false
    #endif
#endif

#endif applec


/*=================================================================================================
/* Common stuff
/*-------------------------------------------------------------------------------------------------*/
#ifndef qUseFPUand020
    #define qUseFPUand020   false
#endif

#define qDebug              false               /* Flag for compiling a debug version
                                                 * or normal version of this application */



#ifndef __MENUS__
#include <Menus.h>
#endif

#ifndef __TYPES__
#include <Types.h>
#endif

#ifndef __OSUTILS__
#include <OSUtils.h>
#endif


/* From Sample.c */
extern  SysEnvRec   gMac;                       /* The environment */
extern  Boolean IsDAWindow (WindowPtr window);  /* In Sample.c */

/* Menu globals */
extern  short       gObjectDisplayed;           /* Which object is being draw currently */              
extern  short       gRenderingStyle;            /* iLineDrawing, iFlatShading, iFlatShadingWithOutline */               
extern  Boolean     gDoBackfacedPolygonRemoval;
extern  Boolean     gDoubleBuffer;
extern  Boolean     gDrawInColor;

/* Utility routines */
pascal  void        DebugMessage (Str255 message);
pascal  void        EnableDisableItem (MenuHandle theMenu, short item, Boolean enable);
pascal  void        LocalToGlobalRect (Rect *globalRect);
pascal  void        MessageAlert (Str255 message);
pascal  void        MessageAlertAndQuit (Str255 message);
pascal  short       ScreenDepth (const Rect *globalRect);


#endif __GLOBALS__
```

[Next](Virtual%20Sphere%20Sample%20Code%201.1-Graphics3D.c.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-Globals.c.md)

