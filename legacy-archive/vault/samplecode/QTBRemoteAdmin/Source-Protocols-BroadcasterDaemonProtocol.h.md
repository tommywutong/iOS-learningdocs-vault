---
title: QTBRemoteAdmin
apple_id: DTS10001045
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTBRemoteAdmin/Listings/Source_Protocols_BroadcasterDaemonProtocol_h.html
archived_at: '2026-07-18T03:20:00.356302Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTBRemoteAdmin](QTBRemoteAdmin.md)


[Next](Source-Protocols-BroadcasterRemoteAdmin.h.md)[Previous](Source-BroadcasterDaemon-main.m.md)

# Source/Protocols/BroadcasterDaemonProtocol.h

```objc
/*
    File:           BroadcasterDaemonProtocol.h
    Description:    This file contains the BroadcasterDaemon protocol. This protocol is
                    used for communication between the daemon and the cgi.

*/

@protocol BroadcasterDaemonProtocol

    // getters
- (NSString *)launchPath;

    // setters
- (void)setLaunchPath:(NSString *)launchPath;

    // methods
- (BOOL)launchBroadcaster:(BOOL)withUI;
- (BOOL)daemonConnectedToBroadcaster;

@end
```

[Next](Source-Protocols-BroadcasterRemoteAdmin.h.md)[Previous](Source-BroadcasterDaemon-main.m.md)

