---
title: How do I achieve smooth video scrubbing with AVPlayer seekToTime:?
apple_id: DTS40016828
resource_type: QA
platform: iOS|macOS
topic: Audio, Video, & Visual Effects
technology: AVFoundation
published: '2016-03-23'
source_url: https://developer.apple.com/library/archive/qa/qa1820/_index.html
archived_at: '2026-07-18T02:34:55.971016Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1820

# How do I achieve smooth video scrubbing with AVPlayer seekToTime:?

## Q:  My app allows the user to scrub video files using a slider control in combination with `AVPlayer` `seekToTime`: but there is a considerable lag in the display of the video frames. How can I achieve smoother scrubbing?

A: Avoid making calls to `AVPlayer` `seekToTime`: in rapid succession. This will cancel the seeks in progress, resulting in a lot of seeking and not a lot of displaying of the target frames. Instead, use the completion handler variant of `AVPlayer` `seekToTime`:, and wait for a seek in progress to complete first before issuing another. Listing 1 and Listing 2 give examples of this technique (Note: these examples assume a valid player object has been created and the player's current item status is being maintained via key-value observing. See the [AV Foundation Programming Guide](https://developer.apple.com/library/ios/documentation/AudioVideo/Conceptual/AVFoundationPG/) for more information):

__Listing 1__  Using the completion handler variant of `AVPlayer` `seekToTime`: for smoother scrubbing (Swift).

```swift
import AVFoundation

class MyClass {

    var isSeekInProgress = false
    let player = <#A valid player object #>
    var chaseTime = kCMTimeZero
    // your player.currentItem.status
    var playerCurrentItemStatus:AVPlayerItemStatus = .Unknown

    ...

    func stopPlayingAndSeekSmoothlyToTime(newChaseTime:CMTime)
    {
        player.pause()

        if CMTimeCompare(newChaseTime, chaseTime) != 0
        {
            chaseTime = newChaseTime;

            if !isSeekInProgress
            {
                trySeekToChaseTime()
            }
        }
    }

    func trySeekToChaseTime()
    {
        if playerCurrentItemStatus == .Unknown
        {
            // wait until item becomes ready (KVO player.currentItem.status)
        }
        else if playerCurrentItemStatus == .ReadyToPlay
        {
            actuallySeekToTime()
        }
    }

    func actuallySeekToTime()
    {
        isSeekInProgress = true
        let seekTimeInProgress = chaseTime
        player.seekToTime(seekTimeInProgress, toleranceBefore: kCMTimeZero,
                toleranceAfter: kCMTimeZero, completionHandler:
        { (isFinished:Bool) -> Void in

            if CMTimeCompare(seekTimeInProgress, chaseTime) == 0
            {
                isSeekInProgress = false
            }
            else
            {
                trySeekToChaseTime()
            }
        })
    }

}
```


__Listing 2__  Using the completion handler variant of `AVPlayer` `seekToTime`: for smoother scrubbing (Objective-C).

```objc
@import AVFoundation;

@interface MyClass ()
{
    AVPlayer player;
    BOOL isSeekInProgress;
    CMTime chaseTime;
    AVPlayerStatus playerCurrentItemStatus; // your player.currentItem.status
    ...
}

@implementation MyClass

...

- (void)stopPlayingAndSeekSmoothlyToTime:(CMTime)newChaseTime
{
    [self->player pause];

    if (CMTIME_COMPARE_INLINE(newChaseTime, !=, self->chaseTime))
    {
        self->chaseTime = newChaseTime;

        if (!self->isSeekInProgress)
            [self trySeekToChaseTime];
    }
}

- (void)trySeekToChaseTime
{
    if (playerCurrentItemStatus == AVPlayerItemStatusUnknown)
    {
        // wait until item becomes ready (KVO player.currentItem.status)
    }
    else if (playerCurrentItemStatus == AVPlayerItemStatusReadyToPlay)
    {
        [self actuallySeekToTime];
    }
}

- (void)actuallySeekToTime
{
    self->isSeekInProgress = YES;
    CMTime seekTimeInProgress = self->chaseTime;
    [self->player seekToTime:seekTimeInProgress toleranceBefore:kCMTimeZero
    toleranceAfter:kCMTimeZero completionHandler:
     ^(BOOL isFinished)
     {
         if (CMTIME_COMPARE_INLINE(seekTimeInProgress, ==, self->chaseTime))
             self->isSeekInProgress = NO;
         else
             [self trySeekToChaseTime];
     }];
}

@end
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-03-23 | New document that how to achieve smooth video scrubbing with AVPlayer seekToTime: |

