---
title: CullGroupSample
apple_id: DTS10000133
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/CullGroupSample/Introduction/Intro.html
archived_at: '2026-07-18T03:05:31.119015Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Headers-3dmf.h.md)

# CullGroupSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

New in QD3D 1.6 is the ability to assign a Bounding Box to a Display Group. When the group is submitted for rendering, it will be cull tested and if it fails, then none of the geometry or other objects inside the group will be submitted for rendering. The speed boost from this ranges from 30% to 3500% or even higher for some conditions. This sample demonstrates the rendering speed increase which results from assigning a Bounding Box to a Display Group. The sample creates a series of objects in display group, and assigns a Bounding Box to the display group. The user is able to compare rendering of the display group both with and without the use of Bounding Boxes.

[Next](Headers-3dmf.h.md)

