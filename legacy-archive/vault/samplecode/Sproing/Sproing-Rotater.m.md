---
title: Sproing
apple_id: DTS10000408
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2011-08-24'
source_url: https://developer.apple.com/library/archive/samplecode/Sproing/Listings/Sproing_Rotater_m.html
archived_at: '2026-07-18T03:25:29.483298Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Sproing](Sproing.md)


[Next](Document%20Revision%20History.md)[Previous](Sproing-Rotater.h.md)

# Sproing/Rotater.m

```objc
/*
     File: Rotater.m 
 Abstract: Rotater simulates an arm which rotates about the specified origin.
 It knows how much of an angle to rotate per frame, but doesn't know
 anything about real time -- you have to send -animate at the correct
 time to advance each frame. 
  Version: 1.1 

 Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple 
 Inc. ("Apple") in consideration of your agreement to the following 
 terms, and your use, installation, modification or redistribution of 
 this Apple software constitutes acceptance of these terms.  If you do 
 not agree with these terms, please do not use, install, modify or 
 redistribute this Apple software. 

 In consideration of your agreement to abide by the following terms, and 
 subject to these terms, Apple grants you a personal, non-exclusive 
 license, under Apple's copyrights in this original Apple software (the 
 "Apple Software"), to use, reproduce, modify and redistribute the Apple 
 Software, with or without modifications, in source and/or binary forms; 
 provided that if you redistribute the Apple Software in its entirety and 
 without modifications, you must retain this notice and the following 
 text and disclaimers in all such redistributions of the Apple Software. 
 Neither the name, trademarks, service marks or logos of Apple Inc. may 
 be used to endorse or promote products derived from the Apple Software 
 without specific prior written permission from Apple.  Except as 
 expressly stated in this notice, no other rights or licenses, express or 
 implied, are granted by Apple herein, including but not limited to any 
 patent rights that may be infringed by your derivative works or by other 
 works in which the Apple Software may be incorporated. 

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

 Copyright (C) 2011 Apple Inc. All Rights Reserved. 

 */


#import "Rotater.h"

#define PI              (2 * asin (1.0))

//  Number of animation frames for any point to catch up to "wheel"
#define FRAMES_TO_SYNC  50

#define DEFAULT_RADIANS_PER_FRAME   (PI/40)
#define DEFAULT_ARM_LENGTH          200


@implementation Rotater

@synthesize origin;
@synthesize radiansPerFrame;
@synthesize armLength;

#pragma mark PUBLIC INSTANCE METHODS -- OVERRIDES FROM NSObject

- (id) init
{
    self = [super init];
    if (self == nil) return self;       // tripped on our shoelaces?

    self.radiansPerFrame = DEFAULT_RADIANS_PER_FRAME;
    self.armLength = DEFAULT_ARM_LENGTH;

    return self;
}


#pragma mark PUBLIC INSTANCE METHODS

- (void) animate                        // move to the next angle
{
    //  Just move the angle; the client must ask for X and Y.
    angle += radiansPerFrame;
}

- (void) setXY:(NSSize)point
{
    NSPoint newPoint = NSMakePoint(point.width, point.height);

    if (NSEqualPoints (newPoint, mostRecentPoint))
        return;

    //  Remember where we are now
    mostRecentPoint = newPoint;

    //  Initialize the catch-up fraction to 100%
    syncFraction = 1.0;
}

- (NSSize) getXY
{
    CGFloat x, y;

    //  Figure where we OUGHT to be (high-school trig is useful, after all)
    x = origin.x + (armLength * cos (angle));
    y = origin.y + (armLength * sin (angle));

    //  If the client did a 'set' to some odd place, partially accomodate
    //  that displacement. And reduce that ÒaccomodationÓ a little bit each time.
    if (syncFraction > 0.0)
    {
        x += syncFraction * (mostRecentPoint.x - x);
        y += syncFraction * (mostRecentPoint.y - y);

        syncFraction -= (1.0 / FRAMES_TO_SYNC);
    }

    //  Round everything
    x = floor (x + 0.5);
    y = floor (y + 0.5);

    mostRecentPoint = NSMakePoint (x, y);
    return NSMakeSize(x, y);
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](Sproing-Rotater.h.md)

