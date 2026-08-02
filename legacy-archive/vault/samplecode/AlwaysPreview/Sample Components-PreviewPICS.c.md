---
title: AlwaysPreview
apple_id: DTS10000761
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/AlwaysPreview/Listings/Sample_Components_PreviewPICS_c.html
archived_at: '2026-07-18T03:00:59.464222Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AlwaysPreview](AlwaysPreview.md)


[Next](Sample%20Components-SampleCode.r.md)[Previous](Sample%20Components-PictMediaHandler.c.md)

# Sample Components/PreviewPICS.c

```c
/*
    File:       PreviewPICS.r

    Written by: Peter Hoddie

    Copyright:  © 1992 by Apple Computer, Inc., all rights reserved.

*/

#include <Aliases.h>
#include <Errors.h>
#include <QuickDraw.h>
#include <Resources.h>

#include <Components.h>
#include <QuickTimeComponents.h>

typedef struct {
    ComponentInstance   self;
} PICSPreviewRecord, **PICSPreviewGlobals;

pascal ComponentResult PICSPreviewDispatch( ComponentParameters *params, Handle store );
pascal ComponentResult PICSPreviewOpen(PICSPreviewGlobals store, ComponentInstance self);
pascal ComponentResult PICSPreviewClose(PICSPreviewGlobals store, ComponentInstance self);
pascal ComponentResult PICSPreviewCanDo( PICSPreviewGlobals store, short ftnNumber );
pascal ComponentResult PICSPreviewVersion( PICSPreviewGlobals store );
pascal ComponentResult PICSPreviewShowData(PICSPreviewGlobals store, OSType dataType, 
                Handle data, const Rect *inHere);

// entry point for all Component Manager requests
pascal ComponentResult PICSPreviewDispatch( ComponentParameters *params, Handle store )
{
    OSErr err = badComponentSelector;
    ComponentFunction componentProc = 0;

    switch (params->what) {
        case kComponentOpenSelect: componentProc = PICSPreviewOpen; break;
        case kComponentCloseSelect: componentProc = PICSPreviewClose; break;
        case kComponentCanDoSelect: componentProc = PICSPreviewCanDo; break;
        case kComponentVersionSelect: componentProc = PICSPreviewVersion; break;
        case kPreviewShowDataSelector: componentProc = PICSPreviewShowData; break;
    }

    if (componentProc)
        err = CallComponentFunctionWithStorage(store, params, componentProc);

    return err;
}

pascal ComponentResult PICSPreviewCanDo( PICSPreviewGlobals store, short ftnNumber )
{
    switch (ftnNumber) {
        case kComponentOpenSelect:
        case kComponentCloseSelect:
        case kComponentCanDoSelect:
        case kComponentVersionSelect:
        case kPreviewShowDataSelector:
            return true;
        default:
            return false;
    }
}

pascal ComponentResult PICSPreviewVersion( PICSPreviewGlobals store )
{
    return 0x00010001;
}

pascal ComponentResult PICSPreviewOpen(PICSPreviewGlobals store, ComponentInstance self)
{
    store = (PICSPreviewGlobals)NewHandle(sizeof(PICSPreviewRecord));
    if (!store) return MemError();
    SetComponentInstanceStorage(self, (Handle)store);
    (**store).self = self;

    return noErr;
}

pascal ComponentResult PICSPreviewClose(PICSPreviewGlobals store, ComponentInstance self)
{
    if (store) DisposeHandle((Handle)store);
    return noErr;
}

pascal ComponentResult PICSPreviewShowData(PICSPreviewGlobals store, OSType dataType, 
                Handle data, const Rect *inHere)
{
    OSErr err = noErr;
    short resRef = 0, saveRes = CurResFile();
    FSSpec theFile;
    Boolean whoCares;
    Handle thePict = nil;
    ComponentInstance ci;

    // because our Component has the pnotComponentNeedsNoCache flag set, we should
    //  only be called to display files.
    if (dataType != rAliasType)
        return paramErr;

    // open up the file to preview
    if (err = ResolveAlias(nil, (AliasHandle)data, &theFile, &whoCares)) goto bail;
    resRef = FSpOpenResFile(&theFile, fsRdPerm);
    if (err = ResError()) goto bail;

    // get the first PICT
    UseResFile(resRef);
    thePict = Get1IndResource('PICT', 1);
    if (!thePict) goto bail;

    // use the PICT Preview Component to display the preview
    if (ci = OpenDefaultComponent(ShowFilePreviewComponentType, 'PICT')) {
        PreviewShowData(ci, 'PICT', thePict, inHere);
        CloseComponent(ci);
    }

bail:
    if (resRef) CloseResFile(resRef);
    UseResFile(saveRes);
    return err;
}
```

[Next](Sample%20Components-SampleCode.r.md)[Previous](Sample%20Components-PictMediaHandler.c.md)

