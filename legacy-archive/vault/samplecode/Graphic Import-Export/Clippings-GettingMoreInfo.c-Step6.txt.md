---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_GettingMoreInfo_c_Step6_txt.html
archived_at: '2026-07-18T03:10:58.350433Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-GettingMoreInfo.c-Variables.txt.md)[Previous](Clippings-GettingMoreInfo.c-NewUserData.txt.md)

# Clippings/GettingMoreInfo.c/Step6.txt

```
    err = GraphicsImportGetDefaultMatrix( importer, &defaultMatrix );
    if( noErr == err )
        printf( "Image has default matrix (matrix type %d).\n", GetMatrixType( &defaultMatrix ) );

    err = GraphicsImportGetDefaultClip( importer, &defaultClip );
    if( noErr == err )
        printf( "Image has default clip.\n" );

    err = GraphicsImportGetDefaultGraphicsMode( importer, &defaultGraphicsMode, &defaultOpColor );
    if( noErr == err )
        printf( "Image has default graphics mode %d.\n", defaultGraphicsMode );

    err = GraphicsImportGetDefaultSourceRect( importer, &defaultSourceRect );
    if( noErr == err )
        printf( "Image has default rectangle (%d,%d,%d,%d).\n", 
                 defaultSourceRect.left, defaultSourceRect.top, 
                 defaultSourceRect.right, defaultSourceRect.bottom );

    err = GraphicsImportGetColorSyncProfile( importer, &colorSyncProfile );
    if( ( noErr == err ) && ( NULL != colorSyncProfile ) )
        printf( "Image has a ColorSync profile (%d bytes).\n", GetHandleSize( colorSyncProfile ) );
```

[Next](Clippings-GettingMoreInfo.c-Variables.txt.md)[Previous](Clippings-GettingMoreInfo.c-NewUserData.txt.md)

