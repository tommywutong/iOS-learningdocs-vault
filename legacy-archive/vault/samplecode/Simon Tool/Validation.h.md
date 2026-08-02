---
title: Simon Tool
apple_id: DTS10000003
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Simon_Tool/Listings/Validation_h.html
archived_at: '2026-07-18T03:23:52.469175Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Simon Tool](Simon%20Tool.md)


[Next](Document%20Revision%20History.md)[Previous](Validation.c.md)

# Validation.h

```
/******************************************************************************
                            P R O J E C T   I N F O
*******************************************************************************

    Project Name:   Simon
       File Name:   Validation.h

     Description:   Header include for Validation.c

                        Copyright © 1992 Apple Computer, Inc.
                        All rights reserved.

*******************************************************************************
                        A U T H O R   I D E N T I T Y
*******************************************************************************

    Initials    Name
    --------    -----------------------------------------------
    CH          Craig Hotchkiss

*******************************************************************************
                        R E V I S I O N   H I S T O R Y
*******************************************************************************

    Change History (most recent first):

         <0>      5/8/92    CH      Creation date

******************************************************************************/



#ifndef __VALIDATION__
    #define __VALIDATION__



#ifdef __cplusplus
    extern "C" {
#endif



/************************************************************************************
*                               PROTOTYPEs
************************************************************************************/
OSErr           DoToolDefault( Ptr* configPtr, Boolean allocateIt, short toolRefNum );
OSErr           DoToolValidate( FTHandle toolHandle );



#ifdef __cplusplus
    }
#endif



#endif __VALIDATION__
```

[Next](Document%20Revision%20History.md)[Previous](Validation.c.md)

