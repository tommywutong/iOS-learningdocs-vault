---
title: Capturing a sequence of still images very quickly with AV Foundation on iOS
apple_id: DTS40014711
resource_type: QA
platform: iOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2014-07-17'
source_url: https://developer.apple.com/library/archive/qa/qa1865/_index.html
archived_at: '2026-07-18T02:35:09.408837Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1865

# Capturing a sequence of still images very quickly with AV Foundation on iOS

## Q:  How can I capture a series of still images in rapid succession using AV Foundation?

A: Call the `captureStillImageAsynchronously:completionHandler:` method a number of times in a row, and they'll be serviced as fast as possible with the results delivered to your completion handler. However, there is a limit to how many outstanding still image requests you can queue up. The current limit is 10. On the 11th outstanding request, you'll get an error.

The recommended approach is to use a timer that fires at an interval about equal to your device’s `activeVideoMaxFrameDuration` as shown in Listing 1:

__Listing 1__  How to capture a number of still images in rapid succession using a timer.

```objc
#import <AVFoundation/AVFoundation.h>

// Maximum number of queued still image requests.
int const MaxStillImageRequests = 10;

@interface MyController : UIViewController

@property dispatch_source_t timer;
@property int stillImageRequests; // Number of queued still image capture requests.
@property int imagesCaptured; // Number of still images captured.

-(void)captureImages:(int)count;

@end

...

//
// Capture still images in rapid succession
//
//     count = number of images to capture
//
-(void)captureImages:(int)count
{
    self.stillImageRequests = 0;
    self.imagesCaptured = 0;

    dispatch_queue_t timerQueue =
        dispatch_queue_create("timer queue",DISPATCH_QUEUE_SERIAL);
    // Create dispatch source that submits the event handler block based on a timer.
    self.timer = dispatch_source_create(DISPATCH_SOURCE_TYPE_TIMER,
                                        0, // unused
                                        DISPATCH_TIMER_STRICT,
                                        timerQueue);
    // Set the event handler block for the timer dispatch source.
    dispatch_source_set_event_handler(self.timer, ^{

        // This block will attempt to capture a new still image each time it is called.

        // Captured requested number of images?
        if (self.imagesCaptured >= count)
        {
            // Done capturing, kill the timer.
            dispatch_source_cancel(self.timer);
        }
        else if (self.stillImageRequests >= MaxStillImageRequests)
        {
           // Don't capture another image if the maximum
           // number of outstanding still image requests has
           // been exceeded.
        }
        else
        {
            self.stillImageRequests++;
            self.imagesCaptured++;

            // Capture a still image.

            AVCaptureStillImageOutput *stillImageOutput =
               <# a AVCaptureStillImageOutput #>;
            [stillImageOutput captureStillImageAsynchronouslyFromConnection:
                 [stillImageOutput connectionWithMediaType:AVMediaTypeVideo]
                     completionHandler:
             ^(CMSampleBufferRef imageDataSampleBuffer, NSError *error)
             {
                 self.stillImageRequests--;

                 if (error)
                 {
                     // Handle the error.
                 }
                 else if (imageDataSampleBuffer)
                 {
                     // Do something with the captured image.
                 }
             }];
        }
    });

    // Timer interval -- use your device’s activeVideoMaxFrameDuration
    uint64_t interval = 0.04;
    // Set timer start time and interval.
    dispatch_source_set_timer(self.timer,
                              dispatch_time(DISPATCH_TIME_NOW, 0), // start time
                              interval * NSEC_PER_SEC, // interval
                              interval * NSEC_PER_SEC); // leeway
    dispatch_resume(self.timer);

}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-07-17 | New document that discusses how to capture a number of still images very quickly with AV Foundation on iOS. |

