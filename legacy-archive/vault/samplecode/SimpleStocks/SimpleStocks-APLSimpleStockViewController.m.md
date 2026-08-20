---
title: SimpleStocks
apple_id: DTS40011103
resource_type: Sample Code
platform: iOS
topic: Graphics & Animation
technology: null
published: '2013-04-03'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleStocks/Listings/SimpleStocks_APLSimpleStockViewController_m.html
archived_at: '2026-07-18T03:24:14.093982Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleStocks](SimpleStocks.md)


[Next](SimpleStocks-APLViewController.m.md)[Previous](SimpleStocks-APLSimpleStockViewController.h.md)

# SimpleStocks/APLSimpleStockViewController.m

```objc
/*
     File: APLSimpleStockViewController.m 
 Abstract: This view controller handles orientation changes and acts as the data source for SimpleStockView. 
  Version: 2.0 

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

 Copyright (C) 2013 Apple Inc. All Rights Reserved. 

 */

#import "APLSimpleStockViewController.h"
#import "APLDailyTradeInfoSource.h"
#import "APLSimpleStockView.h"

@implementation APLSimpleStockViewController

- (void)didRotateFromInterfaceOrientation:(UIInterfaceOrientation)fromInterfaceOrientation {
    [[self view] setNeedsDisplay];
}

#pragma mark GraphViewDataSource methods

- (NSInteger)graphViewDailyTradeInfoCount:(APLSimpleStockView *)graphView {
    return [[DailyTradeInfoSource tradeInfoArray] count];
}

/*
 Return the month to be drawn.
 */
- (NSArray *)graphViewSortedMonths:(APLSimpleStockView *)graphView {
    NSCalendar *calendar = [NSCalendar currentCalendar];
    NSArray *closingDates = [[DailyTradeInfoSource tradeInfoArray] valueForKeyPath:@"tradingDate"];
    __block NSCountedSet *months = [NSCountedSet set];
    [closingDates enumerateObjectsUsingBlock:^(id closingDate, NSUInteger index, BOOL *stop) {
        [months addObject:[calendar components:NSMonthCalendarUnit fromDate:closingDate]];
    }];
    NSSortDescriptor *descriptor = [NSSortDescriptor sortDescriptorWithKey:@"month" ascending:YES];
    NSArray *descriptors = [NSArray arrayWithObject:descriptor];
    return [months sortedArrayUsingDescriptors:descriptors];
}

/*
 For the given month (in components) return the number of trades some months have 20 trading days, some have 23. This method makes it possible for us to layout the months names accordingly
 */
- (NSInteger)graphView:(APLSimpleStockView *)graphView tradeCountForMonth:(NSDateComponents *)components {
    NSCalendar *calendar = [NSCalendar currentCalendar];
    NSArray *closingDates = [[DailyTradeInfoSource tradeInfoArray] valueForKeyPath:@"tradingDate"];
    __block NSCountedSet *months = [NSCountedSet set];
    [closingDates enumerateObjectsUsingBlock:^(id closingDate, NSUInteger index, BOOL *stop) {
        [months addObject:[calendar components:NSMonthCalendarUnit fromDate:closingDate]];
    }];
    return [months countForObject:components];
}

/*
 * Return the model objects
 */
- (NSArray *)graphViewDailyTradeInfos:(APLSimpleStockView *)graphView {
    return [DailyTradeInfoSource tradeInfoArray];
}

/*
 * Return the max closing price
 */
- (CGFloat)graphViewMaxClosingPrice:(APLSimpleStockView *)graphView {
    return [[[DailyTradeInfoSource tradeInfoArray] valueForKeyPath:@"@max.closingPrice"] floatValue];
}

/*
 * Return the min closing price
 */
- (CGFloat)graphViewMinClosingPrice:(APLSimpleStockView *)graphView {
    return [[[DailyTradeInfoSource tradeInfoArray] valueForKeyPath:@"@min.closingPrice"] floatValue];
}

/*
 * Return the max trading volume
 */
- (CGFloat)graphViewMaxTradingVolume:(APLSimpleStockView *)graphView {
    return [[[DailyTradeInfoSource tradeInfoArray] valueForKeyPath:@"@max.tradingVolume"] floatValue];
}

/*
 * Return the min trading volume
 */
- (CGFloat)graphViewMinTradingVolume:(APLSimpleStockView *)graphView {
    return [[[DailyTradeInfoSource tradeInfoArray] valueForKeyPath:@"@min.tradingVolume"] floatValue];
}

@end
```

[Next](SimpleStocks-APLViewController.m.md)[Previous](SimpleStocks-APLSimpleStockViewController.h.md)

