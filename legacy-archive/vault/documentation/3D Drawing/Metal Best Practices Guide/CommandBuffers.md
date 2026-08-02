---
title: Metal Best Practices Guide
apple_id: TP40016642
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Graphics & Animation
technology: Metal
published: '2017-03-27'
source_url: https://developer.apple.com/library/archive/documentation/3DDrawing/Conceptual/MTLBestPracticesGuide/CommandBuffers.html
archived_at: '2026-07-15T03:48:43.718946Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Metal Best Practices Guide](index.md)



## Command Buffers

__Best Practice:__ Submit the fewest possible command buffers per frame without underutilizing the GPU.

Command buffers are the unit of work submission in Metal; they are created by the CPU and executed by the GPU. This relationship allows you to balance CPU and GPU work by adjusting the number of command buffers submitted per frame.

Most Metal apps keep their CPU work one or two frames ahead of their GPU work by implementing triple buffering. This means that there is usually sufficient CPU work queued up to keep the GPU busy by submitting only one or two command buffers per frame (preferably one). However, if the CPU work does not keep far enough ahead of the GPU work, the GPU will starve. More frequent command buffer submissions may keep the GPU busy but may also introduce CPU stalls caused by CPU-GPU synchronization. Managing this tradeoff effectively is the key to improved performance and can be facilitated with the Metal System Trace profiling template in Instruments.

> [!NOTE]
> 

[Render Command Encoders (iOS and tvOS)](RenderCommandEncoders.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmzqfvjvomi)

[Indirect Buffers](IndirectBuffers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dmnbsfvbuqmzrfvjvomi)
