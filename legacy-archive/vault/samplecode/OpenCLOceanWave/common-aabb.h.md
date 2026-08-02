---
title: OpenCL_OceanWave
apple_id: DTS40009447
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenCL
published: '2011-04-13'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_OceanWave/Listings/common_aabb_h.html
archived_at: '2026-07-18T03:17:44.109086Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [OpenCL_OceanWave](OpenCLOceanWave.md)


[Next](common-bufferobject.cpp.md)[Previous](main.cpp.md)

Current information on this Developer Library topic can be found here:

- [Performance > Multiprocessing](https://developer.apple.com/referencelibrary/Performance/idxMultiprocessing-date.html)

# common/aabb.h

```c
// Version:    <1.0>
//
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Inc. ("Apple")
//             in consideration of your agreement to the following terms, and your use,
//             installation, modification or redistribution of this Apple software
//             constitutes acceptance of these terms.  If you do not agree with these
//             terms, please do not use, install, modify or redistribute this Apple
//             software.
//
//             In consideration of your agreement to abide by the following terms, and
//             subject to these terms, Apple grants you a personal, non - exclusive
//             license, under Apple's copyrights in this original Apple software ( the
//             "Apple Software" ), to use, reproduce, modify and redistribute the Apple
//             Software, with or without modifications, in source and / or binary forms;
//             provided that if you redistribute the Apple Software in its entirety and
//             without modifications, you must retain this notice and the following text
//             and disclaimers in all such redistributions of the Apple Software. Neither
//             the name, trademarks, service marks or logos of Apple Inc. may be used to
//             endorse or promote products derived from the Apple Software without specific
//             prior written permission from Apple.  Except as expressly stated in this
//             notice, no other rights or licenses, express or implied, are granted by
//             Apple herein, including but not limited to any patent rights that may be
//             infringed by your derivative works or by other works in which the Apple
//             Software may be incorporated.
//
//             The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
//             WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
//             WARRANTIES OF NON - INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
//             PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION
//             ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
//
//             IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
//             CONSEQUENTIAL DAMAGES ( INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
//             SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
//             INTERRUPTION ) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION
//             AND / OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER
//             UNDER THEORY OF CONTRACT, TORT ( INCLUDING NEGLIGENCE ), STRICT LIABILITY OR
//             OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
// Copyright ( C ) 2008 Apple Inc. All Rights Reserved.
//
////////////////////////////////////////////////////////////////////////////////////////////////////

#ifndef __AABB_H__
#define __AABB_H__

#include "compute_types.h"
#include "compute_math.h"

#include <OpenGL/gl.h>

class aabbf3
{

public:

    typedef enum OverlapType
    { 
        AABB_INSIDE     = 0,
        AABB_INTERSECTS = 1,
        AABB_OUTSIDE    = 2
    };

    aabbf3( void ) :
        min(+MAXFLOAT, +MAXFLOAT, +MAXFLOAT),
        max(-MAXFLOAT, -MAXFLOAT, -MAXFLOAT)
    {
        // EMPTY!
    }

    aabbf3( const aabbf3 &a ):
        min( a.min ),
        max( a.max )
    {
        // EMPTY!
    }

    aabbf3(
        float fMinX, float fMaxX,
        float fMinY, float fMaxY,
        float fMinZ, float fMaxZ)
    {
        min = make_float3(fMinX, fMinY, fMinZ);
        max = make_float3(fMaxX, fMaxY, fMaxZ);
    }


    aabbf3( const float3 &rkMin, const float3 &rkMax ):
        min( rkMin ),
        max( rkMax )
    {
        // EMPTY!
    }

    aabbf3( const float3 &rkCenter, const float fRadius ):
        min( rkCenter.x - fRadius, rkCenter.y - fRadius, rkCenter.z - fRadius ),
        max( rkCenter.x + fRadius, rkCenter.y + fRadius, rkCenter.z + fRadius )
    {
        // EMPTY!
    }

    bool operator == ( const aabbf3 &a ) const
    {
        return !( *this != a );
    }

    bool operator != ( const aabbf3 &a ) const
    {
        return ( (( min.x - a.min.x ) != 0.0f) || (( max.x - a.max.x ) != 0.0f) ||
                 (( min.y - a.min.y ) != 0.0f) || (( max.y - a.max.y ) != 0.0f) ||
                 (( min.z - a.min.z ) != 0.0f) || (( max.z - a.max.z ) != 0.0f) );
    }

    bool isValid( void ) const
    {
        return ( min.x < max.x ) && ( min.y < max.y ) && ( min.z < max.z );
    }

    operator bool() const 
    {
        return isValid();
    }

    void invalidate( void )
    {
        min.x = +MAXFLOAT;
        max.x = -MAXFLOAT;
        min.y = +MAXFLOAT; 
        max.y = -MAXFLOAT;
        min.z = +MAXFLOAT;
        max.z = -MAXFLOAT;
    }

    float3 getCenter( void ) const
    {
        float3 kExtents = min + max;
        return kExtents * 0.5f;
    }

    float getRadius( void ) const
    {
        float3 kSize = getSize() * 0.5f;
        return length(kSize);
    }

    float getWidth( void ) const    { return max.x - min.x; }
    float getHeight( void ) const   { return max.y - min.y; }
    float getDepth( void ) const    { return max.z - min.z; }

    float3 getSize( void ) const 
    { 
        return float3( max.x - min.x, max.y - min.y, max.z - min.z ); 
    }

    float getVerticalDiscRadius( void ) const
    {
        float fSX = ( max.x - min.x );
        float fSY = ( max.y - min.y );

        fSX *= 0.5f;
        fSY *= 0.5f;

        return sqrtf( fSX * fSX + fSY * fSY );
    }

    const aabbf3 operator + ( const aabbf3 &a ) const
    {
        return aabbf3( 
            fmin( min.x, a.min.x ),
            fmax( max.x, a.max.x ),
            fmin( min.y, a.min.y ),
            fmax( max.y, a.max.y ),
            fmin( min.z, a.min.z ),
            fmax( max.z, a.max.z ));
    }

    const aabbf3 operator + ( const float3 &rkPoint ) const
    {
        return aabbf3(
            fmin( min.x, rkPoint.x ),
            fmax( max.x, rkPoint.x ),
            fmin( min.y, rkPoint.y ),
            fmax( max.y, rkPoint.y ),
            fmin( min.z, rkPoint.z ),
            fmax( max.z, rkPoint.z ));
    }

    const aabbf3 operator + ( const float fDelta ) const
    {
        return aabbf3(
            min.x - fDelta, max.x + fDelta,
            min.y - fDelta, max.y + fDelta,
            min.z - fDelta, max.z + fDelta );
    }

    const aabbf3 operator - ( const float fDelta ) const
    {
        return aabbf3(
            min.x + fDelta, max.x - fDelta,
            min.y + fDelta, max.y - fDelta,
            min.z + fDelta, max.z - fDelta );
    }

    aabbf3 &operator += ( const aabbf3 &a )
    {
        min.x = fmin( min.x, a.min.x ),
        max.x = fmax( max.x, a.max.x ),
        min.y = fmin( min.y, a.min.y ),
        max.y = fmax( max.y, a.max.y ),
        min.z = fmin( min.z, a.min.z ),
        max.z = fmax( max.z, a.max.z );

        return *this;
    }

    bool outside( const aabbf3 &a ) const
    {
        return ( a.min.x < min.x || a.max.x > max.x ||
                 a.min.y < min.y || a.max.y > max.y ||
                 a.min.z < min.z || a.max.z > max.z );
    }

    void extend( const aabbf3 &a )
    {
        min.x = fmin( min.x, a.min.x ),
        max.x = fmax( max.x, a.max.x ),
        min.y = fmin( min.y, a.min.y ),
        max.y = fmax( max.y, a.max.y ),
        min.z = fmin( min.z, a.min.z ),
        max.z = fmax( max.z, a.max.z );
    }

    aabbf3 &operator += ( const float3 &rkPoint )
    {
        min.x = fmin( min.x, rkPoint.x );
        max.x = fmax( max.x, rkPoint.x );
        min.y = fmin( min.y, rkPoint.y );
        max.y = fmax( max.y, rkPoint.y );
        min.z = fmin( min.z, rkPoint.z );
        max.z = fmax( max.z, rkPoint.z );

        return *this;
    }

    void extend( const float3 &rkPoint )
    {
        min.x = fmin( min.x, rkPoint.x );
        max.x = fmax( max.x, rkPoint.x );
        min.y = fmin( min.y, rkPoint.y );
        max.y = fmax( max.y, rkPoint.y );
        min.z = fmin( min.z, rkPoint.z );
        max.z = fmax( max.z, rkPoint.z );
    }

    void extend( const float3 &rkPoint, float fRadius )
    {
        min.x = fmin( min.x, rkPoint.x - fRadius );
        max.x = fmax( max.x, rkPoint.x + fRadius);
        min.y = fmin( min.y, rkPoint.y - fRadius );
        max.y = fmax( max.y, rkPoint.y + fRadius);
        min.z = fmin( min.z, rkPoint.z - fRadius );
        max.z = fmax( max.z, rkPoint.z + fRadius );
    }

    aabbf3 &operator += ( const float fDelta )
    {
        min.x -= fDelta;
        max.x += fDelta;
        min.y -= fDelta;
        max.y += fDelta;
        min.z -= fDelta;
        max.z += fDelta;

        return *this;
    }

    void outset( float fDelta )
    {
        min.x -= fDelta;
        max.x += fDelta;
        min.y -= fDelta;
        max.y += fDelta;
        min.z -= fDelta;
        max.z += fDelta;
    }

    aabbf3 &operator -= ( const float fDelta )
    {
        min.x += fDelta;
        max.x -= fDelta;
        min.y += fDelta;
        max.y -= fDelta;
        min.z += fDelta;
        max.z -= fDelta;

        return *this;
    }

    void translate( const float3 &rkPoint )
    {
        min.x += rkPoint.x;
        max.x += rkPoint.x;
        min.y += rkPoint.y;
        max.y += rkPoint.y;
        min.z += rkPoint.z;
        max.z += rkPoint.z;
    }

    void transform( const float16 &rkM )
    {
        float3 akCorners[8];
        getCorners( akCorners );

        invalidate();

        extend( rkM * akCorners[0] );
        extend( rkM * akCorners[1] );
        extend( rkM * akCorners[2] );
        extend( rkM * akCorners[3] );
        extend( rkM * akCorners[4] );
        extend( rkM * akCorners[5] );
        extend( rkM * akCorners[6] );
        extend( rkM * akCorners[7] );
    }

    void getCorners( float3 akCorners[8] ) const
    {
        akCorners[0] = make_float3( min.x, min.y, min.z );
        akCorners[1] = make_float3( min.x, max.y, min.z );
        akCorners[2] = make_float3( max.x, max.y, min.z );
        akCorners[3] = make_float3( max.x, min.y, min.z );

        akCorners[4] = make_float3( min.x, min.y, max.z );
        akCorners[5] = make_float3( min.x, max.y, max.z );
        akCorners[6] = make_float3( max.x, max.y, max.z );
        akCorners[7] = make_float3( max.x, min.y, max.z );
    }

    bool contains( const float3 &rkPoint ) const
    {
        return ( rkPoint.x >= min.x && rkPoint.x <= max.x &&
                 rkPoint.y >= min.y && rkPoint.y <= max.y &&
                 rkPoint.z >= min.z && rkPoint.z <= max.z );
    }

    OverlapType intersects( const aabbf3 &rkOther ) const
    {
        if ( rkOther.min.x >= min.x && rkOther.max.x <= max.x &&
             rkOther.min.y >= min.y && rkOther.max.y <= max.y &&
             rkOther.min.z >= min.z && rkOther.max.z <= max.z )
        {
            return AABB_INSIDE;
        }

        bool bOverlapX = ( min.x < rkOther.max.x && max.x > rkOther.min.x );
        bool bOverlapY = ( min.y < rkOther.max.y && max.y > rkOther.min.y );
        bool bOverlapZ = ( min.z < rkOther.max.z && max.z > rkOther.min.z );

        return ( bOverlapX && bOverlapY && bOverlapZ ) ? (AABB_INTERSECTS) : AABB_OUTSIDE;
    }

    OverlapType intersectsSphere( const float3 &c, float fRadius ) const
    {
        return intersects( aabbf3( c, fRadius ));
    }

    void render() const
    {
        if ( !isValid() ) 
            return;

        float3 akCorners[8];
        getCorners(akCorners);

        glDisable( GL_LIGHTING );

        glBegin( GL_LINE_STRIP );
        {
            for(uint i = 0; i < 8; i++)
                glVertex3f(akCorners[i].x, akCorners[i].y, akCorners[i].z);
        }
        glEnd();

        glBegin( GL_LINES );
        {
            glVertex3f(akCorners[7].x, akCorners[7].y, akCorners[7].z);
            glVertex3f(akCorners[3].x, akCorners[3].y, akCorners[3].z);

            glVertex3f(akCorners[6].x, akCorners[6].y, akCorners[6].z);
            glVertex3f(akCorners[2].x, akCorners[2].y, akCorners[2].z);

            glVertex3f(akCorners[5].x, akCorners[5].y, akCorners[5].z);
            glVertex3f(akCorners[1].x, akCorners[1].y, akCorners[1].z);
        }
        glEnd();

        glEnable( GL_LIGHTING );
    }

public:

    float3 min;
    float3 max;

};

#endif
```

[Next](common-bufferobject.cpp.md)[Previous](main.cpp.md)

