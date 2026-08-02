---
title: iOS Device Compatibility Reference
apple_id: TP40013599
resource_type: Guide
platform: iOS
topic: Data Management
technology: null
published: '2017-10-30'
source_url: https://developer.apple.com/library/archive/documentation/DeviceInformation/Reference/iOSDeviceCompatibility/HardwareGPUInformation/HardwareGPUInformation.html
archived_at: '2026-07-15T07:31:54.554845Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [iOS Device Compatibility Reference](Introduction.md)


[Next](Cameras.md)[Previous](Displays.md)

# Graphics Processors

Since the introduction of the original iPhone, Apple has continued to improve the GPU capabilities in new iOS devices. When you write a Metal or OpenGL ES app, you need to understand the specific limits of each device you app runs on.

Table 3-1 lists the devices that are compatible with Metal and OpenGL ES 3.0.

__Table 3-1__  Metal and OpenGL ES 3.0 compatible devices

| Device name | GPU |
| iPhone 8  iPhone 8 Plus  iPhone X | Apple A11 GPU |
| iPhone 7  iPhone 7 Plus | Apple A10 GPU |
| iPhone 6s  iPhone 6s Plus  iPhone SE | Apple A9 GPU |
| iPhone 6  iPhone 6 Plus | Apple A8 GPU |
| iPhone 5s | Apple A7 GPU |
| iPad Pro 12.9-inch (2nd generation)  iPad Pro (10.5-inch) | Apple A10 GPU |
| iPad (5th generation)  iPad Pro (12.9-inch)  iPad Pro (9.7-inch) | Apple A9 GPU |
| iPad Air 2  iPad mini 4 | Apple A8 GPU |
| iPad Air  iPad mini 3  iPad mini 2 | Apple A7 GPU |
| iPod touch (6th generation) | Apple A8 GPU |

Together, the A7, A8, A9, A10, and A11 GPUs create a new generation of graphics hardware that support both Metal and OpenGL ES 3.0. To get the most out of a 3D, graphics-dominated app running on the these GPUs, use Metal. Metal provides extremely low-overhead access to these GPUs, enabling incredibly high performance for your sophisticated graphics rendering and computational tasks. Metal eliminates many performance bottlenecks—such as costly state validation—that are found in traditional graphics APIs. Both Metal and OpenGL ES 3.0 incorporate many new features, such as multiple render targets and transform feedback, that have not been available on mobile processors before. This means that advanced rendering techniques that have previously been available only on desktop machines, such as deferred rendering, can now be used in iOS apps. Refer to the _[Metal Programming Guide](../Miscellaneous/Metal%20Programming%20Guide/About%20Metal%20and%20This%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demrr)_ for more information about what features are visible to Metal apps.

A Metal feature set describes the features, limits, and capabilities of a Metal implementation. Each Metal feature set is defined by a [MTLFeatureSet](https://developer.apple.com/documentation/metal/mtlfeatureset) value that references a specific OS and GPU pairing. Refer to the [Metal Feature Sets](https://developer.apple.com/metal/feature-sets/) tables for specific information about the feature availability, implementation limits, and pixel format capabilities of each Metal feature set.

[Next](Cameras.md)[Previous](Displays.md)

