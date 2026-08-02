---
title: MoofWarsOld
apple_id: DTS10000057
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-14'
source_url: https://developer.apple.com/library/archive/samplecode/MoofWarsOld/Listings/MoofWars_GridTilesFormat_h.html
archived_at: '2026-07-18T03:15:02.614427Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MoofWarsOld](MoofWarsOld.md)


[Next](MoofWars-MoofWars.cp.md)[Previous](MoofWars-AppConditionals.h.md)

# MoofWars/GridTilesFormat.h

```
/*
    File:       GridTilesFormat.h

    Contains:   This file describes the formats of a TileCollection and a TileGrid.  We provide 
                them both here so that our applications that build compiled files can also access
                the resource format.

    Written by: Timothy Carroll 

    Copyright:  Copyright © 1996-1999 by Apple Computer, Inc., All Rights Reserved.

                You may incorporate this Apple sample source code into your program(s) without
                restriction. This Apple sample source code has been provided "AS IS" and the
                responsibility for its operation is yours. You are not permitted to redistribute
                this Apple sample source code as "Apple sample source code" after having made
                changes. If you're going to re-distribute the source, we require that you make
                it clear in the source that the code was descended from Apple sample source
                code, but that you've made changes.

    Change History (most recent first):
                7/2/1999    Karl Groethe    Updated for Metrowerks Codewarror Pro 2.1

                8/15/96     Timothy Carroll Initial Release


*/


/*************************************************************************************
Resource Data Structures
*************************************************************************************/

typedef struct TileCollectionResHeader TileCollectionResHeader;
const UInt32 TileCollectionResType = 'TILE';

struct TileCollectionResHeader
{
    UInt32 version;
    SInt16 depth;
    UInt16 flags;
    UInt32 numTiles;

    // Followed by 1k per tile in 32x32x8 bit format.
};


typedef UInt16 CellGridType;

typedef struct TileGridResHeader TileGridResHeader;
const UInt32 TileGridResType = 'GRID';

struct TileGridResHeader
{
    UInt32 version;
    UInt16 flags;
    SInt16 tileResID;
    UInt32 width;
    UInt32 height;
    UInt32 defaultTile;

    // followed by width x height x CellGridType for tile information in row x column format.
};
```

[Next](MoofWars-MoofWars.cp.md)[Previous](MoofWars-AppConditionals.h.md)

