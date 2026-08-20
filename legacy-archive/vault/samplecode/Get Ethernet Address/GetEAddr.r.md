---
title: Get Ethernet Address
apple_id: DTS10000232
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Get_Ethernet_Address/Listings/GetEAddr_r.html
archived_at: '2026-07-18T03:10:49.854004Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Get Ethernet Address](Get%20Ethernet%20Address.md)


[Next](Document%20Revision%20History.md)[Previous](GetEAddr.c.md)

# GetEAddr.r

```c
/*
    File: GetEAddr.r
    Rich Kubota
    DTS
    June 2, 1992

    Resource file for sample program to demonstrate the use of the LAP Manager to determine the
    current AppleTalk connection device based on the ADEV resource ID.  Also 
    demonstrates a call to EGetInfo to obtain the burned in Ethernet address
    whether on the card or built-in on the Quadra's.  This program assumes the 
    use of the Apple Ethernet phase 1 0r 2 driver ADEV's.

*/

#include "Types.r"

resource 'ALRT' (1000) {
    {40, 40, 203, 278},
    1000,
    {   /* array: 4 elements */
        /* [1] */
        OK, visible, sound1,
        /* [2] */
        OK, visible, sound1,
        /* [3] */
        OK, visible, sound1,
        /* [4] */
        OK, visible, sound1
    }
};

resource 'ALRT' (1001) {
    {40, 40, 117, 335},
    1001,
    {   /* array: 4 elements */
        /* [1] */
        OK, visible, sound1,
        /* [2] */
        OK, visible, sound1,
        /* [3] */
        OK, visible, sound1,
        /* [4] */
        OK, visible, sound1
    }
};

resource 'DLOG' (1000) {
    {40, 40, 240, 280},
    dBoxProc,
    visible,
    goAway,
    0x0,
    1000,
    ""
};

resource 'DITL' (1000) {
    {   /* array DITLarray: 2 elements */
        /* [1] */
        {124, 92, 144, 150},
        Button {
            enabled,
            "OK"
        },
        /* [2] */
        {7, 7, 112, 232},
        StaticText {
            disabled,
            "^0"
        }
    }
};

resource 'DITL' (1001) {
    {   /* array DITLarray: 3 elements */
        /* [1] */
        {44, 194, 65, 278},
        Button {
            enabled,
            "Done"
        },
        /* [2] */
        {6, 9, 24, 146},
        StaticText {
            disabled,
            "Ethernet Address is:"
        },
        /* [3] */
        {6, 149, 24, 286},
        StaticText {
            disabled,
            "^0"
        }
    }
};
```

[Next](Document%20Revision%20History.md)[Previous](GetEAddr.c.md)

