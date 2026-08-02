---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_VirtualSphere_c.html
archived_at: '2026-07-18T02:59:15.439187Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Virtual%20Sphere%20Sample%20Code%201.1-VirtualSphere.h.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-SampleAdditional.h.md)

# Virtual Sphere Sample Code 1.1/VirtualSphere.c

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* VirtualSphere.c
/*
/* Implements the Virtual Sphere algorithm for 3D rotation using a 2D input device.
/* See paper "A Study in Interactive 3-D Rotation Using 2-D Control Devices" by
/* Michael Chen, S. Joy Mountford and Abigail Sellen published in the ACM Siggraph '88
/* proceedings (Volume 22, Number 4, August 1988) for more detail.  The code here
/* provides a much simpler implementation than that described in the paper.
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1991-1993 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __VIRTUALSPHERE__
#include "VirtualSphere.h"
#endif

/* Local routine */
static void PointOnUnitSphere (Point    p,
                               Point    cueCenter,
                               Integer  cueRadius,
                               CPoint3D *v);

/*=================================================================================================
/* VirtualSphere
/* 
/* Determine the axis and angle of rotation from the last 2 locations of the mouse
/* relative to the Virtual Sphere cue circle.  
/*-------------------------------------------------------------------------------------------------*/
pascal void VirtualSphere (Point    p,  
                           Point    q,
                           Point    cueCenter,
                           Integer  cueRadius,
                           Matrix4D rotationMatrix)
{
    CPoint3D        op, oq;

    /* Project mouse points to 3-D points on the +z hemisphere of a unit
     * sphere. */
    PointOnUnitSphere (p, cueCenter, cueRadius, &op);
    PointOnUnitSphere (q, cueCenter, cueRadius, &oq);

    /* Consider the two projected points as vectors from the center of the 
     * unit sphere. Compute the rotation matrix that will transform vector
     * op to oq. */
    SetRotationMatrix (rotationMatrix, &op, &oq);
}

/*=================================================================================================
/* PointOnUnitSphere
/*
/* Project a 2D point on a circle to a 3D point on the +z hemisphere of a unit sphere.
/* If the 2D point is outside the circle, it is first mapped to the nearest point on
/* the circle before projection.
/* Orthographic projection is used, though technically the field of view of the camera
/* should be taken into account.  However, the discrepancy is neglegible.
/*-------------------------------------------------------------------------------------------------*/
static void PointOnUnitSphere (Point    p,
                               Point    cueCenter,
                               Integer  cueRadius,
                               CPoint3D *v)
{
    Real    length;
    Real    lengthSqared;

    /* Turn the mouse points into vectors relative to the center of the circle
     * and normalize them.  Note we need to flip the y value since the 3D coordinate
     * has positive y going up. */
    v->x = (Real)  (p.h - cueCenter.h) / (Real) cueRadius;
    v->y = (Real) -(p.v - cueCenter.v) / (Real) cueRadius;

    lengthSqared = v->x*v->x + v->y*v->y;

    /* Project the point onto the sphere, assuming orthographic projection.
     * Points beyond the virtual sphere are normalized onto 
     * edge of the sphere (where z = 0). */
    if (lengthSqared < 1.0) {
        v->z = sqrt (1.0 - lengthSqared);
    } else {
        length = sqrt (lengthSqared);
        v->x /= length;
        v->y /= length;
        v->z = 0.0;
    }
}
```

[Next](Virtual%20Sphere%20Sample%20Code%201.1-VirtualSphere.h.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-SampleAdditional.h.md)

