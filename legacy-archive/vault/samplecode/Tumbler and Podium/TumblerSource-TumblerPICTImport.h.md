---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_PICTImport_h.html
archived_at: '2026-07-18T03:27:21.089370Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblerpodium.c.md)[Previous](TumblerSource-TumblerPICTImport.c.md)

# TumblerSource/Tumbler_PICTImport.h

```
// Tumbler_PICTImport.h
//
// picture import related function prototypes for the the Tumbler application
//
// Modification History
//
//  11/26/94        nick        added in stuff from symantec proto_helper app, add defines


#ifndef _Tumbler_PICTIMPORT_H_
#define _Tumbler_PICTIMPORT_H_

/* Tumbler_PICTImport.c */
TQ3Boolean TextureFromPICT(PicHandle pict, TQ3StoragePixmap *bmap);
TQ3Status AddTextureToDocument(DocumentPtr theDocument, TQ3StoragePixmap *textureImage);


#endif
```

[Next](TumblerSource-Tumblerpodium.c.md)[Previous](TumblerSource-TumblerPICTImport.c.md)

