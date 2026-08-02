---
title: Simon Tool
apple_id: DTS10000003
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Simon_Tool/Listings/Globals_h.html
archived_at: '2026-07-18T03:23:52.049524Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simon Tool](Simon%20Tool.md)


[Next](Load.c.md)[Previous](FVAL.c.md)

# Globals.h

```
/************************************************************************************
                                P R O J E C T   I N F O
*************************************************************************************

    Project Name:   Simon
       File Name:   Globals.h

     Description:   Common typedefs and other definitions that are common to all
                    C code.  This does not mean globals in the A5 sense.

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



#ifndef __GLOBALS__
    #define __GLOBALS__



/************************************************************************************
                                    Constants
************************************************************************************/



/************************************************************************************
                                    Callback Types
************************************************************************************/
typedef pascal void (*ClientListProcPtr)();



/************************************************************************************
                                        Types
************************************************************************************/
typedef struct      ConfigGlobals { 
    short                   fToolVersion;
    Boolean                 fPersistentPackets;
    Boolean                 fOKToContinue;
} ConfigGlobalRec;
typedef ConfigGlobalRec *ConfigGlobalPtr;


typedef struct      SetupGlobals { 
    short                   fLastItemHit;
} SetupGlobalRec;
typedef SetupGlobalRec *SetupGlobalPtr;


typedef struct      DefaultStruct { 
    short                   fDefaultVersion;
    short                   fDefaultLanguage;
    Boolean                 fDefaultPersistentPackets;
    Boolean                 fDefaultOKToContinue;
} DefaultRec;
typedef DefaultRec *DefaultPtr;


    /* global structure for the tool */
typedef struct      ToolGlobals { 
    SetupGlobalRec          fSetupRecord;
    DefaultRec              fDefaultRecord;
    ConfigGlobalPtr         fConfigPtr;
} ToolGlobalRec;
typedef ToolGlobalRec *ToolGlobalPtr;




#ifdef __cplusplus
    extern "C" {
#endif



/************************************************************************************
                                Global PROTOTYPEs here
************************************************************************************/



#ifdef __cplusplus
    }
#endif



#endif __GLOBALS__
```

[Next](Load.c.md)[Previous](FVAL.c.md)

