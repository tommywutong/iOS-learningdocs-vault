---
title: QTMusicToo
apple_id: DTS10000915
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-19'
source_url: https://developer.apple.com/library/archive/samplecode/QTMusicToo/Listings/_QTMusic_Sample_Sequencer_SequencerTest_Filing_h.html
archived_at: '2026-07-18T03:21:07.862912Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTMusicToo](QTMusicToo.md)


[Next](%E2%80%A2QTMusic%20Sample%20Sequencer-SequencerTest%20Movies.h.md)[Previous](%E2%80%A2QTMusic%20Sample%20Sequencer-SequencerTest%20Filing.c.md)

# •QTMusic Sample Sequencer/SequencerTest Filing.h

```c
/*
 * file: SequencerTest Filing.h
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

#define kCreatorFileType 'STDo'
#define kDocumentFileType 'Stdo'
#define kDocumentResType 'Stdo'

/*--------------------------
    Prototypes
--------------------------*/

void OpenDoc(short n,short item, short ref);
short SaveDoc(short n,short item, short ref);
short SaveAsDoc(short n,short item, short ref);

void OpenDocSpec(FSSpec *fSpec);
```

[Next](%E2%80%A2QTMusic%20Sample%20Sequencer-SequencerTest%20Movies.h.md)[Previous](%E2%80%A2QTMusic%20Sample%20Sequencer-SequencerTest%20Filing.c.md)

