---
title: WaveformViewDemo
apple_id: DTS40008653
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: null
published: '2009-04-15'
source_url: https://developer.apple.com/library/archive/samplecode/WaveformViewDemo/Listings/Source_CocoaUI_CAWaveformView_mm.html
archived_at: '2026-07-18T03:28:09.076045Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WaveformViewDemo](WaveformViewDemo.md)


[Next](Source-CocoaUI-CAWaveformViewSharedData.h.md)[Previous](Source-CocoaUI-CAWaveformView.h.md)

# Source/CocoaUI/CAWaveformView.mm

```objc
/*  Copyright © 2007 Apple Inc. All Rights Reserved.

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
*/
#import "CAWaveformView.h"

#define NSRectToCGRect(r) CGRectMake(r.origin.x, r.origin.y, r.size.width, r.size.height)


@implementation CAWaveformView

#pragma mark ___Initialization___



- (void) Initialize
{
    backgroundColor = [[NSColor colorWithCalibratedRed: 95.0/255.0 green: 95.0/255.0 blue: 95.0/255.0 alpha:1.0] retain];
    lineColor = [[NSColor colorWithCalibratedRed: 0 green: 0 blue: 0 alpha:1.0] retain];

    [myBackgroundWell setColor:backgroundColor];        
    [myLineWell setColor: lineColor];

    if (waveformPoints) 
        free(waveformPoints);   

    waveformPoints = (CGPoint*) malloc(2*kMaxWaveformSamples*sizeof(CGPoint));  


}

- (id)initWithFrame:(NSRect)frame 
{
    self = [super initWithFrame:frame];
    if (self) {
        waveformPoints = NULL;
        [self Initialize];
   }
    return self;
}


- (void) dealloc
{   
    if (backgroundColor) [backgroundColor release];
    if (lineColor) [lineColor release];

    if (waveformPoints) {
        free(waveformPoints);
        waveformPoints = NULL;
    }

    [super dealloc];
}

#pragma mark ___IBActions___

- (void) setLineColor:(NSColor*) color
{
    if ( color != lineColor ) {
        [color retain];
        [lineColor release];
        lineColor = color;
    }
}

- (void) setBackgroundColor:(NSColor*) color
{
    if ( color != backgroundColor ) {
        [color retain];
        [backgroundColor release];
        backgroundColor = color;
    }
}

- (IBAction) changeBackgroundColor: (id) sender
{
    [self setBackgroundColor : [sender color]];
    [self setNeedsDisplay: YES];
}

- (IBAction) changeLineColor: (id) sender
{
    [self  setLineColor: [sender color]];
    [self setNeedsDisplay: YES];
}

#pragma mark ___Drawing___

- (NSRect) getRect
{
    return [self frame];
}

- (void) plotNum: (UInt32) num dataPoints:(Float32*) data
{
    if (num < 1) return;

    if ([myHoldButton state] == NSOnState) return;

    NSRect r = [self getRect];

    Float32 width   = r.size.width;
    Float32 height  = r.size.height;

    Float32 dy = height / 2. / 1.5;
    UInt32 pixelWidth = (UInt32) width; 
    UInt32 stride = num / pixelWidth;

    UInt32 mid = (UInt32) ( height / 2.0);

    // make the first point 
    waveformPointsCount = 0;
    Float32 value = mid + data[0] * dy;
    waveformPoints[waveformPointsCount].x = 0;
    waveformPoints[waveformPointsCount].y = value;
    waveformPointsCount++;

    UInt32 sampleIndex;
    for (UInt32 i= 1; i< pixelWidth; i++){

        sampleIndex = i*stride;     
        value = mid + data[sampleIndex] * dy;

        waveformPoints[waveformPointsCount].x   = i;
        waveformPoints[waveformPointsCount].y   = value;
        waveformPointsCount++;

        waveformPoints[waveformPointsCount].x   = i;
        waveformPoints[waveformPointsCount].y   = value;
        waveformPointsCount++;

     }

    value = waveformPoints[waveformPointsCount-1].y;
    waveformPoints[waveformPointsCount].x       = pixelWidth;
    waveformPoints[waveformPointsCount].y       = value;    

    [self setNeedsDisplay: YES];
}


- (void) drawRect: (NSRect) rect
{
    if (waveformPointsCount < 1) return;

    NSGraphicsContext *nsctx = [NSGraphicsContext currentContext];
    CGContextRef context = (CGContextRef)[nsctx graphicsPort];
    CGRect r = NSRectToCGRect(rect);

    CGContextSetRGBFillColor(context, 
    [backgroundColor redComponent], [backgroundColor greenComponent], [backgroundColor blueComponent], 
    [backgroundColor alphaComponent]);
    CGContextFillRect(context, r);

    CGContextSetRGBStrokeColor(context,[lineColor redComponent], [lineColor greenComponent], [lineColor blueComponent], 
    [lineColor alphaComponent]);
    CGContextStrokeLineSegments(context, waveformPoints, waveformPointsCount);

}

@end
```

[Next](Source-CocoaUI-CAWaveformViewSharedData.h.md)[Previous](Source-CocoaUI-CAWaveformView.h.md)

