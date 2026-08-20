---
title: BoxMooV
apple_id: DTS10000099
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/BoxMooV/Listings/sources_BoxMooV_window_c.html
archived_at: '2026-07-18T03:02:14.992316Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [BoxMooV](BoxMooV.md)


[Next](sources-BoxPaintmain.c.md)[Previous](sources-BoxMooVTexture.c.md)

# sources/BoxMooV_window.c

```c
/*  window.c                                                                            

    Rick Evans - Sept. 1996 derived from BoxPaint_window.c
    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#include <Devices.h>

#include    "BoxMooV_window.h"
#include    "BoxMooV_document.h"

/* -------------------------------------------------------------------------------------------
** Window_New
** Kind of a dummy function at the moment.
*/
WindowPtr Window_New(void)
{
    WindowPtr   tempWindow = GetNewCWindow( kWindowResID, NULL, (WindowPtr)-1L );

    return tempWindow ;
}


/* -------------------------------------------------------------------------------------------
** Window_Delete
** Call this function when we are done with a window, deallocate any storage allocated for this,
** this gets called when we close a document.
*/

void Window_Delete(WindowPtr theWindow)
{

    if( theWindow != NULL )
    {
        DisposeWindow ( theWindow ) ;
    }

}

/* -------------------------------------------------------------------------------------------
** Window_Update
** 
*/
void Window_Update( WindowPtr theWindow )
{

    CGrafPtr            savedPort ;

    if( theWindow != NULL ) 
    {
        DocumentHdl     myDocumentHandle = Document_GetFromWindow(theWindow);
        Rect            updateRect = (**(theWindow->visRgn)).rgnBBox;

        if( myDocumentHandle != NULL )
        {
            GetPort((GrafPtr *) &savedPort );
            SetPort( theWindow ) ;

            BeginUpdate( theWindow );

            HLock( (Handle)myDocumentHandle  ) ;
            Document_Draw(*myDocumentHandle ) ;
            HUnlock( (Handle)myDocumentHandle  ) ;

            EndUpdate( theWindow );
            SetPort( (GrafPtr )savedPort ) ;
        }
    }
}


/* ---------------------------------------------------------------------------------- 
**  Window_Activate
**  is called when an theEvent is received that reports that
**  a theWindow is being either activated or deactivated. 
*/
void Window_Activate(WindowPtr theWindow, short activate)
{
    if (theWindow) {
        if (activate) {

            /*  do whatever else you'd like to do for a activate theEvent */
            /* LoadScrap() ;
            */
        } else {

            /*  do whatever you'd like to do for a deactivate theEvent */
            /*UnloadScrap() ;
            */
        }
    }
}

void Window_DoContent (WindowPtr theWindow, EventRecord *event)
{
#if defined(__MWERKS__)
#pragma unused ( event )
#endif
    CGrafPtr    oldPort;
    DocumentHdl theDocument = Document_GetFromWindow(theWindow);

    GetPort((GrafPtr *)&oldPort);
    SetPort(theWindow);

    SetPort((GrafPtr)oldPort);
}


/* ---------------------------------------------------------------------------------- 
**  Window_GetNextWindow
**  Returns the next in the queue
*/
WindowPtr Window_GetNextWindow(WindowPtr theWindow)
{
    if (theWindow != NULL)
        return (WindowPtr)((WindowPeek)theWindow)->nextWindow;
    else return NULL;
}

/* ---------------------------------------------------------------------------------- 
**  Window_DestroyAll destroys all the windows in the app
**  
*/
void Window_DestroyAll(void)
{
    WindowPtr theWindow;

    theWindow = FrontWindow();                      /*  Start with the active window    */

    while (theWindow != NULL)
    {
        Document_Delete( Document_GetFromWindow(theWindow) ) ;  /*  delete it   */
        theWindow = Window_GetNextWindow(theWindow);            /*  go down the list    */
    }
}
```

[Next](sources-BoxPaintmain.c.md)[Previous](sources-BoxMooVTexture.c.md)

