---
title: LocateMe
apple_id: DTS40007801
resource_type: Sample Code
platform: iOS
topic: Data Management
technology: CoreLocation
published: '2014-09-17'
source_url: https://developer.apple.com/library/archive/samplecode/LocateMe/Listings/LocateMe_SetupViewController_m.html
archived_at: '2026-07-18T03:13:46.342126Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [LocateMe](LocateMe.md)


[Next](LICENSE.txt.md)[Previous](LocateMe-GetLocationViewController.m.md)

# LocateMe/SetupViewController.m

```objc
/*
Copyright (C) 2014 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

*/

#import "SetupViewController.h"
#import <CoreLocation/CoreLocation.h>

NSString * const kSetupInfoKeyAccuracy = @"SetupInfoKeyAccuracy";
NSString * const kSetupInfoKeyDistanceFilter = @"SetupInfoKeyDistanceFilter";
NSString * const kSetupInfoKeyTimeout = @"SetupInfoKeyTimeout";

static NSString * const kAccuracyNameKey = @"AccuracyNameKey";
static NSString * const kAccuracyValueKey = @"AccuracyValueKey";


@interface SetupViewController () <UIPickerViewDelegate, UIPickerViewDataSource>

@property (nonatomic, strong) NSMutableDictionary *setupInfo;
@property (nonatomic, strong) NSArray *accuracyOptions;
@property (nonatomic, assign) BOOL configureForTracking;

@property (nonatomic, weak) IBOutlet UIPickerView *accuracyPicker;
@property (nonatomic, weak) IBOutlet UISlider *slider;

@end


#pragma mark -

@implementation SetupViewController

- (void)viewDidLoad {
    [super viewDidLoad];

    NSMutableArray *options = [NSMutableArray array];
    [options addObject:@{kAccuracyNameKey: NSLocalizedString(@"AccuracyBest", @"AccuracyBest"), kAccuracyValueKey: @(kCLLocationAccuracyBest)}];
    [options addObject:@{kAccuracyNameKey: NSLocalizedString(@"Accuracy10", @"Accuracy10"), kAccuracyValueKey: @(kCLLocationAccuracyNearestTenMeters)}];
    [options addObject:@{kAccuracyNameKey: NSLocalizedString(@"Accuracy100", @"Accuracy100"), kAccuracyValueKey: @(kCLLocationAccuracyHundredMeters)}];
    [options addObject:@{kAccuracyNameKey: NSLocalizedString(@"Accuracy1000", @"Accuracy1000"), kAccuracyValueKey: @(kCLLocationAccuracyKilometer)}];
    [options addObject:@{kAccuracyNameKey: NSLocalizedString(@"Accuracy3000", @"Accuracy3000"), kAccuracyValueKey: @(kCLLocationAccuracyThreeKilometers)}];
    self.accuracyOptions = options;
}

- (void)viewWillAppear:(BOOL)animated {
    [super viewWillAppear:animated];

    [self.accuracyPicker selectRow:2 inComponent:0 animated:NO];
    self.setupInfo = [NSMutableDictionary dictionary];
    self.setupInfo[kSetupInfoKeyDistanceFilter] = @100.0;
    self.setupInfo[kSetupInfoKeyTimeout] = @30.0;
    self.setupInfo[kSetupInfoKeyAccuracy] = @(kCLLocationAccuracyHundredMeters);
}


#pragma mark - Actions

- (IBAction)done:(id)sender {
    [self dismissViewControllerAnimated:YES completion:nil];
    if ([self.delegate respondsToSelector:@selector(setupViewController:didFinishSetupWithInfo:)]) {
        [self.delegate setupViewController:self didFinishSetupWithInfo:self.setupInfo];
    }
}

- (IBAction)sliderChangedValue:(id)sender {
    if (self.configureForTracking) {
        self.setupInfo[kSetupInfoKeyDistanceFilter] = @(pow(10, [(UISlider *)sender value]));
    } else {
        self.setupInfo[kSetupInfoKeyTimeout] = [NSNumber numberWithDouble:[(UISlider *)sender value]];
    }
}


#pragma mark - UIPickerViewDataSource

- (NSInteger)numberOfComponentsInPickerView:(UIPickerView *)pickerView {
    return 1;
}

- (NSInteger)pickerView:(UIPickerView *)pickerView numberOfRowsInComponent:(NSInteger)component {
    return 5;
}

- (NSString *)pickerView:(UIPickerView *)pickerView titleForRow:(NSInteger)row forComponent:(NSInteger)component {
    NSDictionary *optionForRow = self.accuracyOptions[row];
    return optionForRow[kAccuracyNameKey];
}


#pragma mark - UIPickerViewDelegate

- (void)pickerView:(UIPickerView *)pickerView didSelectRow:(NSInteger)row inComponent:(NSInteger)component {
    NSDictionary *optionForRow = self.accuracyOptions[row];
    self.setupInfo[kSetupInfoKeyAccuracy] = optionForRow[kAccuracyValueKey];
}

@end
```

[Next](LICENSE.txt.md)[Previous](LocateMe-GetLocationViewController.m.md)

