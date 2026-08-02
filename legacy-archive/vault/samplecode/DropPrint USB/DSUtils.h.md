---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Listings/DSUtils_h.html
archived_at: '2026-07-18T03:07:21.205200Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DropPrint USB](DropPrint%20USB.md)


[Next](ListInDialog.c.md)[Previous](DSUtils.c.md)

# DSUtils.h

```c
/******************************************************************************
**
**  Project Name:   DropShell
**     File Name:   DSUtils.h
**
**   Description:   header w/protos for DSUtils
**
*******************************************************************************
**                       A U T H O R   I D E N T I T Y
*******************************************************************************
**
**  Initials    Name
**  --------    -----------------------------------------------
**  SCS         Stephan Somogyi
**  LDR         Leonard Rosenthol
**
*******************************************************************************
**                      R E V I S I O N   H I S T O R Y
*******************************************************************************
**
**    Date      Author  Description
**  ---------   ------  ---------------------------------------------
**  20 Feb 94   LDR     Exported new file system routines
**  11 Dec 93   SCS     Universal Headers/UPPs (Phoenix 68k/PPC & PPCC)
**                      Skipped System 6 compatible rev of DropShell source
**  12/09/91    LDR     Added protos for new routines
**  11/24/91    LDR     original version
**
******************************************************************************/

#ifndef __DSUTILS_H__
#define __DSUTILS_H__

#include <Types.h>
#include <Memory.h>
#include <QuickDraw.h>
#include <OSUtils.h>
#include <ToolUtils.h>
#include <Menus.h>
#include <Packages.h>
#include <Traps.h>
#include <Files.h>
#include <Resources.h>
#include <Errors.h>

#include <Aliases.h>
#include <Processes.h>
#include <PPCToolbox.h>

#include "DSGlobals.h"

#ifndef _FSAH_
#define _FSAH_
typedef FSSpecArrayPtr *FSSpecArrayHandle;       /* handle to array of FSSpecs */
#endif


void CenterAlert ( short theID );
void ErrorAlert ( short stringListID, short stringIndexID, short errorID );

void GetMyAppName(Str255 appName);
void GetAppFSSpec(FSSpec *appSpec);

OSErr ForceFinderUpdate(FSSpec *pFSS, Boolean flush);
Boolean FSpIsBusy(FSSpecPtr theFile);
Boolean FSpIsFolder(FSSpecPtr theFSSpec);
FSSpecArrayHandle   NewFSSpecList(void);
void DisposeFSSpecList(FSSpecArrayHandle fsList);
void AddToFSSpecList(FSSpec *fSpec, FSSpecArrayHandle fileList);

OSErr GetTargetFromSelf (AEAddressDesc *targetDesc);
OSErr GetTargetFromSignature (OSType processSig, AEAddressDesc *targetDesc);
OSErr GetTargetFromBrowser (Str255 promptStr, AEAddressDesc *targetDesc);

void _SendDocsToSelf (AEDescList *aliasList);
void SendODOCToSelf (FSSpec *theFileSpec);
void SendQuitToSelf (void);

#endif
```

[Next](ListInDialog.c.md)[Previous](DSUtils.c.md)

