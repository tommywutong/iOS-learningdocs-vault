---
title: AVCustomEdit
apple_id: DTS40013411
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/AVCustomEdit/Listings/ReadMe_md.html
archived_at: '2026-07-18T03:00:12.283112Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVCustomEdit](AVCustomEdit.md)


[Next](AVCustomEdit-Swift-Shaders.metal.md)[Previous](AVCustomEdit-main.m.md)

# ReadMe.md

```
# AVCustomEdit

Using AVFoundation custom compositors to add transitions to an AVMutableComposition.

## Overview

AVCustomEdit is a simple AVFoundation based movie editing application demonstrating custom compositing to add transitions. The sample demonstrates the use of custom compositors to add transitions to an AVMutableComposition. It implements the AVVideoCompositing and AVVideoCompositionInstruction protocols to have access to individual source frames, which are then rendered using OpenGL or Metal off screen rendering.

Note: These developed transitions are not supported on simulator.

The main classes are as follows:

APLViewController:

A UIViewController subclass. This contains the view controller logic including playback and editing setup.

APLTransitionTypeController:

A subclass of UITableViewController which controls UI for selecting transition type.

APLSimpleEditor:

This class setups an AVComposition with relevant AVVideoCompositions using the provided clips and time ranges.

APLCustomVideoCompositionInstruction:

Custom video composition instruction class implementing AVVideoCompositionInstruction protocol.

APLCustomVideoCompositor:

Custom video compositor class implementing AVVideoCompositing protocol.


Objective-C Target

APLOpenGLRenderer:

Base class renderer setups an EAGLContext for rendering, it also loads, compiles and links the vertex and fragment shaders for both Y and UV plane.

APLDiagonalWipeRenderer:

A subclass of APLOpenGLRenderer, renders the given source buffers to perform a diagonal wipe over the transition time range.

APLCrossDissolveRenderer:

A subclass of APLOpenGLRenderer, renders the given source buffers to perform a cross dissolve over the transition time range.


Swift Target

APLMetalRenderer:

Base class renderer setups a reference to the preferred system default Metal device.

APLDiagonalWipeRenderer:

A subclass of APLMetalRenderer, renders the given source buffers to perform a diagonal wipe over the transition time range.

APLCrossDissolveRenderer:

A subclass of APLMetalRenderer, renders the given source buffers to perform a cross dissolve over the transition time range.


## Requirements

### Build

Xcode 8.3.3, iOS 10.0 SDK

### Runtime

iOS 9.3.3 or later

Copyright (C) 2013 - 2017 Apple Inc. All rights reserved.
```

[Next](AVCustomEdit-Swift-Shaders.metal.md)[Previous](AVCustomEdit-main.m.md)

