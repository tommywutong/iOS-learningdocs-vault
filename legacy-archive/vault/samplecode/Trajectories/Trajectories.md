---
title: Trajectories
apple_id: DTS40008883
resource_type: Sample Code
platform: macOS
topic: null
technology: OpenCL
published: '2009-09-24'
source_url: https://developer.apple.com/library/archive/samplecode/Trajectories/Introduction/Intro.html
archived_at: '2026-07-18T03:27:08.910369Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# Trajectories

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2009-09-24 Minor Bug Fixes. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqobygmwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 Xcode v3.2 |
| __Runtime Requirements:__ | Mac OS X v10.6 |

This tool demonstrates how to execute a simple game physics engine for computing trajectory of a projectile within a framework of OpenCL kernels. The projectile trajectories are computed using parametric forms. Two types of trajectories are computed: when target and launch point are at the same level and when a projectile is dropped from a moving system. The inputs to the kernels are the constants initial time, time delta, and the initial velocity. Additionally, one kernel takes the initial angle as input, whilst the other takes the initial height as input. The outputs are position vectors, velocity vector, and speed. Additionally, since most game physics engines in use today are designed using C++, the framework here makes use of C++.

[Next](ReadMe.txt.md)

