---
title: People
apple_id: DTS40009050
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: SyncServices
published: '2009-07-21'
source_url: https://developer.apple.com/library/archive/samplecode/SyncServices_People/Listings/AppControllerExtensions_m.html
archived_at: '2026-07-18T03:25:52.531242Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [People](People.md)


[Next](AppControllerSyncing-annotated.m.md)[Previous](AppControllerExtensions.h.md)

# AppControllerExtensions.m

```objc
/*

File: AppControllerExtensions.m

Abstract: Part of the People project demonstrating use of the
              SyncServices framework

Version: 0.1

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Computer, Inc. ("Apple") in consideration of your agreement to the
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
Neither the name, trademarks, service marks or logos of Apple Computer,
Inc. may be used to endorse or promote products derived from the Apple
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

Copyright © 2005-2009 Apple Computer, Inc., All Rights Reserved.

*/ 

#import "AppControllerExtensions.h"
#import "Constants.h"

@implementation AppController (Extensions)

- (BOOL)matchName:(NSString *)name withRecord:(NSDictionary *)record
{
    BOOL rc = NO;
    NSString *firstName = nil;
    NSString *lastName = nil;
    NSRange range = [name rangeOfString:@" "];
    if (range.location != NSNotFound) {
        firstName = [name substringToIndex:range.location];
        lastName = [name substringFromIndex:range.location + 1];
    }
    if (lastName) {
        rc = (([[record objectForKey:FirstNameKey] caseInsensitiveCompare:firstName] == NSOrderedSame) &&
              ([[record objectForKey:LastNameKey] caseInsensitiveCompare:lastName] == NSOrderedSame));
        if (rc == YES) return YES;
    }
    return (([[[record objectForKey:FirstNameKey] lowercaseString] rangeOfString:name].length > 0) ||
            ([[[record objectForKey:MiddleNameKey] lowercaseString] rangeOfString:name].length > 0) ||
            ([[[record objectForKey:LastNameKey] lowercaseString] rangeOfString:name].length > 0) ||
            ([[[record objectForKey:CompanyNameKey] lowercaseString] rangeOfString:name].length > 0) ||
            ([[[record objectForKey:LocationNameKey] lowercaseString] rangeOfString:name].length > 0));
}

- (void)_find:(NSString *)string
{
    NSString *name = [string lowercaseString];

    if ((name == nil) || ([name isEqualToString:@""])) return;

    NSInteger selectedRow = [m_table selectedRow];
    NSUInteger idx = NSNotFound;
    NSUInteger ii, count;
    for (ii = selectedRow + 1, count = [m_records count]; ii < count; ii++) {
        NSDictionary *record = [m_records objectAtIndex:ii];
        if ([self matchName:name withRecord:record]) {
            idx = ii;
            break;
        }
    }
    if (idx == NSNotFound) {
        for (ii = 0; ii <= selectedRow; ii++) {
            NSDictionary *record = [m_records objectAtIndex:ii];
            if ([self matchName:name withRecord:record]) {
                idx = ii;
                break;
            }
        }
    }
    if (idx != NSNotFound) {
        [m_table selectRowIndexes:[NSIndexSet indexSetWithIndex:idx] byExtendingSelection:NO];        
        [m_table scrollRowToVisible:idx];
    } else {
        NSBeep();
    }
}

- (IBAction)find:(id)sender
{
    [self _find:[sender stringValue]];
}

static NSInteger sortFunction (id ldict, id rdict, void *context) {
    NSComparisonResult rc;
    NSString *leftName = [ldict objectForKey:LastNameKey];
    NSString *rightName = [rdict objectForKey:LastNameKey];

    if ((leftName != nil) && (rightName != nil)) {
        rc = [leftName caseInsensitiveCompare:rightName];
    } else if (leftName == nil) {
        rc = rightName ? NSOrderedAscending : NSOrderedSame;
    } else {
        rc = NSOrderedDescending;
    }
    if (rc == NSOrderedSame) {
        leftName = [ldict objectForKey:FirstNameKey];
        rightName = [rdict objectForKey:FirstNameKey];
        if ((leftName != nil) && (rightName != nil)) {
            rc = [leftName caseInsensitiveCompare:rightName];
        } else if (leftName == nil) {
            rc = rightName ? NSOrderedAscending : NSOrderedSame;
        } else {
            rc = NSOrderedDescending;
        }
    }
    if (rc == NSOrderedSame) {
        leftName = [ldict objectForKey:CompanyNameKey];
        rightName = [rdict objectForKey:CompanyNameKey];
        rc = [leftName caseInsensitiveCompare:rightName];
    }
    return rc;
}

- (void)sortNamesAndDisplay
{
    NSInteger idx = [m_table selectedRow];
    NSDictionary *selectedRecord = nil;

    if (idx != -1) selectedRecord = [m_records objectAtIndex:idx];
    [m_records sortUsingFunction:sortFunction context:nil];

    [m_table reloadData];
    if (selectedRecord) {
        [self _find:[NSString stringWithFormat:@"%@ %@", [selectedRecord objectForKey:FirstNameKey], [selectedRecord objectForKey:LastNameKey]]];
    }
}

@end
```

[Next](AppControllerSyncing-annotated.m.md)[Previous](AppControllerExtensions.h.md)

