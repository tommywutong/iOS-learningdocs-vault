---
title: Simon Tool
apple_id: DTS10000003
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Simon_Tool/Listings/FSET_c.html
archived_at: '2026-07-18T03:23:51.922968Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simon Tool](Simon%20Tool.md)


[Next](FVAL.c.md)[Previous](FSCR.c.md)

# FSET.c

```c
/************************************************************************************
                                P R O J E C T   I N F O
*************************************************************************************

    Project Name:   Simon
       File Name:   FSET.c

     Description:   Contains C code specific to the setup code resource
                    of a simple file transfer tool.  This is where any user 
                    interface is presented.

                        Copyright © 1992 Apple Computer, Inc.
                        All rights reserved.

*************************************************************************************
                            A U T H O R   I D E N T I T Y
*************************************************************************************

    Initials    Name
    --------    -----------------------------------------------
    CH          Craig Hotchkiss

*************************************************************************************
                            R E V I S I O N   H I S T O R Y
*************************************************************************************

    Change History (most recent first):

         <0>      5/8/92    CH      Creation date

************************************************************************************/



/************************************************************************************
                                STANDARD Mac HEADERS 
************************************************************************************/

#ifdef DUMPFILENAME
    #pragma load DUMPFILENAME
#else
    #define DoNotDump   1
    #include Load.c
#endif



/************************************************************************************
                                Other dependent HEADERs
************************************************************************************/

#ifndef __GLOBALS__
    #include "Globals.h"
#endif



/************************************************************************************
    Procedure:  FSET

    Purpose:    

    Inputs:     

    Outputs:
************************************************************************************/
pascal      long        FSET( FTHandle toolHandle, short message, 
                                long p1, long p2, long p3 )
{
    long            retValue = ftNotSupported;
    #if Debugging == 1
        #if DefaultDebug == 1
            Str255          tempString;
        #endif
    #endif


#pragma unused ( p1, p2, p3 )

    (**toolHandle).errCode = noErr;

    switch ( message ) {
        case ftSpreflightMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     Unused
                    p2:     Unused
                    p3:     long*               magicCookie - gets allocated here
                    returns:    Handle to the tool's user interface DITL
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FSET/ftSpreflightMsg received.;g" );
                #endif
            #endif

            retValue = nil;

            break;

        case ftSsetupMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     Unused
                    p2:     Unused
                    p3:     long*               magicCookie - just passed
                    returns:    nothing
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FSET/ftSsetupMsg received.;g" );
                #endif
            #endif

            break;

        case ftSitemMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     short*              itemHit
                    p2:     Unused
                    p3:     long*               magicCookie - just passed
                    returns:    nothing
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FSET/ftSitemMsg received.;g" );
                #endif
            #endif

            break;

        case ftSfilterMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     EventRecord*        theEvent
                    p2:     short*              itemHit
                    p3:     long*               magicCookie - just passed
                    returns:    Boolean indicating if event was handled.
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FSET/ftSfilterMsg received.;g" );
                #endif
            #endif

            break;

        case ftScleanupMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     Unused
                    p2:     Unused
                    p3:     long*               magicCookie - disposed of here.
                    returns:    nothing
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FSET/ftScleanupMsg received.;g" );
                #endif
            #endif

            break;

        default:
            #if Debugging == 1
                #if DefaultDebug == 1
                    DebugStr( "\p FSET - Did not understand message -- ;g" );
                    NumToString( (long) message, tempString );
                    DebugStr( tempString );
                #endif
            #endif

            break;
    } /* message switch */

    return ( retValue );
} /*FSET*/
```

[Next](FVAL.c.md)[Previous](FSCR.c.md)

