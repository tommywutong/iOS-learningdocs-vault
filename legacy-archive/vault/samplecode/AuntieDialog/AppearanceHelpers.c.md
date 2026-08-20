---
title: AuntieDialog
apple_id: DTS10000556
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/AuntieDialog/Listings/AppearanceHelpers_c.html
archived_at: '2026-07-18T03:01:33.438701Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AuntieDialog](AuntieDialog.md)


[Next](AppearanceHelpers.h.md)[Previous](AuntieDialog.md)

# AppearanceHelpers.c

```c
    //
    //  LEGAL NOTICE
    //  ============
    //
    //  You may incorporate this sample code into your applications
    //  without restriction. This sample code has been provided "AS
    //  IS" and the responsibility for its operation is 100% yours.
    //  You are not permitted to redistribute the source as "Apple
    //  sample code" after having made changes. If you're going to
    //  re-distribute the source, we require that you make it clear
    //  in the source that the code was descended from Apple sample
    //  code, but that you've made changes.
    //

#include "AppearanceHelpers.h"
#include "Assertions.h"

#ifdef __MWERKS__

// includes for MetroWerks CodeWarrior

#include <ControlDefinitions.h>

#endif

#define MIN( a, b )     ( ( (a) < (b) ) ? (a) : (b) )

pascal OSStatus SetProgressIndicatorState( ControlHandle control, Boolean isDeterminate )
{
    OSStatus    err;
    Boolean     state;

    if ( control == nil )
        return paramErr;

    state = !isDeterminate; 
    err = SetControlData( control, 0, kControlProgressBarIndeterminateTag, sizeof( state ),
            (Ptr)&state );

    return err;
}

pascal OSStatus SetPushButtonDefaultState( ControlHandle control, Boolean isDefault )
{
    OSStatus    err;

    if ( control == nil )
        return paramErr;

    err = SetControlData( control, 0, kControlPushButtonDefaultTag, sizeof( isDefault ),
            (Ptr)&isDefault );

    return err;
}

pascal OSStatus GetListBoxListHandle( ControlHandle control, ListHandle* list )
{
    Size        actualSize;
    OSStatus    err;

    if ( control == nil )
        return paramErr;

    if ( list == nil )
        return paramErr;

    err = GetControlData( control, 0, kControlListBoxListHandleTag, sizeof( ListHandle ),
             (Ptr)list, &actualSize );

    return err;
}
```

[Next](AppearanceHelpers.h.md)[Previous](AuntieDialog.md)

