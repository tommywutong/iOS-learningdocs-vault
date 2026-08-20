---
title: RosyWriter
apple_id: DTS40011110
resource_type: Sample Code
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/RosyWriter/Listings/Classes_RosyWriterOpenCVRenderer_mm.html
archived_at: '2026-07-18T03:22:16.845424Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [RosyWriter](RosyWriter.md)


[Next](Classes-Utilities-OpenGLPixelBufferView.m.md)[Previous](Classes-RosyWriterViewController.h.md)

# Classes/RosyWriterOpenCVRenderer.mm

```objc

/*
 Copyright (C) 2016 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 The RosyWriter OpenCV based effect renderer
 */

#import "RosyWriterOpenCVRenderer.h"

// To build OpenCV into the project:
//  - Download opencv2.framework for iOS
//  - Insert framework into project's Frameworks group
//  - Make sure framework is included under the target's Build Phases -> Link Binary With Libraries.
#import <opencv2/opencv.hpp>

@implementation RosyWriterOpenCVRenderer

#pragma mark RosyWriterRenderer

- (BOOL)operatesInPlace
{
    return YES;
}

- (FourCharCode)inputPixelFormat
{
    return kCVPixelFormatType_32BGRA;
}

- (void)prepareForInputWithFormatDescription:(CMFormatDescriptionRef)inputFormatDescription outputRetainedBufferCountHint:(size_t)outputRetainedBufferCountHint
{
    // nothing to do, we are stateless
}

- (void)reset
{
    // nothing to do, we are stateless
}

- (CVPixelBufferRef)copyRenderedPixelBuffer:(CVPixelBufferRef)pixelBuffer
{
    CVPixelBufferLockBaseAddress( pixelBuffer, 0 );

    unsigned char *base = (unsigned char *)CVPixelBufferGetBaseAddress( pixelBuffer );
    size_t width = CVPixelBufferGetWidth( pixelBuffer );
    size_t height = CVPixelBufferGetHeight( pixelBuffer );
    size_t stride = CVPixelBufferGetBytesPerRow( pixelBuffer );
    size_t extendedWidth = stride / sizeof( uint32_t ); // each pixel is 4 bytes/32 bits

    // Since the OpenCV Mat is wrapping the CVPixelBuffer's pixel data, we must do all of our modifications while its base address is locked.
    // If we want to operate on the buffer later, we'll have to do an expensive deep copy of the pixel data, using memcpy or Mat::clone().

    // Use extendedWidth instead of width to account for possible row extensions (sometimes used for memory alignment).
    // We only need to work on columms from [0, width - 1] regardless.

    cv::Mat bgraImage = cv::Mat( (int)height, (int)extendedWidth, CV_8UC4, base );

    for ( uint32_t y = 0; y < height; y++ )
    {
        for ( uint32_t x = 0; x < width; x++ )
        {
            bgraImage.at<cv::Vec<uint8_t,4> >(y,x)[1] = 0;
        }
    }

    CVPixelBufferUnlockBaseAddress( pixelBuffer, 0 );

    return (CVPixelBufferRef)CFRetain( pixelBuffer );
}

@end
```

[Next](Classes-Utilities-OpenGLPixelBufferView.m.md)[Previous](Classes-RosyWriterViewController.h.md)

