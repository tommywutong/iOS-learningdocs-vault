---
title: iChatTheater
apple_id: DTS10004197
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2012-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/iChatTheater/Listings/SlideshowView_m.html
archived_at: '2026-07-18T03:29:34.860592Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iChatTheater](iChatTheater.md)


[Next](SoundAdditions.h.md)[Previous](SlideshowView.h.md)

# SlideshowView.m

```objc
/*

 File: SlideshowView.m

 Abstract: This view class is designed to render into an arbitrary
           NSGraphicsContext in a thread-safe manner. When drawing on
           screen via the -drawRect: method on the main thread, it
           renders into its bounds rectangle. When drawing into the
           CVPixelBufferRef via the -renderIntoPixelBuffer:forTime:
           method on a separate thread, it renders into the bounds of
           the supplied buffer. It also keeps track of changes so that
           it can skip re-rendering an identical image for iChat Theater.

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

#import "SlideshowView.h"
#import "SoundAdditions.h"
#import <InstantMessage/IMService.h>
#import <InstantMessage/IMAVManager.h>
#import <CoreVideo/CoreVideo.h>

#define kDefaultSlideshowDir @"/Library/Desktop Pictures/Plants"
#define kSavedSlideshowDirPref @"LastSlideshowDir"

#define kFramerate       30.0
#define kSlideDuration    4.0
#define kTransitionTime   0.5
#define kPauseLabelSize  60.0

#define kDefaultFocusPoint NSMakePoint(-100.0, -100.0)

#define kNoTime UINT64_MAX

@implementation SlideshowView

#pragma mark -
#pragma mark Lifecycle

// Clear the dates used to time how far into the slideshow we are.
- (void) _clearTimes {
    _startTime = _pauseTime = kNoTime;
}

- (void) awakeFromNib {
    // Initialise the focus point ivars.
    _focusPoint = _lastRenderFocusPoint = kDefaultFocusPoint;
    [self _clearTimes];

    [self registerForDraggedTypes:[NSArray arrayWithObject:NSFilenamesPboardType]];

    NSString *savedDir = [[NSUserDefaults standardUserDefaults] objectForKey:kSavedSlideshowDirPref];
    BOOL isDir = NO;
    BOOL exists = (savedDir != nil && [[NSFileManager defaultManager] fileExistsAtPath:savedDir isDirectory:&isDir]);
    if (exists && isDir)
        [self performSelector:@selector(_loadImagesAtPath:) withObject:savedDir];
}

- (void) dealloc {
    [self stop];

    [_imagePath release];
    [_images release];
    [_focusImage release];

    [super dealloc];
}

- (NSArray *) _imagesAtPath:(NSString *)path {
    // Load all images up front for simplicity.
    // This gets very slow (not to mention menory intensive) with a large 
    // directory of images - a great enhancement for this class would be to 
    // load the image files as we go during playback.
    NSMutableArray *images = [NSMutableArray array];
    NSDirectoryEnumerator *files = [[NSFileManager defaultManager] enumeratorAtPath:path];
    NSString *filepath;

    while ((filepath = [files nextObject]) != nil) {
        NSImage *image = [[NSImage alloc] initWithContentsOfFile:[path stringByAppendingPathComponent:filepath]];
        if (image != nil)
            [images addObject:image];
        [image release];
    }

    return images;
}

- (void) _loadImagesAtPath:(NSString *)path {
    if (![_imagePath isEqualToString:path]) {
        if (_images != nil)
            [self stop];

        [_images release];
        _images = [[self _imagesAtPath:path] copy];

        _imagePath = [path copy];
    }
}

#pragma mark -
#pragma mark Drag and Drop

- (NSDragOperation) draggingEntered:(id <NSDraggingInfo>)sender {
    return [self draggingUpdated:sender];
}

- (NSDragOperation) draggingUpdated:(id <NSDraggingInfo>)sender {
    NSArray *filenames = [[sender draggingPasteboard] propertyListForType:NSFilenamesPboardType];
    BOOL isDir = NO;
    if ([filenames count] == 1) {
        BOOL exists = [[NSFileManager defaultManager] fileExistsAtPath:[filenames lastObject] isDirectory:&isDir];
        if (!exists)
            isDir = NO;
    }

    return isDir ? NSDragOperationCopy : NSDragOperationNone;
}

- (void) draggingExited:(id <NSDraggingInfo>)sender { }

- (BOOL) prepareForDragOperation:(id <NSDraggingInfo>)sender {
    return YES;
}

- (BOOL) performDragOperation:(id <NSDraggingInfo>)sender {
    NSArray *filenames = [[sender draggingPasteboard] propertyListForType:NSFilenamesPboardType];
    NSString *dirPath = [filenames lastObject];
    [self _loadImagesAtPath:dirPath];
    [[NSUserDefaults standardUserDefaults] setObject:dirPath forKey:kSavedSlideshowDirPref];
    return YES;
}

- (void) concludeDragOperation:(id <NSDraggingInfo>)sender { }

#pragma mark -
#pragma mark Rendering

- (BOOL)isOpaque
{
    return YES;
}

// Convenience method to draw an image in a rect, scaling to fit maximally.
- (void) _drawImage:(NSImage *)image inRect:(NSRect)rect fraction:(float)fraction {
    if (image != nil) {
        NSRect imageBounds = { NSZeroPoint, [image size] };
        float scaledHeight = NSWidth(rect) * NSHeight(imageBounds);
        float scaledWidth  = NSHeight(rect) * NSWidth(imageBounds);

        if (scaledHeight < scaledWidth) {
            // rect is wider than image: fit height
            float horizMargin = NSWidth(rect) - scaledWidth / NSHeight(imageBounds);
            rect.origin.x += horizMargin / 2.0;
            rect.size.width -= horizMargin;
        } else {
            // rect is taller than image: fit width
            float vertMargin = NSHeight(rect) - scaledHeight / NSWidth(imageBounds);
            rect.origin.y += vertMargin / 2.0;
            rect.size.height -= vertMargin;
        }

        [image drawInRect:rect fromRect:imageBounds operation:NSCompositeSourceOver fraction:fraction];
    }
}

// Determine which image(s) to display, and how much fading to do between the current and previous image.
// If not in a transition, write back into timeInOut the time at which the previous transition ended.
// The outCurrentImage, outPrevImage, and outProgress parameters are optional.
- (void) _getCurrentImage:(NSImage **)outCurrentImage prevImage:(NSImage **)outPrevImage progress:(float *)outProgress forTime:(uint64_t *)timeInOut {
    unsigned n = [_images count];
    if (_startTime == kNoTime || n == 0) {
        // Write out appropriate values if we're not playing.
        if (outCurrentImage != NULL)
            *outCurrentImage = NULL;
        if (outPrevImage != NULL)
            *outPrevImage = NULL;
        if (outProgress != NULL)
            *outProgress = 0.0;
        if (timeInOut != NULL)
            *timeInOut = kNoTime;
        return;
    }

    // Determine slideshow progress.
    uint64_t elapsedTime = (_pauseTime == kNoTime || *timeInOut < _pauseTime) ? (*timeInOut - _startTime) : (_pauseTime - _startTime);
    double elapsed = (double)elapsedTime / CVGetHostClockFrequency();
    float curIndexProgress = elapsed / kSlideDuration;
    int curImageIndex = curIndexProgress;

    // Progress: 0..1 during the last kTransitionTime seconds of a slide's duration.
    // Note that we set the prevImageIndex to -1 if the current image is fully
    // opaque.
    float progress = MIN(1.0, (curIndexProgress - curImageIndex) / (kTransitionTime / kSlideDuration));
    int prevImageIndex = (progress < 1.0) ? curImageIndex - 1 : -1;
    if (outProgress != NULL)
        *outProgress = progress;

    // Write appropriate value into timeInOut
    if (_pauseTime != kNoTime) {
        // paused: the image will correspond to the time we actually paused
        *timeInOut = _pauseTime;                                                    
    } else if (prevImageIndex == -1) {
        // still frame: the time the current image first appeared fully opaque
        *timeInOut = _startTime + CVGetHostClockFrequency() * (kTransitionTime + curImageIndex * kSlideDuration);
    } else {
        // in transition: rendering will correspond exactly to the supplied timestamp
    }

    // Get images by index.
    if (outCurrentImage != NULL)
        *outCurrentImage  = (curImageIndex  < 0) ? nil : [_images objectAtIndex:(curImageIndex  % n)];
    if (outPrevImage != NULL)
        *outPrevImage = (prevImageIndex < 0) ? nil : [_images objectAtIndex:(prevImageIndex % n)];
}

- (void) _drawFocusPoint:(NSPoint)focusPoint inBounds:(NSRect)bounds {
    // Load 'red dot' image if necessary (will be cached in the 
    // _focusImage ivar after the first use).
    if (_focusImage == nil)
        _focusImage = [[NSImage imageNamed:@"laser-dot"] retain];

    // Adjust laser pointer point (in frame bounds) to supplied bounds.
    NSRect frameBounds = [self bounds];
    NSPoint adjPoint = NSMakePoint(floor(focusPoint.x * NSWidth(bounds)  / NSWidth(frameBounds)),
                                   floor(focusPoint.y * NSHeight(bounds) / NSHeight(frameBounds)));

    // Center the image over the point. Scale the laser pointer relative to the size of the bounds.
    NSRect srcRect = { NSZeroPoint, [_focusImage size] };
    float dstSize = MIN(NSWidth(bounds), NSHeight(bounds)) / 30.0;
    NSRect dstRect = NSMakeRect(adjPoint.x - dstSize  / 2.0,
                                adjPoint.y - dstSize / 2.0,
                                dstSize, dstSize);

    [_focusImage drawInRect:dstRect
                   fromRect:srcRect
                  operation:NSCompositeSourceOver
                   fraction:1.0];
}

- (void) _drawImage:(NSImage *)image prevImage:(NSImage *)prevImage progress:(float)progress focusPoint:(NSPoint)focusPoint inBounds:(NSRect)bounds pause:(BOOL)pauseFlag {
    // Clear background before drawing.
    [[NSColor blackColor] set];
    NSRectFill(bounds);

    // Draw image(s).  If there is a 'previous image', we draw that first, 
    // and blend the current image over it.
    [self _drawImage:prevImage inRect:bounds fraction:1.0];
    [self _drawImage:image inRect:bounds fraction:((prevImage == nil) ? 1.0 : progress)];

    // Draw pause indicator
    if (pauseFlag) {
        [[NSColor colorWithCalibratedWhite:0.0 alpha:0.5] set];
        NSRect pauseRect = NSMakeRect(NSMinX(bounds) + (NSWidth(bounds) - kPauseLabelSize) / 2.0,
                                      NSMinY(bounds) + (NSHeight(bounds) - kPauseLabelSize) / 2.0,
                                      kPauseLabelSize / 3.0, kPauseLabelSize);

        NSRectFillListUsingOperation(&pauseRect, 1, NSCompositeSourceOver);

        pauseRect.origin.x += NSWidth(pauseRect) * 2.0;
        NSRectFillListUsingOperation(&pauseRect, 1, NSCompositeSourceOver);
    }

    // Draw laser pointer.
    [self _drawFocusPoint:focusPoint inBounds:bounds];
}

- (void) drawRect:(NSRect)aRect {
    @synchronized(self) {
        // Render for the current time, and update the _lastDrawRectTime with the adjusted value.
        NSImage *currentImage, *prevImage;
        float progress;
        _lastDrawRectTime = CVGetCurrentHostTime();
        [self _getCurrentImage:&currentImage prevImage:&prevImage progress:&progress forTime:&_lastDrawRectTime];

        [self _drawImage:currentImage prevImage:prevImage progress:progress focusPoint:_focusPoint inBounds:[self bounds] pause:(_pauseTime != kNoTime)];
    }
}

- (void) _update {
    // Take the current time, and determine the adjusted time.
    // If it's the same as the _lastDrawRectTime, then there's no need to re-render.
    uint64_t time = CVGetCurrentHostTime();
    [self _getCurrentImage:NULL prevImage:NULL progress:NULL forTime:&time];

    if (time != _lastDrawRectTime)
        [self setNeedsDisplay:YES];
}

#pragma mark -
#pragma mark Play / Pause / Stop

// Starts the slideshow, pretending it actually started timeOffset ago.
// This is used to account for time spent in the pause state,
// and also to allow us to start without a fading transition (we pretend the 
// start date was just long enough ago that the fade has already happened).
- (void) _startWithTimeOffset:(uint64_t)timeOffset {
    _startTime = CVGetCurrentHostTime() - timeOffset;
    [self display];
    _timer = [[NSTimer scheduledTimerWithTimeInterval:(1.0 / kFramerate)
                                               target:self
                                             selector:@selector(_update)
                                             userInfo:nil
                                              repeats:YES] retain];
}

- (void) start {
    [self stop];

    if (_imagePath == nil)
        [self _loadImagesAtPath:kDefaultSlideshowDir];

    // Use a kTransitionTime offset to begin the slideshow with first image 
    // fully opaque
    [self _startWithTimeOffset:kTransitionTime];
    [[self window] makeFirstResponder:self];
}

// Stop the timer used to drive the slideshow.
- (void) _stopTimer {
    [_timer invalidate];
    [_timer release];
    _timer = nil;
}

// Stop the slideshow.
- (void) stop {
    [self _stopTimer];
    [self _clearTimes];
    [self _update];
}

// Toggle the pause state.
- (void) _togglePause {
    if (_startTime != kNoTime) {
        if (_pauseTime == kNoTime) {
            // Play a sound.
            [[NSSound soundNamed:@"Purr"] playMonoForiChat:YES];

            // Pause, recording when this pause started.
            _pauseTime = CVGetCurrentHostTime();

            // Stop the timer user to drive the slideshow (this will stop any
            // updating of frames).
            [self _stopTimer];
        } else {
            // Play a sound.
            [[NSSound soundNamed:@"Hero"] playMonoForiChat:YES];

            // Unpause.
            uint64_t timeOffset = _pauseTime - _startTime;
            [self _clearTimes];

            // Start with an offset to cover the time spent in pause.
            [self _startWithTimeOffset:timeOffset];
        }

        [self _update];
    }
}

- (void) keyDown:(NSEvent *)theEvent {
    if ([[theEvent characters] isEqualToString:@" "])
        [self _togglePause];
}

#pragma mark -
#pragma mark Focus Point

// Hide the mouse pointer (used when the user has the laser pointer 'clicked').
- (void) _hideCursor:(BOOL)flag {
    if (flag != _cursorHidden) {
        if (flag)
            [NSCursor hide];
        else
            [NSCursor unhide];
        _cursorHidden = flag;
    }
}

- (void) _setFocusPoint:(NSEvent *)theEvent {
    // Nil event means mouseUp.
    NSPoint point = (theEvent != nil) ? [self convertPoint:[theEvent locationInWindow] fromView:nil] : kDefaultFocusPoint;

    if (!NSEqualPoints(point, _focusPoint)) {
        // Hide cursor if laser pointer is visible.
        [self _hideCursor:NSPointInRect(point, [self bounds])];

        _focusPoint = point;
        [self setNeedsDisplay:YES];
    }
}

- (void) mouseDown:(NSEvent *)theEvent {
    [self _setFocusPoint:theEvent];
}

- (void) mouseDragged:(NSEvent *)theEvent {
    [self _setFocusPoint:theEvent];
}

- (void) mouseUp:(NSEvent *)theEvent {
    [self _setFocusPoint:nil];
}

#pragma mark -
#pragma mark *** Video Data Source ***

- (void) getPixelBufferPixelFormat:(OSType *)pixelFormatOut {
    *pixelFormatOut = kCVPixelFormatType_32ARGB;
}

- (NSGraphicsContext *) _graphicsContextWithPixelBuffer:(CVPixelBufferRef)buffer {
    // Create a CGBitmapContext with the CVPixelBuffer. Parameters MUST match pixel format returned in _IMGetPixelBufferPixelFormat:, above.
    size_t width = CVPixelBufferGetWidth(buffer);
    size_t height = CVPixelBufferGetHeight(buffer);
    CGColorSpaceRef colorSpace = CGColorSpaceCreateDeviceRGB();
    CGContextRef cgContext = CGBitmapContextCreate(CVPixelBufferGetBaseAddress(buffer),
        width, height,
        8,
        CVPixelBufferGetBytesPerRow(buffer),
        colorSpace,
        kCGImageAlphaPremultipliedFirst);
    CGColorSpaceRelease(colorSpace);

    // Create an NSGraphicsContext.
    NSGraphicsContext *context = [NSGraphicsContext graphicsContextWithGraphicsPort:cgContext flipped:NO];
    CGContextRelease(cgContext);

    return context;
}

- (BOOL) renderIntoPixelBuffer:(CVPixelBufferRef)buffer forTime:(CVTimeStamp *)timeStamp {
    // determine what to render
    NSImage *currentImage, *prevImage;
    float progress;
    uint64_t adjTime = timeStamp->hostTime;
    [self _getCurrentImage:&currentImage prevImage:&prevImage progress:&progress forTime:&adjTime];

    // Don't render if nothing has changed.
    @synchronized(self) {
        if (adjTime == _lastRenderTime && NSEqualPoints(_focusPoint, _lastRenderFocusPoint))
            return NO;
    }

    // Lock the pixel buffer's base address so that we can draw into it.
    if (CVPixelBufferLockBaseAddress(buffer, 0) == kCVReturnSuccess) {

        // Create and use an NSGraphicsContext.
        NSGraphicsContext *context = [self _graphicsContextWithPixelBuffer:buffer];
        if (context != nil) {
            // Synchronize with -drawRect:
            @synchronized(self) {
                NSGraphicsContext *oldContext = [[NSGraphicsContext currentContext] retain];
                [NSGraphicsContext setCurrentContext:context];

                // Render.
                NSRect cleanRect = NSRectFromCGRect(CVImageBufferGetCleanRect(buffer));
                [self _drawImage:currentImage prevImage:prevImage progress:progress focusPoint:_focusPoint inBounds:cleanRect pause:NO];
                [context flushGraphics];

                // Clean up and finish.
                timeStamp->hostTime = _lastRenderTime = adjTime;
                _lastRenderFocusPoint = _focusPoint;
                [NSGraphicsContext setCurrentContext:oldContext];
                [oldContext release];
            }

            CVPixelBufferUnlockBaseAddress(buffer, 0);
            return YES;
        }
    }

    return NO;
}

@end
```

[Next](SoundAdditions.h.md)[Previous](SlideshowView.h.md)

