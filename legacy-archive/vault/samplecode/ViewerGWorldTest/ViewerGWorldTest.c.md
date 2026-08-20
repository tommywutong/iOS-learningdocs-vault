---
title: ViewerGWorldTest
apple_id: DTS10000129
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerGWorldTest/Listings/ViewerGWorldTest_c.html
archived_at: '2026-07-18T03:28:00.601319Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ViewerGWorldTest](ViewerGWorldTest.md)


[Next](Document%20Revision%20History.md)[Previous](ViewerGWorldTest.md)

# ViewerGWorldTest.c

```c
/*
 * Hack to show how to use the viewer to make pictures.  Click to quit.
 * nickt@apple.com
 */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <StandardFile.h>
#include <QuickDraw.h>
#include <QDOffscreen.h>
#include <Windows.h>


#include "QD3DViewer.h"


Boolean         gQuitFlag = false;
WindowPtr       gMainWindow     = nil ;

static void InitToolbox()
{
    Handle      menuBar = nil;

    MaxApplZone() ;
    MoreMasters() ; MoreMasters() ; MoreMasters() ; 

    InitGraf( &qd.thePort );
    InitFonts();
    InitWindows();
    InitMenus();
    TEInit() ;
    InitDialogs(0L) ;
    InitCursor();

    FlushEvents( everyEvent, 0 ) ;
    // initialize application globals

    gQuitFlag = false;

}

static Boolean MetafileFileSpecify( FSSpec *theFile )
{
    StandardFileReply   theSFReply ;
    SFTypeList          myTypes = { '3DMF' } ;
    const short         numTypes = 1 ;
    OSErr               myErr ;


    StandardGetFile( nil, numTypes, myTypes, &theSFReply ) ;

    if( theSFReply.sfGood )
        *theFile = theSFReply.sfFile ;

    return theSFReply.sfGood ;

}

void main(void)
{
    TQ3Status   myStatus;
    Rect        rBounds = { 50, 50, 350, 350 } ;
    Str255      title = "\pSpinning Box" ;
    FSSpec      theFileSpec ;
    OSErr       myErr ;
    GWorldPtr   myGWorld ;

    InitToolbox() ;

    if(MetafileFileSpecify( &theFileSpec )) {
        SetCursor(*(GetCursor(watchCursor)));
        gQuitFlag = false ;
        gMainWindow = NewCWindow(nil,&rBounds,title,false,noGrowDocProc,(WindowPtr)-1,true,0) ;
        SetWTitle( gMainWindow, theFileSpec.name );
        ShowWindow( gMainWindow ) ;
        SetPort( gMainWindow ) ;

        myErr = NewGWorld(  &myGWorld,
                            32,
                            &gMainWindow->portRect,
                            nil,
                            nil,
                            0L );

        SetCursor(&qd.arrow) ;

        if( myErr == noErr ) 
        {
            TQ3ViewerObject         myViewer ;
            short                   refNum ;


            myViewer = Q3ViewerNew ( (CGrafPtr)myGWorld, 
                                        &gMainWindow->portRect, 
                                        kQ3ViewerDefault ) ;

            if( myViewer != NULL )
            {
                myErr = FSpOpenDF ( &theFileSpec, fsRdPerm, &refNum ) ;
                if( myErr == noErr )
                {
                    PicHandle       myPict = NULL ;

                    Q3ViewerUseFile( myViewer, refNum ) ;
                    SetPort( (GrafPtr)myGWorld ) ;
                    Q3ViewerDraw( myViewer ) ;
                    myPict = Q3ViewerGetPict( myViewer ) ;

                    SetPort( gMainWindow ) ;
                    DrawPicture( myPict, &gMainWindow->portRect ) ;

                    while( !Button() )
                        ;
                }
            }
        }
    }
}
```

[Next](Document%20Revision%20History.md)[Previous](ViewerGWorldTest.md)

