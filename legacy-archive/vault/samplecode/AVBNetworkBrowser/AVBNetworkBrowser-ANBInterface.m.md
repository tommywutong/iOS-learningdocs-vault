---
title: AVBNetworkBrowser
apple_id: DTS40014220
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioVideoBridging
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/samplecode/sc1827/Listings/AVBNetworkBrowser_ANBInterface_m.html
archived_at: '2026-07-26T19:54:13.916682Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVBNetworkBrowser](AVBNetworkBrowser.md)


[Next](AVBNetworkBrowser-ANBWindowController.h.md)[Previous](AVBNetworkBrowser-ANBInterface.h.md)

# AVBNetworkBrowser/ANBInterface.m

```objc
/*

     File: ANBInterface.m
 Abstract: Implementation for class which wraps around an AVBInterface and provides tracking of AVDECC Entities. It also uses IOKit to track the entity discovery objects to reset the delegate and restart discovery after a link down.
  Version: 1.0

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

 Copyright (C) 2014 Apple Inc. All Rights Reserved.

 */

#import "ANBInterface.h"

#import "ANBAVDECCEntity.h"

#import <SystemConfiguration/SystemConfiguration.h>

@interface ANBInterface ()
{
    //Instance variables for tracking the addition of entity discovery objects
    dispatch_queue_t _notificationQueue;
    IONotificationPortRef _notificationPort;

    io_iterator_t _entityDiscoveryIterator;
}

@end

@implementation ANBInterface

//Create a matching dictionary for this interface.
- (NSDictionary *)iokitMatchingDictionary
{
    NSMutableDictionary *matchDict = [NSMutableDictionary dictionary];

    [matchDict setObject:@"IOAVB17221EntityDiscovery" forKey:@kIOProviderClassKey];
    [matchDict setObject:@{@kIOProviderClassKey:@kIOEthernetInterfaceClass, @"BSD Name":self.ifName} forKey:@kIOParentMatchKey];

    return matchDict;
}

- (id)initWithInterface:(AVBInterface *)anInterface
{
    self = [super init];
    if(self)
    {
        self.interface = anInterface;
        self.ifName = anInterface.interfaceName;

        //Get the name that is used for the interface in System Preferences
        SCPreferencesRef prefs = SCPreferencesCreate(kCFAllocatorDefault, CFSTR("com.apple.samplecode.ANBInterface"), NULL);

        if(prefs)
        {
            CFArrayRef services = SCNetworkServiceCopyAll(prefs);

            if(services)
            {
                CFIndex index;
                CFIndex count = CFArrayGetCount(services);

                for(index = 0; index < count; index++)
                {
                    SCNetworkServiceRef service = CFArrayGetValueAtIndex(services, index);

                    SCNetworkInterfaceRef interfaceRef = SCNetworkServiceGetInterface(service);

                    CFStringRef bsdName = SCNetworkInterfaceGetBSDName(interfaceRef);

                    if([self.ifName isEqualToString:(__bridge NSString *)bsdName])
                    {
                        self.userInterfaceName = [NSString stringWithFormat:@"%@ - %@", (__bridge NSString *)(SCNetworkInterfaceGetLocalizedDisplayName(interfaceRef)), self.ifName];
                        break;
                    }
                }

                CFRelease(services);
            }
            CFRelease(prefs);
        }
        else
        {
            //Couldn't get a system configuration object so just use the BSD name
            self.userInterfaceName = self.ifName;
        }

        self.avdeccEntities = [NSMutableArray array];

        //The following code is needed to handle the way AVB17221EntityDiscovery behaves in OS X Mavericks. In Mavericks the AVB17221EntityDiscovery object
        //will go away whenever the link goes down on the interface. When the link comes back up, a new AVB17221EntityDiscovery object is created for the
        //interface. The delegate needs to be reset to this object and the iterators re-primed when this happens. This IOKit matching will make this happen
        _notificationQueue = dispatch_queue_create([NSString stringWithFormat:@"com.apple.samplecode.%@.%@", [self className], self.ifName].UTF8String, 0);

        mach_port_t masterPort = 0;

        IOMasterPort(mach_task_self(), &masterPort);

        if(masterPort)
        {
            _notificationPort = IONotificationPortCreate(masterPort);
            IONotificationPortSetDispatchQueue(_notificationPort, _notificationQueue);

            IOObjectRelease(masterPort);
        }

        CFDictionaryRef matchDict = (CFDictionaryRef)CFBridgingRetain([self iokitMatchingDictionary]);

        if(matchDict)
        {
            IOServiceAddMatchingNotification(_notificationPort, kIOMatchedNotification, matchDict, entityDiscoveryMatchedCallback, (__bridge void *)self, &_entityDiscoveryIterator);

            dispatch_async(_notificationQueue, ^{
                entityDiscoveryMatchedCallback((__bridge void *)self, _entityDiscoveryIterator);
            });
        }
    }
    return self;
}

//Function called by IOKit for the notification
static void entityDiscoveryMatchedCallback(void *refcon, io_iterator_t iterator)
{
    @autoreleasepool
    {
        io_service_t service;

        //Loop through the iterator to clear it
        while((service = IOIteratorNext(iterator)))
        {
            IOObjectRelease(service);
        }

        //The IOKit match is very explicit this will only be called for the one we care about
        if(refcon)
        {
            [(__bridge ANBInterface *)refcon _entityDiscoveryMatched];
        }
    }
}

//Called when the IOKit notification fires
- (void)_entityDiscoveryMatched
{
    int timeout = 20;

    //Since the AudioVideoBridging framework also uses this same notification asynchronously it may not have updated it's internal state yet.
    //Try this a few times (will timeout after 2 seconds)
    while(timeout > 0 && !self.interface.entityDiscovery)
    {
        usleep(100);
    }

    //Set ourself as the discovery delegate and prime the iterators so they start matching
    self.interface.entityDiscovery.discoveryDelegate = self;
    [self.interface.entityDiscovery primeIterators];
}

#pragma mark AVB17221EntityDiscoveryDelegate methods

- (void)didAddRemoteEntity:(AVB17221Entity *)newEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    ANBAVDECCEntity *avdeccEntity = [[ANBAVDECCEntity alloc] initWithADPEntity:newEntity onInterface:self.interface];

    //Call this on the main queue because it causes a UI update.
    dispatch_async(dispatch_get_main_queue(), ^{
        //Trigger the KVO notifications and add the entity
        [self willChangeValueForKey:@"avdeccEntities"];
        [self.avdeccEntities addObject:avdeccEntity];
        [self didChangeValueForKey:@"avdeccEntities"];
    });

    [avdeccEntity parseEntity];
}

- (void)didRemoveRemoteEntity:(AVB17221Entity *)oldEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    ANBAVDECCEntity *entity = nil;

    //Do we actually have one of these?
    for(ANBAVDECCEntity *possible in self.avdeccEntities)
    {
        if(possible.adpEntity.entityID == oldEntity.entityID)
        {
            entity = possible;
            break;
        }
    }

    if(entity)
    {
        //Call this on the main queue because it causes a UI update.
        dispatch_async(dispatch_get_main_queue(), ^{
            //Trigger the KVO notifications and remove the entity
            [self willChangeValueForKey:@"avdeccEntities"];
            [self.avdeccEntities removeObject:entity];
            [self didChangeValueForKey:@"avdeccEntities"];
        });
    }
}

- (void)didRediscoverRemoteEntity:(AVB17221Entity *)entity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    //We don't care about rediscoveries but the protocol requires this
}

- (void)didUpdateRemoteEntity:(AVB17221Entity *)entity changedProperties:(AVB17221EntityPropertyChanged)changedProperties on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    //We don't care about updates but the protocol requires this
}

- (void)didAddLocalEntity:(AVB17221Entity *)newEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    ANBAVDECCEntity *avdeccEntity = [[ANBAVDECCEntity alloc] initWithADPEntity:newEntity onInterface:self.interface];

    //Call this on the main queue because it causes a UI update.
    dispatch_async(dispatch_get_main_queue(), ^{
        //Trigger the KVO notifications and add the entity
        [self willChangeValueForKey:@"avdeccEntities"];
        [self.avdeccEntities addObject:avdeccEntity];
        [self didChangeValueForKey:@"avdeccEntities"];
    });

    [avdeccEntity parseEntity];
}

- (void)didRemoveLocalEntity:(AVB17221Entity *)oldEntity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    ANBAVDECCEntity *entity = nil;

    //Do we actually have one of these?
    for(ANBAVDECCEntity *possible in self.avdeccEntities)
    {
        if(possible.adpEntity.entityID == oldEntity.entityID)
        {
            entity = possible;
            break;
        }
    }

    if(entity)
    {
        //Call this on the main queue because it causes a UI update.
        dispatch_async(dispatch_get_main_queue(), ^{
            //Trigger the KVO notifications and remove the entity
            [self willChangeValueForKey:@"avdeccEntities"];
            [self.avdeccEntities removeObject:entity];
            [self didChangeValueForKey:@"avdeccEntities"];
        });
    }
}

- (void)didRediscoverLocalEntity:(AVB17221Entity *)entity on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    //We don't care about rediscoveries but the protocol requires this
}

- (void)didUpdateLocalEntity:(AVB17221Entity *)entity changedProperties:(AVB17221EntityPropertyChanged)changedProperties on17221EntityDiscovery:(AVB17221EntityDiscovery *)entityDiscovery
{
    //We don't care about updates but the protocol requires this
}

- (void)dealloc
{
    //Clean up the IOKit code
    if(_entityDiscoveryIterator)
    {
        IOObjectRelease(_entityDiscoveryIterator);
    }

    if(_notificationPort)
    {
        IONotificationPortDestroy(_notificationPort);
    }
}

@end
```

[Next](AVBNetworkBrowser-ANBWindowController.h.md)[Previous](AVBNetworkBrowser-ANBInterface.h.md)

