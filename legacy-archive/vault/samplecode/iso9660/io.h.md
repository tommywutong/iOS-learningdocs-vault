---
title: iso9660
apple_id: DTS10000429
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/iso9660/Listings/i_o_h.html
archived_at: '2026-07-18T03:29:47.032008Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iso9660](iso9660.md)


[Next](mydialog.c.md)[Previous](io.c.md)

# i_o.h

```
/*
    File:       i_o.h

    Description:

    Author:     

    Copyright:  Copyright: © 1990-1999 by Apple Computer, Inc.
                all rights reserved.

    Disclaimer: You may incorporate this sample code into your applications without
                restriction, though the sample code has been provided "AS IS" and the
                responsibility for its operation is 100% yours.  However, what you are
                not permitted to do is to redistribute the source as "DSC Sample Code"
                after having made changes. If you're going to re-distribute the source,
                we require that you make it clear in the source that the code was
                descended from Apple Sample Code, but that you've made changes.

    Change History (most recent first):
                6/24/99 Updated for Metrowerks Codewarror Pro 2.1(KG)

*/
OSErr isoOpen(StringPtr fn, short *RefNum);
OSErr isoRead(short referenceNumber, Ptr dest, long count, long offset);
OSErr isoWrite(short referenceNumber, Ptr buffer, long count, long offset);
OSErr ZeroDisk(short referenceNumber);
short GetDriveNumber(short vRefNum);
```

[Next](mydialog.c.md)[Previous](io.c.md)

