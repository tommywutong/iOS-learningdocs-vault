---
title: QTBRemoteAdmin
apple_id: DTS10001045
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTBRemoteAdmin/Listings/Source_BroadcasterDaemon_main_m.html
archived_at: '2026-07-18T03:20:00.275301Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTBRemoteAdmin](QTBRemoteAdmin.md)


[Next](Source-Protocols-BroadcasterDaemonProtocol.h.md)[Previous](Source-BroadcasterDaemon-BroadcasterDaemon.m.md)

# Source/BroadcasterDaemon/main.m

```objc
/*
    File:           main.m
    Description:    This file instantiates the Broadcaster daemon object which handles
                    the connection between the cgi and QuickTime Broadcaster.

*/

#import <Foundation/Foundation.h>
#import "BroadcasterDaemon.h"

int main(int argc, const char *argv[])
{
    NSAutoreleasePool *pool;

    // init
    pool = [[NSAutoreleasePool alloc] init];

    // daemonize
    daemon(0, 0);

    // init the Broadcaster daemon
    [[[BroadcasterDaemon alloc] init] autorelease];

    // run forever
    [[NSRunLoop currentRunLoop] run];

    // release
    [pool release];

    return 0;
}
```

[Next](Source-Protocols-BroadcasterDaemonProtocol.h.md)[Previous](Source-BroadcasterDaemon-BroadcasterDaemon.m.md)

