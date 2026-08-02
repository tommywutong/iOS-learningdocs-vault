---
title: OpenGL Driver Monitor User Guide
apple_id: TP40006474
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLDriverMonitorUserGuide/Performance/performance.html
archived_at: '2026-07-15T07:36:51.932581Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Driver Monitor User Guide](Introduction.md)


[Next](OpenGL%20Driver%20Monitor%20Parameters.md)[Previous](Using%20OpenGL%20Driver%20Monitor.md)

# Identifying and Solving Performance Issues

OpenGL Driver Monitor is not the primary tool for analyzing performance issues in an OpenGL application. It’s the backup tool that experts use when Instruments and OpenGL Profiler don’t reveal the cause of a performance problem. This chapter assumes that you have already used Apple’s other tools to analyze your OpenGL application.

The strategies described here can help you identify the most common problems that occur in OpenGL applications. Keep in mind that analyzing difficult performance problems is more of an art than a science. Although you’ll want to start with these basic strategies, you’ll need to devise additional ones tailored to the type of problem you see, and to whether you are trying to solve a driver issue or an application one.

Before you begin to use OpenGL Driver Monitor as an analysis tool, it’s a good idea to check your code to see if you are following the most recent best practices for using OpenGL. See:

- The “Improving Performance” chapter in _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_ for a discussion of best practices
- _[OpenGL Profiler User Guide](../OpenGL%20Profiler%20User%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3dinzv)_. You’ll find advice on functions that you need to make sure you use correctly, if you use them at all.

To check data transfer rates, monitor the following:

- VRAM usage. See whether VRAM usage is at capacity by looking at Current Video Memory in Use (`vramUsedBytes`) or Current Free Video Memory (`vramFreeBytes`). If it is at capacity, investigate whether the system is low on VRAM or whether VRAM usage is unusually high for an application running on the system.
- Swap rate. A variety of parameters, such as Buffer Swaps (`bufferSwapCount`), let you investigate the cause of unusually high swap rates. Check to see whether the swapped data is dynamic or static. If the data os static, make sure you are using caches, vertex buffer objects, or some other technique that’s optimized for static data. Use swaps only for dynamic data, and only when the data changes.
- The time spent by the CPU waiting for the GPU. Look at CPU Wait for GPU (`hardwareWaitTime`). If the CPU spends a lot of time simply waiting, check to see whether you are calling `glFlush` or `glFinish` inappropriately. There are only a few cases where you actually need to use these calls, and these cases are rare. For more information, see the “Improving Performance” chapter in _[OpenGL Programming Guide for Mac](../OpenGL%20Programming%20Guide%20for%20Mac/About%20OpenGL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobx)_.

You need to make sure that your application is not paging texture and surface data unnecessarily. When it does page, you should use the accelerated graphics port (AGP pathway, which is also known as DMA transfer). Non-AGP transfers slow performance. You can check for less optimal paging by looking at these parameters:

- Surface Page Off Data (Non-AGP) (`surfacePageOffBytes`)
- Surface Page On Data (Non-AGP) (`surfacePageInBytes`)
- Texture Page Off Data (Non-AGP) (`texturePageOutBytes`)
- Texture Page Off Data (Non-AGP) (`texturePageInBytes`)

Non-AGP transfer is acceptable only if you must reorder data or align it. If possible, use this type of data transfer at initialization time and not during a rendering loop.

If your application has a lot of paging activity, whether it’s AGP or non-AGP, consider using framebuffer objects.

[Next](OpenGL%20Driver%20Monitor%20Parameters.md)[Previous](Using%20OpenGL%20Driver%20Monitor.md)

