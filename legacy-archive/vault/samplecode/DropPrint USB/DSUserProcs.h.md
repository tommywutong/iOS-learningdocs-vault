---
title: DropPrint USB
apple_id: DTS10000288
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/DropPrint_USB/Listings/DSUserProcs_h.html
archived_at: '2026-07-18T03:07:21.037986Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DropPrint USB](DropPrint%20USB.md)


[Next](DSUtils.c.md)[Previous](DSUserProcs.c.md)

# DSUserProcs.h

```c
/******************************************************************************
**
**  Project Name:   DropShell
**     File Name:   DSUserProcs.h
**
**   Description:   Header w/prototypes for specific AppleEvent handlers 
**                  used by the DropShell
**
*******************************************************************************
**                       A U T H O R   I D E N T I T Y
*******************************************************************************
**
**  Initials    Name
**  --------    -----------------------------------------------
**  LDR         Leonard Rosenthol
**  MTC         Marshall Clow
**  SCS         Stephan Somogyi
**
*******************************************************************************
**                      R E V I S I O N   H I S T O R Y
*******************************************************************************
**
**    Date      Time    Author  Description
**  --------    -----   ------  ---------------------------------------------
**  02/20/94            LDR     Modified Preflight & Postflight to take item count
**  01/25/92            LDR     Removed the use of const on the userDataHandle
**  12/09/91            LDR     Added SelectFile & UserGlobals prototypes
**  11/24/91            LDR     Added new routines & changed ones
**  10/29/91            SCS     Changes for THINK C 5
**  10/28/91            LDR     Officially renamed DropShell (from QuickShell)
**                              Added a bunch of comments for clarification
**  10/06/91    00:02   MTC     Converted to MPW C
**  04/09/91    00:02   LDR     Original Version
**
******************************************************************************/

#ifndef __DSUSERPROCS_H__
#define __DSUSERPROCS_H__

#include "DSGlobals.h"
#include "DSUtils.h"

pascal void InstallOtherEvents (void);

pascal void OpenApp (void);
pascal void QuitApp (void);
pascal Boolean PreFlightDocs ( Boolean opening, short itemCount, Handle *userDataHandle );
pascal void OpenDoc ( FSSpecPtr myFSSPtr,  Boolean opening, Handle userDataHandle );
pascal void PostFlightDocs ( Boolean opening, short itemCount, Handle userDataHandle );
pascal void SelectFile ( void );

pascal Boolean  InitUserGlobals(void);
pascal void DisposeUserGlobals(void);

#endif
```

[Next](DSUtils.c.md)[Previous](DSUserProcs.c.md)

