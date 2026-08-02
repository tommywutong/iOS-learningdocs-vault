---
title: PickOne
apple_id: DTS10000117
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/PickOne/Listings/sources_PickOne_window_c.html
archived_at: '2026-07-18T03:18:59.183639Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PickOne](PickOne.md)


[Next](sources-PictRead.c.md)[Previous](sources-PickOneutility.c.md)

# sources/PickOne_window.c

```c
/*  window.c                                                                            

    Michael Bishop - August 21 1996                                                 
    Nick Thompson
    (c)1994-96 Apple computer Inc., All Rights Reserved                             

*/

#include    <Devices.h>

#include    "PickOne_window.h"
#include    "PickOne_document.h"

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
** Window_Dispose
** Call this function when we are done with a window, deallocate any storage allocated for this,
** this gets called when we close a document.
*/

void Window_Dispose(WindowPtr theWindow)
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
        DocumentHdl     myDocumentHandle = Window_GetDocument(theWindow);
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

/* -------------------------------------------------------------------------------------------
** Window_GetDocument
** Gets the document associated with a window
*/

DocumentHdl Window_GetDocument( WindowPtr theWindow)
{
    if (theWindow != NULL)
        return  (DocumentHdl) GetWRefCon ( theWindow );
    else return NULL;
}

/* -------------------------------------------------------------------------------------------
** Window_SetDocument
** Gets the document associated with a window
*/

int Window_SetDocument( WindowPtr theWindow,  DocumentHdl theDocument)
{
    if (theWindow != NULL)
    {
        SetWRefCon (theWindow, (long)theDocument ) ;
        return  true;
    }
    else return false;
}



void Window_DoContent (WindowPtr theWindow, EventRecord *theEvent)
{
#pragma unused  (theEvent)

    CGrafPtr    oldPort;
    DocumentHdl theDocument = Window_GetDocument(theWindow);

    GetPort((GrafPtr *)&oldPort);
    SetPort(theWindow);

    Document_DoPickAndRotate(theDocument);

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
        Document_Dispose( Window_GetDocument(theWindow) ) ; /*  delete it   */
        theWindow = Window_GetNextWindow(theWindow);            /*  go down the list    */
    }
}
```

[Next](sources-PictRead.c.md)[Previous](sources-PickOneutility.c.md)

