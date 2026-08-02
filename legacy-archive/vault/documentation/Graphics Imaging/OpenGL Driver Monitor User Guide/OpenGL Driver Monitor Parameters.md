---
title: OpenGL Driver Monitor User Guide
apple_id: TP40006474
resource_type: Guide
platform: Xcode Developer Tools
topic: Languages & Utilities
technology: OpenGL
published: '2015-03-09'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGLDriverMonitorUserGuide/Glossary/Glossary.html
archived_at: '2026-07-15T07:36:51.906596Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Driver Monitor User Guide](Introduction.md)


[Next](Document%20Revision%20History.md)[Previous](Identifying%20and%20Solving%20Performance%20Issues.md)

# OpenGL Driver Monitor Parameters

OpenGL Driver Monitor parameters are represented as descriptive names and as symbolic names. The parameters you can set for a specific driver are often a subset of what’s listed here.

Each descriptive name describes what the parameter represents and lists its symbolic name.

**2D Command Data**
: The number of bytes sent using 2D graphics contexts. `command2DBytes`

**2D Context Switches**
: The total number of context switches to a 2D context on the GPU. `context2DSwitchCount`

**2D Contexts**
: The total number of 2D contexts in use on the GPU. `context2DCount`

**AGP Data Mapped**
: The number of bytes that are mapped into the AGP Graphics Address Remapping Table (GART) or equivalent hardware. `gartMapInBytes`

**AGP Data Unmapped**
: The number of bytes that are unmapped from the AGP Graphics Address Remapping Table (GART) (or equivalent hardware). `gartMapOutBytes`

**Buffer Swaps**
: The total number of buffer swaps (or blits) that the GPU perform. `bufferSwapCount`

**CPU Texture Page-off Wait (non-DMA)**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to finish activity. This is the that the CPU could use to modify a texture prior to paging the texture. This metric applies only if the texture must be paged using the CPU and not using direct memory access (DMA). `texturePageOffWaitTime`

**CPU Texture Page-on Wait**
: The amount of time, in nanoseconds, that the CPU waits for a texture upload command to be completed by the GPU. This is the that the CPU could use for updating and reloading a texture. Typically, there is very little, if any time, spent waiting here. `texturePageInWaitTime`

**CPU Texture Upload Wait (2D context only)**
: The amount of time, in nanoseconds, that the CPU waits for a texture upload to complete before the buffer can be modified. This particular metric tracks usage only by 2D contexts, and is somewhat obsolete. `textureWaitTime`

**CPU Wait for 2D Operations to Finish**
: The amount of time, in nanoseconds, that the CPU waits for all 2D commands issued on a single context to complete. `finish2DWaitTime`

**CPU Wait for 2D Swap to Complete**
: The amount of time, in nanoseconds, that the CPU waits for a previously issued 2D buffer swap to complete. `swapComplete2DWaitTime`

**CPU Wait for DVD Operations to Finish**
: The amount of time, in nanoseconds, that the CPU waits for all DVD commands issued on a single context to complete. `finishDVDWaitTime`

**CPU Wait for DVD Swap to Complete**
: The amount of time, in nanoseconds, that the CPU waits for a previously issued DVD buffer swap to complete. `swapCompleteDVDWaitTime`

**CPU Wait for Free 2D Command Buffer**
: The amount of time, in nanoseconds, that the CPU waits for a 2D command buffer to become available. `freeCommandBuffer2DWaitTime`

**CPU Wait for Free OpenGL Command Buffer**
: The amount of time, in nanoseconds, that the CPU waits for an OpenGL command buffer to become available. `freeCommandBufferGLWaitTime`

**CPU Wait for Free OpenGL Data Buffer**
: The amount of time, in nanoseconds, that the CPU waits for an OpenGL data buffer to become available. `freeDataBufferGLWaitTime`

**CPU Wait for Free 2D Context Switch Buffer**
: The amount of time, in nanoseconds, that the CPU waits for a 2D context-switching buffer to become available. `freeContextBuffer2DWaitTime`

**CPU Wait for Free OpenGL Context Switch Buffer**
: The amount of time, in nanoseconds, that the CPU waits for an OpenGL context-switching buffer to become available. `freeContextBufferGLWaitTime`

**CPU Wait for Free DVD Context Switch Buffer**
: The amount of time, in nanoseconds, that the CPU waits for a DVD context-switching buffer to become available. `freeContextBufferDVDWaitTime`

**CPU Wait for GPU**
: The amount of time, in nanoseconds, that the CPU stalled while waiting on the GPU for any reason. `hardwareWaitTime`

**CPU Wait for Mapped AGP Buffer Removal**
: The amount of time, in nanoseconds, the CPU waits for the GPU to finish an operation on a buffer that needs to be removed from the Graphics Address Remapping Table (GART). `removeFromGARTWaitTime`

**CPU Wait for OpenGL Swap to Complete**
: The amount of time, in nanoseconds, that the CPU waits for a previously issued OpenGL buffer swap to complete. `swapCompleteGLWaitTime`

**CPU Wait for Operations to Finish**
: The amount of time, in nanoseconds, that the CPU waits for all GPU operations to complete and then to be idle. Generally, only the window server waits for this state. `finishAll2DWaitTime`

**CPU Wait for OpenGL Operations to Finish**
: The amount of time, in nanoseconds, that the CPU waits for all OpenGL commands issued on a single context to complete. This is essentially the time spent in `glFinish`. `finishGLWaitTime`

**CPU Wait in User Code**
: The amount of time, in nanoseconds, that the CPU waits while the client (user-level) OpenGL driver waits for a hardware time stamp to arrive (usually for making texture modifications or waiting for a fence to complete). `clientGLWaitTime`

**CPU Wait to perform Surface Read**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU may read from a surface. `surfaceReadLockIdleWaitTime`

**CPU Wait to perform Surface Resize**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU may change the dimensions of a surface. `surfaceSetShapeIdleWaitTime`

**CPU Wait to perform Surface Write**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU may write to a surface. `surfaceWriteLockIdleWaitTime`

**CPU Wait to perform VRAM Surface Page-off**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU can page a surface out of VRAM. `surfaceCopyOutWaitTime`

**CPU Wait to perform VRAM Surface Page-on**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU can page a surface in to VRAM. `surfaceCopyInWaitTime`

**CPU Wait to Submit Commands**
: The amount of time, in nanoseconds, that the CPU waits before being able to submit a new batch of commands to the GPU. `hardwareSubmitWaitTime`

**Current AGP Memory**
: The total size, in bytes, of the AGP Graphics Address Remapping Table (GART). `gartSizeBytes`

**Current Free AGP Memory**
: The total number of free bytes in the AGP Graphics Address Remapping Table (GART). `gartFreeBytes`

**Current Mapped AGP Memory**
: The total number of bytes mapped into AGP Graphics Address Remapping Table (GART). `gartUsedBytes`

**Current Free Video Memory**
: The total number of bytes of free VRAM. This parameter is vendor specific and not available for all drivers. `vramFreeBytes`

**Current Largest Free Video Memory Block**
: The largest free contiguous chunk of VRAM, in bytes. This parameter is vendor specific and not available for all drivers. `vramLargestFree`

**Current Video Memory in Use**
: The total number of bytes of VRAM in use. This parameter is vendor specific and not available for all drivers. `vramUsedBytes`

**DVD Command Data**
: The number of bytes sent using DVD contexts. `commandDVDBytes`

**DVD Context Switches**
: The total number of context switches to a DVD context on the GPU. `contextDVDSwitchCount`

**DVD Contexts**
: The total number of DVD contexts in use on the GPU. `contextDVDCount`

**Extra OpenGL Data**
: The number of bytes used for extra OpenGL command traffic (usually vertex data). Not used by all drivers in all modes. `dataGLBytes`

**Last GPU Submission Time**
: The last submitted time stamp to the GPU, as an absolute time value. `submitStamp`

**Last Read GPU time**
: The last time stamp read back from the GPU, as an absolute time value. `lastReadStamp`

**OpenGL Command Data**
: The number of bytes sent using OpenGL contexts. `commandGLBytes`

**OpenGL Contexts**
: The total number of OpenGL contexts in use on the GPU. `contextGLCountcontextGLCount`

**OpenGL Data Buffers**
: The total number of extra OpenGL data buffers allocated. `dataBufferCount`

**OpenGL Context Switches**
: The total number of context switches to an OpenGL context on the GPU. `contextGLSwitchCount`

**Surface Page Off Data (Non-AGP)**
: The number of bytes transferred due to surface page-off operations. `surfacePageOffBytes`

**Surface Page On Data (Non-AGP)**
: The number of bytes transferred due to surface page-on operations. `surfacePageInBytes`

**Surfaces**
: The total number of surfaces allocated by the GPU. `surfaceCount`

**Swap Data**
: The number of bytes sent by swap commands. `swapBytes`

**Target Minimum Mapped AGP Memory**
: The minimum amount of data, in bytes, that a driver tries to keep mapped into AGP Graphics Address Remapping Table (GART). `gartCacheBytes`

**Texture Page Off Data (Non-AGP)**
: The number of bytes transferred for texture page-off operations. Under most conditions, textures are not paged off but are simply thrown away since a backup exists in system memory. Texture page-off traffic usually happens when VRAM pressure forces a page-off of a texture that only has valid data in VRAM, such as a texture created using the function `glCopyTexImage`, or modified using the functiona `glCopyTexSubImage` or _glTexSubImage_. `texturePageOutBytes`

**Texture Page On Data (Non-AGP)**
: The number of bytes transferred for texture page-ins. Textures mapped using AGP will not show up here. `texturePageInBytes`

**Textures**
: The total number of kernel textures allocated by the GPU. `textureCount`

**Total Command Data**
: The number of bytes sent using all graphics contexts (2D, OpenGL, DVD). `commandBytes`

Each symbolic name describes what the parameter represents and lists its descriptive name.

**bufferSwapCount**
: The total number of buffer swaps (or blits) that the GPU perform. (Buffer Swaps)

**clientGLWaitTime**
: The amount of time, in nanoseconds, that the CPU waits while the client (user-level) OpenGL driver waits for a hardware time stamp to arrive (usually for making texture modifications or waiting for a fence to complete). (CPU Wait in User Code)

**command2DBytes**
: The number of bytes sent using 2D graphics contexts. (2D Command Data)

**commandBytes**
: The number of bytes sent using all graphics contexts (2D, OpenGL, DVD). (Total Command Data)

**commandDVDBytes**
: The number of bytes sent using DVD contexts. (DVD Command Data)

**commandGLBytes**
: The number of bytes sent using OpenGL contexts. (OpenGL Command Data)

**context2DCount**
: The total number of 2D contexts in use on the GPU. (2D Contexts)

**context2DSwitchCount**
: The total number of context switches to a 2D context on the GPU. (2D Context Switches)

**contextDVDCount**
: The total number of DVD contexts in use on the GPU. (DVD Contexts)

**contextDVDSwitchCount**
: The total number of context switches to a DVD context on the GPU. (DVD Context Switches)

**contextGLCount**
: The total number of OpenGL contexts in use on the GPU. (OpenGL Contexts)

**contextGLSwitchCount**
: The total number of context switches to an OpenGL context on the GPU. (OpenGL Context Switches)

**dataBufferCount**
: The total number of extra OpenGL data buffers allocated. (OpenGL Data Buffers)

**dataGLBytes**
: The number of bytes used for extra OpenGL command traffic (usually vertex data). Not used by all drivers in all modes. (Extra OpenGL Data)

**finish2DWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for all 2D commands issued on a single context to complete. (CPU Wait for 2D Operations to Finish)

**finishAll2DWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for all GPU operations to complete and then to be idle. Generally, only the window server waits for this state. (CPU Wait for Operations to Finish)

**finishDVDWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for all DVD commands issued on a single context to complete. (CPU Wait for DVD Operations to Finish)

**finishGLWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for all OpenGL commands issued on a single context to complete. This is essentially the time spent in `glFinish`. (CPU Wait for OpenGL Operations to Finish)

**freeCommandBuffer2DWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a 2D command buffer to become available. (CPU Wait for Free 2D Command Buffer)

**freeCommandBufferGLWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for an OpenGL command buffer to become available. (CPU Wait for Free OpenGL Command Buffer)

**freeContextBuffer2DWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a 2D context-switching buffer to become available. (CPU Wait for Free 2D Context Switch Buffer)

**freeContextBufferDVDWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a DVD context-switching buffer to become available. (CPU Wait for Free DVD Context Switch Buffer)

**freeContextBufferGLWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for an OpenGL context-switching buffer to become available. (CPU Wait for Free OpenGL Context Switch Buffer)

**freeDataBufferGLWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for an OpenGL data buffer to become available. (CPU Wait for Free OpenGL Data Buffer)

**gartCacheBytes**
: The minimum amount of data, in bytes, that a driver tries to keep mapped into AGP Graphics Address Remapping Table (GART). (Target Minimum Mapped AGP Memory)

**gartFreeBytes**
: The total number of free bytes in the AGP Graphics Address Remapping Table (GART). (Current Free AGP Memory)

**gartMapInBytes**
: The number of bytes that are mapped into the AGP Graphics Address Remapping Table (GART) or equivalent hardware. (AGP Data Mapped)

**gartMapOutBytes**
: The number of bytes that are unmapped from the AGP Graphics Address Remapping Table (GART) (or equivalent hardware). (AGP Data Unmapped)

**gartSizeBytes**
: The total size, in bytes, of the AGP Graphics Address Remapping Table (GART). (Current AGP Memory)

**gartUsedBytes**
: The total number of bytes mapped into AGP Graphics Address Remapping Table (GART). (Current Mapped AGP Memory)

**hardwareSubmitWaitTime**
: The amount of time, in nanoseconds, that the CPU waits before being able to submit a new batch of commands to the GPU. (CPU Wait to Submit Commands)

**hardwareWaitTime**
: The amount of time, in nanoseconds, that the CPU stalled while waiting on the GPU for any reason. (CPU Wait for GPU)

**lastReadStamp**
: The last time stamp read back from the GPU, as an absolute time value. (Last Read GPU time)

**removeFromGARTWaitTime**
: The amount of time, in nanoseconds, the CPU waits for the GPU to finish an operation on a buffer that needs to be removed from the Graphics Address Remapping Table (GART). (CPU Wait for Mapped AGP Buffer Removal)

**submitStamp**
: The last submitted time stamp to the GPU, as an absolute time value. (Last GPU Submission Time)

**surfaceCount**
: The total number of surfaces allocated by the GPU.(Surfaces)

**surfaceCopyInWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU can page a surface in to VRAM. (CPU Wait to perform VRAM Surface Page-on)

**surfaceCopyOutWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU can page a surface out of VRAM. (CPU Wait to perform VRAM Surface Page-off)

**surfacePageInBytes**
: The number of bytes transferred due to surface page-on operations. (Surface Page On Data (Non-AGP))

**surfacePageOffBytes**
: The number of bytes transferred due to surface page-off operations. (Surface Page Off Data (Non-AGP))

**surfaceReadLockIdleWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU may read from a surface. (CPU Wait to perform Surface Read)

**surfaceSetShapeIdleWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU may change the dimensions of a surface. (CPU Wait to perform Surface Resize)

**surfaceWriteLockIdleWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to become idle so that the CPU may write to a surface. (CPU Wait to perform Surface Write)

**swapBytes**
: The number of bytes sent by swap commands. (Swap Data)

**swapComplete2DWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a previously issued 2D buffer swap to complete. (CPU Wait for 2D Swap to Complete)

**swapCompleteDVDWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a previously issued DVD buffer swap to complete. (CPU Wait for DVD Swap to Complete)

**swapCompleteGLWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a previously issued OpenGL buffer swap to complete. (CPU Wait for OpenGL Swap to Complete)

**textureCount**
: The total number of kernel textures allocated by the GPU. (Textures)

**texturePageInBytes**
: The number of bytes transferred for texture page-ins. Textures mapped using AGP will not show up here. (Texture Page On Data (Non-AGP))

**texturePageInWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a texture upload command to be completed by the GPU. This is the that the CPU could use for updating and reloading a texture. Typically, there is very little, if any time, spent waiting here. (CPU Texture Page-on Wait)

**texturePageOffWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for the GPU to finish activity. This is the that the CPU could use to modify a texture prior to paging the texture. This metric applies only if the texture must be paged using the CPU and not using direct memory access (DMA). (CPU Texture Page-off Wait (non-DMA))

**texturePageOutBytes**
: The number of bytes transferred for texture page-off operations. Under most conditions, textures are not paged off but are simply thrown away since a backup exists in system memory. Texture page-off traffic usually happens when VRAM pressure forces a page-off of a texture that only has valid data in VRAM, such as a texture created using the function `glCopyTexImage`, or modified using the functions `glCopyTexSubImage` or `glTexSubImage`. (Texture Page Off Data (Non-AGP))

**textureWaitTime**
: The amount of time, in nanoseconds, that the CPU waits for a texture upload to complete before the buffer can be modified. This particular metric tracks usage only by 2D contexts, and is somewhat obsolete. (CPU Texture Upload Wait (2D context only))

**vramFreeBytes**
: The total number of bytes of free VRAM. This parameter is vendor specific and not available for all drivers. (Current Free Video Memory)

**vramLargestFree**
: The largest free contiguous chunk of VRAM, in bytes. This parameter is vendor specific and not available for all drivers. (Current Largest Free Video Memory Block)

**vramUsedBytes**
: The total number of bytes of VRAM in use. This parameter is vendor specific and not available for all drivers. (Current Video Memory in Use)

[Next](Document%20Revision%20History.md)[Previous](Identifying%20and%20Solving%20Performance%20Issues.md)

