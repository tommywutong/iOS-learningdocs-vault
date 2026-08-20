---
title: PGPuam
apple_id: DTS10000259
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-07-22'
source_url: https://developer.apple.com/library/archive/samplecode/PGPuam/Listings/sources_FatCR_PPC_r.html
archived_at: '2026-07-18T03:18:29.842539Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PGPuam](PGPuam.md)


[Next](sources-LaunchApplication.c.md)[Previous](sources-clientUAMGlue.c.md)

# sources/FatCR PPC.r

```c

#include "MixedMode.r"

/*
Use the project ProcInfo.¹ to determine the correct value for the ProcInfo field below.

A single '$' means a hex value.  You can also use the C format of 0x... if you want.
Run ProcInfo.¹ to prove for yourself that a C routine (kCStackBased) that has no
arguments and returns void has a ProcInfo of $1 or 0x1.
Two dollar signs indicate a rez variable, as in $$Resource.  $$Resource tells rez 
to read the resource fork of a file and return, as a string, the data of a resource 
of a certain type and ID.


Use type 'MWCW' as 'fdes'; if you want a fat resource.
*/


type 'uamc' as 'sdes';

resource 'uamc'  (0, "PGP UAM Code resource",sysheap) {
    $0,                                                 // 68K ProcInfo
    $00E0,                                              // PowerPC ProcInfo
    "",                                                 // Specify filename, type, and ID of resource
                                                        //   containing 68k code
    $$Resource("PGP client UAM-PPC", 'uamc', 0)         // Specify filename, type, and ID of resource
                                                        //   containing a pef container
};
```

[Next](sources-LaunchApplication.c.md)[Previous](sources-clientUAMGlue.c.md)

