---
title: VideoSnake
apple_id: DTS40012327
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-28'
source_url: https://developer.apple.com/library/archive/samplecode/VideoSnake/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:27:55.223583Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VideoSnake](VideoSnake.md)


[Next](LICENSE.txt.md)[Previous](Resources-Shaders-videoSnake.fsh.md)

# ReadMe.txt

```

VideoSnake

This sample demonstrates temporal synchronization of video with motion data from the accelerometer and gyroscope. It also includes a class which illustrates best practices for using the AVAssetWriter API to record movies.  This is based on the VideoSnake demo presented at WWDC 2012, Session 520, "What's new in Camera Capture".


Classes
VideoSnakeViewController
-- The UIViewController subclass.  This file contains the view controller logic, including support for the record button and preview.
VideoSnakeSessionManager
-- This file manages the capture pipeline, including the AVCaptureSession, the various queues, and resource management.
VideoSnakeOpenGLRenderer
-- This file manages the OpenGL processing for the video snakey effect and delivers rendered buffers.
VideoSnakeAppDelegate
-- Standard Application Delegate

Shaders
-- OpenGL shader code for the "snakey" effect

Utilities
MotionSynchronizer
-- Manages input from CoreMotion and synchronizes motion sample with video samples from the CaptureSession.
MovieRecorder
-- Illustrates real-time use of AVAssetWriter to record the displayed effect.
OpenGLPixelBufferView
-- This is a view that displays pixel buffers on the screen using OpenGL.

GL
-- Utilities used by the GL processing.


===============================================================
Copyright © 2013 Apple Inc. All rights reserved.
```

[Next](LICENSE.txt.md)[Previous](Resources-Shaders-videoSnake.fsh.md)

