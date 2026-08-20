---
title: MoreFinderEvents
apple_id: DTS10000206
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoreFinderEvents/Listings/MoreFinderEvents_h.html
archived_at: '2026-07-18T03:15:15.278787Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoreFinderEvents](MoreFinderEvents.md)


[Next](TestFinderEvents.c.md)[Previous](MoreFinderEvents.cp.md)

# MoreFinderEvents.h

```
    //
    //  Complaints and kudos to:
    //
    //      Pete Gontier
    //      Apple Macintosh Developer Technical Support
    //      <gurgle@apple.com>
    //

#pragma once

#ifndef __ALIASES__
#   include <Aliases.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif

pascal OSErr MFE_Reveal             (const AliasRecord **);
pascal OSErr MFE_PutAway            (const AliasRecord **);
pascal OSErr MFE_OpenGetInfo        (const AliasRecord **);
pascal OSErr MFE_OpenSharing        (const AliasRecord **);
pascal OSErr MFE_CloseWindow        (const AliasRecord **);
pascal OSErr MFE_CloseGetInfo       (const AliasRecord **);
pascal OSErr MFE_CloseSharing       (const AliasRecord **);
pascal OSErr MFE_MakeAlias          (const AliasRecord **);
pascal OSErr MFE_Duplicate          (const AliasRecord **);
pascal OSErr MFE_OpenSelection      (const AliasRecord **);
pascal OSErr MFE_PrintSelection     (const AliasRecord **);
pascal OSErr MFE_PageSetup          (const AliasRecord **);
pascal OSErr MFE_PrintWindow        (const AliasRecord **);

pascal OSErr MFE_Move               (   const AliasRecord **aliasToDrag,
                                        const AliasRecord **destAlias       );
pascal OSErr MFE_Copy               (   const AliasRecord **aliasToDrag,
                                        const AliasRecord **destAlias       );

pascal OSErr MFE_UnmountVolume      (short vRefNum);

pascal OSErr MFE_ShowClipboard      (void);
pascal OSErr MFE_HideClipboard      (void);
pascal OSErr MFE_ShowAbout          (void);
pascal OSErr MFE_HideAbout          (void);
pascal OSErr MFE_Sleep              (void);
pascal OSErr MFE_Restart            (void);
pascal OSErr MFE_ShutDown           (void);
pascal OSErr MFE_EmptyTrash         (void);

#ifdef __cplusplus
}
#endif
```

[Next](TestFinderEvents.c.md)[Previous](MoreFinderEvents.cp.md)

