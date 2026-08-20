---
title: 3D Rotation Controller
apple_id: DTS10000124
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/3D_Rotation_Controller/Listings/Virtual_Sphere_Sample_Code_1_1_VirtualSphere_h.html
archived_at: '2026-07-18T02:59:15.494841Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [3D Rotation Controller](3D%20Rotation%20Controller.md)


[Next](Document%20Revision%20History.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-VirtualSphere.c.md)

# Virtual Sphere Sample Code 1.1/VirtualSphere.h

```c
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥
/* VirtualSphere.h
/*
/* Implements the Virtual Sphere algorithm for 3D rotation using a 2D input device.
/* See paper "A Study in Interactive 3-D Rotation Using 2-D Control Devices" by
/* Michael Chen, S. Joy Mountford and Abigail Sellen published in the ACM Siggraph '88
/* proceedings (Volume 22, Number 4, August 1988) for more detail.  The code here
/* provides a much simpler implementation than that described in the paper.
/*
/* Author: Michael Chen, Human Interface Group / ATG
/* Copyright © 1987-93 Apple Computer, Inc.  All rights reserved.
/*
/* Part of Virtual Sphere Sample Code Release v1.1
/*¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥¥*/

#ifndef __VIRTUALSPHERE__
#define __VIRTUALSPHERE__

#ifndef __TYPES__
#include <Types.h>
#endif

#ifndef __GRAPHICS3D__
#include "Graphics3D.h"
#endif

pascal void VirtualSphere (Point    p,  
                           Point    q,
                           Point    cueCenter,
                           Integer  cueRadius,
                           Matrix4D rotationMatrix);


#endif __VIRTUALSPHERE__
```

[Next](Document%20Revision%20History.md)[Previous](Virtual%20Sphere%20Sample%20Code%201.1-VirtualSphere.c.md)

