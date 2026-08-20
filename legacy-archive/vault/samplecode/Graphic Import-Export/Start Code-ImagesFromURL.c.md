---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Start_Code_ImagesFromURL_c.html
archived_at: '2026-07-18T03:11:01.170246Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Start%20Code-MovieToImages.c.md)[Previous](Start%20Code-GettingMoreInfo.c.md)

# Start Code/ImagesFromURL.c

```c
// Graphics Importer and Exporter Samples
// This example creates a URL data reference and opens
// the image from this created reference
// Originally written by Sam Bushell for QuickTime "Live" '99
// WWDC 2000 Introduction to QuickTime


#include "MacShell.h"

void ImageFromURL( void )
{
    OSErr err = noErr;
    DialogPtr dialog;
    short itemHit;
    short itemKind;
    Handle itemHandle;
    Rect itemRect;
    GraphicsImportComponent importer = 0;
    Rect naturalBounds, windowBounds;
    WindowPtr window = NULL;    
    Str255 str;
    Handle urlDataRef = NULL;

    // show a dialog and prompt for the URL
    dialog = GetNewDialog( 1006, NULL, (WindowPtr)-1 );
    SetDialogDefaultItem( dialog, kStdOkItemIndex );
    SetDialogCancelItem( dialog, kStdCancelItemIndex );
    SelectDialogItemText( dialog, 3, 0, 1000 );
    ModalDialog( NULL, &itemHit );
    GetDialogItem( dialog, 3, &itemKind, &itemHandle, &itemRect );
    GetDialogItemText( itemHandle, str );
    DisposeDialog( dialog );
    if( kStdCancelItemIndex == itemHit ) return;

    // the default URL is
    // "http://www.apple.com/quicktime/developers/icefloe/images/writinguin.gif"

    // URL data references must be nul-terminated
    PtrToHand( &str[1], &urlDataRef, 1 + str[0] );
    (*urlDataRef)[ str[0] ] = 0;

    // locate and open a graphics importer component for the data reference
// Step 1. Insert ImporterForDataRef.clp here...

    // get the native size of the image associated with the importer
    err = GraphicsImportGetNaturalBounds( importer, &naturalBounds );

    windowBounds = naturalBounds;
    OffsetRect( &windowBounds, 10, 45 );
    window = NewCWindow( NULL, &windowBounds, "\pImage From URL", true, documentProc, (WindowPtr)-1, true, 0);

    // set the graphics port for drawing
    err = GraphicsImportSetGWorld( importer, GetWindowPort( window ), NULL );

    // draw the image
    err = GraphicsImportDraw( importer );

    CloseComponent( importer );
    DisposeHandle( urlDataRef );
}
```

[Next](Start%20Code-MovieToImages.c.md)[Previous](Start%20Code-GettingMoreInfo.c.md)

