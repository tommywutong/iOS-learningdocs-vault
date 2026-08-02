---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSScript_h.html
archived_at: '2026-07-18T03:14:42.947906Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSToken.h.md)[Previous](Sources-MSScript.c.md)

# Sources/MSScript.h

```c
// MSScript.h
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// Human Interface changes and GX Printing by Don Swatman
// ©Apple Computer Inc 1996, all rights reserved.

#pragma once

#include <Types.h>
#include <OSA.h>

#include "MSGlobals.h"

#define kDefaultDocumentScript  300


OSErr       InitEditorScripting( void );
OSErr       SetOSAActiveProcedure( void );
OSErr       CloseEditorScripting( void );
OSErr       CompileDocument( DPtr theDoc );
OSErr       ExecuteDocument( DPtr theDoc );
OSErr       ScriptForMenuExists( short theMenu, short theItem, Boolean *exists );
OSErr       ExecuteScriptForMenu( short theMenu, short theItem );
OSErr       EditMenuScript( short theMenu, short theItem );

short               GetScriptActiveItem( void );
MenuScriptRecPtr    GetMenuScriptRecPtr( short theResID );

OSAError    LoadDocumentScript( DPtr theDoc, short theFileRef );
OSAError    StoreDocumentScript( DPtr theDoc, short theFileRef );

OSAError    GetScriptProperty( OSAID contextID, const AEDesc* propertyName, AEDesc* result );
OSAError    SetScriptProperty( OSAID contextID, const AEDesc* propertyName, const AEDesc* value );

OSErr       GetScriptDesc( OSAID theScriptID, DescType theWantType, AEDesc* theResult );
OSErr       SetScriptDesc( const AEDesc* theData, OSAID* theResult );
```

[Next](Sources-MSToken.h.md)[Previous](Sources-MSScript.c.md)

