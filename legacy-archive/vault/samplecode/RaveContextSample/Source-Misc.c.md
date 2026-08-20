---
title: RaveContextSample
apple_id: DTS10000156
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RaveContextSample/Listings/Source_Misc_c.html
archived_at: '2026-07-18T03:21:50.994452Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RaveContextSample](RaveContextSample.md)


[Next](Source-Process.c.md)[Previous](Source-Menus.c.md)

# Source/Misc.c

```c
/****************************/
/*      MISC ROUTINES       */
/* By Brian Greenstone      */
/****************************/


/***************/
/* EXTERNALS   */
/***************/
#include <Events.h>
#include <Dialogs.h>
#include <Processes.h>
#include <NumberFormatting.h>
#include <math.h>

#include <QD3D.h>
#include <QD3DErrors.h>

#include "myglobals.h"
#include "misc.h"

extern  EventRecord gTheEvent;


/****************************/
/*    CONSTANTS             */
/****************************/

#define     ERROR_ALERT_ID      401

/**********************/
/*     VARIABLES      */
/**********************/

unsigned long seed0 = 0, seed1 = 0, seed2 = 0;
unsigned long seed0_alt = 0, seed1_alt = 0, seed2_alt = 0;


/****************** DO SYSTEM ERROR ***************/

void ShowSystemErr(long err)
{
Str255      numStr;

    NumToString(err, numStr);
    DoAlert (numStr);
    CleanQuit();
}

/*********************** DO ALERT *******************/

void DoAlert(Str255 s)
{
    ParamText(s,NIL_STRING,NIL_STRING,NIL_STRING);
    NoteAlert(ERROR_ALERT_ID,nil);
}

/*********************** DO FATAL ALERT *******************/

void DoFatalAlert(Str255 s)
{
    ParamText(s,NIL_STRING,NIL_STRING,NIL_STRING);
    NoteAlert(ERROR_ALERT_ID,nil);
    CleanQuit();
}

/************ CLEAN QUIT ***************/

void CleanQuit(void)
{
    ExitToShell();
}




/******************** MY RANDOM LONG **********************/
//
// My own random number generator that returns a LONG
//
// NOTE: call this instead of MyRandomShort if the value is going to be
//      masked or if it just doesnt matter since this version is quicker
//      without the 0xffff at the end.
//

static unsigned long MyRandomLong(void)
{
  return seed2 ^= (((seed1 ^= (seed2>>5)*1568397607UL)>>7)+
                   (seed0 = (seed0+1)*3141592621UL))*2435386481UL;
}


/************** RANDOM FLOAT ********************/
//
// returns a random float between 0 and 1
//

float RandomFloat(void)
{
unsigned long   r;
float   f;

    r = MyRandomLong() & 0xfff;     
    if (r == 0)
        return(0);

    f = (float)r;                           // convert to float
    f = f / (float)0xfff;                   // get # between 0..1
    return(f);
} 
```

[Next](Source-Process.c.md)[Previous](Source-Menus.c.md)

