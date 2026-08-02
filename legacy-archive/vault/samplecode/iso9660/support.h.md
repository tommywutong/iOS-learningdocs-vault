---
title: iso9660
apple_id: DTS10000429
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/iso9660/Listings/support_h.html
archived_at: '2026-07-18T03:29:47.525467Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iso9660](iso9660.md)


[Next](Document%20Revision%20History.md)[Previous](support.c.md)

# support.h

```
/*
    File:       support.h

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
void pStrCopy(StringPtr p1, StringPtr p2);
short pStrLen(StringPtr p);
short CreateISOName(char *dest, StringPtr src);
Boolean HFSFile(StringPtr fn, short *vRefNum);
void ClearOut(Ptr buffer, short count);
void SpaceOut(Ptr buffer, short count);
void CharCopy(char *dest, char *src, short length);
long NormalizeLong(long incoming);
short NormalizeWord(short incoming);
void NormalizeVolumeName(char *someString);
OSErr GetFileInfo(StringPtr name, short vRefNum, long *rsrcLength, long *dataLength, OSType *fType, OSType *fCreator, short *flags);
OSErr GetFinderFlags(StringPtr name, short vRefNum, short *flags);
```

[Next](Document%20Revision%20History.md)[Previous](support.c.md)

