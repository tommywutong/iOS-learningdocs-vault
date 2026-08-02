---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSUtils_h.html
archived_at: '2026-07-18T03:14:43.239437Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSWindow.c.md)[Previous](Sources-MSUtils.c.md)

# Sources/MSUtils.h

```c
// MSUtils.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSUTILS__
#define __MSUTILS__

#include <Types.h>
#include <Quickdraw.h>
#include <Packages.h>
#include <GestaltEqu.h>
#include <Editions.h>
#include <Printing.h>

#ifndef __MSGLOBALS__
#include "MSGlobals.h"
#endif

Boolean     GestaltAvailable( void );

Boolean     CheckEnvironment( void );

void        ShowError( Str255 theError, long theErrorCode );

Boolean     FeatureIsImplemented( OSType theFeature, short theTestBit );

void        GetTempFileName( DPtr aDoc, Str255 newString );

Boolean     Ours( WindowPtr aWindow );

void        SetShortMenus( void );
void        SetLongMenus( void );

void        SetStyleMenu( DPtr theDoc );

void        SetFontMenu( DPtr theDoc );

void        AdornDefaultButton(DialogPtr theDialog, short theItem);

pascal void DrawDefaultOutline( DialogPtr theDialog, short theItem );

void        RetrieveText( DialogPtr aDialog, short anItem, Str255 aString );

void        SetText( DialogPtr aDialog, short itemNo, Str255 theString );

void        GetRectOfDialogItem( DialogPtr theDialog, short theItem, Rect *theRect );

    // Changed for 7.0 and Outline Fonts
void        SetSizeMenu( DPtr theDoc );

long        LesserOf( long A, long B );

long        GreaterOf( long A, long B );

Boolean     DoPageSetup(DPtr theDoc);

Boolean     CtrlKeyPressed( const EventRecord *theEvent );

Boolean     OptionKeyPressed( const EventRecord *theEvent );

short       NumToolboxTraps(void);
TrapType    GetTrapType(short theTrap);
Boolean     TrapAvailable(short theTrap);


#define     kMenuTitle 0

Boolean     SetMenuItemState (  Boolean    theState,
                                MenuHandle theMenu,
                                short      item );

#endif
```

[Next](Sources-MSWindow.c.md)[Previous](Sources-MSUtils.c.md)

