---
title: iChatTheater
apple_id: DTS10004197
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2012-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/iChatTheater/Listings/SoundAdditions_m.html
archived_at: '2026-07-18T03:29:35.085282Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatTheater](iChatTheater.md)


[Next](ThreadedGLView.h.md)[Previous](SoundAdditions.h.md)

# SoundAdditions.m

```objc
/*

 File: SoundAdditions.m

 Abstract: These category methods prepare the receiver to play into
           the iChat Theater audio device if it is available. The
           -[NSSound setChannelMapping:] method is necessary to map
           the audio channels of the sound with those of the iChat
           Theater session.

 Version: 2.0

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
 Apple Inc. ("Apple") in consideration of your agreement to the
 following terms, and your use, installation, modification or
 redistribution of this Apple software constitutes acceptance of these
 terms.  If you do not agree with these terms, please do not use,
 install, modify or redistribute this Apple software.

 In consideration of your agreement to abide by the following terms, and
 subject to these terms, Apple grants you a personal, non-exclusive
 license, under Apple's copyrights in this original Apple software (the
 "Apple Software"), to use, reproduce, modify and redistribute the Apple
 Software, with or without modifications, in source and/or binary forms;
 provided that if you redistribute the Apple Software in its entirety and
 without modifications, you must retain this notice and the following
 text and disclaimers in all such redistributions of the Apple Software. 
 Neither the name, trademarks, service marks or logos of Apple Inc. 
 may be used to endorse or promote products derived from the Apple
 Software without specific prior written permission from Apple.  Except
 as expressly stated in this notice, no other rights or licenses, express
 or implied, are granted by Apple herein, including but not limited to
 any patent rights that may be infringed by your derivative works or by
 other works in which the Apple Software may be incorporated.

 The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
 MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
 THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
 FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
 OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

 IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
 OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
 MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
 AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
 STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.

 Copyright (C) 2007 - 2008 Apple Inc. All Rights Reserved.

 */

#import "SoundAdditions.h"
#import <InstantMessage/IMAVManager.h>

@implementation NSSound (iChatTheaterAdditions)

- (BOOL) playMonoForiChat:(BOOL)flag {
    if (flag) {
        // Set the audio output device.
        IMAVManager *avManager = [IMAVManager sharedAVManager];
        [self setPlaybackDeviceIdentifier:[avManager audioDeviceUID]];

        // Get the channel info for iChat Theater.
        NSArray *channels = [avManager audioDeviceChannels];
        NSUInteger channelCount = [channels count];

        // For a mono sound, map its single channel to those of the IMAVManager (whether mono or stereo).
        NSArray *mapping = (channelCount > 0) ? [NSArray arrayWithObject:channels] : nil;
        [self setChannelMapping:mapping];
    } else {
        // Use default playback device and channel mapping.
        [self setPlaybackDeviceIdentifier:nil];
        [self setChannelMapping:nil];
    }

    return [self play];
}

- (BOOL) playStereoForiChat:(BOOL)flag {
    if (flag) {
        // Set the audio output device.
        IMAVManager *avManager = [IMAVManager sharedAVManager];
        [self setPlaybackDeviceIdentifier:[avManager audioDeviceUID]];

        // Get the channel info for iChat Theater.
        NSArray *channels = [avManager audioDeviceChannels];
        NSUInteger channelCount = [channels count];

        if (channelCount == 2) {
            // Map each channel directly.
            [self setChannelMapping:channels];

        } else if (channelCount == 1) {
            // Map both channels to the same single channel in iChat Theater.
            NSNumber *channel = [channels lastObject];
            [self setChannelMapping:[NSArray arrayWithObjects:channel, channel, nil]];

        } else {
            // No mapping (iChat Theater is not running).
            [self setChannelMapping:nil];
        }
    } else {
        // Use default playback device and channel mapping.
        [self setPlaybackDeviceIdentifier:nil];
        [self setChannelMapping:nil];
    }

    return [self play];
}

@end
```

[Next](ThreadedGLView.h.md)[Previous](SoundAdditions.h.md)

