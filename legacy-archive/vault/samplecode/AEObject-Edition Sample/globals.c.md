---
title: AEObject-Edition Sample
apple_id: DTS10000204
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AEObject-Edition_Sample/Listings/globals_c.html
archived_at: '2026-07-18T02:59:32.267168Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AEObject-Edition Sample](AEObject-Edition%20Sample.md)


[Next](Initialize.c.md)[Previous](Files.c.md)

# globals.c

```c
/*------------------------------------------------------------------------------
*
*  Apple Developer Technical Support
*
*  Global variables for this sample
*
*  Program:    AEObject-Edition Sample
*  File:       Files.c -   C Source
*
*  by:         C.K. Haun <TR>
*
*  Copyright © 1990-1992 Apple Computer, Inc.
*  All rights reserved.
*
*------------------------------------------------------------------------------
* All our globals.
* Probably more than you would use in a commercial application, but I created
* many of these to make the sample easier to understand.  I hope it did.
*----------------------------------------------------------------------------*/
#ifndef __GLOBALS__
#define __GLOBALS__
#include "Sampdefines.h"
Boolean gHasColor = false;
short gCurrentColor = 1;    /* defaults to black */
RGBColor gColorArray[7] = {
{0,0,0},
{0,0,0},
{0,0,0xFFFF},
{0,0xFFFF,0},
{0xFFFF,0,0},
{0xFFFF,0xFFFF,0},
{0,0,0}
};
AEInteractAllowed gInteractLevel;

Handle gScrapData;                                          /* picture data currently on clipboard */
/* individual menu handles */
MenuHandle gAppleMenuHandle, gFileMenuHandle, gEditMenuHandle, gToolMenuHandle,
gAppleEventMenuHandle,gEditionMenuHandle,gWindowMenuHandle,gColorMenuHandle;
short gHelpItem; /* our added help menu item */
Boolean gStop;                                              /* Stop flag for this app */
unsigned long gMasterWindowID = 10000;                      /* for section tracking */
Rect gShowPubRect;                                          /* rectangle of the currently selected publisher */
Rect gShowSubRect;                                          /* rectangle of the currently selected subscriber */
SectionHandle gShowingSecHandle = nil;                      /* currently selected section */
SectionHandle gClipSection = nil;                           /* if the clipboard contains a section */
PicHandle gClipPict;                                        /* for the section picture */
Boolean gShowPub = false;                                   /* telling if a publisher or subscriber */
Boolean gShowSub = false;                                   /* border should be displayed */
Boolean gShowingAll = false;                                /* show all borders toggle */
Boolean gInBackground = false;                              /* Where Are We? */
Boolean gExpanded = false;                                  /* flag for expanded dialogs, for this sample */
Boolean gResizeSub = false;                                 /* resize flag for this sample */
short gClipHasContents = kClipEmpty;                        /* indicates the contents of the clipboard (PICT, TEXT, section ) */
EventRecord gERecord;                                       /* guess */
ProcessSerialNumber gOurSN;                                 /* serial number of this process (us, our application) */
Boolean gHasAppleEvents;                                    /* not really necessary, since we fail if these */
Boolean gHasEditionManager;                                 /* aren't available, but it's only 4 bytes.... */


short actsToIDs[6] =                                        /* converts my action codes to tool menu item IDs */
{
    0, 1, 2, 3, 4, 6
};



SectionHandle gLastSection;                                  /* for double click testing */
unsigned long gLastSecClickTick;
RgnHandle mousergn;                                     /* for WaitNextEvent */

SFTypeList myList = 
{
    kMyDocumentFileType
};

SectionHandle gSecHandle;
EditionRefNum gEdRefNum;
EditionContainerSpec gEdSpec;
unsigned long gSectionID = 1;
long gMySleep;
prefStruct gPreferences;
/* some globals for AppleEvent transactions */

short gLocalInteraction;
short gAESendInteraction;
AEDesc gTargetAddress;
AEDesc gNullDesc;   /* seed nul deeescriptor, does not have to be a global, you can recreate it */
                    /* all the time if you want, but I like doing it this way*/
AEDesc * gCurrentReply; /* so anyone can add error descriptors */
Str63 targetName;
Boolean gAESwitchLayer;
short gAddressMode;
short gReplyMode;
/* here are the global handles for how we're specifying our */
/* objects */
/* See the AESampStructs.h file for the definition of these handles */
WindowObjectDefHandle gWindObjSpecHandle;
TextObjectDefHandle gTextObjSpecHandle;
ShapeObjectDefHandle gShapeObjSpecHandle;

short gSendInteractArray[] = 
{
kAENeverInteract, kAECanInteract, kAEAlwaysInteract, 
};

short gReplyLevels[] = 
{
    kAENoReply, kAEWaitReply,kAEQueueReply
};


#endif /* defined */
```

[Next](Initialize.c.md)[Previous](Files.c.md)

