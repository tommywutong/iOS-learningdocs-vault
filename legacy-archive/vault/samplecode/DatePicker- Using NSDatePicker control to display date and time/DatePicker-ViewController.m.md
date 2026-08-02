---
title: 'DatePicker: Using NSDatePicker control to display date and time'
apple_id: DTS10004134
resource_type: Sample Code
platform: macOS
topic: User Experience
technology: AppKit
published: '2018-05-03'
source_url: https://developer.apple.com/library/archive/samplecode/DatePicker/Listings/DatePicker_ViewController_m.html
archived_at: '2026-07-18T03:06:05.117057Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DatePicker: Using NSDatePicker control to display date and time](DatePicker-%20Using%20NSDatePicker%20control%20to%20display%20date%20and%20time.md)


[Next](ReadMe.md.md)[Previous](DatePicker-GalleryViewController.h.md)

# DatePicker/ViewController.m

```objc
/*
 Copyright (C) 2018 Apple Inc. All Rights Reserved.
 See LICENSE.txt for this sample’s licensing information

 Abstract:
 This sample's main view controller.
 */

#import "ViewController.h"

@interface ViewController () <NSDatePickerCellDelegate>

@property (assign) id localChangedObserver;

@property (strong) NSDatePicker *datePickerControl;
@property (weak) IBOutlet NSBox *outerBox; // Used to hold the NSDatePicker and time elements.
@property (weak) IBOutlet NSView *datePickerBox; // Used to hold the NSDatePicker itself.

@property (weak) IBOutlet NSButton *setToTodayButton;

// Formatted date labels.
@property (weak) IBOutlet NSTextField *dateResult1;
@property (weak) IBOutlet NSTextField *dateResult2;
@property (weak) IBOutlet NSTextField *dateResult3;
@property (weak) IBOutlet NSTextField *dateResult4;
@property (weak) IBOutlet NSTextField *dateResult5;

// Appearance.
@property (weak) IBOutlet NSPopUpButton* pickerStylePopup;

// Date elements (3 checkboxes).
@property (weak) IBOutlet NSButton *YearMonthElementFlag;
@property (weak) IBOutlet NSButton *YearMonthDayElementFlag;
// Time elements (3 checkboxes).
@property (weak) IBOutlet NSButton *HourMinuteElementFlag;
@property (weak) IBOutlet NSButton *HourMinuteSecondElementFlag;

@property (weak) IBOutlet NSButton *overrideDateCheck;
@property (weak) IBOutlet NSDatePicker *overrideDate;

// Date range.
@property (weak) IBOutlet NSButton *singleDateMode;
@property (weak) IBOutlet NSButton *rangeDateMode;
@property (weak) IBOutlet NSTextField *secondsRangeEdit;
@property (weak) IBOutlet NSTextField *secondsRangeEditLabel;

@property (weak) IBOutlet NSDatePicker *minDatePicker;
@property (weak) IBOutlet NSDatePicker *maxDatePicker;

@end


#pragma mark -

@implementation ViewController

// -------------------------------------------------------------------------------
//  viewDidLoad
// -------------------------------------------------------------------------------
- (void)viewDidLoad
{
    [super viewDidLoad];

    // Based our date formatter on CFDateFormatter: allows more configurability and better localization.
    [NSDateFormatter setDefaultFormatterBehavior:NSDateFormatterBehavior10_4];

    // We start out with NSClockAndCalendarDatePickerStyle.
    [self setupDatePickerControl:NSClockAndCalendarDatePickerStyle];

    self.minDatePicker.dateValue = [NSDate date];
    self.maxDatePicker.dateValue = [NSDate distantFuture];

    [self updateControls];  // Force update of all UI elements and the picker itself.

    // Listen for locale changes so we can update our formatted strings.
    _localChangedObserver =
        [[NSNotificationCenter defaultCenter] addObserverForName:NSCurrentLocaleDidChangeNotification
                                                          object:nil
                                                           queue:nil
                                                      usingBlock:^(NSNotification *notification) {
                                                          // Our Locale was changed by the user,
                                                          // update our formatted date strings.
                                                          [self updateDateResult];
                                                      }];

    // Workaround to window resize problem with NSTabViewController on 10.13.
    self.preferredContentSize = self.view.frame.size;
}

// -------------------------------------------------------------------------------
//  dealloc
// -------------------------------------------------------------------------------
- (void)dealloc
{
    [[NSNotificationCenter defaultCenter] removeObserver:self.localChangedObserver];
}

// -------------------------------------------------------------------------------
//  setupDatePickerControl:pickerStyle
//
//  Delete and re-create a new NSDatePicker.
// -------------------------------------------------------------------------------
- (void)setupDatePickerControl:(NSDatePickerStyle)pickerStyle
{
    // We need to re-create the picker control (due to a resize bug when switching between styles).
    if (self.datePickerControl != nil)  // Hide and release the previous date picker, if any.
    {
        self.datePickerControl.hidden = YES;
        _datePickerControl = nil;
    }

    // Compute the frame placement and size that we want to use for the NSDatePicker.
    NSRect frame = NSMakeRect(0.0, 0.0, 295.0, 154.0);

    if (pickerStyle != NSClockAndCalendarDatePickerStyle)
    {
        frame.size.width -= 100;// For non-clock/calendar style, we narrow it a bit.
    }
    _datePickerControl = [[NSDatePicker alloc] initWithFrame:frame];
    // We want to be the cell's delegate to catch date validation (via validateProposedDateValue).
    self.datePickerControl.delegate = self;
    // We want to respond to date/time changes.
    self.datePickerControl.action = @selector(datePickerAction:);
    self.datePickerControl.datePickerStyle = pickerStyle; // Set our desired picker style.
    self.datePickerControl.drawsBackground = YES;

    // Always set the date/time to TODAY, note that our delete override might block this.
    self.datePickerControl.dateValue = [NSDate date];
    [self.datePickerBox addSubview:self.datePickerControl];

    // Sync the picker style popup with the new style change.
    [self.pickerStylePopup selectItemWithTag:pickerStyle];

    [self.datePickerControl setNeedsDisplay:YES];

    [self updateControls]; // Force update of all UI elements and the picker itself.
}

// -------------------------------------------------------------------------------
//  updateDateResult
// -------------------------------------------------------------------------------
- (void)updateDateResult
{
    NSDate *theDate = self.datePickerControl.dateValue;
    if (theDate != nil)
    {
        NSDateFormatter *formatter = [[NSDateFormatter alloc] init];

        /* Some examples:
        [formatter setDateStyle:NSDateFormatterNoStyle];        // <no date displayed>
        [formatter setDateStyle:NSDateFormatterMediumStyle];    // Jan 24, 1984
        [formatter setDateStyle:NSDateFormatterShortStyle];     // 1/24/84
        [formatter setDateStyle:NSDateFormatterLongStyle];      // January 24, 1984
        [formatter setDateStyle:NSDateFormatterFullStyle];      // Tuesday, January 24, 1984

        [formatter setTimeStyle:NSDateFormatterNoStyle];        // <no time displayed>
        [formatter setTimeStyle:NSDateFormatterShortStyle];     // 2:44 PM
        [formatter setTimeStyle:NSDateFormatterMediumStyle];    // 2:44:55 PM
        [formatter setTimeStyle:NSDateFormatterLongStyle];      // 2:44:55 PM PDT
        [formatter setTimeStyle:NSDateFormatterFullStyle];      // 2:44:55 PM PDT
        */

        NSString *formattedDateString;

        formatter.dateStyle = NSDateFormatterShortStyle;
        formatter.timeStyle = NSDateFormatterNoStyle;
        formattedDateString = [formatter stringFromDate:theDate];
        self.dateResult1.stringValue = formattedDateString;

        formatter.dateStyle = NSDateFormatterShortStyle;
        formatter.timeStyle = NSDateFormatterShortStyle;
        formattedDateString = [formatter stringFromDate:theDate];
        self.dateResult2.stringValue = formattedDateString;

        formatter.dateStyle = NSDateFormatterMediumStyle;
        formatter.timeStyle = NSDateFormatterShortStyle;
        formattedDateString = [formatter stringFromDate:theDate];
        self.dateResult3.stringValue = formattedDateString;

        formatter.dateStyle = NSDateFormatterLongStyle;
        formatter.timeStyle = NSDateFormatterShortStyle;
        formattedDateString = [formatter stringFromDate:theDate];
        self.dateResult4.stringValue = formattedDateString;

        formatter.dateStyle = NSDateFormatterFullStyle;
        formatter.timeStyle = NSDateFormatterFullStyle;
        formattedDateString = [formatter stringFromDate:theDate];
        self.dateResult5.stringValue = formattedDateString;
    }
}

// -------------------------------------------------------------------------------
//  updateControls
//
//  Force update of all UI elements and the picker itself.
// -------------------------------------------------------------------------------
- (void)updateControls
{
    [self.datePickerControl setNeedsDisplay:YES]; // Force it to update.

    [self updateDatePickerMode];
    [self updateDateTimeElementFlags];
    [self updateDateResult];
}


#pragma mark - NSDatePicker

// -------------------------------------------------------------------------------
//  setPickerStyle:sender:
//
//  User chose a different picker style from the Picker Style popup.
// -------------------------------------------------------------------------------
- (IBAction)setPickerStyle:(id)sender
{
    // Find which style was chosen from the popup.
    NSUInteger tag = [sender selectedTag];

    if (self.datePickerControl.datePickerStyle != tag)
    {
        // Hide the date picker while we re-configure things.
        self.datePickerControl.hidden = YES;

        [self setupDatePickerControl:tag]; // Set our desired picker style.

        // Finished, show the data picker again.
        self.datePickerControl.hidden = NO;

        [self updateControls]; // Force update of all UI elements and the picker itself.
    }
}

// -------------------------------------------------------------------------------
//  datePickerAction:sender:
//
//  The user interacted with the date picker control so update the date/time examples.
// -------------------------------------------------------------------------------
- (IBAction)datePickerAction:(id)sender
{
    [self updateDateResult];
}

// -------------------------------------------------------------------------------
//  dateOverrideAction:sender:
//
//  The user checked/unchecked the "Date Override" checkbox - which in effect
//  turns on or off the delegate method to override the date.
// -------------------------------------------------------------------------------
- (IBAction)dateOverrideAction:(id)sender
{
    // Enable/disable override data picker based on checkbox state.
    self.overrideDate.enabled = [sender state];
    self.setToTodayButton.enabled = ![sender state]; // Can't set today when we override the date.

    // Set us up as the delegate if we want to override the date/time.
    self.datePickerControl.delegate = [sender state] ? self : nil;

    // Force the delete "datePickerCell" to be updated.
    self.datePickerControl.dateValue = [NSDate date];

    // Date picker modes turned off for date override.
    self.singleDateMode.enabled = ![sender state];
    self.rangeDateMode.enabled = ![sender state];

    // Date picker in single date mode for date override.
    self.datePickerControl.datePickerMode = NSSingleDateMode;
    self.singleDateMode.state = NSControlStateValueOn;

    [self updateControls]; // Force update of all UI elements and the picker itself.
}

// -------------------------------------------------------------------------------
//  setToday:sender
//
//  Sets the date picker value to 'today'.
// -------------------------------------------------------------------------------
- (IBAction)setToday:(id)sender
{
    self.datePickerControl.dateValue = [NSDate date];
}

// -------------------------------------------------------------------------------
//  dateOverrideChangeAction:sender
//
//  Action method for the "overrideDate" date picker (user clicked up or down arrow).
// -------------------------------------------------------------------------------
- (IBAction)dateOverrideChangeAction:(id)sender
{
    self.datePickerControl.dateValue = [NSDate date]; // Force the delete "datePickerCell" to be updated.

    [self updateDateResult];
}


#pragma mark - Date Time Elements

// Date/time element checkbox selections.

typedef NS_ENUM(NSInteger, TimeElementFlags)
{
    hourMinuteDatePickerElementFlag = 0,
    hourMinuteSecondDatePickerElementFlag,
};

typedef NS_ENUM(NSInteger, DateElementFlags)
{
    yearMonthDatePickerElementFlag = 0,
    yearMonthDayDatePickerElementFlag,
};

// -------------------------------------------------------------------------------
//  setDateElementFlags:sender:
//
//  The user checked/unchecked one of the "Date Element" checkboxes.
// -------------------------------------------------------------------------------
- (IBAction)setDateElementFlags:(id)sender
{
    NSButton *checkBox = sender;
    NSInteger tag = checkBox.tag;
    BOOL checked = checkBox.state;
    NSDatePickerElementFlags flags = self.datePickerControl.datePickerElements;

    if (self.datePickerControl.datePickerStyle == NSClockAndCalendarDatePickerStyle)
    {
        // For clock-calender stype: month, day, year are required.
        flags |= NSYearMonthDatePickerElementFlag;
        flags |= NSYearMonthDayDatePickerElementFlag;
    }
    else
    {
        // Picker style is either: NSTextFieldAndStepperDatePickerStyle or NSTextFieldDatePickerStyle
        // Allow for the month, day, year to be changed.
        //
        switch (tag)
        {
            case yearMonthDatePickerElementFlag:
                // Display and allow editing of the year and month elements of the date.
                if (checked)
                    flags |= NSYearMonthDatePickerElementFlag;
                else
                    flags ^= NSYearMonthDatePickerElementFlag;
                break;

            case yearMonthDayDatePickerElementFlag:
                // Display and allow editing of the year, month and day elements of the date.
                if (checked)
                    flags |= NSYearMonthDayDatePickerElementFlag;
                else
                    flags ^= NSYearMonthDayDatePickerElementFlag;
                break;
        }
    }

    self.datePickerControl.datePickerElements = flags;
}

// -------------------------------------------------------------------------------
//  setTimeElementFlags:sender:
//
//  The user checked/unchecked one of the "Time Element" checkboxes.
// -------------------------------------------------------------------------------
- (IBAction)setTimeElementFlags:(id)sender
{
    NSButton *checkBox = sender;
    NSInteger tag = checkBox.tag;
    BOOL checked = checkBox.state;
    NSDatePickerElementFlags flags = self.datePickerControl.datePickerElements;

    switch (tag)
    {
        case hourMinuteDatePickerElementFlag:
            if (checked)
                flags |= NSHourMinuteDatePickerElementFlag;
            else
                flags ^= NSHourMinuteDatePickerElementFlag;
            break;

        case hourMinuteSecondDatePickerElementFlag:
            if (checked)
                flags |= NSHourMinuteSecondDatePickerElementFlag;
            else
                flags ^= NSHourMinuteSecondDatePickerElementFlag;
            break;
    }
    self.datePickerControl.datePickerElements = flags;
}

// -------------------------------------------------------------------------------
//  updateDateTimeElementFlags
//
//  Updates our checkboxes to reflect the current control flags.
// -------------------------------------------------------------------------------
- (void)updateDateTimeElementFlags
{
    NSDatePickerElementFlags elementFlags = self.datePickerControl.datePickerElements;

    // Date elements:
    self.YearMonthElementFlag.state = (elementFlags & NSYearMonthDatePickerElementFlag) != 0;
    self.YearMonthDayElementFlag.state = (elementFlags & NSYearMonthDayDatePickerElementFlag) != 0;

    // Time elements:
    self.HourMinuteElementFlag.state = ((elementFlags & NSHourMinuteDatePickerElementFlag) != 0);
    self.HourMinuteSecondElementFlag.state = ((elementFlags & NSHourMinuteSecondDatePickerElementFlag) != 0);
}


#pragma mark - Picker Min Max Date

// -------------------------------------------------------------------------------
//  setMinDate:sender:
//
//  User wants to set the minimum date for the picker.
// -------------------------------------------------------------------------------
- (IBAction)setMinDate:(id)sender
{
    self.datePickerControl.minDate = self.minDatePicker.dateValue;
}

// -------------------------------------------------------------------------------
//  setMaxDate:sender:
//
//  User wants to set the maximum date for the picker.
// -------------------------------------------------------------------------------
- (IBAction)setMaxDate:(id)sender
{
    self.datePickerControl.maxDate = self.maxDatePicker.dateValue;
}


#pragma mark - Picker Mode

typedef NS_ENUM(NSInteger, DateMode)
{
    kSingleDateMode = 1,
    kRangeDateMode
};

// -------------------------------------------------------------------------------
//  setDatePickerMode:sender:
//
//  User wants to change the "Date Picker Mode".
// -------------------------------------------------------------------------------
- (IBAction)setDatePickerMode:(id)sender
{
    NSButton *chosenRadio = sender;
    switch (chosenRadio.tag)
    {
        case kSingleDateMode:
        {
            self.datePickerControl.datePickerMode = NSSingleDateMode;
            break;
        }
        case kRangeDateMode:
        {
            self.datePickerControl.datePickerMode = NSRangeDateMode;
            break;
        }
    }
    [self updateControls];  // Force update of all UI elements and the picker itself.
}

// -------------------------------------------------------------------------------
//  updateDatePickerMode
//
//  Used to update the NSDatePicker's NSDatePickerMode attributes.
// -------------------------------------------------------------------------------
- (void)updateDatePickerMode
{
    NSDatePickerMode mode = self.datePickerControl.datePickerMode;
    switch (mode)
    {
        case NSSingleDateMode:
        {
            // Interval value not applicable.
            self.secondsRangeEdit.enabled = NO;
            self.secondsRangeEditLabel.textColor = [NSColor lightGrayColor];

            self.datePickerControl.timeInterval = 0;
            break;
        }

        case NSRangeDateMode:
        {
            // Interval value applies.
            self.secondsRangeEdit.enabled = YES;
            self.secondsRangeEditLabel.textColor = [NSColor blackColor];

            // Set the date range by start date
            // (here we use the current date in the date picker control), and time interval (in seconds).
            NSString *secsStr = self.secondsRangeEdit.stringValue;
            NSInteger numSeconds = secsStr.integerValue;
            self.datePickerControl.timeInterval = numSeconds;

            break;
        }
    }
}

// -------------------------------------------------------------------------------
//  textDidEndEditing:notification
//
//  The user finished editing the time interval (in seconds).
//
//  This controller is a delegate to the NSTextField: number of seconds (for the date range),
//  so here we get notified when the user has finished editing the seconds range,
//  then we update the date picker control.
//
//  NOTE: don't use "textDidEndEditing" because NSTextField is not NSText, rather is a subclass
//  of NSControl, so use the delegate methods from NSControl.
// -------------------------------------------------------------------------------
- (void)controlTextDidEndEditing:(NSNotification *)notification
{
    [self updateDatePickerMode]; // Force update of the date picker control.
}


#pragma mark - NSDatePickerCellDelegate

// -------------------------------------------------------------------------------
//  datePickerCell:aDatePickerCell:proposedDateValue:proposedTimeInterval
//
//  Delegate to NSDatePickerCell.
// -------------------------------------------------------------------------------
- (void)datePickerCell:(NSDatePickerCell *)aDatePickerCell validateProposedDateValue:(NSDate **)proposedDateValue
          timeInterval:(NSTimeInterval*)proposedTimeInterval
{
    ViewController *controller = (ViewController *)aDatePickerCell.delegate;

    if ((controller == self) && (aDatePickerCell == self.datePickerControl.cell))
    {
        // Override the date and time?
        if (self.overrideDateCheck.cell.state)
        {
            // Override the date using the user specified date.
            *proposedDateValue = self.overrideDate.dateValue;
        }
    }
}

@end
```

[Next](ReadMe.md.md)[Previous](DatePicker-GalleryViewController.h.md)

