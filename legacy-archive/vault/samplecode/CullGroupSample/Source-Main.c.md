---
title: CullGroupSample
apple_id: DTS10000133
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CullGroupSample/Listings/Source_Main_c.html
archived_at: '2026-07-18T03:05:31.777183Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CullGroupSample](CullGroupSample.md)


[Next](Source-Menus.c.md)[Previous](Source-Events.c.md)

# Source/Main.c

```c
/****************************/
/*       CULL TEST          */
/* By Brian Greenstone      */
/****************************/


/****************************/
/*    EXTERNALS             */
/****************************/
#include <Fonts.h>
#include <Resources.h>

#include <Rave.h>

#include "myglobals.h"
#include "qd3d_support.h"
#include "objects.h"
#include "mymenus.h"
#include "mywindows.h"
#include "myevents.h"
#include "main.h"
#include "misc.h"
#include "3dmf.h"
#include "process.h"

extern  QD3DSetupOutputType     gModelViewInfo;

/****************************/
/*    PROTOTYPES            */
/****************************/

static  void ToolBoxInit(void);


/****************************/
/*    CONSTANTS             */
/****************************/


/****************************/
/*    VARIABLES             */
/****************************/


short       gMainAppRezFile;



/*****************/
/* TOOLBOX INIT  */
/*****************/

static void ToolBoxInit(void)
{
TQ3Status   myStatus;

    MaxApplZone();
    InitGraf(&qd.thePort);
    FlushEvents ( everyEvent, REMOVE_ALL_EVENTS);
    InitFonts();
    InitWindows();
    InitDialogs(NIL_POINTER);
    InitCursor();
    InitMenus();
    TEInit();

    gMainAppRezFile = CurResFile();


            /* SEE IF QD3D AVAILABLE */

    if((void *)Q3Initialize == (void *)kUnresolvedCFragSymbolAddress)
        DoFatalAlert("\pQuickDraw 3D version 1.5 or better is required to run this application!");

    myStatus = Q3Initialize();
    if ( myStatus == kQ3Failure )
        DoFatalAlert("\pQ3Initialize returned failure.");               
}



/*****************/
/* TOOLBOX EXIT  */
/*****************/

static void ToolBoxExit(void)
{
TQ3Status   myStatus;

    myStatus = Q3Exit();
    if ( myStatus == kQ3Failure )
        DoFatalAlert("\pQ3Exit returned failure.");             
}


/************************************************************/
/******************** PROGRAM MAIN ENTRY  *******************/
/************************************************************/


void main(void)
{
    ToolBoxInit();
    InitMenuBar();

                /* INIT STUFF */

    InitObjectManager();
    InitTest();                             // create QD3D window environment   

                /* PROGRAM MAIN LOOP */

    while (true)
        HandleEvents();

    ToolBoxExit();
}
```

[Next](Source-Menus.c.md)[Previous](Source-Events.c.md)

