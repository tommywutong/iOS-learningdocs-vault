---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/MacShell_MacShell_h.html
archived_at: '2026-07-18T03:10:59.994848Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](MacShell-MacShell.r.md)[Previous](MacShell-MacShell.c.md)

# MacShell/MacShell.h

```c
#ifndef __MACSHELL_H__
    #define __MACSHELL_H__

// build for carbon
#ifndef TARGET_API_MAC_CARBON
    #define TARGET_API_MAC_CARBON 1
#endif

// includes
#include <ConditionalMacros.h>
#include <Gestalt.h>
#include <Types.h>
#include <Memory.h>
#include <Quickdraw.h>
#include <Fonts.h>
#include <Events.h>
#include <Menus.h>
#include <TextEdit.h>
#include <TextUtils.h>
#include <MacWindows.h>
#include <MacMemory.h>
#include <Dialogs.h>
#include <OSUtils.h>
#include <ToolUtils.h>
#include <Devices.h>
#include <FixMath.h>
#include <Endian.h>
#include <Resources.h>
#include <Navigation.h>
#include <Movies.h>
#include <ImageCompression.h>
#include <ImageCodec.h>
#include <QuickTimeComponents.h>

// Typedefs
//------------------------------------------------------------------------------
typedef const OSTypePtr TypeListPtr;

#if TARGET_OS_MAC
    typedef MenuHandle          MenuReference;
    typedef WindowPtr           WindowReference;
    typedef NavObjectFilterUPP  QTFrameFileFilterUPP;
#endif

#if TARGET_OS_WIN32
    typedef HMENU               MenuReference;
    typedef HWND                WindowReference;
    typedef FileFilterUPP       QTFrameFileFilterUPP;
#endif

// Defines & Constants
//------------------------------------------------------------------------------
#define BailNULL(n)  if (!n) goto bail;
#define BailError(n) if (n) goto bail;
#if TARGET_OS_MAC
    #define PASCAL_RTN pascal
#endif

enum {
    kAppleMenuID            = 128,
        kAppleMenuAbout         = 1,
    kFileMenuID             = 129,
        kFileMenuQuit           = 1,
    kDemoMenuID             = 130,
        kDemoMenuDraw           = 1,
        kDemoMenuScaleRotate    = 2,
        kDemoMenuAlpha          = 3,
        kDemoMenuMoreInfo       = 4,
        kDemoMenuMultipleImage  = 5,
        kDemoMenuURLImage       = 6,
        kDemoMenuFiltersExport  = 7,
        kDemoMenuMovieImage     = 8 
};

void pause( void );
void DrawImage( void );
void ScaleAndRotate( void );
void AlphaComposite( void );
void GetMoreInfo( void );
void MultipleImage( void );
void ImageFromURL( void );
void FilterExport( void );
void MovieToImage( void );

Boolean IsQuickTimeInstalled(void);
OSErr GetOneFileWithPreview (short theNumTypes, TypeListPtr theTypeList, FSSpecPtr theFSSpecPtr, void *theFilterProc);
OSErr PutFile(ConstStr255Param thePrompt, ConstStr255Param theFileName, FSSpecPtr theFSSpecPtr, Boolean *theIsSelected, Boolean *theIsReplacing);
OSErr BuildMovieValidFileTypes( Handle list, long *count );
OSErr BuildGraphicsImporterValidFileTypes( Handle list, long *count );
OSErr BuildGraphicsImporterValidFileNameSuffixes( Handle list, long *count );
OSErr BuildAllValidFileTypes( Handle list, long *count );
OSErr BuildAllValidFileNameSuffixes( Handle list, long *count );

#endif // __MACSHELL_H__
```

[Next](MacShell-MacShell.r.md)[Previous](MacShell-MacShell.c.md)

