---
title: iso9660
apple_id: DTS10000429
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/iso9660/Listings/ErrorMsg_c.html
archived_at: '2026-07-18T03:29:46.786080Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iso9660](iso9660.md)


[Next](ErrorMsg.h.md)[Previous](DialogUtils.h.md)

# ErrorMsg.c

```c
/*
    File:       ErrorMsg.h

    Description:

    Author:     

    Copyright:  Copyright: © 1990-1999 by Apple Computer, Inc.
                all rights reserved.

    Disclaimer: You may incorporate this sample code into your applications without
                restriction, though the sample code has been provided "AS IS" and the
                responsibility for its operation is 100% yours.  However, what you are
                not permitted to do is to redistribute the source as "DSC Sample Code"
                after having made changes. If you're going to re-distribute the source,
                we require that you make it clear in the source that the code was
                descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
                6/24/99 Updated for Metrowerks Codewarror Pro 2.1(KG)

*/
#include <stdio.h>
#include <Dialogs.h>
#include <strings.h>

#include "HighSierra.h"
#include "BuildISO.h"
#include "DialogUtils.h"

#include "ErrorMsg.h"

/************************************************************************
 *
 *  Function:       ErrorMsg
 *
 *  Purpose:        tell user about some error
 *
 *  Returns:        nothing
 *
 *  Side Effects:   displays an error message
 *
 *  Description:    we assume that you are passing stuff in as if you
 *                  were using printf.  Put up a dialog that tells what
 *                  went wrong using your message.
 *
 ************************************************************************/
void
ErrorMsg(char *a, ...)
{
    char    errorString[255];

    sprintf(errorString, a);
    C2PStr(errorString);
    ParamText((StringPtr)errorString, NULL, NULL, NULL);
    Alert(DU_CenterALRT(129), 0L);
}
```

[Next](ErrorMsg.h.md)[Previous](DialogUtils.h.md)

