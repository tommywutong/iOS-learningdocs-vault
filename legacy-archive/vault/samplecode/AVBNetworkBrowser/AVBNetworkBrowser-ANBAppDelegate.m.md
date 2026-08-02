---
title: AVBNetworkBrowser
apple_id: DTS40014220
resource_type: Sample Code
platform: macOS
topic: Audio, Video, & Visual Effects
technology: AudioVideoBridging
published: '2014-03-20'
source_url: https://developer.apple.com/library/archive/samplecode/sc1827/Listings/AVBNetworkBrowser_ANBAppDelegate_m.html
archived_at: '2026-07-26T19:54:13.799402Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [AVBNetworkBrowser](AVBNetworkBrowser.md)


[Next](AVBNetworkBrowser-ANBAVDECCEntity.h.md)[Previous](AVBNetworkBrowser-ANBAppDelegate.h.md)

# AVBNetworkBrowser/ANBAppDelegate.m

```objc
/*

     File: ANBAppDelegate.m
 Abstract: Implementation for application delegate class. This class also does the IOKit matching for network interface controllers.
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

#import "ANBAppDelegate.h"

#import <AudioVideoBridging/AudioVideoBridging.h>

#import "ANBInterface.h"

#import "ANBWindowController.h"

#import <IOKit/IOKitLib.h>
#import <IOKit/IOKitKeys.h>

//This is an Apple OUI which is used for sample code purposes only. This MUST be changed for other uses.
#define ABU_OUI 0x000393llu

@interface ANBAppDelegate ()
{
    //instance variables for IOKit matching of network interface controllers
    NSMutableDictionary *_interfaces;
    dispatch_queue_t _controllerQueue;
    IONotificationPortRef _notificationPort;
    io_iterator_t _controllerMatchIterator;
    io_iterator_t _controllerTerminateIterator;

    //instance variables for maintaining local information
    NSMutableDictionary *_anbInterfaces;
}

@end

@implementation ANBAppDelegate

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    //Generate the controller ID by replacing the OUI portion of the controller ID used by the Mac
    self.controllerEntityID = ([AVBInterface myEntityID] & 0x000000ffffffffff) | (ABU_OUI << 40);

    //Create an instance of our UI window
    self.windowController = [[ANBWindowController alloc] init];

    [self.windowController.window makeKeyAndOrderFront:nil];

    _interfaces = [[NSMutableDictionary alloc] init];
    _anbInterfaces = [[NSMutableDictionary alloc] init];

    _controllerQueue = dispatch_queue_create("com.apple.samplecode.ANBWindowController.controller", 0);

    //Match on all instances of "IOEthernetAVBController". Any NIC which supports AVB is a subclass of this class.
    CFDictionaryRef matchDict = IOServiceMatching("IOEthernetAVBController");

    if(matchDict)
    {
        CFRetain(matchDict);

        mach_port_t masterPort = 0;

        IOMasterPort(mach_task_self(), &masterPort);

        _notificationPort = IONotificationPortCreate(masterPort);
        IONotificationPortSetDispatchQueue(_notificationPort, _controllerQueue);

        //Create notificatins for both matching and termination. Matching is for when a controller is first attached (or first call when the application runs for already attached interfaces) and termination is for when a controller is removed (only expected to apply to Thunderbolt Ethernet Adapters or Docks).
        IOServiceAddMatchingNotification(_notificationPort, kIOMatchedNotification, matchDict, controllerArrivalCallback, (__bridge void *)self, &_controllerMatchIterator);
        IOServiceAddMatchingNotification(_notificationPort, kIOTerminatedNotification, matchDict, controllerDepartureCallback, (__bridge void *)self, &_controllerTerminateIterator);

        //Prime the iterators and get any already matched controllers.
        controllerArrivalCallback((__bridge void *)self, _controllerMatchIterator);
        controllerDepartureCallback((__bridge void *)self, _controllerTerminateIterator);

        IOObjectRelease(masterPort);
    }
}

//When the window is closed, terminate the application
- (BOOL)applicationShouldTerminateAfterLastWindowClosed:(NSApplication *)sender
{
    return YES;
}

#pragma mark Network Interface Controller IOKit Matching

//Calback routine for the IOKit matched notification
static void controllerArrivalCallback(void *refcon, io_iterator_t iterator)
{
    @autoreleasepool
    {
        io_service_t service;

        while((service = IOIteratorNext(iterator)))
        {
            //For each network controller call into our app delegate class and run the match code
            [(__bridge ANBAppDelegate *)refcon didMatchNetworkController:service];
            IOObjectRelease(service);
        }
    }
}

//Callback routing for the IOKit termination notification
static void controllerDepartureCallback(void *refcon, io_iterator_t iterator)
{
    @autoreleasepool
    {
        io_service_t service;

        while((service = IOIteratorNext(iterator)))
        {
            //For each network controlller call into our app delegate class and run the termination code
            [(__bridge ANBAppDelegate *)refcon didTerminateNetworkController:service];
        }
    }
}

//Handler for network controller terminations
- (void)didTerminateNetworkController:(io_service_t)networkControllerService
{
    //We need to find the BSD Name for the network controller since everything internally is based on the BSD Name.
    //We do this by iterating the children of the controller and finding the first "IOEthernetInterface" object.
    //From that object we get the BSD name and then remove.

    io_iterator_t iterator = 0;

    IORegistryEntryGetChildIterator(networkControllerService, kIOServicePlane, &iterator);

    if(iterator)
    {
        io_service_t service;

        while((service = IOIteratorNext(iterator)))
        {
            if(IOObjectConformsTo(service, kIOEthernetInterfaceClass))
            {
                CFStringRef bsdName = (CFStringRef)IORegistryEntryCreateCFProperty(service, CFSTR("BSD Name"), kCFAllocatorDefault, 0);

                if(bsdName)
                {
                    //Need to synchronize onto the controller queue so that only one thing is changing the _interfaces dictionary at a time.
                    dispatch_async(_controllerQueue, ^{
                        @autoreleasepool
                        {
                            NSString *ifName = (__bridge NSString *)bsdName;
                            if([_interfaces objectForKey:ifName])
                            {
                                //Call our handler for dealing with removed AVBInterface objects (well it's subclasses anyway)
                                [self didRemoveInterface:[_interfaces objectForKey:ifName]];
                                [_interfaces removeObjectForKey:ifName];
                            }

                            CFRelease(bsdName);
                        }
                    });
                }

                IOObjectRelease(service);

                break;
            }
            IOObjectRelease(service);
        }

        IOObjectRelease(iterator);
    }
}

//Handler for network controller matches
- (void)didMatchNetworkController:(io_service_t)networkControllerService
{
    //We need to find the BSD Name for the network controller since everything internally is based on the BSD Name.
    //We do this by iterating the children of the controller and finding the first "IOEthernetInterface" object.
    //From that object we get the BSD name and then add.

    io_iterator_t iterator = 0;

    IORegistryEntryGetChildIterator(networkControllerService, kIOServicePlane, &iterator);

    if(iterator)
    {
        io_service_t service;

        while((service = IOIteratorNext(iterator)))
        {
            if(IOObjectConformsTo(service, kIOEthernetInterfaceClass))
            {
                CFStringRef bsdName = (CFStringRef)IORegistryEntryCreateCFProperty(service, CFSTR("BSD Name"), kCFAllocatorDefault, 0);

                if(bsdName)
                {
                    //Need to synchronize onto the controller queue so that only one thing is changing the _interfaces dictionary at a time.
                    dispatch_async(_controllerQueue, ^{
                        @autoreleasepool
                        {
                            NSString *ifName = (__bridge NSString *)bsdName;
                            if([AVBInterface isAVBEnabledOnInterfaceNamed:ifName])
                            {
                                //AVB is enabled on the interface so we can use it, create an AVBEthernetInterface for it.
                                if(![_interfaces objectForKey:ifName])
                                {
                                    AVBInterface *interface = [[AVBEthernetInterface alloc] initWithInterfaceName:ifName];
                                    if(interface)
                                    {
                                        //Call our handler for dealing with added AVBInterface objects
                                        [_interfaces setObject:interface forKey:ifName];
                                        [self didAddInterface:interface];
                                    }
                                }
                            }
                            else
                            {
                                //It isn't an AVB enabled interface (AVB will not work on it) so if we have an object for it (since the user may have just turned off AVB on the interface) then remove it
                                if([_interfaces objectForKey:ifName])
                                {
                                    //Call our handler for dealing with removed AVBInterface objects (well it's subclasses anyway)
                                    [self didRemoveInterface:[_interfaces objectForKey:ifName]];
                                    [_interfaces removeObjectForKey:ifName];
                                }
                            }

                            CFRelease(bsdName);
                        }
                    });
                }

                IOObjectRelease(service);

                break;
            }
            IOObjectRelease(service);
        }

        IOObjectRelease(iterator);
    }
}

//This is our handler for dealing with added AVBInterface objects
- (void)didAddInterface:(AVBInterface *)interface
{
    //Create our wrapper object which we use for UI interactions and maintaining our UI based versions of AVB entities
    ANBInterface *anbInterface = [[ANBInterface alloc] initWithInterface:interface];

    if(anbInterface)
    {
        [_anbInterfaces setObject:anbInterface forKey:interface.interfaceName];

        //Use KVO to monitor for the addition and removal on AVDECC entities so that we can update the UI.
        [anbInterface addObserver:self forKeyPath:@"avdeccEntities" options:0 context:nil];

        //This needs to happen on the main queue since it updates the UI
        dispatch_async(dispatch_get_main_queue(), ^{
            [self.windowController didUpdateInterfaceEntities:_anbInterfaces];
        });
    }
}

//This is our handler for dealing with removed AVBInterface objects
- (void)didRemoveInterface:(AVBInterface *)interface
{
    ANBInterface *anbInterface = [_anbInterfaces objectForKey:interface.interfaceName];

    //Remove the KVO we added in didAddInterface
    [anbInterface removeObserver:self forKeyPath:@"avdeccEntities"];

    [_anbInterfaces removeObjectForKey:interface.interfaceName];

    //This needs to happen on the main queue since it updates the UI
    dispatch_async(dispatch_get_main_queue(), ^{
        [self.windowController didUpdateInterfaceEntities:_anbInterfaces];
    });
}

- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{
    //Is it our KVO for the avdeccEntities?
    if([keyPath isEqualToString:@"avdeccEntities"])
    {
        //The assumption here is that the KVO happens on the main thread/main queue because we only change this property on
        //the main queue in the ANBAVDECCEntity class. If that can't be gauranteed then this call should be dispatch_async'ed to
        //the main queue.
        [self.windowController didUpdateInterfaceEntities:_anbInterfaces];
    }
    else
    {
        [super observeValueForKeyPath:keyPath ofObject:object change:change context:context];
    }

}

- (void)dealloc
{
    //Clean up the IOKit code
    if(_controllerTerminateIterator)
    {
        IOObjectRelease(_controllerTerminateIterator);
    }

    if(_controllerMatchIterator)
    {
        IOObjectRelease(_controllerMatchIterator);
    }

    if(_notificationPort)
    {
        IONotificationPortDestroy(_notificationPort);
    }

    //This is using ARC so no call to super
}

@end
```

[Next](AVBNetworkBrowser-ANBAVDECCEntity.h.md)[Previous](AVBNetworkBrowser-ANBAppDelegate.h.md)

