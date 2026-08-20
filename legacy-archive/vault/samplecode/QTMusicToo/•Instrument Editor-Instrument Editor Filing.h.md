---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_Instrument_Editor_Instrument_Editor_Filing_h.html
archived_at: '2026-07-18T03:21:06.470533Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Menus.c.md)[Previous](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Filing.c.md)

# •Instrument Editor/Instrument Editor Filing.h

```c
/*
 * file: Instrument Editor Filing.h
 *
 * started 12 January 1992 16:45
 * david van brink
 *
 */

/*--------------------------
    Inclusions
--------------------------*/

 #include <Files.h>

/*--------------------------
    Constants
--------------------------*/

#define kCreatorFileType 'InEd'
#define kDocumentFileType 'IEDo'
#define kDocumentResType 'IEDo'
#define kInstrumentListResType 'IELo'

/*--------------------------
    Prototypes
--------------------------*/

void OpenDoc(short n,short item, short ref);
short SaveDoc(short n,short item, short ref);
short SaveAsDoc(short n,short item, short ref);

void OpenDocSpec(FSSpec *fSpec);
```

[Next](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Menus.c.md)[Previous](%E2%80%A2Instrument%20Editor-Instrument%20Editor%20Filing.c.md)

