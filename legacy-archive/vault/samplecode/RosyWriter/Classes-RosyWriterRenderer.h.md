---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Classes_RosyWriterRenderer_h.html
archived_at: '2026-07-18T03:22:17.267745Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Classes-RosyWriterViewController.h.md)[Previous](Classes-RosyWriterCIFilterRenderer.h.md)

# Classes/RosyWriterRenderer.h

```objc

 /*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 A generic protocol for renderer objects used by RosyWriterCapturePipeline
 */

#import <Foundation/Foundation.h>
#import <CoreMedia/CoreMedia.h>
#import <CoreVideo/CoreVideo.h>

@protocol RosyWriterRenderer <NSObject>

@required

/* Format/Processing Requirements */
@property(nonatomic, readonly) BOOL operatesInPlace; // When YES the input pixel buffer is written to by the renderer instead of writing the result to a new pixel buffer.
@property(nonatomic, readonly) FourCharCode inputPixelFormat; // One of 420f, 420v, or BGRA

/* Resource Lifecycle */
// Prepare and destroy expensive resources inside these callbacks.
// The outputRetainedBufferCountHint tells out of place renderers how many of their output buffers will be held onto by the downstream pipeline at one time.
// This can be used by the renderer to size and preallocate their pools.
- (void)prepareForInputWithFormatDescription:(CMFormatDescriptionRef)inputFormatDescription outputRetainedBufferCountHint:(size_t)outputRetainedBufferCountHint;
- (void)reset;

/* Rendering */
// Renderers which operate in place should return the input pixel buffer with a +1 retain count.
// Renderers which operate out of place should create a pixel buffer to return from a pool they own.
// When rendering to a pixel buffer with the GPU it is not necessary to block until rendering has completed before returning.
// It is sufficient to call glFlush() to ensure that the commands have been flushed to the GPU.
- (CVPixelBufferRef)copyRenderedPixelBuffer:(CVPixelBufferRef)pixelBuffer;

@optional

// This property must be implemented if operatesInPlace is NO and the output pixel buffers have a different format description than the input.
// If implemented a non-NULL value must be returned once the renderer has been prepared (can be NULL after being reset).
@property(nonatomic, readonly) CMFormatDescriptionRef __attribute__((NSObject)) outputFormatDescription;

@end
```

[Next](Classes-RosyWriterViewController.h.md)[Previous](Classes-RosyWriterCIFilterRenderer.h.md)

