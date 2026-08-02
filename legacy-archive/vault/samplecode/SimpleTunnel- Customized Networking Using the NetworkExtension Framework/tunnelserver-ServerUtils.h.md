---
title: 'SimpleTunnel: Customized Networking Using the NetworkExtension Framework'
apple_id: TP40016140
resource_type: Sample Code
platform: iOS|macOS
topic: Networking, Internet, & Web
technology: NetworkExtension
published: '2016-10-04'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleTunnel/Listings/tunnel_server_ServerUtils_h.html
archived_at: '2026-07-18T03:24:25.423556Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleTunnel: Customized Networking Using the NetworkExtension Framework](SimpleTunnel-%20Customized%20Networking%20Using%20the%20NetworkExtension%20Framework.md)


[Next](tunnelserver-AddressPool.swift.md)[Previous](tunnelserver-ServerConfiguration.swift.md)

# tunnel_server/ServerUtils.h

```
/*
    Copyright (C) 2016 Apple Inc. All Rights Reserved.
    See LICENSE.txt for this sample’s licensing information

    Abstract:
    This file declares utility Objective-C functions used by the SimpleTunnel server.
 */

#ifndef ServerUtils_h
#define ServerUtils_h

/// Get the identifier for the UTUN interface.
UInt32 getUTUNControlIdentifier(int socket);

/// Setup a socket as non-blocking.
BOOL setUTUNAddress(NSString *ifname, NSString *address);

/// Set the IP address on a UTUN interface.
int getUTUNNameOption(void);

/// Get value of the UTUN iterface name socket option.
BOOL setSocketNonBlocking(int socket);

#endif /* ServerUtils_h */
```

[Next](tunnelserver-AddressPool.swift.md)[Previous](tunnelserver-ServerConfiguration.swift.md)

