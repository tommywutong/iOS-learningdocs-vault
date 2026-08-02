---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_MyMath_h.html
archived_at: '2026-07-18T02:59:14.503625Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Virtual%20Sphere%20Sample%20Code%201.1-ObjectData.h.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-MyMath.c.md)

# Virtual Sphere Sample Code 1.1/MyMath.h

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* MyMath.h
/*
/* Header file to hide all the ugliness when using floating point and fixed point
/* math between MPW C and Think C.  Instead of figuring out when to and when
/* not to include SANE.h and Math.h, and their order, just include MyMath.h.
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1991-1993 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __MyMath__
#define __MyMath__

#ifndef __GLOBALS__
#include "Globals.h"
#endif

#define Real    double


/*=================================================================================================
/* LightSpeed C dependencies
/*-------------------------------------------------------------------------------------------------*/
#ifdef THINK_C

#if __option(mc68881)
    #ifndef  _MATH_
    #include "Math.h"
    #endif

    pascal  Fixed   Real2Fix (Real a);
    pascal  Real    Fix2Real (Fixed a);
#else
    #ifndef  _SANE_
    #include "SANE.h"
    #endif
    /* Don't include Math.h or you will be sorry! */

    #define Real2Fix    X2Fix
    #define Fix2Real    Fix2X
    pascal  Real asin (Real x);
    pascal  Real atan2 (Real y, Real x);
#endif

#endif THINK_C


/*=================================================================================================
/* MPW C dependencies
/* MPW C is nice because the math libraries takes care of the different math format.
/*-------------------------------------------------------------------------------------------------*/
#ifdef applec

#ifndef _SANE_
#include "SANE.h"
#endif

#define Real2Fix    X2Fix
#define Fix2Real    Fix2X

#endif applec



#endif __MyMath__
```

[Next](Virtual%20Sphere%20Sample%20Code%201.1-ObjectData.h.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-MyMath.c.md)

