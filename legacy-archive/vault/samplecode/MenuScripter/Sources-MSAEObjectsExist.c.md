---
title: MenuScripter
apple_id: DTS10000668
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MenuScripter/Listings/Sources_MSAEObjectsExist_c.html
archived_at: '2026-07-18T03:14:38.071876Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MenuScripter](MenuScripter.md)


[Next](Sources-MSAEObjectsExist.h.md)[Previous](Sources-MSAEMove.h.md)

# Sources/MSAEObjectsExist.c

```c
// MSAEObjectsExist.c
//
// Original version by Jon Lansdell and Nigel Humphreys.
// 4.0 and 3.1 updates by Greg Sutton.
// ©Apple Computer Inc 1996, all rights reserved.

/*  
    Changes for 4.0

    27-Feb-96 : GS : Added call to HandleGetData() to see if properties etc. exist
*/

#include "MSAEObjectsExist.h"

#include "MSAEUtils.h"
#include "MSAEGetData.h"


#pragma segment AppleEvent


// -----------------------------------------------------------------------
//  Name:       DoObjectsExist
//  Purpose:    Handles the kAEDoObjectsExist AppleEvent. Basically just
//              tries to resolve the object to see if it exists.
// -----------------------------------------------------------------------

pascal OSErr DoObjectsExist(const AppleEvent    *theAppleEvent,
                                    AppleEvent  *reply, 
                                    long        handlerRefCon)
{
#ifdef __MWERKS__
    #pragma unused (handlerRefCon)
#endif

    AEDesc          directObject = {typeNull, NULL},
                    directDesc = {typeNull, NULL},
                    replyDesc = {typeNull, NULL},
                    aDesc = {typeNull, NULL};
    long            itemCount;
    Boolean         exists;
    OSErr           existsErr,
                    err;

    err = AEGetParamDesc(theAppleEvent, keyDirectObject, typeWildCard, &directObject);

    err = GotRequiredParams(theAppleEvent);
    if (noErr != err) goto done;

    if (typeNull == directObject.descriptorType)
        exists = true;      // Yes, our application does exist?????
    else
    {
        existsErr = AEResolve(&directObject, kAEIDoMinimum, &directDesc);

        if (noErr == existsErr)
        {
            switch ( directDesc.descriptorType )
            {
                case typeAEList:
                case typeAERecord:
                    err = AECountItems( &directDesc, &itemCount );  // If not empty then
                    if (noErr != err) goto done;                    //  it exists

                    exists = ( itemCount > 0 );
                    break;

                default:
                    err = HandleGetData( &directDesc, typeWildCard, &aDesc );
                    exists = ( noErr == err );
            }
        }                                       
        else
            exists = false;
    }

    err = AECreateDesc(typeBoolean, (Ptr)&exists, sizeof(exists), &replyDesc);
    if (noErr != err) goto done;

    err = AddResultToReply(&replyDesc, reply, err);

done:
    (void)AEDisposeDesc( &directObject );
    (void)AEDisposeDesc( &directDesc );
    (void)AEDisposeDesc( &replyDesc );
    (void)AEDisposeDesc( &aDesc );

    return err;
} // DoObjectsExist
```

[Next](Sources-MSAEObjectsExist.h.md)[Previous](Sources-MSAEMove.h.md)

