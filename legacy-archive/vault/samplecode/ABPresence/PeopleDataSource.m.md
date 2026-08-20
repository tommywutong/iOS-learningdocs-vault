---
title: ABPresence
apple_id: DTS10004061
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: InstantMessage
published: '2006-08-04'
source_url: https://developer.apple.com/library/archive/samplecode/ABPresence/Listings/PeopleDataSource_m.html
archived_at: '2026-07-18T02:59:22.392477Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [ABPresence](ABPresence.md)


[Next](ServiceWatcher.h.md)[Previous](PeopleDataSource.h.md)

# PeopleDataSource.m

```objc
/*

File: PeopleDataSource.m

Abstract: This class acts as the data source for the ABPresence table view. 
It provides your buddies real names as well as the appropriate status gem.

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

#import "PeopleDataSource.h"

#import <InstantMessage/IMService.h>
#import "ABPersonDisplayNameAdditions.h"
#import "ServiceWatcher.h"

@implementation PeopleDataSource

- (void) dealloc
{
    [_abPeople release];
    [_imPersonStatus release];

    [super dealloc];
}

// Initialize and register for AddressBook notifications
- (void) awakeFromNib
{
    _imPersonStatus = [[NSMutableArray alloc] init];

    // We don't need to query the staus of everyone, we will wait for notifications of
    // their status to arrive, so we just set them all up as offline.
    [self setupABPeople];

    [[NSNotificationCenter defaultCenter] addObserver: self
                                             selector: @selector(abDatabaseChangedExternallyNotification:)
                                                 name: kABDatabaseChangedExternallyNotification
                                               object: nil];

    [[NSNotificationCenter defaultCenter] addObserver: self
                                             selector: @selector(addressBookPersonStatusChanged:)
                                                 name: kAddressBookPersonStatusChanged
                                               object: nil];

    [[NSNotificationCenter defaultCenter] addObserver: self
                                             selector: @selector(statusImagesChanged:)
                                                 name: kStatusImagesChanged
                                               object: nil];
}

#pragma mark -
#pragma mark Data Loading

/* This dumps all the status information and rebuilds the array against the current _abPeople
   Fairly expensive, so this is only done when necessary */
- (void) rebuildStatusInformation
{   
    // Now scan through all the people, adding their status to the status cache array
    int i = 0, count = [_abPeople count];
    for ( i = 0 ; i < count ; i++ ) {
        ABPerson * person = [_abPeople objectAtIndex: i];

        IMPersonStatus bestStatus = IMPersonStatusOffline; // Let's assume they're offline to start
        for (IMService * service in [IMService allServices]) {
            NSArray * screenNames = [service screenNamesForPerson: person];

            for (NSString * screenName in screenNames) {
                NSDictionary * dictionary = [service infoForScreenName: screenName];
                NSNumber * status = [dictionary objectForKey: IMPersonStatusKey];
                if ( status != nil ) {
                    IMPersonStatus thisStatus = [status intValue];
                    if ( IMComparePersonStatus(bestStatus, thisStatus) != NSOrderedAscending ) 
                        bestStatus = thisStatus;
                }
            }
        }

        [_imPersonStatus replaceObjectAtIndex: i withObject: [NSNumber numberWithUnsignedInt: bestStatus]];
    }

    [_table reloadData];
}

/* Rebuild status information for a given person, much faster than a full rebuild */
- (void) rebuildStatusInformationForPerson:(ABPerson *)forPerson
{
    int i = 0, count = [_abPeople count];
    for ( i = 0 ; i < count ; i++ ) {
        ABPerson * person = [_abPeople objectAtIndex: i];

        // If this is the person we're looking for
        if ( person == forPerson ) {
            IMPersonStatus bestStatus = IMPersonStatusOffline; // Let's assume they're offline to start

            // Scan through all the services, taking the 'best' status we can find
            for (IMService * service in [IMService allServices]) {
                NSArray * screenNames = [service screenNamesForPerson: person];

                // Ask for the status on each of their screen names
                for (NSString * screenName in screenNames) {
                    NSDictionary * dictionary = [service infoForScreenName: screenName];
                    NSNumber * status = [dictionary objectForKey: IMPersonStatusKey];
                    if ( status != nil ) {
                        IMPersonStatus thisStatus = [status intValue];
                        if ( IMComparePersonStatus(bestStatus, thisStatus) != NSOrderedAscending ) 
                            bestStatus = thisStatus;
                    }
                }
            }

            [_imPersonStatus replaceObjectAtIndex: i withObject: [NSNumber numberWithUnsignedInt: bestStatus]];
            [_table reloadData];
            break;
        }       
    }

}

/* Sets up all our internal data */
- (void) setupABPeople
{
    // Forget all my old people
    [_abPeople release];

    // Keep around a copy of all the people in the AB now
    _abPeople = [[[ABAddressBook sharedAddressBook] people] mutableCopy];

    // Sort them by display name
    [_abPeople sortUsingSelector: @selector(compareDisplayNames:)];

    // Assume everyone is offline.
    [_imPersonStatus removeAllObjects];
    int i = 0, count = [_abPeople count];
    NSNumber *offlineNumber =  [NSNumber numberWithUnsignedInt: IMPersonStatusOffline];
    for ( i = 0 ; i < count ; i++ ) {
        [_imPersonStatus addObject:offlineNumber];
    }
}

/* This will do a full flush of people in our AB Cache, along with rebuilding their status */
- (void) reloadABPeople
{
    [self setupABPeople];

    // Now recache all the status info, this will spawn a reload of the table
    [self rebuildStatusInformation];
}

#pragma mark -
#pragma mark NSTableView Data Source

- (NSInteger)numberOfRowsInTableView:(NSTableView *)tableView
{
    return [_abPeople count];
}

- (id)tableView:(NSTableView *)tableView objectValueForTableColumn:(NSTableColumn *)tableColumn row:(NSInteger)row
{
    NSString * identifier = [tableColumn identifier];
    if ( [identifier isEqualToString: @"image"]) {
        IMPersonStatus status = [[_imPersonStatus objectAtIndex: row] intValue];
        return [NSImage imageNamed: [IMService imageNameForStatus: status]];

    } else if ( [identifier isEqualToString: @"name"] ) {
        return [[_abPeople objectAtIndex: row] displayName];
    }

    return nil;
}


#pragma mark -
#pragma mark Notifications

// Posted from ServiceWatcher
// The object of this notification is an ABPerson who's status has
// Changed
- (void) addressBookPersonStatusChanged:(NSNotification *)notification
{
    [self rebuildStatusInformationForPerson: [notification object]];
}

// Posted from ServiceWatcher
// We should reload the tableview, because the user has changed the
// status images that iChat is using.
- (void) statusImagesChanged:(NSNotification *)notification
{
    [_table reloadData];
}

// If the AB database changes, force a reload of everyone
// We could look in the notification to catch differential updates, but for now
// This is fine.
- (void) abDatabaseChangedExternallyNotification:(NSNotification *)notification
{
    [self reloadABPeople];
}

@end
```

[Next](ServiceWatcher.h.md)[Previous](PeopleDataSource.h.md)

