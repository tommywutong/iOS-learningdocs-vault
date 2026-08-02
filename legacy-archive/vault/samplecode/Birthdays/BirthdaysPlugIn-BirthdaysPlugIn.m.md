---
title: Birthdays
apple_id: DTS10003982
resource_type: Sample Code
platform: Safari|macOS
topic: Data Management
technology: null
published: '2010-07-20'
source_url: https://developer.apple.com/library/archive/samplecode/Birthdays/Listings/BirthdaysPlugIn_BirthdaysPlugIn_m.html
archived_at: '2026-07-18T03:01:53.953721Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Birthdays](Birthdays.md)


[Next](Code-Birthdays.css.md)[Previous](BirthdaysPlugIn-BirthdaysPlugIn.h.md)

# BirthdaysPlugIn/BirthdaysPlugIn.m

```objc

/*
     File: BirthdaysPlugIn.m
 Abstract: Widget plug-in that fetches birthdays occurring in the current day, week, or month 
 and returns relevant strings back to JavaScript.
  Version: 1.2

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

 Copyright (C) 2010 Apple Inc. All Rights Reserved.

*/

#import "BirthdaysPlugIn.h"

// Comparison function for sorting returned ABPeople by birthday
NSInteger CompareDates(id person1, id person2, void *context) {
    if ([person1 isMemberOfClass:[ABPerson class]] && [person2 isMemberOfClass:[ABPerson class]]) {


        NSCalendar *gregorian = [[[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar] autorelease];

        NSDateComponents *cal1 = [gregorian components:unitFlags fromDate:[person1 valueForKey:kABBirthdayProperty]];
        NSDateComponents *cal2 = [gregorian components:unitFlags fromDate:[person2 valueForKey:kABBirthdayProperty]];

        if ([cal1 month] < [cal2 month]) {
            return NSOrderedAscending;
        }  else if ([cal1 month] > [cal2 month]) {
            return NSOrderedDescending;
        } else { // same month; compare the days
            if ([cal1 day] < [cal2 day]) {
                return NSOrderedAscending;
            } else if ([cal1 day] > [cal2 day]) {
                return NSOrderedDescending;
            }
        }
        return NSOrderedSame;
    }
    return NSOrderedDescending;
}


@implementation BirthdaysPlugIn

#pragma mark *** WidgetPlugin methods ***

// initWithWebView is called as the Dashboard widget and its WebView
// are initialized, which is when the widget plug-in is loaded
// This is just an object initializer; DO NOT use the passed WebView
// to manipulate WebScriptObjects or anything in the WebView's hierarchy
- (id) initWithWebView:(WebView*)webView {
    self = [super init];
    return self;
}

#pragma mark *** WebScripting methods ***

// windowScriptObjectAvailable passes the JavaScript window object referring
// to the plug-in's parent window (in this case, the Dashboard widget)
// We use that to register our plug-in as a var of the window object;
// This allows the plug-in to be referenced from JavaScript via 
// window.<plugInName>, or just <plugInName>
- (void) windowScriptObjectAvailable:(WebScriptObject*)webScriptObject {
    [webScriptObject setValue:self forKey:@"BirthdaysPlugIn"];
}

// Prevent direct key access from JavaScript
// Write accessor methods and expose those if necessary
+ (BOOL) isKeyExcludedFromWebScript:(const char*)key {
    return YES;
}

// Used for convenience of WebScripting names below
NSString * const kWebSelectorPrefix = @"web_";

// This is where prefixing our JavaScript methods with web_ pays off:
// instead of a huge if/else trail to decide which methods to exclude,
// just check the selector names for kWebSelectorPrefix
+ (BOOL) isSelectorExcludedFromWebScript:(SEL)aSelector {
    return !([NSStringFromSelector(aSelector) hasPrefix:kWebSelectorPrefix]);
}

// Another simple implementation: take the first token of the Obj-C method signature
// and remove the web_ prefix. So web_birthdaysToday is called from JavaScript as
// BirthdaysPlugIn.birthdaysToday
+ (NSString *) webScriptNameForSelector:(SEL)aSelector {
    NSString*   selName = NSStringFromSelector(aSelector);

    if ([selName hasPrefix:kWebSelectorPrefix] && ([selName length] > [kWebSelectorPrefix length])) {
        return [[[selName substringFromIndex:[kWebSelectorPrefix length]] componentsSeparatedByString: @":"] objectAtIndex: 0];
    }
    return nil;
}

#pragma mark *** Web-exposed methods ***

- (NSArray *) web_birthdaysToday {
    return [self stringResultsForPeople:[self birthdaysToday]];
}

- (NSArray *) web_birthdaysThisWeek {
    return [self stringResultsForPeople:[self birthdaysThisWeek]];
}

- (NSArray *) web_birthdaysThisMonth {
    return [self stringResultsForPeople:[self birthdaysThisMonth]];
}

#pragma mark *** Birthday logic ***

- (NSArray *) birthdaysToday {
    // AB search requires "today" to be an interval of 1 (not 0)
    return [self peopleWithBirthdaysInFuture:1];
}

// Find upcoming birthdays remaining this week
// Does not find birthdays in the past (i.e. starts from today)
- (NSArray *) birthdaysThisWeek {
    NSDate *now = [NSDate date];
    NSCalendar *gregorian = [[[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar] autorelease];
    NSDateComponents *todaysDate = [gregorian components:NSWeekdayCalendarUnit fromDate:now];

    int daysLeftInWeek = (kDaysInWeek - [todaysDate weekday]);
    return [self peopleWithBirthdaysInFuture:daysLeftInWeek];
}

// Finds upcoming birthdays for the rest of the current month
// Does not find birthdays in the past (i.e. starts from today)
- (NSArray *) birthdaysThisMonth {
    NSDate *rightNow = [NSDate date];
    NSCalendar *gregorian = [[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar];
    NSRange monthRange = [gregorian rangeOfUnit:NSDayCalendarUnit inUnit:NSMonthCalendarUnit forDate:rightNow];
    NSDateComponents *dayOfWeekComponent = [gregorian components:NSDayCalendarUnit fromDate:rightNow];

        // Needs to be at least 1 for search to work;
        // If today is the last day of the month we still have a value of 1,
        // second to last day --> 2, etc
    int daysLeftInMonth = 1;
    daysLeftInMonth += ( monthRange.length - [dayOfWeekComponent day]);
    return [self peopleWithBirthdaysInFuture:daysLeftInMonth];
}

// Searches Address Book for people with birthdays in the next __ days
- (NSArray *) peopleWithBirthdaysInFuture:(int)days {       
    NSNumber *searchInterval = [NSNumber numberWithInt:(kSecondsInDay*days)];
    ABSearchElement *birthdayToday = [ABPerson searchElementForProperty:kABBirthdayProperty
                                                                  label:nil
                                                                    key:nil
                                                                  value:searchInterval
                                                             comparison:kABWithinIntervalFromTodayYearless];

    return [[ABAddressBook addressBook] recordsMatchingSearchElement:birthdayToday];
}

- (NSDate *) myBirthday {
    return [[[ABAddressBook sharedAddressBook] me] valueForProperty:kABBirthdayProperty];;
}

#pragma mark *** Utility methods ***

// Condense useful info into string arrays for transmission across ObjC-JS bridge
- (NSArray *) stringResultsForPeople:(NSArray *) people {

    NSArray *sortedPeople = [people sortedArrayUsingFunction:CompareDates context:NULL];

    NSMutableArray *results = [NSMutableArray arrayWithCapacity:[sortedPeople count]];
    ABPerson *currPerson = nil;
    NSEnumerator *peopleEnumerator = [sortedPeople objectEnumerator];
    while (currPerson = [peopleEnumerator nextObject]) {
        NSString *firstName = [currPerson valueForProperty:kABFirstNameProperty];
        NSString *lastName = [currPerson valueForProperty:kABLastNameProperty];



        NSCalendar *gregorian = [[[NSCalendar alloc] initWithCalendarIdentifier:NSGregorianCalendar] autorelease];

        // kABBirthdayProperty is only guaranteed to be an NSDate; convert it to NSDateComponents
        NSDateComponents *birthday = [gregorian components:unitFlags fromDate:[currPerson valueForProperty:kABBirthdayProperty]];
        NSMutableArray *personDetails = [NSMutableArray arrayWithCapacity:2];


        [personDetails addObject:(firstName ? firstName : @"")];
        [personDetails addObject:(lastName ? lastName : @"")];
        [personDetails addObject:[NSString stringWithFormat:@"%d/%d", [birthday month], [birthday day]]];
        [personDetails addObject:[currPerson uniqueId]];
        [results addObject:personDetails];
    }

    return results;
}

@end
```

[Next](Code-Birthdays.css.md)[Previous](BirthdaysPlugIn-BirthdaysPlugIn.h.md)

