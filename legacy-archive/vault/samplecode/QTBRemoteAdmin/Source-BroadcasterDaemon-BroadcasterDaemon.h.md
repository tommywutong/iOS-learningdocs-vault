---
title: QTBRemoteAdmin
apple_id: DTS10001045
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTBRemoteAdmin/Listings/Source_BroadcasterDaemon_BroadcasterDaemon_h.html
archived_at: '2026-07-18T03:20:00.017325Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTBRemoteAdmin](QTBRemoteAdmin.md)


[Next](Source-BroadcasterDaemon-BroadcasterDaemon.m.md)[Previous](Source-BroadcasterAdminCGI-main.m.md)

# Source/BroadcasterDaemon/BroadcasterDaemon.h

```objc
/*
    File:           BroadcasterDaemon.h
    Description:    This file contains the BroadcasterDaemon class interface. The BroadcasterDaemon
                    class handles the connection between the cgi and QuickTime Broadcaster.

*/

#import <Foundation/Foundation.h>
#import "BroadcasterDaemonProtocol.h"

@interface BroadcasterDaemon : NSObject <BroadcasterDaemonProtocol>
{
    id              broadcastController;
    NSConnection    *cgiConnection;
    NSConnection    *broadcasterConnection;
    NSString        *launchPath;
}

    // setters
- (void)setBroadcastController:(id)theBroadcastController;
- (void)setCGIConnection:(NSConnection *)theConnection;
- (void)setBroadcasterConnection:(NSConnection *)theConnection;

    // overrides/delegates
- (NSMethodSignature *)methodSignatureForSelector:(SEL)theSelector;
- (void)forwardInvocation:(NSInvocation *)theInvocation;

    // notifications 
- (void)connectionDidDie:(NSNotification *)notification;
- (void)broadcasterDidLaunch:(NSNotification *)notification;
- (void)broadcasterWillQuit:(NSNotification *)notification;

    // methods
- (BOOL)makeAppConnection;

@end
```

[Next](Source-BroadcasterDaemon-BroadcasterDaemon.m.md)[Previous](Source-BroadcasterAdminCGI-main.m.md)

