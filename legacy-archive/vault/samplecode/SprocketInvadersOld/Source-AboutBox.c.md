---
title: SprocketInvadersOld
apple_id: DTS10000061
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/SprocketInvadersOld/Listings/Source_AboutBox_c.html
archived_at: '2026-07-18T03:25:24.845130Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SprocketInvadersOld](SprocketInvadersOld.md)


[Next](Source-AboutBox.h.md)[Previous](Resources-Art.r.md)

# Source/AboutBox.c

```c
//¥ ------------------------------------------------------------------------------------------  ¥
//¥
//¥ Copyright © 1996 Apple Computer, Inc., All Rights Reserved
//¥
//¥
//¥     You may incorporate this sample code into your applications without
//¥     restriction, though the sample code has been provided "AS IS" and the
//¥     responsibility for its operation is 100% yours.  However, what you are
//¥     not permitted to do is to redistribute the source as "DSC Sample Code"
//¥     after having made changes. If you're going to re-distribute the source,
//¥     we require that you make it clear in the source that the code was
//¥     descended from Apple Sample Code, but that you've made changes.
//¥
//¥     Authors:
//¥         Chris De Salvo
//¥
//¥ ------------------------------------------------------------------------------------------  ¥

//¥ ------------------------------  Includes

#include <Dialogs.h>

#include "AboutBox.h"
#include "SIResources.h"

//¥ ------------------------------  Private Definitions
//¥ ------------------------------  Private Types
//¥ ------------------------------  Private Variables
//¥ ------------------------------  Private Functions
//¥ ------------------------------  Public Variables

//¥ --------------------    AboutBox

void
AboutBox(void)
{
    Alert(kALRTAboutBox, nil);
}
```

[Next](Source-AboutBox.h.md)[Previous](Resources-Art.r.md)

