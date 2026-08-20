---
title: Plug-in  - Sample Renderer
apple_id: DTS10000120
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Plug-in__-_Sample_Renderer/Listings/Source_SR_ConfigData_c.html
archived_at: '2026-07-18T03:19:18.098086Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Plug-in  - Sample Renderer](Plug-in%20-%20Sample%20Renderer.md)


[Next](Source-SRLine.c.md)[Previous](Source-SRClipUtilities.c.md)

# Source/SR_ConfigData.c

```c
/******************************************************************************
 **                                                                          **
 **     Module:     SR_ConfigData.c                                          **
 **                                                                          **
 **                                                                          **
 **     Purpose:    Generic sample renderer routines                         **
 **                                                                          **
 **                                                                          **
 **                                                                          **
 **     Copyright (C) 1996-1997 Apple Computer, Inc.  All rights reserved.   **
 **                                                                          **
 **                                                                          **
 *****************************************************************************/
#include <assert.h>

#include <string.h>

#include "QD3D.h"

#include "SR.h"
#include "SR_ConfigData.h"

#define LOCAL_BUFFER_SIZE   sizeof(short)

/*===========================================================================*\
 *
 *  Routine:    SR_GetConfigurationData()
 *
 *  Comments:   
 *
\*===========================================================================*/

TQ3Status SR_GetConfigurationData(
    TQ3RendererObject           renderer, 
    unsigned char               *dataBuffer, 
    unsigned long               bufferSize,
    unsigned long               *actualDataSize,    
    void                        *rendererPrivate)
{
    UNUSED(renderer);

    *actualDataSize = LOCAL_BUFFER_SIZE;

    if (dataBuffer != NULL)  {
        if (bufferSize >= LOCAL_BUFFER_SIZE) {
            memcpy(
                (char *) dataBuffer, 
                (char *) &(((TSRPrivate *) rendererPrivate)->dummyConfigData),
                LOCAL_BUFFER_SIZE);
        } else {
            memcpy(
                (char *) dataBuffer,
                (char *) &(((TSRPrivate *) rendererPrivate)->dummyConfigData),
                bufferSize);
            *actualDataSize = bufferSize;
        }
    }

    return (kQ3Success);
}


/*===========================================================================*\
 *
 *  Routine:    SR_GetConfigurationData()
 *
 *  Comments:   
 *
\*===========================================================================*/

TQ3Status SR_SetConfigurationData(
    TQ3RendererObject           renderer, 
    unsigned char               *dataBuffer, 
    unsigned long               bufferSize, 
    void                        *rendererPrivate)
{
    UNUSED(renderer);

    if (dataBuffer != NULL && bufferSize == LOCAL_BUFFER_SIZE) {
        memcpy(
            (char *) &(((TSRPrivate *) rendererPrivate)->dummyConfigData),
            (char *) dataBuffer, 
            bufferSize);
        return (kQ3Success);
    }

    return (kQ3Failure);
}
```

[Next](Source-SRLine.c.md)[Previous](Source-SRClipUtilities.c.md)

