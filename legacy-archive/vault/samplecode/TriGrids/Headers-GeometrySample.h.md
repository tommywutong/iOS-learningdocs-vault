---
title: TriGrids
apple_id: DTS10000105
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/TriGrids/Listings/Headers_GeometrySample_h.html
archived_at: '2026-07-18T03:27:19.422581Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TriGrids](TriGrids.md)


[Next](Headers-MathUtilities.h.md)[Previous](TriGrids.md)

# Headers/GeometrySample.h

```
/*
    GeometrySample.h

    © 1995 Apple Computer, Inc.

    03/22/95    rdd     initial version
    04/14/95    rdd     added geometry and face uv attributes
*/

unsigned long GetLibraryMaxSimpleTriGrid(void);
TQ3GeometryObject NewLibraryTriGrid(unsigned long num);


/*
 * Geometry Library Constants
 */

/*
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
/* EOF */
```

[Next](Headers-MathUtilities.h.md)[Previous](TriGrids.md)

