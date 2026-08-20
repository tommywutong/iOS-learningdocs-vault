---
title: LightTable
apple_id: DTS40008927
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2017-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/LightTable/Listings/LightTable_LTView_m.html
archived_at: '2026-07-18T03:13:31.399166Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LightTable](LightTable.md)


[Next](LightTable-DualTouchTracker.m.md)[Previous](LightTable-DragTracker.h.md)

# LightTable/LTView.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This custom view uses CALayers to arange and draw slides. Drag and Drop images onto this view to add them as slides. Double-click a slide to edit the masking of the image to the slide. This view tracks both mouse and touch events to modify the slide. Using two fingers on the trackpad will adjust the position and size of the slide under the cursor.
 */

#import "InputTrackers.h"
#import "LTView.h"
#import "LTMaskLayer.h"

// The _LTOverlayLayer class is used so that our overlay layer with the drag handles is not included in hit testing. Otherwise, hit testing would always return the overlay layer since it is the top layer and fills the entire view. I used an underbar in the classname and implemented it in this file because it is a private helper class of LTView.
@interface LTOverlayLayer : CALayer
@end

@implementation LTOverlayLayer
- (BOOL)containsPoint:(CGPoint)p {
    return NO;
}
@end


#pragma mark Tracking Dictionary Keys
// These are the keys for properties we store in the InputTracker dictionary.
static NSString *kLayerKey = @"layer";
static NSString *kInitialFrameKey = @"initialFrame";
static NSString *kInitialPositionKey = @"initialPosition";
static NSString *kResizeIndexKey = @"resizeIndex";

// This is pointer value that we use as the binding context fot LTView
NSString *kLTOberserverContext = @"LTView.context";

// In 64bit, NS and CG points/rects are interchangeable without compiler warnings. But for 32 bit, we have to do a whole bunch of conversions to make the compiler happy. There is no CG equivalent call for NSPointInRect. We use it a fair amount in this sample, so this macro will make reading the code easier later on.
#define LTPointInRect(p,r) NSPointInRect(NSPointFromCGPoint(p), NSRectFromCGRect(r))

#pragma mark Resize Rect Helpers
static void resizeRectsForFrame(CGRect *resizeRects, CGRect frame) {
    if (!resizeRects) return;
    CGFloat width = 5.0;

    //top left
    resizeRects[0] = CGRectMake(CGRectGetMinX(frame) - width, CGRectGetMaxY(frame), width, width);
    //top middle
    resizeRects[1] = CGRectMake(CGRectGetMidX(frame) - width/2.0, CGRectGetMaxY(frame), width, width);
    //top right
    resizeRects[2] = CGRectMake(CGRectGetMaxX(frame), CGRectGetMaxY(frame), width, width);
    //right middle
    resizeRects[3] = CGRectMake(CGRectGetMaxX(frame), CGRectGetMidY(frame) - width/2.0, width, width);
    //bottom right
    resizeRects[4] = CGRectMake(CGRectGetMaxX(frame), CGRectGetMinY(frame)- width, width, width);
    //bottom middle
    resizeRects[5] = CGRectMake(CGRectGetMidX(frame) - width/2.0, CGRectGetMinY(frame) - width, width, width);
    //bottom left
    resizeRects[6] = CGRectMake(CGRectGetMinX(frame) - width, CGRectGetMinY(frame) - width, width, width);
    //left middle
    resizeRects[7] = CGRectMake(CGRectGetMinX(frame) - width, CGRectGetMidY(frame) - width/2.0, width, width);
}

static NSInteger indexOfResizeRectForPoint(CGRect *resizeRects, CGPoint point) {
    if (!resizeRects) return -1;

    if (LTPointInRect(point, resizeRects[0])) return 0;
    if (LTPointInRect(point, resizeRects[1])) return 1;
    if (LTPointInRect(point, resizeRects[2])) return 2;
    if (LTPointInRect(point, resizeRects[3])) return 3;
    if (LTPointInRect(point, resizeRects[4])) return 4;
    if (LTPointInRect(point, resizeRects[5])) return 5;
    if (LTPointInRect(point, resizeRects[6])) return 6;
    if (LTPointInRect(point, resizeRects[7])) return 7;

    return -1;
}

@interface LTView()
// Private properties:
@property (nonatomic, strong) NSMutableArray *inputTrackers;
@property (nonatomic, strong) LTMaskLayer *editingSlide;
@property (nonatomic, strong) CALayer *overlayLayer;

@property (nonatomic, strong) NSMutableArray *slides;
@property (nonatomic, strong) NSString *keyPath;

// Provate methods:
- (void)_initTrackers;
- (void)drawDragHandleFrames:(CGRect *)handleFrames inContext:(CGContextRef)context;
@end


@implementation LTView

+ (void) initialize{
    [self exposeBinding:kLTViewSlides];
    [self exposeBinding:kLTViewSelectionIndexes];
}

- (instancetype)initWithCoder:(NSCoder *)coder
{
    self = [super initWithCoder:coder];
    if (self) {
        // setup the CALayer for the overall full-screen view
        CALayer *backingLayer = [CALayer layer];
        _overlayLayer = [LTOverlayLayer layer];

        self.layer = backingLayer;
        [self setWantsLayer:YES];

        backingLayer.frame = NSRectToCGRect(self.frame);
        backingLayer.bounds = CGRectMake(0, 0, self.frame.size.width, self.frame.size.height);
        CGColorRef backgroundColor = CGColorCreateGenericRGB(1, 1, 1, 1.0);
        backingLayer.backgroundColor = backgroundColor;
        // The CGColorRef has to be released after assignment as described in Technical Q&A QA1565.
        CFRelease(backgroundColor);
        backingLayer.opaque = YES;

        // The overlay layer is used to draw any drag handles, so that they are always on top of all slides. We must take care to make sure this layer is always the last one.
        _overlayLayer.frame = backingLayer.frame;
        _overlayLayer.opaque = NO;
        _overlayLayer.delegate = self; // We want to be the delegate so we can do the drag handle drawing
        // The CGColorRef has to be released after assignment as described in Technical Q&A QA1565.
        backgroundColor = CGColorCreateGenericRGB(0, 0, 0, 0.0);
        _overlayLayer.backgroundColor = backgroundColor;
        // The CGColorRef has to be released after assignment as described in Technical Q&A QA1565.
        CFRelease(backgroundColor);
        _overlayLayer.autoresizingMask = kCALayerWidthSizable | kCALayerHeightSizable;
        [backingLayer addSublayer:_overlayLayer];

        // init ivars
        _slides = [NSMutableArray array];
        self.selectionIndexes = [NSIndexSet indexSet];

        // init the input trackers
        [self _initTrackers];

        // register for dragging
        [self registerForDraggedTypes:@[NSFilenamesPboardType]];

        // we want touch events
        [self setAcceptsTouchEvents:YES];
    }
    return self;
}

// Create the set of tracker objects the LTView needs. See InputTracker.h for more information.
- (void)_initTrackers {
    _inputTrackers = [NSMutableArray new];

    ClickTracker *clickTracker = [ClickTracker new];
    clickTracker.action = @selector(clickAction:);
    clickTracker.doubleAction = @selector(doubleClickAction:);
    clickTracker.view = self;
    [_inputTrackers addObject:clickTracker];

    DragTracker *dragTracker = [DragTracker new];
    dragTracker.beginTrackingAction = @selector(beginMouseDrag:);
    dragTracker.view = self;
    [_inputTrackers addObject:dragTracker];

    DualTouchTracker *touchTracker = [DualTouchTracker new];
    touchTracker.beginTrackingAction = @selector(dualTouchesBegan:);
    touchTracker.view = self;
    [_inputTrackers addObject:touchTracker];
}


#pragma mark CALayerDelegate

- (void)drawLayer:(CALayer *)layer inContext:(CGContextRef)context {
    CGContextSetFillColorWithColor(context, layer.backgroundColor);
    CGContextFillRect(context, layer.bounds);

    if ((self.selectionIndexes).count) {
        CGContextSetRGBStrokeColor(context, 0, 0, 0, 1);
        CGContextSetRGBFillColor(context, 1, 1, 1, 1);

        for (CALayer *sublayer in [(self.layer).sublayers objectsAtIndexes:self.selectionIndexes]) {
            CGRect frame = sublayer.frame;
            CGRect handleFrames[8] = {0.0};

            resizeRectsForFrame(handleFrames, frame);
            [self drawDragHandleFrames:handleFrames inContext:context];
        }
    }

    if (self.editingSlide) {
        CGContextSetRGBStrokeColor(context, 0, 0, 0, 1);
        CGContextSetRGBFillColor(context, 1, 1, 1, 1);

        CGRect frame = self.editingSlide.photoFrame;
        CGRect handleFrames[8] = {0.0};

        resizeRectsForFrame(handleFrames, frame);
        [self drawDragHandleFrames:handleFrames inContext:context];
    }
}

- (void)drawDragHandleFrames:(CGRect *)handleFrames inContext:(CGContextRef)context {
    CGContextFillRects(context, handleFrames, 8);
    CGContextStrokeRectWithWidth(context, handleFrames[0], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[1], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[2], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[3], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[4], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[5], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[6], 1.0);
    CGContextStrokeRectWithWidth(context, handleFrames[7], 1.0);
}


#pragma mark NSDraggingDestination

- (NSDragOperation)draggingEntered:(id <NSDraggingInfo>)sender {

    NSPasteboard *pboard = [sender draggingPasteboard];
    NSDragOperation sourceDragMask = [sender draggingSourceOperationMask];

    if ( [[pboard types] containsObject:NSFilenamesPboardType] ) {
        if (sourceDragMask & NSDragOperationCopy) {
            return NSDragOperationCopy;
        }
    }
    return NSDragOperationNone;
}

- (BOOL)performDragOperation:(id <NSDraggingInfo>)sender {
    NSPasteboard *draggingPasteboard = [sender draggingPasteboard];
    NSArray *classArray = @[[NSURL class]]; 
    NSDictionary *options = @{NSPasteboardURLReadingContentsConformToTypesKey: [NSImage imageTypes]};
    NSArray *items = [draggingPasteboard readObjectsForClasses:classArray options:options];
    NSPoint slideOrigin = [self convertPoint:[sender draggingLocation] fromView:nil]; // [self convertPointFromBase:[sender draggingLocation]];

    for (NSURL *fileURL in items) {
        id newObject = [self.theNewObjectCreator newObject];
        NSImage *image = [[NSImage alloc] initWithContentsOfURL:fileURL];
        NSSize maxSize = self.bounds.size;
        maxSize.width /= 2.0;
        maxSize.height /= 2.0;
        NSRect slideFrame = {NSZeroPoint, image.size};

        // Reduce the size of the slide until it fits on no more than a quarter of the view.
        while(slideFrame.size.width > maxSize.width || slideFrame.size.height > maxSize.height) {
            slideFrame.size.width /= 2.0;
            slideFrame.size.height /= 2.0;
        }

        // Start the photo filling the entire slide.
        NSRect photoFrame = slideFrame;
        slideFrame.origin = slideOrigin;
        slideFrame.origin.y -= slideFrame.size.height / 2.0;

        [newObject setValue:[NSValue valueWithRect:slideFrame] forKey:kLTViewSlidePropertyFrame];
        [newObject setValue:[NSValue valueWithRect:photoFrame] forKey:kLTViewSlidePropertyPhotoFrame];
        [newObject setValue:[NSData dataWithContentsOfURL:fileURL] forKey:kLTViewSlidePropertyPhoto];

        [self.theNewObjectCreator insertObject:newObject atArrangedObjectIndex:_slides.count];

        // Shift the next image over a bit.
        slideOrigin.x += slideFrame.size.width + 5;
    }

    return YES;
}


#pragma mark NSKeyValueBindingCreation

- (void)bind:(NSString *)binding toObject:(id)observable withKeyPath:(NSString *)keyPath options:(NSDictionary *)options {
    if ([binding isEqualToString:kLTViewSlides]) {
        self.theNewObjectCreator = observable;
        self.keyPath = keyPath;
        [self.theNewObjectCreator addObserver:self forKeyPath:keyPath options:NSKeyValueObservingOptionNew context:(void *)kLTOberserverContext];
        return;
    }

    [super bind:binding toObject:observable withKeyPath:keyPath options:options];
}

- (void)unbind:(NSString *)binding {
    if ([binding isEqualToString:kLTViewSlides]) {
        [self.theNewObjectCreator removeObserver:self forKeyPath:_keyPath];
    }

    [super unbind:binding];
}


#pragma mark NSKeyValueObserving

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context {
    if ([keyPath isEqualTo:self.keyPath] && context == (__bridge void *)kLTOberserverContext) {
        switch([change[NSKeyValueChangeKindKey] integerValue]) {
            case NSKeyValueChangeSetting:
            {
                NSMutableArray *slides = [self mutableArrayValueForKey:kLTViewSlides];
                [slides removeAllObjects];
                [slides addObjectsFromArray:[object valueForKey:self.keyPath]];
                [self.overlayLayer setNeedsDisplay];
            }
                break;

            default:
                break;

        }
        return;
    }

    if (context == (__bridge void *)kLTOberserverContext) {
        LTMaskLayer *layer = nil;
        for (LTMaskLayer *subLayer in (self.layer).sublayers) {
            if (subLayer.source == object) {
                layer = subLayer;
                break;
            }
        }

        if ([keyPath isEqualTo:kLTViewSlidePropertyCornerRadius]) {
            layer.cornerRadius = [[object valueForKeyPath:keyPath] floatValue];
            return;
        }

        if ([keyPath isEqualTo:kLTViewSlidePropertyFrameThickness]) {
            layer.borderWidth = [[object valueForKeyPath:keyPath] floatValue];
            return;
        }

        if ([keyPath isEqualTo:kLTViewSlidePropertyFrame]) {
            layer.frame = NSRectToCGRect([[object valueForKeyPath:keyPath] rectValue]);
            [self.overlayLayer setNeedsDisplay]; // Update drag handles.
            return;
        }

        if ([keyPath isEqualTo:kLTViewSlidePropertyPhotoFrame]) {
            layer.photoLayer.frame = NSRectToCGRect([[object valueForKeyPath:keyPath] rectValue]);
            [self.overlayLayer setNeedsDisplay]; // Update drag handles.
            return;
        }
    }

    [super observeValueForKeyPath:keyPath ofObject:object change:change context:context];
}


#pragma mark NSResponder

// Route all events to the input tracker collection. See InputTracker.h.

- (void)mouseDown:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}

- (void)mouseDragged:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}

- (void)mouseUp:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}

- (void)touchesBeganWithEvent:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}

- (void)touchesMovedWithEvent:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}

- (void)touchesEndedWithEvent:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}

- (void)touchesCancelledWithEvent:(NSEvent *)event {
    [self.inputTrackers makeObjectsPerformSelector:_cmd withObject:event];
}


#pragma mark API

static BOOL gOldAnimationIsDisabled = FALSE;
static double gOldAnimationDuration = 0.25;

@synthesize selectionIndexes = _selectionIndexes;

// These functions set up the Core Animation variables that we want and restore whatever was there.
+ (void)setupCAAnimationStack {
    gOldAnimationIsDisabled = [CATransaction animationDuration];
    gOldAnimationDuration = [CATransaction disableActions];

    [CATransaction setValue:@NO forKey:kCATransactionDisableActions];
    [CATransaction setValue:@0.0f forKey:kCATransactionAnimationDuration];
}

+ (void)restoreCAAnimationStack {
    [CATransaction setValue:@(gOldAnimationIsDisabled) forKey:kCATransactionDisableActions];
    [CATransaction setValue:@(gOldAnimationDuration) forKey:kCATransactionAnimationDuration];
}

- (NSInteger)countOfSlides {
    return self.slides.count;
}

- (id)objectInSlidesAtIndex:(NSInteger)index {
    return self.slides[index];
}

- (NSArray *)slidesAtIndexes:(NSIndexSet *)indexes {
    return [self.slides objectsAtIndexes:indexes];
}

- (void)insertSlides:(NSArray *)array atIndexes:(NSIndexSet *)indexes {
    NSUInteger layerIndex = indexes.firstIndex;

    for (id slide in array) {
        NSImage *image = [[NSImage alloc] initWithData:[slide valueForKey:kLTViewSlidePropertyPhoto]];

        CGRect frame = NSRectToCGRect([[slide valueForKey:kLTViewSlidePropertyFrame] rectValue]);
        LTMaskLayer *slideLayer = [LTMaskLayer layer];
        slideLayer.photo = image;
        slideLayer.frame = frame;
        slideLayer.bounds = CGRectMake(0, 0, frame.size.width, frame.size.height);
        slideLayer.cornerRadius = [[slide valueForKey:kLTViewSlidePropertyCornerRadius] floatValue];
        slideLayer.borderWidth = [[slide valueForKey:kLTViewSlidePropertyFrameThickness] floatValue];
        slideLayer.photoLayer.frame = NSRectToCGRect([[slide valueForKey:kLTViewSlidePropertyPhotoFrame] rectValue]);
        slideLayer.source = slide;

        // Finally insert the layer at the same index of the data source. Note: The data source is always one less than the number of sublayers because we have the overlay layer. This means that we always insert slide layers under the overlay layer (just like we want).
        [self.layer insertSublayer:slideLayer atIndex:(unsigned int)layerIndex];
        layerIndex = [indexes indexGreaterThanIndex:layerIndex];

        // Add observers for the properties that LTView displays. Why not have the LTMaskLayer doing the observing? Mainly because, LTView needs to know about frame changes to update the resizeRects. So we do them all in the same place to keeps things simpler for the sample project.
        [slide addObserver:self forKeyPath:kLTViewSlidePropertyFrame options:0 context:(void *)kLTOberserverContext];
        [slide addObserver:self forKeyPath:kLTViewSlidePropertyPhotoFrame options:0 context:(void *)kLTOberserverContext];
        [slide addObserver:self forKeyPath:kLTViewSlidePropertyCornerRadius options:0 context:(void *)kLTOberserverContext];
        [slide addObserver:self forKeyPath:kLTViewSlidePropertyFrameThickness options:0 context:(void *)kLTOberserverContext];

    }

    [_slides insertObjects:array atIndexes:indexes];
}

- (void)removeSlidesAtIndexes:(NSIndexSet *)indexes {
    // Stop observing all the properties we started observing when we inserted the layer above.
    for (id slide in [_slides objectsAtIndexes:indexes]) {
        [slide removeObserver:self forKeyPath:kLTViewSlidePropertyFrame];
        [slide removeObserver:self forKeyPath:kLTViewSlidePropertyPhotoFrame];
        [slide removeObserver:self forKeyPath:kLTViewSlidePropertyCornerRadius];
        [slide removeObserver:self forKeyPath:kLTViewSlidePropertyFrameThickness];
    }

    // Finally remove all the layers at the same indexes of the data source. Note: The data source is always one less than the number of sublayers because we have the overlay layer. This means that we always remove slide layers under the overlay layer and never the overlay layer itself.
    [self.slides removeObjectsAtIndexes:indexes];

    for (CALayer *layer in [(self.layer).sublayers objectsAtIndexes:indexes]) {
        [layer removeFromSuperlayer];
    }
}

// We commit the changes to the LTMaskLayer at the end of tracking so that we only hit the data source a minimal amount. Also, this way, Undo will undo the whole tracking action instead of just one small step of it.
- (void)commitFrameChangeOfLayer:(LTMaskLayer *)layer {
    CGRect photoFrame;

    // This methods is called when either the mask layer's frame has changed, or when the photo layer's frame has changed. Note, changing the mask layer's frame implies a photo layer frame change, but not the other way around.
    if (layer.superlayer == self.layer) {
        photoFrame = layer.photoLayer.frame;
        [layer.source setValue:[NSValue valueWithRect:NSRectFromCGRect(layer.frame)] forKey:kLTViewSlidePropertyFrame];
    } else {
        layer = (LTMaskLayer *)layer.superlayer;
        photoFrame = layer.photoLayer.frame;
    }

    [layer.source setValue:[NSValue valueWithRect:NSRectFromCGRect(photoFrame)] forKey:kLTViewSlidePropertyPhotoFrame];

    [self.overlayLayer setNeedsDisplay];
}


#pragma mark Input Tracker Support and Actions

- (void)disableTrackersExcluding:(InputTracker*)excluded {
    for (InputTracker *tracker in self.inputTrackers) {
        if (tracker != excluded) {
            tracker.isEnabled = NO;
        }
    }
}

- (void)enableTrackers {
    for (InputTracker *tracker in self.inputTrackers) {
        tracker.isEnabled = YES;
    }
}

// The user clicked and is not in the process of adjusting the photo masking. Modify the selection accordingly. A different set of tracker actions will manage dragging.
- (void)clickAction:(ClickTracker*)tracker {
    CGPoint trackerLocation = NSPointToCGPoint(tracker.location);
    CGPoint layerLocation = [self.overlayLayer convertPoint:trackerLocation fromLayer:self.layer];

    // Check for clicks in any existing resize handles first.
    for (CALayer *sublayer in [(self.layer).sublayers objectsAtIndexes:self.selectionIndexes]) {
        CGRect resizeRects[8] = {0.0};
        resizeRectsForFrame(resizeRects, sublayer.frame);
        NSInteger resizeIndex = indexOfResizeRectForPoint(resizeRects, layerLocation);

        if (resizeIndex >= 0) return; // in resize handle, don't change selection
    }

    // Use layer hit testing to find the targeted layer, if any.
    CALayer *layer = [self.layer hitTest:trackerLocation];
    layer = (layer == self.layer) ? nil : layer;

    if (layer) {
        NSUInteger layerIndex = [(self.layer).sublayers indexOfObject:layer];
        if (layerIndex != NSNotFound) {
            BOOL isCommandDown = ((tracker.modifiers & NSEventModifierFlagCommand) != 0);
            if (isCommandDown) {
                NSMutableIndexSet *newIndexSet = [self.selectionIndexes mutableCopy];

                if ([newIndexSet containsIndex:layerIndex]) {
                    [newIndexSet removeIndex:layerIndex];
                } else {
                    [newIndexSet addIndex:layerIndex];
                    self.selectionIndexes = [[NSIndexSet alloc] initWithIndexSet:newIndexSet];
                }

            } else {
                if (![self.selectionIndexes containsIndex:layerIndex]) {
                    self.selectionIndexes = [NSIndexSet indexSetWithIndex:layerIndex];
                }
            }
        }
    } else {
        self.selectionIndexes = [NSIndexSet indexSet];
    }

    // Redraw resize handles for new selection.
    [self.overlayLayer setNeedsDisplay];
}

// The user clicked while adjusting the photo masking of a slide. If the click is outside the photo's unmasked frame (and not in a resize handle either), then stop adjusting the photo masking.
- (void)editingClickAction:(ClickTracker*)tracker {
    CGPoint layerLocation = [self.layer convertPoint:NSPointToCGPoint(tracker.location) fromLayer:nil];
    if (!LTPointInRect(layerLocation, self.editingSlide.photoFrame)){
        CGRect resizeRects[8];
        resizeRectsForFrame(resizeRects, self.editingSlide.photoFrame);
        NSInteger resizeIndex = indexOfResizeRectForPoint(resizeRects, layerLocation);
        if (resizeIndex < 0) {
            self.editingSlide.masksToBounds = YES;
            self.editingSlide = nil;
            tracker.action = @selector(clickAction:);
            [self clickAction:tracker];
        }
    }
}

// The user double cliked. If adjusting a photo mask, then stop. Otherwise, begin adjusting a photo mask if the double click occured on a slide.
- (void)doubleClickAction:(ClickTracker*)tracker {
    if (self.editingSlide) {
        self.editingSlide.masksToBounds = YES;
        self.editingSlide = nil;
        tracker.action = @selector(clickAction:);
        [self clickAction:tracker];
        [self.overlayLayer setNeedsDisplay];
        return;
    } else {
        CGPoint trackerLocation = NSPointToCGPoint(tracker.location);

        CALayer *layer = [self.layer hitTest:trackerLocation];
        layer = (layer == self.layer) ? nil : layer;

        if (layer) {
            // We don't allow selections during photo mask adjustments.
            self.selectionIndexes = [NSIndexSet indexSet];

            // Begin photo mask adjustment mode.
            self.editingSlide = (LTMaskLayer *)layer;
            layer.masksToBounds = NO;

            // Change the click action because selection modification is not valid in this mode.
            tracker.action = @selector(editingClickAction:);
        }
    }

    // Update the resize handle drawing.
    [self.overlayLayer setNeedsDisplay];
}


// The user has exceeded the drag threshold, and we are not currently tracking touches. Start drag tracking. 
- (void)beginMouseDrag:(DragTracker*)tracker {
    CGPoint layerLocation = [self.layer convertPoint:NSPointToCGPoint(tracker.initialPoint) fromLayer:nil];

    if (self.editingSlide) {
        // The user is adjusting a photo mask
        CALayer *layer = self.editingSlide.photoLayer;

        // Check if the use is resizing via a drag handle
        CGRect resizeRects[8];
        resizeRectsForFrame(resizeRects, self.editingSlide.photoFrame);
        NSInteger resizeIndex = indexOfResizeRectForPoint(resizeRects, layerLocation);

        if (resizeIndex >= 0) {
            // Drag handle resize
            tracker.userInfo = @{kLayerKey: layer,
                                    kInitialFrameKey: [NSValue valueWithRect:NSRectFromCGRect(layer.frame)],
                                    kResizeIndexKey: @(resizeIndex)};

            // Notice how we manage which type of tracking we are performing by simply changing the tracking action methods.
            tracker.updateTrackingAction = @selector(resizeSlide:);
            tracker.endTrackingAction = @selector(resizeSlideEnd:);

            [self disableTrackersExcluding:tracker]; // No other tracking allowed while dragging.
        } else {
            // The user is moving the photo inside the mask. Note: we don't need to confrim this by comparing the mouse location against the photo's frame, because the dragging threshold means the click action will have already fired, making the assessment for us and updated the _editingSlide value.
            NSDictionary *userInfo = @{kLayerKey: layer,
                                    kInitialPositionKey: [NSValue valueWithPoint:NSPointFromCGPoint(layer.position)]};
            tracker.userInfo = @[userInfo];

            // Notice how we manage which type of tracking we are performing by simply changing the tracking action methods.
            tracker.updateTrackingAction = @selector(dragSlides:);
            tracker.endTrackingAction = @selector(dragSlidesEnd:);

            [self disableTrackersExcluding:tracker]; // No other tracking allowed while dragging.
        }
        return;
    }

    // The user is not modifying a photo mask. Determine if the user is resizing via drag handle, moving the selection, or dragging in empty space.
    // Loop through every layer in the selection.
    for (CALayer *layer in [(self.layer).sublayers objectsAtIndexes:self.selectionIndexes]) {
        CGRect resizeRects[8];
        resizeRectsForFrame(resizeRects, layer.frame);
        NSInteger resizeIndex = indexOfResizeRectForPoint(resizeRects, layerLocation);

        // Check the resize handles.
        if (resizeIndex >= 0) {
            // Resize only this layer.
            tracker.userInfo = @{kLayerKey: layer,
                                kInitialFrameKey: [NSValue valueWithRect:NSRectFromCGRect(layer.frame)],
                                kResizeIndexKey: @(resizeIndex)};

            // Notice how we manage which type of tracking we are performing by simply changing the tracking action methods.
            tracker.updateTrackingAction = @selector(resizeSlide:);
            tracker.endTrackingAction = @selector(resizeSlideEnd:);

            [self disableTrackersExcluding:tracker]; // No other tracking allowed while dragging.
            return;
        }

        // Check if the cursor is within this slide. If so, move the entire selection.
        if ([layer containsPoint:[layer convertPoint:layerLocation fromLayer:self.layer]]){
            NSMutableArray *array = [NSMutableArray arrayWithCapacity:(self.selectionIndexes).count];
            for (CALayer *layer in [(self.layer).sublayers objectsAtIndexes:self.selectionIndexes]) {
                NSDictionary *userInfo = @{kLayerKey: layer,
                                        kInitialPositionKey: [NSValue valueWithPoint:NSPointFromCGPoint(layer.position)]};
                [array addObject:userInfo];
            }
            tracker.userInfo = array;

            // Notice how we manage which type of tracking we are performing by simply changing the tracking action methods.
            tracker.updateTrackingAction = @selector(dragSlides:);
            tracker.endTrackingAction = @selector(dragSlidesEnd:);

            [self disableTrackersExcluding:tracker]; // No other tracking allowed while dragging.
            return;
        }
    }

    // If we get here, then the user has dragged in empty space. Notice how we manage which type of tracking we are performing by simply changing the tracking action methods. In this case, the actions are left as nil, so nothing will occur. 

    // A rubber band selection is left as an exercise to the reader.
}

// Mouse dragging of either the selection or of an LTMaskLayer's photo sublayer. Though, this method only looks at an array of CALayers in the tracker userInfo, and does not need to distinguish between the two.
- (void)dragSlides:(DragTracker*)tracker {
    NSPoint delta = tracker.delta;
    NSArray *array = tracker.userInfo;

    // Turn off animation so that each layer is moved immediately.
    [LTView setupCAAnimationStack];
    for (NSDictionary *userInfo in array){
        CALayer *layer = userInfo[kLayerKey];
        NSPoint initialPosition = [userInfo[kInitialPositionKey] pointValue];
        if (layer) {
            initialPosition.x += delta.x;
            initialPosition.y += delta.y;
            layer.position = NSPointToCGPoint(initialPosition);
        }
    }
    [LTView restoreCAAnimationStack];

    // Update drag handles
    [self.overlayLayer setNeedsDisplay];
}

// Mouse dragging of either the selection or of an LTMaskLayer's photo sublayer has ended. Though, this method only looks at an array of CALayers in the tracker userInfo, and does not need to distinguish between the two.
- (void)dragSlidesEnd:(DragTracker*)tracker {    
    [self dragSlides:tracker];

    // Commit the new CALayer frame values to the data source
    for (NSDictionary *userInfo in tracker.userInfo){
        [self commitFrameChangeOfLayer:userInfo[kLayerKey]];
    }

    // reset the tracker back to nil values
    tracker.userInfo = nil;
    tracker.updateTrackingAction = nil;
    tracker.endTrackingAction = nil;

    // Tracking over, re-enable all trackers.
    [self enableTrackers];
}

// Mouse resizing of a layer via a drag handle. This may be an LTMaskLayer or its photo sublayer. Though, this method only looks at the CALayer in the tracker userInfo, and does not need to distinguish between the two.
- (void)resizeSlide:(DragTracker*)tracker {
    NSPoint delta = tracker.delta;
    NSDictionary *userInfo = tracker.userInfo;
    CALayer *layer = userInfo[kLayerKey];

    CGRect frame = NSRectToCGRect([userInfo[kInitialFrameKey] rectValue]);
    switch ([userInfo[kResizeIndexKey] integerValue]) {
        case 0: //top left
            frame.origin.x += delta.x;
            frame.size.width -= delta.x;
            frame.size.height += delta.y;
            break;

        case 1: //top middle
            frame.size.height += delta.y;
            break;

        case 2: //top right
            frame.size.width += delta.x;
            frame.size.height += delta.y;
            break;

        case 3: //right middle
            frame.size.width += delta.x;
            break;

        case 4: //bottom right
            frame.origin.y += delta.y;
            frame.size.width += delta.x;
            frame.size.height -= delta.y;
            break;

        case 5: //bottom middle
            frame.origin.y += delta.y;
            frame.size.height -= delta.y;
            break;

        case 6: //bottom left
            frame.origin.x += delta.x;
            frame.origin.y += delta.y;
            frame.size.width -= delta.x;
            frame.size.height -= delta.y;
            break;

        case 7: //left middle
            frame.origin.x += delta.x;
            frame.size.width -= delta.x;
            break;

        default:
            break;
    }

    // Turn off animation so that each layer is moved immeditaly.
    [LTView setupCAAnimationStack];
    layer.frame = frame;
    [LTView restoreCAAnimationStack];

    // Update resize handles
    [self.overlayLayer setNeedsDisplay];
}

- (void)resizeSlideEnd:(DragTracker*)tracker {    
    [self resizeSlide:tracker];

    // Commit the new CALayer frame values to the data source
    NSDictionary *userInfo = tracker.userInfo;
    [self commitFrameChangeOfLayer:userInfo[kLayerKey]];

    // Reset the tracker back to nil values
    tracker.userInfo = nil;
    tracker.updateTrackingAction = nil;
    tracker.endTrackingAction = nil;

    // Tracking over, re-enable all trackers.
    [self enableTrackers];
}


// The user has two fingers on the trackpad, has exceeded the movement threshold, and we are not currently tracking the mouse. Start dual-touch tracking.
- (void)dualTouchesBegan:(DualTouchTracker*)tracker {
    CALayer *layer = nil;
    CGPoint trackerLocation = NSPointToCGPoint(tracker.initialPoint);

    if (self.editingSlide) {
        // The user is adjusting a photo mask, use the photo sublayer if the cursor is over the unmasked photo
        CGPoint layerLocation = [self.layer convertPoint:trackerLocation fromLayer:nil];
        if (LTPointInRect(layerLocation, _editingSlide.photoFrame)) {
            layer = self.editingSlide.photoLayer;
        }
    } else {
        // The user is not adjusting a photo mask. Determine which LTMaskLayer is under the cursor, if any.
        layer = [self.layer hitTest:trackerLocation];
        layer = (layer == self.layer) ? nil : layer;
    }

    if (layer) {
        tracker.userInfo = @{kLayerKey: layer,
                                    kInitialFrameKey: [NSValue valueWithRect:NSRectFromCGRect(layer.frame)]};

        // Notice how we manage which type of tracking we are performing by simply changing the tracking action methods.
        tracker.updateTrackingAction = @selector(dualTouchesMoved:);
        tracker.endTrackingAction = @selector(dualTouchesEnded:);

        [self disableTrackersExcluding:tracker]; // No other tracking allowed while dragging.

        // Hide the cursor since the user is not moving the cursor.
        [NSCursor hide];
    }/* else {
        The cursor is not over an appropriate layer. Notice how we manage which type of tracking we are performing by simply changing the tracking action methods. In this case, the actions are left as nil, so nothing will occur.  
    } */
}

- (void)dualTouchesMoved:(DualTouchTracker*)tracker {
    NSDictionary *userInfo = tracker.userInfo;
    CGPoint deltaOrigin = NSPointToCGPoint(tracker.deltaOrigin);
    CGSize deltaSize = NSSizeToCGSize(tracker.deltaSize);

    CGRect originalFrame = NSRectToCGRect([userInfo[kInitialFrameKey] rectValue]);
    CGRect newFrame = originalFrame;
    newFrame.origin.x += deltaOrigin.x;
    newFrame.origin.y += deltaOrigin.y;
    newFrame.size.width += deltaSize.width;
    newFrame.size.height += deltaSize.height;

    // Update the Layer's frame
    CALayer *layer = userInfo[kLayerKey];
    [LTView setupCAAnimationStack];
    layer.frame = newFrame;
    [LTView restoreCAAnimationStack];

    // Update selection handles if needed
    [self.overlayLayer setNeedsDisplay];

    // Warp the cursor so that new touches are targeted to this Slide.
    NSPoint trackerLocation = NSPointFromCGPoint([layer.superlayer convertPoint:NSPointToCGPoint(tracker.initialPoint) fromLayer:nil]);

    // Calculate the original cursor offest.
    deltaOrigin.x = trackerLocation.x - CGRectGetMinX(originalFrame);
    deltaOrigin.y = trackerLocation.y - CGRectGetMinY(originalFrame);

    // Determine new cursor offest
    deltaOrigin.x = (deltaOrigin.x/CGRectGetWidth(originalFrame)) * CGRectGetWidth(newFrame);
    deltaOrigin.y = (deltaOrigin.y/CGRectGetHeight(originalFrame)) * CGRectGetHeight(newFrame);

    // Use new cursor offset to warp cursor in screen space
    CGPoint cgCursorLocation = newFrame.origin;
    cgCursorLocation.x += deltaOrigin.x;
    cgCursorLocation.y += deltaOrigin.y;
    cgCursorLocation = [layer.superlayer convertPoint:cgCursorLocation toLayer:nil];

    NSPoint nsCursorLocation = NSPointFromCGPoint(cgCursorLocation);
    nsCursorLocation = [self convertPoint:nsCursorLocation fromView:nil]; // [self convertPointToBase:nsCursorLocation];

    NSRect rect = NSZeroRect;
    rect.origin = nsCursorLocation;
    rect = [self.window convertRectToScreen:rect];
    nsCursorLocation = rect.origin;

    nsCursorLocation.y = [NSScreen mainScreen].frame.size.height - nsCursorLocation.y;
    CGWarpMouseCursorPosition(NSPointToCGPoint(nsCursorLocation));
}

- (void)dualTouchesEnded:(DualTouchTracker*)tracker {
    NSDictionary *userInfo = tracker.userInfo;
    [self commitFrameChangeOfLayer:userInfo[kLayerKey]];

    tracker.updateTrackingAction = nil;
    tracker.endTrackingAction = nil;
    [self enableTrackers];

    // We explicitly hide the cursor, so unhide it here.
    [NSCursor unhide];
    [NSCursor setHiddenUntilMouseMoves:YES];
}

@end

// See LTView.h for definitions of these properties
NSString *kLTViewSlides = @"slides";
NSString *kLTViewSelectionIndexes = @"selectionIndexes";
NSString *kLTViewSlidePropertyFrame = @"frame";
NSString *kLTViewSlidePropertyPhotoFrame = @"photoFrame";
NSString *kLTViewSlidePropertyPhoto = @"photo";
NSString *kLTViewSlidePropertyCornerRadius = @"cornerRadius";
NSString *kLTViewSlidePropertyFrameThickness = @"frameThickness";
```

[Next](LightTable-DualTouchTracker.m.md)[Previous](LightTable-DragTracker.h.md)

