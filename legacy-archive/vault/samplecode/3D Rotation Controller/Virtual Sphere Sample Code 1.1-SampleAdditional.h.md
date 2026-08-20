---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_SampleAdditional_h.html
archived_at: '2026-07-18T02:59:14.929279Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Virtual%20Sphere%20Sample%20Code%201.1-VirtualSphere.c.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-SampleAdditional.c.md)

# Virtual Sphere Sample Code 1.1/SampleAdditional.h

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* SampleAdditional.c
/*
/* This file contains routines to replace the standard ones in Sample.c
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1991-1993 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __SAMPLEADDITIONAL__
#define __SAMPLEADDITIONAL__

#ifndef __GLOBALS__
#include "Globals.h"
#endif

#ifndef __EVENTS__
#include <Events.h>
#endif

#ifndef __WINDOWS__
#include <Windows.h>
#endif

void    Initialize3D (WindowPtr window);
void    CleanUp3D (void);

void    CheckSystemConfiguration (void);
void    AdjustAdditionalMenus (void);
void    DoAdditionalMenuCommand (long menuResult);
void    DoContentClick (WindowPtr window, EventRecord *event);
void    DrawWindow (WindowPtr window);
void    UpdateWindow (WindowPtr window);

#endif __SAMPLEADDITIONAL__
```

[Next](Virtual%20Sphere%20Sample%20Code%201.1-VirtualSphere.c.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-SampleAdditional.c.md)

