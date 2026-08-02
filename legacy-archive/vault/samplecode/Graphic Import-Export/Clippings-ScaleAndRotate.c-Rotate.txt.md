---
title: Graphic Import-Export
apple_id: DTS10001037
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Graphic_Import-Export/Listings/Clippings_ScaleAndRotate_c_Rotate_txt.html
archived_at: '2026-07-18T03:10:58.996614Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Graphic Import-Export](Graphic%20Import-Export.md)


[Next](Clippings-ScaleAndRotate.c-SetBoundsRect.txt.md)[Previous](Clippings-MultipleImages.clp-SetMatrix.txt.md)

# Clippings/ScaleAndRotate.c/Rotate.txt

```
    // set the contents of a matrix so that it performs no transformation
    SetIdentityMatrix( &matrix );

    // modify the contents of a matrix so that it defines a rotation operation
    // 90 degrees to the right - anchor at 0.0 top-left 
    RotateMatrix( &matrix,          // pointer to the matrix structure
                  Long2Fix( 90 ),   // the number of degrees of rotation NOTE: THIS IS A FIXED VALUE
                  0,                // x coordinate of anchor point
                  0 );              // y coordinate of anchor point


    // we need to return the top-left corner of the rotated image back to it's
    // origin, so add a translation value to a specified matrix 
    TranslateMatrix( &matrix,                           // pointer to the matrix structure
                     Long2Fix( naturalBounds.bottom ),  // deltaH - value added to the x coordinate NOTE: FIXED VALUES
                     0 );                               // deltaV - value added to the y coordinate 

    // set the transformation matrix to use for drawing an image             
    err = GraphicsImportSetMatrix( importer, &matrix );
```

[Next](Clippings-ScaleAndRotate.c-SetBoundsRect.txt.md)[Previous](Clippings-MultipleImages.clp-SetMatrix.txt.md)

