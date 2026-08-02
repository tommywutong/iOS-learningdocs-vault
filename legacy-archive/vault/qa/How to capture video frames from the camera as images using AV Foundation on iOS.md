---
title: How to capture video frames from the camera as images using AV Foundation on
  iOS
apple_id: DTS40010192
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2010-09-29'
source_url: https://developer.apple.com/library/archive/qa/qa1702/_index.html
archived_at: '2026-07-18T02:34:14.539307Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1702

# How to capture video frames from the camera as images using AV Foundation on iOS

## Q:  How do I capture video frames from the camera as images using AV Foundation?

A: To perform a real-time capture, first create a capture session by instantiating an `AVCaptureSession` object. You use an `AVCaptureSession` object to coordinate the flow of data from AV input devices to outputs.

Next, create a input data source that provides video data to the capture session by instantiating a `AVCaptureDeviceInput` object. Call `addInput` to add that input to the `AVCaptureSession` object.

Create an output destination by instantiating an `AVCaptureVideoDataOutput` object , and add it to the capture session using `addOutput`.

`AVCaptureVideoDataOutput` is used to process uncompressed frames from the video being captured. An instance of `AVCaptureVideoDataOutput` produces video frames you can process using other media APIs. You can access the frames with the `captureOutput:didOutputSampleBuffer:fromConnection:` delegate method. Use `setSampleBufferDelegate:queue:` to set the sample buffer delegate and the queue on which callbacks should be invoked. The delegate of an `AVCaptureVideoDataOutputSampleBuffer` object must adopt the `AVCaptureVideoDataOutputSampleBufferDelegate` protocol. Use the `sessionPreset` property to customize the quality of the output.

You invoke the capture session `startRunning` method to start the flow of data from the inputs to the outputs, and `stopRunning` to stop the flow.

Listing 1 shows an example of this. `setupCaptureSession` creates a capture session, adds a video input to provide video frames, adds an output destination to access the captured frames, then starts flow of data from the inputs to the outputs. While the capture session is running, the captured video sample buffers are sent to the sample buffer delegate using `captureOutput:didOutputSampleBuffer:fromConnection:`. Each sample buffer (`CMSampleBufferRef`) is then converted to a `UIImage` in `imageFromSampleBuffer`.

__Listing 1__  Configuring a capture device to record video with AV Foundation and saving the frames as `UIImage` objects.

```objc
#import <AVFoundation/AVFoundation.h>

// Create and configure a capture session and start it running
- (void)setupCaptureSession
{
    NSError *error = nil;

    // Create the session
    AVCaptureSession *session = [[AVCaptureSession alloc] init];

    // Configure the session to produce lower resolution video frames, if your
    // processing algorithm can cope. We'll specify medium quality for the
    // chosen device.
    session.sessionPreset = AVCaptureSessionPresetMedium;

    // Find a suitable AVCaptureDevice
    AVCaptureDevice *device = [AVCaptureDevice
                             defaultDeviceWithMediaType:AVMediaTypeVideo];

    // Create a device input with the device and add it to the session.
    AVCaptureDeviceInput *input = [AVCaptureDeviceInput deviceInputWithDevice:device
                                                                    error:&error];
    if (!input) {
        // Handling the error appropriately.
    }
    [session addInput:input];

    // Create a VideoDataOutput and add it to the session
    AVCaptureVideoDataOutput *output = [[[AVCaptureVideoDataOutput alloc] init] autorelease];
    [session addOutput:output];

    // Configure your output.
    dispatch_queue_t queue = dispatch_queue_create("myQueue", NULL);
    [output setSampleBufferDelegate:self queue:queue];
    dispatch_release(queue);

    // Specify the pixel format
    output.videoSettings =
                [NSDictionary dictionaryWithObject:
                    [NSNumber numberWithInt:kCVPixelFormatType_32BGRA]
                    forKey:(id)kCVPixelBufferPixelFormatTypeKey];


    // If you wish to cap the frame rate to a known value, such as 15 fps, set
    // minFrameDuration.
    output.minFrameDuration = CMTimeMake(1, 15);

    // Start the session running to start the flow of data
    [session startRunning];

    // Assign session to an ivar.
    [self setSession:session];
}

// Delegate routine that is called when a sample buffer was written
- (void)captureOutput:(AVCaptureOutput *)captureOutput
         didOutputSampleBuffer:(CMSampleBufferRef)sampleBuffer
         fromConnection:(AVCaptureConnection *)connection
{
    // Create a UIImage from the sample buffer data
    UIImage *image = [self imageFromSampleBuffer:sampleBuffer];

     < Add your code here that uses the image >

}

// Create a UIImage from sample buffer data
- (UIImage *) imageFromSampleBuffer:(CMSampleBufferRef) sampleBuffer
{
    // Get a CMSampleBuffer's Core Video image buffer for the media data
    CVImageBufferRef imageBuffer = CMSampleBufferGetImageBuffer(sampleBuffer);
    // Lock the base address of the pixel buffer
    CVPixelBufferLockBaseAddress(imageBuffer, 0);

    // Get the number of bytes per row for the pixel buffer
    void *baseAddress = CVPixelBufferGetBaseAddress(imageBuffer);

    // Get the number of bytes per row for the pixel buffer
    size_t bytesPerRow = CVPixelBufferGetBytesPerRow(imageBuffer);
    // Get the pixel buffer width and height
    size_t width = CVPixelBufferGetWidth(imageBuffer);
    size_t height = CVPixelBufferGetHeight(imageBuffer);

    // Create a device-dependent RGB color space
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();

    // Create a bitmap graphics context with the sample buffer data
    CGContextRef context = CGBitmapContextCreate(baseAddress, width, height, 8,
      bytesPerRow, colorSpace, kCGBitmapByteOrder32Little | kCGImageAlphaPremultipliedFirst);
    // Create a Quartz image from the pixel data in the bitmap graphics context
    CGImageRef quartzImage = CGBitmapContextCreateImage(context);
    // Unlock the pixel buffer
    CVPixelBufferUnlockBaseAddress(imageBuffer,0);

    // Free up the context and color space
    CGContextRelease(context);
    CGColorSpaceRelease(colorSpace);

    // Create an image object from the Quartz image
    UIImage *image = [UIImage imageWithCGImage:quartzImage];

    // Release the Quartz image
    CGImageRelease(quartzImage);

    return (image);
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2010-09-29 | Updated the imageFromSampleBuffer code to correctly create a UIImage from the sample buffer data. |
| 2010-07-20 | New document that shows how to capture video frames from the camera as images using AV Foundation on iOS |

