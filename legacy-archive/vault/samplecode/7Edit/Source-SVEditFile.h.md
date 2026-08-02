---
title: 7Edit
apple_id: DTS10000200
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/7Edit/Listings/Source_SVEditFile_h.html
archived_at: '2026-07-18T02:59:21.124976Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [7Edit](7Edit.md)


[Next](Source-SVEditGlobals.c.md)[Previous](Source-SVEditFile.c.md)

# Source/SVEditFile.h

```c
/*
    File:       SVEditFile.h

    Contains:   

    Written by: Original version by Jon Lansdell and Nigel Humphreys.
                            3.1 updates by Greg Sutton. 

    Copyright:  Copyright ©1995-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/19/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/

#ifndef __SVEDITFILE__
#define __SVEDITFILE__

#include <Memory.h>
#include <Quickdraw.h>
#include <Traps.h>
#include <Files.h>
#include <Packages.h>
#include <Editions.h>
#include <AppleEvents.h>
#include <Printing.h>

#include "SVEditGlobals.h"
#include "SVEditUtils.h"
#include "SVEditWindow.h"

pascal void DoQuit(DescType saveOpt);

pascal OSErr DoClose(WindowPtr aWindow,Boolean canInteract,DescType dialogAnswer);

short DoFileDialog ( short theDlogID, WindowRef theWindow );

pascal OSErr GetFileNameToSaveAs(DPtr theDocument);

pascal OSErr DoSave(DPtr theDocument, FSSpec theFSSpec);

pascal OSErr GetFileContents(FSSpec theFSSpec, DPtr theDocument);

pascal void FileError(Str255 s, Str255 f);

pascal OSErr DoCreate(FSSpec theSpec);

pascal OSErr WriteFile(DPtr theDocument, short refNum, FSSpec theFSSpec);
pascal OSErr ReadFile(DPtr theDocument, short  refNum, Str255 fn);

pascal OSErr SaveUsingTemp(DPtr theDocument);

pascal OSErr OpenOld(FSSpec aFSSpec);

pascal OSErr OpenUsingAlias(AliasHandle theAliasH);

pascal OSErr GetFile(FSSpec *theFSSpec);

short DoSaveBeforeClosing ( short theDlogID, WindowRef theWindow );

#endif
```

[Next](Source-SVEditGlobals.c.md)[Previous](Source-SVEditFile.c.md)

