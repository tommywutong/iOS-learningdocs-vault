---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Listings/TumblerSource_Tumbler_camera_h.html
archived_at: '2026-07-18T03:27:21.266295Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Tumbler and Podium](Tumbler%20and%20Podium.md)


[Next](TumblerSource-Tumblercursor.c.md)[Previous](TumblerSource-Tumblercamera.c.md)

# TumblerSource/Tumbler_camera.h

```
// Tumbler_camera.h
//
// Camera related function prototypes for the the Tumbler application
//
// Modification History
//
//  11/26/94        nick        initial cut - symantec proto_helper app, add defines


#ifndef _Tumbler_CAMERA_H_
#define _Tumbler_CAMERA_H_


// routines from Tumbler_camera.c
void        GetGroupBBox(TQ3ViewObject viewObject, TQ3GroupObject mainGroup, TQ3GroupObject lightGroup, TQ3BoundingBox *viewBBox);
void        AdjustLightsPositions(DocumentPtr theDocument);

TQ3Point3D  AdjustCamera(DocumentPtr theDocument, short winWidth, short winHeight);

#endif
```

[Next](TumblerSource-Tumblercursor.c.md)[Previous](TumblerSource-Tumblercamera.c.md)

