---
title: 'MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder
  in Metal'
apple_id: TP40017382
resource_type: Sample Code
platform: tvOS|iOS|macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalGameOfLife/Listings/Common_AAPLViewController_m.html
archived_at: '2026-07-18T03:14:48.464630Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalGameOfLife: Data-parallel Programming with the MTLComputeCommandEncoder in Metal](MetalGameOfLife-%20Data-parallel%20Programming%20with%20the%20MTLComputeCommandEncoder%20in.md)


[Next](README.md.md)[Previous](Common-AAPLRenderer.m.md)

# Common/AAPLViewController.m

```objc
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
The view controller class for the Game of Life sample. Manages an MTKView for displaying graphics rendered by Metal
    and mediates touch and mouse interactions.
*/

#import "AAPLViewController.h"
#import "AAPLRenderer.h"

@import Metal;
@import simd;
@import MetalKit;

@interface AAPLViewController ()
@property (nonatomic, weak) MTKView *metalView;
@property (nonatomic, strong) AAPLRenderer * renderer;
@end

@implementation AAPLViewController

#pragma mark - View Controller Methods

- (void)viewDidLoad
{
    [super viewDidLoad];

    self.metalView = (MTKView *)self.view;

    [self setupView];

#if TARGET_OS_IOS || TARGET_OS_TV
    // On iOS and tvOS, we need to expressly enable multitouch on our view and
    // request to be made first responder so we can listen for touches
    self.metalView.userInteractionEnabled = YES;
#if !TARGET_OS_TV
    // On iPhone and iPad, we go further and track multiple touches at once
    self.metalView.multipleTouchEnabled = YES;
#endif
    [self becomeFirstResponder];
#endif
}

#if TARGET_OS_IPHONE
- (BOOL)prefersStatusBarHidden {
    return YES;
}

- (BOOL)canBecomeFirstResponder {
    return YES;
}
#endif

#pragma mark - Setup Methods

- (void)setupView
{
    self.metalView.device = MTLCreateSystemDefaultDevice();
    self.metalView.colorPixelFormat = MTLPixelFormatBGRA8Unorm;
    self.metalView.clearColor = MTLClearColorMake(0, 0, 0, 1);

    self.metalView.drawableSize = self.metalView.bounds.size;

    // Create renderer and make it the delegate of our MTKView
    self.renderer = [[AAPLRenderer alloc] initWithView:self.metalView];
}

#pragma mark - Interaction (Touch / Mouse) Handling

- (CGPoint)locationInGridForLocationInView:(CGPoint)point
{
    CGSize viewSize = self.view.frame.size;
    CGFloat normalizedWidth = point.x / viewSize.width;
    CGFloat normalizedHeight = point.y / viewSize.height;
    CGFloat gridX = round(normalizedWidth * self.renderer.gridSize.width);
    CGFloat gridY = round(normalizedHeight * self.renderer.gridSize.height);
    return CGPointMake(gridX, gridY);
}

- (void)activateRandomCellsForPoint:(CGPoint)point
{
    // Translate between the coordinate space of the view and the game grid,
    // then forward the request to the compute phase to do the real work
    CGPoint gridLocation = [self locationInGridForLocationInView:point];
    [self.renderer activateRandomCellsInNeighborhoodOfCell:gridLocation];
}

#if TARGET_OS_IPHONE
- (void)touchesBegan:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event
{
    for (UITouch *touch in touches)
    {
        // Turn on random cells in the vicinity of the touched location
        CGPoint location = [touch locationInView:self.view];
        [self activateRandomCellsForPoint:location];
    }
}

- (void)touchesMoved:(NSSet<UITouch *> *)touches withEvent:(UIEvent *)event
{
    for (UITouch *touch in touches)
    {
        // Turn on random cells in the vicinity of the touched location
        CGPoint location = [touch locationInView:self.view];
        [self activateRandomCellsForPoint:location];
    }
}
#else
- (void)mouseDown:(NSEvent *)event {
    // Translate the cursor position into view coordinates, accounting for the fact that
    // App Kit's default window coordinate space has its origin in the bottom left
    CGPoint location = [self.view convertPoint:[event locationInWindow] fromView:nil];
    location.y = self.view.bounds.size.height - location.y;
    // Turn on random cells in the vicinity of the clicked location
    [self activateRandomCellsForPoint:location];
}

- (void)mouseDragged:(NSEvent *)event {
    // Translate the cursor position into view coordinates, accounting for the fact that
    // App Kit's default window coordinate space has its origin in the bottom left
    CGPoint location = [self.view convertPoint:[event locationInWindow] fromView:nil];
    location.y = self.view.bounds.size.height - location.y;
    // Turn on random cells in the vicinity of the clicked location
    [self activateRandomCellsForPoint:location];
}
#endif

@end
```

[Next](README.md.md)[Previous](Common-AAPLRenderer.m.md)

