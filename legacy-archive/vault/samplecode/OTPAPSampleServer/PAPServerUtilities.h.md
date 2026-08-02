---
title: OTPAPSampleServer
apple_id: DTS10000252
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/OTPAPSampleServer/Listings/PAPServerUtilities_h.html
archived_at: '2026-07-18T03:17:19.128207Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OTPAPSampleServer](OTPAPSampleServer.md)


[Next](SetServerStatusOption.c.md)[Previous](PAPServerUtilities.c.md)

# PAPServerUtilities.h

```c
/*

    file: PAPServerUtilities.h

    by:     Rich Kubota
            Developer Technical Support

*/

#ifndef __PAPSERVERUTILITIES__
#define __PAPSERVERUTILITIES__


#ifndef __CONDITIONALMACROS__
#include <ConditionalMacros.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif

#if PRAGMA_ALIGN_SUPPORTED
#pragma options align=mac68k
#endif

#if PRAGMA_IMPORT_SUPPORTED
#pragma import on
#endif

#include <Types.h>
#include <OSUtils.h>

#define kRootFolderDirID    2
#define kBootVolVRefNum     -1


// Prototypes
extern short            NumToolboxTraps(void);
extern TrapType         GetTrapType(short theTrap);
extern Boolean          TrapAvailable(short theTrap);
extern pascal   OSErr   HCreateMinimum(short vRefNum,
                               long dirID,
                               ConstStr255Param fileName);
extern OSErr            OpenTempFile(short *fRefNum);
extern OSErr            WriteDataToTempFile(short fRefNum, UInt8 *buffer, UInt32 len);
extern OSErr            CloseTempFile(short fRefNum);


#if PRAGMA_IMPORT_SUPPORTED
#pragma import off
#endif

#if PRAGMA_ALIGN_SUPPORTED
#pragma options align=reset
#endif

#ifdef __cplusplus
}
#endif

#endif /* __PAPSERVERUTILITIES__ */
```

[Next](SetServerStatusOption.c.md)[Previous](PAPServerUtilities.c.md)

