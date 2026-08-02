---
title: How to capture screen activity to a movie file using AV Foundation on OS X
  10.7 Lion and later
apple_id: DTS40011007
resource_type: QA
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2015-05-20'
source_url: https://developer.apple.com/library/archive/qa/qa1740/_index.html
archived_at: '2026-07-18T02:34:32.407793Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1740

# How to capture screen activity to a movie file using AV Foundation on OS X 10.7 Lion and later

## Q:  How do I capture screen activity to a QuickTime movie on OS X 10.7 Lion and later?

A: On OS X 10.7 Lion and later, the way to make a movie of screen activity is to use AV Foundation.

`// Create an image from the entire main display`

`CGImageRef image = CGDisplayCreateImage(kCGDirectMainDisplay);`

See _[How to take an image snapshot of the screen on Mac OS X Lion](https://developer.apple.com/library/archive/qa/qa1741/_index.html#//apple_ref/doc/uid/DTS40011008)_ for more information.

To perform a real-time screen capture and save it to a QuickTime movie file, you need minimally three AV objects:

- An `AVCaptureSession` object, which coordinates the flow of data from AV input sources to outputs.
- An `AVCaptureScreenInput` object, which is the input data source that provides video data from the given display.
- An `AVCaptureMovieFileOutput` object, which is the output destination for you to write captured media data to a QuickTime movie file.

In the following example, the code creates a capture session, adds a screen input to provide video frames, adds an output destination to save captured frames, starts the flow of data from the input to the output, and stops the flow in 5 seconds. By letting the class conform to the `AVCaptureFileOutputRecordingDelegate` protocol and setting the recording delegate properly, you can monitor when the recording is finished via the delegate method.

__Listing 1__  Conforming to the `AVCaptureFileOutputRecordingDelegate` protocol

```objc
#import <Foundation/Foundation.h>
#import <AVFoundation/AVFoundation.h>

@interface Recorder : NSObject <AVCaptureFileOutputRecordingDelegate> {
@private
    AVCaptureSession *mSession;
    AVCaptureMovieFileOutput *mMovieFileOutput;
    NSTimer *mTimer;
}

-(void)screenRecording:(NSURL *)destPath;

@end
```


__Listing 2__  Screen recording example

```objc
-(void)screenRecording:(NSURL *)destPath
{
    // Create a capture session
    mSession = [[AVCaptureSession alloc] init];

    // Set the session preset as you wish
    mSession.sessionPreset = AVCaptureSessionPresetMedium;

    // If you're on a multi-display system and you want to capture a secondary display,
    // you can call CGGetActiveDisplayList() to get the list of all active displays.
    // For this example, we just specify the main display.
    // To capture both a main and secondary display at the same time, use two active
    // capture sessions, one for each display. On Mac OS X, AVCaptureMovieFileOutput
    // only supports writing to a single video track.
    CGDirectDisplayID displayId = kCGDirectMainDisplay;

    // Create a ScreenInput with the display and add it to the session
    AVCaptureScreenInput *input = [[[AVCaptureScreenInput alloc] initWithDisplayID:displayId] autorelease];
    if (!input) {
        [mSession release];
        mSession = nil;
        return;
    }
    if ([mSession canAddInput:input])
        [mSession addInput:input];

    // Create a MovieFileOutput and add it to the session
    mMovieFileOutput = [[[AVCaptureMovieFileOutput alloc] init] autorelease];
    if ([mSession canAddOutput:mMovieFileOutput])
        [mSession addOutput:mMovieFileOutput];

    // Start running the session
    [mSession startRunning];

    // Delete any existing movie file first
    if ([[NSFileManager defaultManager] fileExistsAtPath:[destPath path]])
    {
        NSError *err;
        if (![[NSFileManager defaultManager] removeItemAtPath:[destPath path] error:&err])
        {
            NSLog(@"Error deleting existing movie %@",[err localizedDescription]);
        }
    }

    // Start recording to the destination movie file
    // The destination path is assumed to end with ".mov", for example, @"/users/master/desktop/capture.mov"
    // Set the recording delegate to self
    [mMovieFileOutput startRecordingToOutputFileURL:destPath recordingDelegate:self];

    // Fire a timer in 5 seconds
    mTimer = [[NSTimer scheduledTimerWithTimeInterval:5 target:self selector:@selector(finishRecord:) userInfo:nil repeats:NO] retain];
}

-(void)finishRecord:(NSTimer *)timer
{
    // Stop recording to the destination movie file
    [mMovieFileOutput stopRecording];

    [mTimer release];
    mTimer = nil;
}

// AVCaptureFileOutputRecordingDelegate methods

- (void)captureOutput:(AVCaptureFileOutput *)captureOutput didFinishRecordingToOutputFileAtURL:(NSURL *)outputFileURL fromConnections:(NSArray *)connections error:(NSError *)error
{
    NSLog(@"Did finish recording to %@ due to error %@", [outputFileURL description], [error description]);

    // Stop running the session
    [mSession stopRunning];

    // Release the session
    [mSession release];
    mSession = nil;
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2015-05-20 | Added additional notes about capturing the main and secondary displays at the same time. Other miscellaneous changes. |
| 2011-08-10 | Corrected a link. |
| 2011-05-13 | New document that shows how to capture screen activity to a movie file using AV Foundation on OS X 10.7 Lion and later. |

