---
title: Simon Tool
apple_id: DTS10000003
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Simon_Tool/Listings/FVAL_c.html
archived_at: '2026-07-18T03:23:51.995059Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simon Tool](Simon%20Tool.md)


[Next](Globals.h.md)[Previous](FSET.c.md)

# FVAL.c

```c
/************************************************************************************
                                P R O J E C T   I N F O
*************************************************************************************

    Project Name:   Simon
       File Name:   FVAL.c

     Description:   Contains C code specific to the validation code resource
                    of a simple file transfer tool.

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

#ifndef __VALIDATION__
    #include "Validation.h"
#endif



/************************************************************************************
************************************************************************************/

/************************************************************************************
    Procedure:  FVAL

    Purpose:    

    Inputs:     

    Outputs:
************************************************************************************/
pascal      long        FVAL( FTHandle toolHandle, short message, 
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
        case ftValidateMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     Unused
                    p2:     Unused
                    p3:     Unused
                    returns:    Boolean true if validation failed
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FVAL/ftValidateMsg received.;g" );
                #endif
            #endif

            if ( noErr == ( retValue = DoToolValidate( toolHandle ) ) ) {
                retValue = (long) false;
            } else {
                retValue = (long) true;
            }

            break;

        case ftDefaultMsg:
                /*      *********************
                        Parameter Definitions
                        *********************
                    p1:     Ptr                 configRecordPtr - gets changed
                    p2:     Boolean             allocate
                    p3:     short               procID - tools refNum
                    returns:    nothing
                */

            #if Debugging == 1
                #if ShowMessage == 1
                    DebugStr( "\p FVAL/ftValidateMsg received.;g" );
                #endif
            #endif

            if ( noErr == ( retValue = DoToolDefault(   (Ptr*) p1, 
                                                        (Boolean) p2, 
                                                        (short) p3 ) ) ) {
                retValue = (long) false;
            } else {
                retValue = (long) true;
            }

            break;

        default:
            #if Debugging == 1
                #if DefaultDebug == 1
                    DebugStr( "\p FVAL - Did not understand message -- ;g" );
                    NumToString( (long) message, tempString );
                    DebugStr( tempString );
                #endif
            #endif

            break;
    } /* message switch */

    return ( retValue );
} /*FVAL*/
```

[Next](Globals.h.md)[Previous](FSET.c.md)

