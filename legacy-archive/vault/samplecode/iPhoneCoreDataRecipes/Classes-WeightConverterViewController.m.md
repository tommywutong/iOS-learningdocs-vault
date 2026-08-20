---
title: iPhoneCoreDataRecipes
apple_id: DTS40008913
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreData
published: '2017-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/iPhoneCoreDataRecipes/Listings/Classes_WeightConverterViewController_m.html
archived_at: '2026-07-18T03:29:39.733858Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [iPhoneCoreDataRecipes](iPhoneCoreDataRecipes.md)


[Next](Classes-InstructionsViewController.m.md)[Previous](Classes-TypeSelectionViewController.m.md)

# Classes/WeightConverterViewController.m

```objc
/*
 Copyright (C) 2017 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 View controller to manage conversion of metric to imperial units of weight and vice versa.
  The controller uses two UIPicker objects to allow the user to select the weight in metric or imperial units.
 */

#import "WeightConverterViewController.h"

#import "MetricPickerController.h"
#import "ImperialPickerController.h"

@interface WeightConverterViewController ()

@property (nonatomic, strong) IBOutlet UIView *pickerViewContainer;

@property (nonatomic, strong) IBOutlet MetricPickerController *metricPickerController;
@property (nonatomic, strong) IBOutlet UIView *metricPickerViewContainer;

@property (nonatomic, strong) IBOutlet ImperialPickerController *imperialPickerController;
@property (nonatomic, strong) IBOutlet UIView *imperialPickerViewContainer;

@property (nonatomic, strong) IBOutlet UISegmentedControl *segmentedControl;

@property (nonatomic, assign) NSUInteger selectedUnit;

@end


#pragma mark -

@implementation WeightConverterViewController

#define METRIC_INDEX 0
#define IMPERIAL_INDEX 1

- (void)viewDidLoad {

    [super viewDidLoad];

    // Set the currently-selected unit for self and the segmented control.
    self.selectedUnit = METRIC_INDEX;
    self.segmentedControl.selectedSegmentIndex = self.selectedUnit;

    [self toggleUnit];
}

- (IBAction)toggleUnit {

    /*
     When the user changes the selection in the segmented control, set the appropriate picker as the current subview of the picker container view (and remove the previous one).
     */
    _selectedUnit = self.segmentedControl.selectedSegmentIndex;
    if (self.selectedUnit == IMPERIAL_INDEX) {
        [self.metricPickerViewContainer removeFromSuperview];
        [self.pickerViewContainer addSubview:self.imperialPickerViewContainer];
        [self.imperialPickerController updateLabel];
    } else {
        [self.imperialPickerViewContainer removeFromSuperview];
        [self.pickerViewContainer addSubview:self.metricPickerViewContainer];
        [self.metricPickerController updateLabel];
    }
}

@end
```

[Next](Classes-InstructionsViewController.m.md)[Previous](Classes-TypeSelectionViewController.m.md)

