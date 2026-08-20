---
title: SampleDS
apple_id: DTS10000657
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: ImageCaptureCore
published: '2003-07-10'
source_url: https://developer.apple.com/library/archive/samplecode/SampleDS/Listings/TWAIN_Helper_Glue_TWSystem_c.html
archived_at: '2026-07-18T03:23:00.306095Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SampleDS](SampleDS.md)


[Next](TWAIN%20Helper%20Glue-TWSystem.h.md)[Previous](TWAIN%20Helper%20Glue-TWGlue.h.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html%23//apple_ref/doc/uid/TP40006079](https://developer.apple.com/library/mac/#documentation/GraphicsImaging/Reference/ImageCaptureDeviceModulesReference/index.html#//apple_ref/doc/uid/TP40006079)

# TWAIN Helper Glue/TWSystem.c

```c
// ===========================================================================
//  TWSystem.c          TWAIN 1.9               ©1991-2001 TWAIN Working Group
// ===========================================================================
//
//

#include "TWSystem.h"
#include "TWDefs.h"

static TW_INT16     HasColor=-1;

// ---------------------------------------------------------------------------
//  ¥ pstrcopy                                                
// ---------------------------------------------------------------------------
//  

TW_INT16 pstrcopy ( pTW_UINT8 destin, pTW_UINT8 source )
{
    BlockMoveData(source, destin, source[0] + 1);

    return(OKAY);
}


// ---------------------------------------------------------------------------
//  ¥ pstrcmp                                                 
// ---------------------------------------------------------------------------
//  

TW_INT16 pstrcmp ( pTW_UINT8 string1, pTW_UINT8 string2 )
{
    TW_INT16 result = RelString(string1, string2, true, true);
    return (result == 0 ? true : false);
}


// ---------------------------------------------------------------------------
//  ¥ pstrcat                                                 
// ---------------------------------------------------------------------------
//  

TW_INT16 pstrcat ( pTW_UINT8 destin, pTW_UINT8 source )
{
    TW_INT16        i;

    for (i=0;i<source[0];i++) 
        destin[destin[0]+i+1]=source[i+1];

    destin[0]=destin[0]+source[0];

    return(OKAY);
}



// ---------------------------------------------------------------------------
//  HasColorQuickDraw                                                 
// ---------------------------------------------------------------------------
//  

TW_INT16 HasColorQuickDraw(void)
{
    SInt32 response = 0;

    OSErr err = Gestalt ( gestaltQuickdrawFeatures, &response );

    if ( err == noErr && ( response >= gestalt32BitQD ) )
        HasColor = TRUE;

    return HasColor;

    /*  ***Carbon*** SysEnvirons is obsolete.  You should be using Gestalt.

    also, Color QuickDraw is always available with Mac OS 8 and later.  */

}


// ---------------------------------------------------------------------------
//  ¥ StandardCautionAlert
// ---------------------------------------------------------------------------
//  

SInt16 StandardCautionAlert ( ConstStringPtr error, ConstStringPtr explanation )
{
    AlertStdAlertParamRec alertParams = { false, 
                                          false, 
                                          nil, 
                                          (ConstStringPtr)kAlertDefaultOKText,
                                          (ConstStringPtr)kAlertDefaultCancelText,
                                          nil,
                                          kAlertStdAlertOKButton,
                                          kAlertStdAlertCancelButton, 
                                          kWindowDefaultPosition };
    SInt16 outItemHit = 0;
    OSErr err = StandardAlert ( kAlertCautionAlert, error, explanation, &alertParams, &outItemHit );
    check_noerr ( err );

    return outItemHit;
}
```

[Next](TWAIN%20Helper%20Glue-TWSystem.h.md)[Previous](TWAIN%20Helper%20Glue-TWGlue.h.md)

