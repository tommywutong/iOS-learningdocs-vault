---
title: SimpleThreads
apple_id: DTS10000756
resource_type: Sample Code
platform: macOS
topic: Performance
technology: Foundation
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/SimpleThreads/Listings/TransferServer_h.html
archived_at: '2026-07-18T03:24:22.237149Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [SimpleThreads](SimpleThreads.md)


[Next](TransferServer.m.md)[Previous](Controller.m.md)

# TransferServer.h

```objc
/*
    File:       TransferServer.h

    Contains:   Sample server class, talked to through Distributed Objects.

    Written by: Quinn "The Eskimo!"

    Created:    Tue 10-Jun-1997

    Copyright:  (c)1997 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):

    You may incorporate this sample code into your applications without
    restriction, though the sample code has been provided "AS IS" and the
    responsibility for its operation is 100% yours.  However, what you are
    not permitted to do is to redistribute the source as "DSC Sample Code"
    after having made changes. If you're going to re-distribute the source,
    we require that you make it clear in the source that the code was
    descended from Apple Sample Code, but that you've made changes.
*/

#import <AppKit/AppKit.h>

@class Controller;

// IMPORTANT: See the documentation ("ReadMe.rtf" under Supporting Files) for
// big picture information about this project.

// TransferServerInterface is a formal protocol that defines the methods which
// the transfer server object responds to.

@protocol TransferServerInterface

- (oneway void)slowTransfer:(Controller *)controller;
    // Starts a slow transfer operation.  The server thread
    // will spend a lot of time doing this operation, occasionally
    // sending messages back to the controller to inform it of
    // its progress.  Note that because the message is "oneway",
    // the thread that invokes this method will continue running,
    // despite the fact that the server thread is off doing
    // things.

- (oneway void)slowerTransfer:(Controller *)controller;
    // As above, but even slower.

@end

@interface TransferServer : NSObject <TransferServerInterface>
{
    long threadID;
}

- (id)init;
    // A simple init override that sets up the threadID instance variable.

+ (void)connectWithPorts:(NSArray *)portArray;
    // This method is invoked on a new thread by the
    // Controller's init method.  The portArray contains
    // two NSPort objects that are the ports of the connection
    // to which the new thread should connect to.  The thread
    // connects to these ports, then creates a server object
    // sets it to be its connection's root object.  It then goes
    // into a run loop handling the incoming Distributed Object
    // requests (ie any methods in TransferServerInterface).

@end
```

[Next](TransferServer.m.md)[Previous](Controller.m.md)

