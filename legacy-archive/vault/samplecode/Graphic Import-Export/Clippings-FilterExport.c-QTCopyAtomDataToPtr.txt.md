---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_FilterExport_c_QTCopyAtomDataToPtr_txt.html
archived_at: '2026-07-18T03:10:57.573470Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-FilterExport.c-QTFindChildByIndex.txt.md)[Previous](Clippings-FilterExport.c-OpenADefaultComponent.txt.md)

# Clippings/FilterExport.c/QTCopyAtomDataToPtr.txt

```
    err = QTCopyAtomDataToPtr( videoFilter,         // atom container containing the leaf atom
                               effectTypeAtom,      // leaf atom who's data will be copied
                               false,               // copy fewer bytes than the number of bytes specified by the size parameter?
                               sizeof(effectType),  // size
                               &effectType,         // target buffer pointer
                               NULL );              // returned actual size; NULL to ignore
```

[Next](Clippings-FilterExport.c-QTFindChildByIndex.txt.md)[Previous](Clippings-FilterExport.c-OpenADefaultComponent.txt.md)

