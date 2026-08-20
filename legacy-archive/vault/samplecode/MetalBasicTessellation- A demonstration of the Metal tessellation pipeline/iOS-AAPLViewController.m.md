---
title: 'MetalBasicTessellation: A demonstration of the Metal tessellation pipeline'
apple_id: TP40017289
resource_type: Sample Code
platform: macOS
topic: null
technology: Metal
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/MetalBasicTessellation/Listings/iOS_AAPLViewController_m.html
archived_at: '2026-07-18T03:14:48.011515Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [MetalBasicTessellation: A demonstration of the Metal tessellation pipeline](MetalBasicTessellation-%20A%20demonstration%20of%20the%20Metal%20tessellation%20pipeline.md)


[Next](LICENSE.txt.md)[Previous](iOS-AAPLViewController.h.md)

# iOS/AAPLViewController.m

```objc
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    View Controller for the iOS version of MetalBasicTessellation.
            The UI elements that can modify a tessellation pass are: a segmented control to select a patch type, a switch to enable/disable wireframe rendering, sliders to change the edge and inside tessellation factors.
            The MTKView's drawing loop is only executed when the view appears, when it receives a view notification (setNeedsDisplay methods), or when its draw method is explicitly called (IBAction receiver methods).
            The MTKView's delegate methods are contained in the TessellationPipeline class.
 */

#import <MetalKit/MetalKit.h>
#import "AAPLViewController.h"
#import "AAPLTessellationPipeline.h"

@interface AAPLViewController ()

@property (weak, nonatomic) IBOutlet MTKView *mtkView;
@property (weak, nonatomic) IBOutlet UILabel *edgeLabel;
@property (weak, nonatomic) IBOutlet UILabel *insideLabel;
@property (strong, nonatomic) AAPLTessellationPipeline* tessellationPipeline;

@end

@implementation AAPLViewController

#pragma mark ViewController setup methods

- (void)viewDidLoad
{
    [super viewDidLoad];

    self.mtkView.paused = YES;
    self.mtkView.enableSetNeedsDisplay = YES;
    self.mtkView.sampleCount = 4;
}

- (void)viewDidAppear:(BOOL)animated
{
    [super viewDidAppear:animated];

    self.tessellationPipeline = [[AAPLTessellationPipeline alloc] initWithMTKView:self.mtkView];
    [self.mtkView draw];
}

#pragma mark IBAction receiver methods

- (IBAction)patchTypeSegmentedControlDidChange:(UISegmentedControl *)sender {
    self.tessellationPipeline.patchType = (sender.selectedSegmentIndex == 0) ? MTLPatchTypeTriangle : MTLPatchTypeQuad;
    [self.mtkView draw];
}

- (IBAction)wireframeDidChange:(UISwitch *)sender {
    self.tessellationPipeline.wireframe = sender.on;
    [self.mtkView draw];
}

- (IBAction)edgeSliderDidChange:(UISlider *)sender {
    self.edgeLabel.text = [NSString stringWithFormat:@"%.1f", sender.value];
    self.tessellationPipeline.edgeFactor = sender.value;
    [self.mtkView draw];
}

- (IBAction)insideSliderDidChange:(UISlider *)sender {
    self.insideLabel.text = [NSString stringWithFormat:@"%.1f", sender.value];
    self.tessellationPipeline.insideFactor = sender.value;
    [self.mtkView draw];
}

@end
```

[Next](LICENSE.txt.md)[Previous](iOS-AAPLViewController.h.md)

