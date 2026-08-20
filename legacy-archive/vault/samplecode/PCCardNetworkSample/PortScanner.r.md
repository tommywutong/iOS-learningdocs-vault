---
title: PCCardNetworkSample
apple_id: DTS10000258
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PCCardNetworkSample/Listings/PortScanner_r.html
archived_at: '2026-07-18T03:18:21.618403Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PCCardNetworkSample](PCCardNetworkSample.md)


[Next](ProjectDefines.h.md)[Previous](PortScanner.c.md)

# PortScanner.r

```c
/*
    File:       PortScanner.r

    Contains:   

    Written by:     

    Copyright:  Copyright © 1998-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                8/16/1999   Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1


*/
#define UseExtendedCFRGTemplate

#include <Types.r>
#include "CodeFragments.r"
#include "OpenTransport.r"
#include "ProjectDefines.h"

resource 'cfrg' (0)
{
  {
  extendedEntry
      {
          kPowerPC,
          kFullLib,
          kNoVersionNum,
          kNoVersionNum,
          kDefaultStackSize,
          kNoAppSubFolder,
          kIsLib,
          kOnDiskFlat,
          kZeroOffset,
          kWholeFork,
          kPortScannerName,
          kOTCFMClass,
          kOTPortScannerCFMTag,
          "",
          "",
          ""
      };
  };
};

resource 'vers' (1) {
    0x1,
    0x0,
    release,
    0x1,
    verUS,
    "1.0d1",
    "1.0, 1999 DTS Sample Code"
};
```

[Next](ProjectDefines.h.md)[Previous](PortScanner.c.md)

