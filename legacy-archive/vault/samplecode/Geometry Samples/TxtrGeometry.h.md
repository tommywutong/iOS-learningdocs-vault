---
title: Geometry Samples
apple_id: DTS10000102
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Geometry_Samples/Listings/Txtr_Geometry_h.html
archived_at: '2026-07-18T03:10:46.053720Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Geometry Samples](Geometry%20Samples.md)


[Next](TxtrMath.h.md)[Previous](TxtrGeometry.c.md)

# Txtr_Geometry.h

```
/*
 *  Txtr_Geometry.h
 *
 *   03/22/95   RDD     Created.
 *   04/14/95   RDD     Added geometry and face uv attributes.
 *   09/20/95   RDD     Cleanup.
 */

#ifndef _HTxtr_Geometry
#define _HTxtr_Geometry


unsigned long GetLibraryMaxSimpleBox(
            void);

unsigned long GetLibraryMaxSimpleTriGrid(
            void);

TQ3GeometryObject NewLibraryBox(
            unsigned long       num);

TQ3GeometryObject NewLibraryTriGrid(
            unsigned long num);


/*
 * Geometry Library Constants
 */

/*
    Box:
        0   Plain
        1   Skewed

    TriGrid:
        0   Flat 5x5
        1   Torus
        2   Wavey Torus
        3   Splash
        4   Sphere
        5   Cone
        6   Pipe
        7   Steps
        8   Spring
 */
#define kGeometryLibrary_BoxMaxSimple           2
#define kGeometryLibrary_TriGridMaxSimple       9


#define kGeometryLibraryRange_Simple            0
#define kGeometryLibraryRange_UVGeoAttributes   100
#define kGeometryLibraryRange_UVFaceAttributes  200

#define kGeometryLibraryRange_Max               kGeometryLibraryRange_UVFaceAttributes
#define kGeometryLibraryRange                   100

#define mHasUVGeoAttributes(num)                ((num >= kGeometryLibraryRange_UVGeoAttributes)  &&                     \
                                                 (num <  kGeometryLibraryRange_UVGeoAttributes + kGeometryLibraryRange))
#define mHasUVFaceAttributes(num)               ((num >= kGeometryLibraryRange_UVFaceAttributes)  &&                    \
                                                 (num <  kGeometryLibraryRange_UVFaceAttributes + kGeometryLibraryRange))


#endif /* _HTxtr_Geometry */
```

[Next](TxtrMath.h.md)[Previous](TxtrGeometry.c.md)

