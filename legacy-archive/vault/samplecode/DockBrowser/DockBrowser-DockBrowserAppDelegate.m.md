---
title: DockBrowser
apple_id: DTS10000695
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: CoreServices
published: '2011-08-18'
source_url: https://developer.apple.com/library/archive/samplecode/DockBrowser/Listings/DockBrowser_DockBrowserAppDelegate_m.html
archived_at: '2026-07-18T03:07:05.994299Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [DockBrowser](DockBrowser.md)


[Next](DockBrowser-main.m.md)[Previous](DockBrowser-DockBrowserAppDelegate.h.md)

# DockBrowser/DockBrowserAppDelegate.m

```objc
/*
     File: DockBrowserAppDelegate.m 
 Abstract: All functionality of this sample is implemented in the
 Application Delegate. 
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

 Copyright (C) 2011 Apple Inc. All Rights Reserved. 

 */

#import "DockBrowserAppDelegate.h"

#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define kTypeAFP                @"_afpovertcp._tcp."
#define kTypeHTTP               @"_http._tcp."

@interface DockBrowserAppDelegate () <NSApplicationDelegate, NSNetServiceBrowserDelegate, NSNetServiceDelegate>

- (void)registerFakeService;
- (void)cancelFakeService;
- (void)mountAFPShareWithHost:(NSString*)host port:(long)port service:(NSNetService*)service;
- (void)displayWebPageOnHost:(NSString*)host port:(long)port service:(NSNetService*)service;

@end



@implementation DockBrowserAppDelegate

@synthesize serviceName, createFakeService;

- (id)init
{
    self = [super init];
    if (self) {
        // Set default values on the properties.
        self.serviceName = kTypeAFP;
        self.createFakeService = NO;
    }

    return self;
}

- (void)applicationDidFinishLaunching:(NSNotification *)aNotification
{
    serviceBrowser = [[NSNetServiceBrowser alloc] init];
    serviceBrowser.delegate = self;

    discoveredServices = [[NSMutableArray alloc] init];

    // Watch our two properties so we know when the user changed something in the preferences.
    // Pass NSKeyValueObservingOptionInitial as an option to trigger a KVO notification immediately and start the browsing.
    [self addObserver:self forKeyPath:@"serviceName" options:(NSKeyValueObservingOptionNew | NSKeyValueObservingOptionInitial) context:&self->serviceName];
    [self addObserver:self forKeyPath:@"createFakeService" options:(NSKeyValueObservingOptionNew | NSKeyValueObservingOptionInitial) context:&self->createFakeService];
}

- (void)applicationWillTerminate:(NSNotification *)notification
{
    [self cancelFakeService];
}

//
// Called when one of our two observed properties changes.  The changes are made by the bindings in place between
// the controls in the preferences UI and our properties.
- (void)observeValueForKeyPath:(NSString *)keyPath ofObject:(id)object change:(NSDictionary *)change context:(void *)context
{   
    if ((context == &self->serviceName) || (context == &self->createFakeService)) {

        if (context == &self->serviceName) {
            [serviceBrowser stop];

            [discoveredServices removeAllObjects];

            [serviceBrowser searchForServicesOfType:[change objectForKey:NSKeyValueChangeNewKey] inDomain:@""];
        }

        // No matter which of the two options in the preferences changed we need to re-evaluate whether or not
        // to broadcast a fake service.  This will ensure the fake service broadcasted matches the service being
        // searched for.
        if (self.createFakeService)
            [self registerFakeService];
        else
            [self cancelFakeService];

    } else {
        [super observeValueForKeyPath:keyPath ofObject:object change:change context:context];
    }

}

#pragma mark - Dock Tile

//
// Application Delegate method implemented to return a custom menu to be displayed when our Dock icon is command
// clicked.
- (NSMenu*)applicationDockMenu:(NSApplication *)sender
{
    return dockMenu;
}

//
// Handles updating the UI in the Dock including the contextual menu and badge.
- (void)updateDockTile
{
    NSString *dockBadgeString = nil;
    if ([discoveredServices count] > 0) {
        NSNumber *discoveredServicesCount = [NSNumber numberWithInteger:[discoveredServices count]];
        dockBadgeString = [NSNumberFormatter localizedStringFromNumber:discoveredServicesCount numberStyle:NSNumberFormatterDecimalStyle];
    }

    // Sort the array so the services appear in alphabetical order
    [discoveredServices sortUsingDescriptors: [NSArray arrayWithObject:
                                               [NSSortDescriptor sortDescriptorWithKey:@"name" ascending:YES selector:@selector(localizedCaseInsensitiveCompare:)]] ];

    // Badge the Dock.  If no hosts were found, nil will be set as the badge string.  This
    // removes any existing badge.
    [[[NSApplication sharedApplication] dockTile] setBadgeLabel:dockBadgeString];

    // For simplicity, we'll recreate the menu each time this method is called.
    [dockMenu removeAllItems];

    for (NSNetService *service in discoveredServices) {

        // Service name is a host unique string (usually).  For the AFP service, it is the name of the
        // host server.  For the HTTP service it may be the name of the website or a host name.
        NSString *hostServiceName = [service name];

        // Never pass nil for an NSMenuItem's title.  In this case, replace the 'hostServiceName' with the empty
        // string.
        if (!hostServiceName)
            hostServiceName = @"";

        NSMenuItem *serviceMenuItem = [[NSMenuItem alloc] initWithTitle:hostServiceName action:@selector(dockMenuItemSelected:) keyEquivalent:@""];

        // When the menu item is selected, we'll need some context in the callback as to which NSNetService instance the
        // menu item was representing.  By setting the tag of the menu item to the index in the array of its
        // corresponding NSNetService it will be easy to locate the NSNetService instance we need to use.
        serviceMenuItem.tag = [discoveredServices indexOfObject:service];

        [dockMenu addItem:serviceMenuItem];

        [serviceMenuItem release];
    }

}

//
// Callback action for a selected NSMenuItem. 
- (void)dockMenuItemSelected:(id)sender
{
    NSMenuItem *selectedItem = (NSMenuItem *)sender;
    NSNetService *selectedService = [discoveredServices objectAtIndex:[selectedItem tag]];

    // Resolving the service may take time and happens in the background.  By setting ourself as the delegate of the NSNetService
    // instance, we'll be notified when the resolve is finished.
    selectedService.delegate = self;

    [selectedService resolveWithTimeout:5];
}

#pragma mark - NSNetServiceBrowser Delegate

//
// Delegate method called by NSNetService to inform us of a new service it has found.
- (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didFindService:(NSNetService *)aNetService moreComing:(BOOL)moreComing
{
    [discoveredServices addObject:aNetService];

    // Only update the UI when NSNetService tells us there won't be additional immediate changes.
    if (!moreComing)
        [self updateDockTile];
}

//
// Delegate method called by NSNetService to inform us that a service has been removed.
- (void)netServiceBrowser:(NSNetServiceBrowser *)aNetServiceBrowser didRemoveService:(NSNetService *)aNetService moreComing:(BOOL)moreComing
{
    [discoveredServices removeObject:aNetService];

    // Only update the UI when NSNetService tells us there won't be additional immediate changes.
    if (!moreComing)
        [self updateDockTile];
}

#pragma mark - NSNetSerivce

//
// Sets up and publishes a fake service entry of the type selected in the preferences.
- (void)registerFakeService
{
    // Stop any previous publications.
    [self cancelFakeService];

    // Create a new service of the type specified by the radio group in the preferences.  The name is what will appear
    // when other clients call [NSNetService name] on our service.  The port in this case does not match that of any listening
    // service which will of course cause any connection to our published service to fail.
    fakeService = [[NSNetService alloc] initWithDomain:@"local." type:self.serviceName name:@"Dock Browser Fake Service" port:12345];
    fakeService.delegate = self;
    [fakeService publish];
}

//
// Stop publishing and release our fake service entry.
- (void)cancelFakeService
{
    [fakeService stop];

    [fakeService release];
    fakeService = nil;
}

#pragma mark - NSNetSerivce Delegate

//
// Delegate method called when the resolve of an NSNetService is finished.  Here we get the address
// and port of the service.
- (void)netServiceDidResolveAddress:(NSNetService *)sender
{
    NSString *hostName = [sender hostName];
    long servicePort = [sender port];

    if (hostName) {
        // Once we have have a host name stop the resolve so we do not receive any more
        // callbacks if NSNetService finds another IP address for the service.  This
        // can happen if a host has an IPv4 and IPv6 adress or is connected to the subnet
        // with more than 1 interface.
        [sender stop];

        if ([[sender type] isEqualToString:kTypeAFP])
            [self mountAFPShareWithHost:hostName port:servicePort service:sender];
        else if ([[sender type] isEqualToString:kTypeHTTP])
            [self displayWebPageOnHost:hostName port:servicePort service:sender];
    }
}

#pragma mark - Connections

//
// Helper method to convert a TXT Record to an NSDictionary.
- (NSDictionary*)dictionaryFromTXT:(NSData*)txtData
{
    if (!txtData)
        return nil;

    NSMutableDictionary *txtDictionary = [[NSNetService dictionaryFromTXTRecordData:txtData] mutableCopy];

    // The 'path' key initially contains an NSData object representing the path.  Here we convert it into an
    // NSString and store it back in the dictionary.
    if ([txtDictionary objectForKey:@"path"]) {

        NSData *pathData = [txtDictionary objectForKey:@"path"];

        NSString *pathString = [[[NSString alloc] initWithBytes:[pathData bytes] length:[pathData length] encoding:NSUTF8StringEncoding] autorelease];

        if (pathString) {
            // If the path starts with a ~ we must precede it with a /
            if ([pathString characterAtIndex:0] == '~')
                pathString = [NSString stringWithFormat:@"/%@", pathString];

            [txtDictionary setValue:pathString forKey:@"path"];

        } else {

            [txtDictionary removeObjectForKey:@"path"];
        }
    }

    return [txtDictionary autorelease];
}

//
// Callback from the AFP Volume mount operation.
static void
VolumeMountCallback(FSVolumeOperation volumeOp, void *clientData, OSStatus err, FSVolumeRefNum mountedVolumeRefNum)
{
    FSDisposeVolumeOperation(volumeOp);
}

//
// Connects to an AFP server at the given address and port.
- (void)mountAFPShareWithHost:(NSString*)host port:(long)port service:(NSNetService*)service
{
    FSVolumeOperation volumeOp;
    OSStatus err;

    NSString *urlString = [NSString stringWithFormat:@"afp://%@:%i", host, port];
    CFURLRef addressURL = CFURLCreateWithString(kCFAllocatorDefault, (CFStringRef)urlString, NULL); 

    err = FSCreateVolumeOperation(&volumeOp);
    if (err == noErr) {

        err = FSMountServerVolumeAsync(addressURL, NULL, NULL, NULL, volumeOp, NULL, 0, VolumeMountCallback,
                                       CFRunLoopGetCurrent(), kCFRunLoopCommonModes);
        if (err != noErr) {
            FSDisposeVolumeOperation(volumeOp);
        }
    }

    CFRelease(addressURL);
}

//
// Displays a web page at the given host, port and path in the default browser.
- (void)displayWebPageOnHost:(NSString*)host port:(long)port service:(NSNetService*)service
{
    NSDictionary *txtDictionary = nil;
    NSString *path = nil;

    // An _http._tcp. service can specify a path in its NSNetService's TXT Record data.
    // This allows clients to discover multiple websites hosted on the same device.
    // Here we check if a path was provided.
    if ((txtDictionary = [self dictionaryFromTXT:[service TXTRecordData]]))
        path = [txtDictionary objectForKey:@"path"];

    NSString *urlString = [NSString stringWithFormat:@"http://%@:%i", host, port];
    if (path)
        urlString = [urlString stringByAppendingString:path];

    NSURL *addressURL = [NSURL URLWithString:urlString];

    // Open the URL in the default browser.
    LSOpenCFURLRef((CFURLRef)addressURL, NULL);
}

@end
```

[Next](DockBrowser-main.m.md)[Previous](DockBrowser-DockBrowserAppDelegate.h.md)

