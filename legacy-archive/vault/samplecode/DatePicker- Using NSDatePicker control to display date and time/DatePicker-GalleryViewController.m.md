---
title: 'DatePicker: Using NSDatePicker control to display date and time'
apple_id: DTS10004134
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/DatePicker/Listings/DatePicker_GalleryViewController_m.html
archived_at: '2026-07-18T03:06:04.934866Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DatePicker: Using NSDatePicker control to display date and time](DatePicker-%20Using%20NSDatePicker%20control%20to%20display%20date%20and%20time.md)


[Next](DatePicker-GalleryViewController.h.md)[Previous](DatePicker-ViewController.h.md)

# DatePicker/GalleryViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This sample's gallery view controller to display varying visual configurations on NSDatePicker.
 */

#import "GalleryViewController.h"

@interface GalleryViewController ()

@property (strong) NSDate *currentTime;
@property (strong) NSTimer *timer;

@property (weak) IBOutlet NSView *city_Cupertino_ClockContainer;
@property (weak) IBOutlet NSView *city_NewYork_ClockContainer;
@property (weak) IBOutlet NSView *city_London_ClockContainer;
@property (weak) IBOutlet NSView *city_Rome_ClockContainer;

@property (weak) IBOutlet NSView *clockContainerViewBezeled;
@property (weak) IBOutlet NSView *fieldContainerViewBezeled;
@property (weak) IBOutlet NSView *fieldContainerViewBezeledColor;
@property (weak) IBOutlet NSView *fieldContainerViewBezeledSmallFont;

@property (weak) IBOutlet NSView *clockContainerViewBordered;
@property (weak) IBOutlet NSView *fieldContainerViewBordered;
@property (weak) IBOutlet NSView *fieldContainerViewBorderedColor;
@property (weak) IBOutlet NSView *fieldContainerViewBorderedSmallFont;

@end


#pragma mark -

@implementation GalleryViewController

- (void)setupCityClock:(NSView *)containerView timeZone:(NSTimeZone *)timeZone
{
    // Only show the clock, by only including time elements.
    NSDatePickerElementFlags flags = 0;
    flags |= NSHourMinuteDatePickerElementFlag;
    flags |= NSHourMinuteSecondDatePickerElementFlag;
    flags |= NSTimeZoneDatePickerElementFlag;

    // Setup the city block and bind it's value to a single NSDate property.
    NSDatePicker *cityClock = [[NSDatePicker alloc] initWithFrame:containerView.bounds];
    cityClock.datePickerStyle = NSClockAndCalendarDatePickerStyle;
    cityClock.datePickerElements = flags;
    cityClock.timeZone = timeZone;
    [cityClock bind:NSValueBinding toObject:self withKeyPath:@"currentTime" options:nil];
    [containerView addSubview:cityClock];
}

- (void)viewWillAppear
{
    [super viewWillAppear];

    // We setup a timer so that each clock's date value is updated to the current time.
    __weak __typeof(self) weakSelf = self;
    _timer = [NSTimer scheduledTimerWithTimeInterval:1.0 repeats:YES block:^(NSTimer * _Nonnull timer) {
        weakSelf.currentTime = [NSDate date];
    }];
}

- (void)viewWillDisappear
{
    [super viewWillDisappear];

    // User tabbed out of our view controller, timer needs to stop.
    [self.timer invalidate];
}

- (void)dealloc
{
    [self.timer invalidate];
}

// -------------------------------------------------------------------------------
//  viewDidLoad
// -------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    _currentTime = [NSDate date];

    // Setup the world clocks in four different time zones.
    NSArray *knownTimeZoneNames = [NSTimeZone knownTimeZoneNames];
    for (NSString *timeZoneName in knownTimeZoneNames)
    {
        // Parse out our known list of time zones.
        NSArray *nameComponents = [timeZoneName componentsSeparatedByString:@"/"];
        if (nameComponents.count > 1)   // GMT time zone has only one component.
        {
            // Find the time zones we want to display.
            NSTimeZone *timeZone = [NSTimeZone timeZoneWithName:timeZoneName];

            NSView *containerView = nil;
            if ([nameComponents[1] isEqualToString:@"Los_Angeles"])
            {
                containerView = self.city_Cupertino_ClockContainer;
            }
            else if ([nameComponents[1] isEqualToString:@"New_York"])
            {
                containerView = self.city_NewYork_ClockContainer;
            }
            else if ([nameComponents[1] isEqualToString:@"London"])
            {
                containerView = self.city_London_ClockContainer;
            }
            else if ([nameComponents[1] isEqualToString:@"Rome"])
            {
                containerView = self.city_Rome_ClockContainer;
            }
            if (containerView != nil)
            {
                // Each clock will then update itself in a timer,
                // updates occur through binding it's value to our property "currentTime".
                [self setupCityClock:containerView timeZone:timeZone];
            }
        }
    }

    // Clock and calendar - bezeled.
    NSDatePicker *bezeledDatePickerControl = [[NSDatePicker alloc] initWithFrame:self.clockContainerViewBezeled.bounds];
    bezeledDatePickerControl.drawsBackground = YES;
    bezeledDatePickerControl.datePickerStyle = NSClockAndCalendarDatePickerStyle;
    bezeledDatePickerControl.bezeled = YES;
    bezeledDatePickerControl.dateValue = [NSDate date];
    [self.clockContainerViewBezeled addSubview:bezeledDatePickerControl];

    // TextField and stepper - bezeled.
    NSDatePicker *fieldStepperPickerControl = [[NSDatePicker alloc] initWithFrame:self.fieldContainerViewBezeled.bounds];
    fieldStepperPickerControl.drawsBackground = YES;
    fieldStepperPickerControl.datePickerStyle = NSTextFieldAndStepperDatePickerStyle;
    fieldStepperPickerControl.bezeled = YES;
    fieldStepperPickerControl.dateValue = [NSDate date];
    [self.fieldContainerViewBezeled addSubview:fieldStepperPickerControl];

    // TextField and stepper - bezeled - background and color text.
    NSDatePicker *fieldStepperPickerControlColored = [[NSDatePicker alloc] initWithFrame:self.fieldContainerViewBezeledColor.bounds];
    fieldStepperPickerControlColored.drawsBackground = YES;
    fieldStepperPickerControlColored.datePickerStyle = NSTextFieldAndStepperDatePickerStyle;
    fieldStepperPickerControlColored.bezeled = YES;
    fieldStepperPickerControlColored.textColor = [NSColor yellowColor];
    fieldStepperPickerControlColored.backgroundColor = [NSColor blueColor];
    fieldStepperPickerControlColored.dateValue = [NSDate date];
    [self.fieldContainerViewBezeledColor addSubview:fieldStepperPickerControlColored];

    // TextField and stepper - bezeled - small font.
    NSDatePicker *fieldStepperPickerControlSmallFont = [[NSDatePicker alloc] initWithFrame:self.fieldContainerViewBezeled.bounds];
    fieldStepperPickerControlSmallFont.drawsBackground = YES;
    fieldStepperPickerControlSmallFont.datePickerStyle = NSTextFieldAndStepperDatePickerStyle;
    fieldStepperPickerControlSmallFont.bezeled = YES;
    // You can use: NSControlSizeMini, NSControlSizeSmall, NSControlSizeRegular.
    fieldStepperPickerControlSmallFont.cell.controlSize = NSControlSizeMini;
    fieldStepperPickerControlSmallFont.cell.font = [NSFont systemFontOfSize:9.0];
    fieldStepperPickerControlSmallFont.dateValue = [NSDate date];
    [self.fieldContainerViewBezeledSmallFont addSubview:fieldStepperPickerControlSmallFont];

    // Clock and calendar - bordered.
    NSDatePicker *borderedPickerControl = [[NSDatePicker alloc] initWithFrame:self.clockContainerViewBordered.bounds];
    borderedPickerControl.drawsBackground = YES;
    borderedPickerControl.datePickerStyle = NSClockAndCalendarDatePickerStyle;
    borderedPickerControl.bordered = YES;
    borderedPickerControl.dateValue = [NSDate date];
    [self.clockContainerViewBordered addSubview:borderedPickerControl];

    // TextField and stepper - bordered.
    NSDatePicker *fieldPickerControl = [[NSDatePicker alloc] initWithFrame:self.fieldContainerViewBordered.bounds];
    fieldPickerControl.drawsBackground = YES;
    fieldPickerControl.datePickerStyle = NSTextFieldAndStepperDatePickerStyle;
    fieldPickerControl.bordered = YES;
    fieldPickerControl.dateValue = [NSDate date];
    [self.fieldContainerViewBordered addSubview:fieldPickerControl];

    // TextField and stepper - bordered - background and color text.
    NSDatePicker *fieldStepperBorderedPickerControlColored = [[NSDatePicker alloc] initWithFrame:self.fieldContainerViewBorderedColor.bounds];
    fieldStepperBorderedPickerControlColored.drawsBackground = YES;
    fieldStepperBorderedPickerControlColored.datePickerStyle = NSTextFieldAndStepperDatePickerStyle;
    fieldStepperBorderedPickerControlColored.bordered = YES;
    fieldStepperBorderedPickerControlColored.textColor = [NSColor yellowColor];
    fieldStepperBorderedPickerControlColored.backgroundColor = [NSColor blueColor];
    fieldStepperBorderedPickerControlColored.dateValue = [NSDate date];
    [self.fieldContainerViewBorderedColor addSubview:fieldStepperBorderedPickerControlColored];

    // TextField and stepper - bordered - small font.
    NSDatePicker *fieldPickerControlSmallFont = [[NSDatePicker alloc] initWithFrame:self.fieldContainerViewBorderedSmallFont.bounds];
    fieldPickerControlSmallFont.drawsBackground = YES;
    fieldPickerControlSmallFont.datePickerStyle = NSTextFieldAndStepperDatePickerStyle;
    fieldPickerControlSmallFont.bordered = YES;
    // You can use: NSControlSizeMini, NSControlSizeSmall, NSControlSizeRegular.
    fieldPickerControlSmallFont.cell.controlSize = NSControlSizeMini;
    fieldPickerControlSmallFont.cell.font = [NSFont systemFontOfSize:9.0];
    fieldPickerControlSmallFont.dateValue = [NSDate date];
    [self.fieldContainerViewBorderedSmallFont addSubview:fieldPickerControlSmallFont];

    // Workaround to window resize problem with NSTabViewController on 10.13.
    self.preferredContentSize = self.view.frame.size;
}

@end
```

[Next](DatePicker-GalleryViewController.h.md)[Previous](DatePicker-ViewController.h.md)

