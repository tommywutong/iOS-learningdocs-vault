---
title: ABPresence
apple_id: DTS10004061
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2006-08-04'
source_url: https://developer.apple.com/library/archive/samplecode/ABPresence/Listings/ServiceWatcher_m.html
archived_at: '2026-07-18T02:59:22.544359Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ABPresence](ABPresence.md)


[Next](Document%20Revision%20History.md)[Previous](ServiceWatcher.h.md)

# ServiceWatcher.m

```objc
/*

File: ServiceWatcher.m

Abstract: This class registers for notifications from IMService. It takes
incoming notifications and processes them into their respective AB cards,
which the PeopleDataSource then responds to.

Version: 1.1

Disclaimer: IMPORTANT:  This Apple software is supplied to you by 
Apple Inc. ("Apple") in consideration of your agreement to the
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
Neither the name, trademarks, service marks or logos of Apple Inc. 
may be used to endorse or promote products derived from the Apple
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

Copyright (C) 2006-2007 Apple Inc. All Rights Reserved.

*/

#import "ServiceWatcher.h"
#import <InstantMessage/IMService.h>
#import <AddressBook/AddressBook.h>

NSString * kAddressBookPersonStatusChanged = @"AddressBookPersonStatusChanged";
NSString * kStatusImagesChanged = @"StatusImagesChanged";

@implementation ServiceWatcher

- (void) startMonitoring
{
    NSNotificationCenter * nCenter = [IMService notificationCenter];

    [nCenter addObserver: self
                selector: @selector(imPersonStatusChangedNotification:)
                    name: IMPersonStatusChangedNotification
                  object: nil];

    [nCenter addObserver: self
                selector: @selector(imStatusImagesChangedAppearanceNotification:)
                    name: IMStatusImagesChangedAppearanceNotification
                  object: nil];
}

- (void) stopMonitoring
{
    NSNotificationCenter * nCenter = [IMService notificationCenter];

    [nCenter removeObserver: self];
}

- (void) awakeFromNib
{
    [self startMonitoring];
}


#pragma mark -
#pragma mark Notifications

/*! Received from IMService's custom notification center. Posted when a different user (screenName) logs in, logs off, goes away, 
    and so on. This notification is for the IMService object.The user information dictionary will always contain an 
    IMPersonScreenNameKey and an IMPersonStatusKey, and no others. */
- (void) imPersonStatusChangedNotification:(NSNotification *)notification
{
    IMService * service = [notification object];
    NSDictionary * userInfo = [notification userInfo];
    NSString * screenName = [userInfo objectForKey: IMPersonScreenNameKey];

    NSArray * abPersons = [service peopleWithScreenName: screenName];

    for (ABPerson * person in abPersons)
        [[NSNotificationCenter defaultCenter] postNotificationName: kAddressBookPersonStatusChanged
                                                            object: person];
}

/*! Received from IMService's custom notification center. Posted when the user changes their preferred images for displaying status. 
    This notification is relevant to no particular object. The user information dictionary will not contain keys. Clients that display 
    status information graphically (using the green/yellow/red dots) should call <tt>imageURLForStatus:</tt> to get the new image. 
    See "Class Methods" for IMService in this document. */
- (void) imStatusImagesChangedAppearanceNotification:(NSNotification *)notification
{
        [[NSNotificationCenter defaultCenter] postNotificationName: kStatusImagesChanged
                                                            object: self];
}

@end
```

[Next](Document%20Revision%20History.md)[Previous](ServiceWatcher.h.md)

