---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSFile_h.html
archived_at: '2026-07-18T03:14:41.511264Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSGlobals.c.md)[Previous](Sources-MSFile.c.md)

# Sources/MSFile.h

```c
// MSFile.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

#ifndef __MSFILE__
#define __MSFILE__

#include <Memory.h>
#include <Quickdraw.h>
#include <Traps.h>
#include <Files.h>
#include <Packages.h>
#include <Editions.h>
#include <AppleEvents.h>
#include <Printing.h>

#include "MSGlobals.h"
#include "MSUtils.h"
#include "MSWindow.h"

void    DoQuit( DescType saveOpt );

OSErr   DoClose( WindowPtr aWindow, Boolean canInteract, DescType dialogAnswer );

short   DoFileDialog( short theDlogID, WindowRef theWindow );

OSErr   GetFileNameToSaveAs( DPtr theDocument );

OSErr   DoSave( DPtr theDocument, FSSpec theFSSpec );

OSErr   GetFileContents( FSSpec theFSSpec, DPtr theDocument );

void    FileError( Str255 s, Str255 f );

OSErr   DoCreate( FSSpec theSpec );

OSErr   WriteFile( DPtr theDocument, short refNum, FSSpec theFSSpec );
OSErr   ReadFile( DPtr theDocument, short  refNum, Str255 fn );

OSErr   SaveUsingTemp( DPtr theDocument );

OSErr   OpenOld( FSSpec aFSSpec );

OSErr   OpenUsingAlias( AliasHandle theAliasH );

OSErr   GetFile( FSSpec *theFSSpec );

short   DoSaveBeforeClosing( short theDlogID, WindowRef theWindow );

#endif
```

[Next](Sources-MSGlobals.c.md)[Previous](Sources-MSFile.c.md)

