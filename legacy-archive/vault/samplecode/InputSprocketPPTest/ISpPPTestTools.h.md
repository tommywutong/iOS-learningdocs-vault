---
title: InputSprocketPPTest
apple_id: DTS10000054
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/InputSprocketPPTest/Listings/ISpPPTestTools_h.html
archived_at: '2026-07-18T03:12:56.999979Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [InputSprocketPPTest](InputSprocketPPTest.md)


[Next](ISpTestGlobals.cp.md)[Previous](ISpPPTestTools.cp.md)

# ISpPPTestTools.h

```c
/*
    File:       ISpPPTestTools.h

    Contains:   xxx put contents here xxx

    Version:    xxx put version here xxx

    Copyright:  © 1998 by Apple Computer, Inc., all rights reserved.

    File Ownership:

        DRI:                xxx put dri here xxx

        Other Contact:      xxx put other contact here xxx

        Technology:         xxx put technology here xxx

    Writers:

        (BWS)   Brent Schorsch

    Change History (most recent first):

         <2>     7/17/98    BWS     add header and change creator for SDK
*/

/*************************************************************************************

File:      ISpPPTestTools.h

Copyright © 1996, 1997, 1998 Apple Computer, Inc., All Rights Reserved


You may incorporate this sample code into your applications without
restriction, though the sample code has been provided "AS IS" and the
responsibility for its operation is 100% yours.  However, what you are
not permitted to do is to redistribute the source as "DSC Sample Code"
after having made changes. If you're going to re-distribute the source,
we require that you make it clear in the source that the code was
descended from Apple Sample Code, but that you've made changes.

*************************************************************************************/


#pragma once

#include <Types.h>

void UInt32ToHexBytes(UInt32 number, unsigned char *bytes);
void UInt32ToHexString(UInt32 number, Str255 theString);
void UnsignedWideToHexString(const UnsignedWide &number, Str255 theString);
void UInt32ToFourByte(UInt32 number, Str255 theString);
```

[Next](ISpTestGlobals.cp.md)[Previous](ISpPPTestTools.cp.md)

