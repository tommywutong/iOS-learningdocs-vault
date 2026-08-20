---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_FilterExport_c_QTInsertChild_txt.html
archived_at: '2026-07-18T03:10:57.778426Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-FilterExport.c-QTNewAtomContainer.txt.md)[Previous](Clippings-FilterExport.c-QTGetEffectsList.txt.md)

# Clippings/FilterExport.c/QTInsertChild.txt

```
    err = QTInsertChild( videoFilter,               // specifies the atom container that contains the parent atom
                         kParentAtomIsContainer,    // specifies the parent atom within the atom container
                         kEffectSourceName,         // type of the new atom to be inserted
                         1,                         // id of new atom
                         0,                         // index -- 0 will insert at the end of the list
                         sizeof(aLong),             // data size
                         &aLong,                    // the data
                         NULL );                    // ptr to newly created atom -- NULL to ignore
```

[Next](Clippings-FilterExport.c-QTNewAtomContainer.txt.md)[Previous](Clippings-FilterExport.c-QTGetEffectsList.txt.md)

