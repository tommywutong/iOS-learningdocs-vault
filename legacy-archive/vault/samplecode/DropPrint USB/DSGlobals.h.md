---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Listings/DSGlobals_h.html
archived_at: '2026-07-18T03:07:20.842327Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DropPrint USB](DropPrint%20USB.md)


[Next](DSUserProcs.c.md)[Previous](DSAppleEvents.h.md)

# DSGlobals.h

```c
/******************************************************************************
**
**  Project Name:   DropShell
**     File Name:   DSGlobals.h
**
**   Description:   Globals used by DropShell
**
*******************************************************************************
**                       A U T H O R   I D E N T I T Y
*******************************************************************************
**
**  Initials    Name
**  --------    -----------------------------------------------
**  LDR         Leonard Rosenthol
**  MTC         Marshall Clow
**  SCS         Stephan Somogyi
**
*******************************************************************************
**                      R E V I S I O N   H I S T O R Y
*******************************************************************************
**
**    Date      Time    Author  Description
**  --------    -----   ------  ---------------------------------------------
**  02/20/94            LDR     Added commenting for Metrowerks
**  12/09/91            LDR     Added gSplashScreen
**  11/24/91            LDR     Added some new #defs & a #inc for DSUtils
**  10/29/91            SCS     Changes for THINK C 5
**  10/28/91            LDR     Officially renamed DropShell (from QuickShell)
**  10/06/91    00:02   MTC     Converted to MPW C
**  04/09/91    00:03   LDR     Added to Projector
**
******************************************************************************/

#ifndef __DSGLOBALS_H__
#define __DSGLOBALS_H__


//#ifndef __MWERKS__
#include <Types.h>
#include <Memory.h>
#include <QuickDraw.h>
#include <OSUtils.h>
#include <ToolUtils.h>
#include <Menus.h>
#include <Packages.h>
#include <Traps.h>
#include <Files.h>
//#endif

#include <Aliases.h>
#include <AppleEvents.h>
#include <Gestalt.h>
#include <Processes.h>


#define kAppleNum   128
#define kFileNum    129

#define kErrStringID    100
#define kCantRunErr     1
#define kAEVTErr        2


extern Boolean      gDone, gOApped, gHasAppleEvents, gWasEvent;
extern EventRecord  gEvent;
extern MenuHandle   gAppleMenu, gFileMenu;
extern WindowPtr    gSplashScreen;

#endif
```

[Next](DSUserProcs.c.md)[Previous](DSAppleEvents.h.md)

