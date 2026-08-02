---
title: DeferredShading
apple_id: DTS40010088
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2015-07-08'
source_url: https://developer.apple.com/library/archive/samplecode/DeferredShading/Listings/GeoUtils_h.html
archived_at: '2026-07-18T03:06:11.433998Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DeferredShading](DeferredShading.md)


[Next](Readme.md.md)[Previous](vectorUtil.c.md)

# GeoUtils.h

```c
/*
 Copyright (C) 2015 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 Utilities for handling geometry.
 */


#ifndef __GEO_UTILS__
#define __GEO_UTILS__

#include <OpenGL/gl3.h>
#include <OpenGL/gl3ext.h>

#include <math.h>
#include <assert.h>
#include <stdlib.h>
#include <string.h>

#ifdef __cplusplus
extern "C" {
#endif

typedef struct _vec2
{
    float x,y;
} vec2;

typedef struct _vec3
{
    float x,y,z;
} vec3;

typedef struct _vec4
{
    float x,y,z,w;
} vec4;

typedef union _mat4union 
{
    vec4 columns[4];
    float m[16];
    float mm[4][4];
} mat4;

static const mat4 ZeroMatrix = 
{
    {{0.0,0.0,0.0,0.0},
    {0.0,0.0,0.0,0.0},
    {0.0,0.0,0.0,0.0},
    {0.0,0.0,0.0,0.0}},
};

static const mat4 IdentityMatrix = 
{
    {{1.0,0.0,0.0,0.0},
    {0.0,1.0,0.0,0.0},
    {0.0,0.0,1.0,0.0},
    {0.0,0.0,0.0,1.0}},
};

static const mat4 FacingPlusXMatrix =
{
    {{0.0, 0.0, 1.0, 0.0},
    {0.0, 1.0, 0.0, 0.0},
    {-1.0,0.0, 0.0, 0.0},
    {0.0, 0.0, 0.0, 1.0}},
};

static const mat4 FacingMinusXMatrix =
{
    {{0.0, 0.0,-1.0, 0.0},
    {0.0, 1.0, 0.0, 0.0},
    {1.0, 0.0, 0.0, 0.0},
    {0.0, 0.0, 0.0, 1.0}},
};

inline float dotproduct(vec4* a, vec4* b)
{
    return  a->x*b->x+
            a->y*b->y+
            a->z*b->z+ 
            a->w*b->w;
}

inline void matMul(const mat4* a, const mat4* b, mat4* dst)
{
    assert(a != b && b != dst && a != dst);
    //column 0
    dst->m[0] = a->m[0] *b->m[0] +
                a->m[4] *b->m[1] +
                a->m[8] *b->m[2] +
                a->m[12]*b->m[3];
    dst->m[1] = a->m[1] *b->m[0] +
                a->m[5] *b->m[1] +
                a->m[9] *b->m[2] +
                a->m[13]*b->m[3];
    dst->m[2] = a->m[2] *b->m[0] +
                a->m[6] *b->m[1] +
                a->m[10]*b->m[2] +
                a->m[14]*b->m[3];
    dst->m[3] = a->m[3] *b->m[0] +
                a->m[7] *b->m[1] +
                a->m[11]*b->m[2] +
                a->m[15]*b->m[3];
    //column 1
    dst->m[4] = a->m[0] *b->m[4] +
                a->m[4] *b->m[5] +
                a->m[8] *b->m[6] +
                a->m[12]*b->m[7];
    dst->m[5] = a->m[1] *b->m[4] +
                a->m[5] *b->m[5] +
                a->m[9] *b->m[6] +
                a->m[13]*b->m[7];
    dst->m[6] = a->m[2] *b->m[4] +
                a->m[6] *b->m[5] +
                a->m[10]*b->m[6] +
                a->m[14]*b->m[7];
    dst->m[7] = a->m[3] *b->m[4] +
                a->m[7] *b->m[5] +
                a->m[11]*b->m[6] +
                a->m[15]*b->m[7];
    //column 2
    dst->m[8] = a->m[0] *b->m[8] +
                a->m[4] *b->m[9] +
                a->m[8] *b->m[10] +
                a->m[12]*b->m[11];
    dst->m[9] = a->m[1] *b->m[8] +
                a->m[5] *b->m[9] +
                a->m[9] *b->m[10] +
                a->m[13]*b->m[11];
    dst->m[10]= a->m[2] *b->m[8] +
                a->m[6] *b->m[9] +
                a->m[10]*b->m[10] +
                a->m[14]*b->m[11];
    dst->m[11]= a->m[3] *b->m[8] +
                a->m[7] *b->m[9] +
                a->m[11]*b->m[10] +
                a->m[15]*b->m[11];
    //column 3
    dst->m[12]= a->m[0] *b->m[12] +
                a->m[4] *b->m[13] +
                a->m[8] *b->m[14] +
                a->m[12]*b->m[15];
    dst->m[13]= a->m[1] *b->m[12] +
                a->m[5] *b->m[13] +
                a->m[9] *b->m[14] +
                a->m[13]*b->m[15];
    dst->m[14]= a->m[2] *b->m[12] +
                a->m[6] *b->m[13] +
                a->m[10]*b->m[14] +
                a->m[14]*b->m[15];
    dst->m[15]= a->m[3] *b->m[12] +
                a->m[7] *b->m[13] +
                a->m[11]*b->m[14] +
                a->m[15]*b->m[15];
}
inline void matVecMul(mat4* m, vec4* v, vec4* dst)
{
    assert(v != dst);
    dst->x =    m->m[0]*v->x +
                m->m[4]*v->y +
                m->m[8]*v->z +
                m->m[12]*v->w;
    dst->y =    m->m[1]*v->x +
                m->m[5]*v->y +
                m->m[9]*v->z +
                m->m[13]*v->w;
    dst->z =    m->m[2]*v->x +
                m->m[6]*v->y +
                m->m[10]*v->z +
                m->m[14]*v->w;
    dst->w =    m->m[3]*v->x +
                m->m[7]*v->y +
                m->m[11]*v->z +
                m->m[15]*v->w;
}

static inline void makeTransformMatrix(float x,float y,float z, mat4* dst)
{
    memcpy(dst, &IdentityMatrix, sizeof(mat4));
    dst->columns[3].x = x;
    dst->columns[3].y = y;
    dst->columns[3].z = z;
    dst->columns[3].w = 1.0;
}

typedef struct _QuadricStruct
{
    GLuint vertCount;
    GLuint indexCount;
    GLuint vertsID;
    GLuint normalsID;
    GLuint colorsID;
    GLuint indicesID;
} quadric;


void createTriangleToothedGear(quadric* q, float radius, float innerradius, float toothRadius, float thickness, int slices);
void createTriangleToothedGearFlat(quadric* q, float radius, float innerradius, float toothRadius, float thickness, int slices);
void createSquareToothedGear(quadric* q, float radius, float innerradius, float toothRadius, float thickness, int slices);
void normalizeVec3(vec3* in, vec3* out);

#ifdef __cplusplus
}
#endif

#endif
```

[Next](Readme.md.md)[Previous](vectorUtil.c.md)

