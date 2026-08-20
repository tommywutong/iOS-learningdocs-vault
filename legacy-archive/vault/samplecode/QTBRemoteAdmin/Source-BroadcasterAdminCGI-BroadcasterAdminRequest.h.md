---
title: QTBRemoteAdmin
apple_id: DTS10001045
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTBRemoteAdmin/Listings/Source_BroadcasterAdminCGI_BroadcasterAdminRequest_h.html
archived_at: '2026-07-18T03:19:59.730003Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTBRemoteAdmin](QTBRemoteAdmin.md)


[Next](Source-BroadcasterAdminCGI-BroadcasterAdminRequest.m.md)[Previous](Source-BroadcasterAdminCGI-BroadcasterAdminHTML.h.md)

# Source/BroadcasterAdminCGI/BroadcasterAdminRequest.h

```objc
/*
    File:           BroadcasterAdminRequest.h
    Description:    This file contains the BroadcasterAdminRequest class interface. The BroadcasterAdminRequest
                    class processes a cgi request and generates a response. It communicates with QuickTime
                    Broadcaster by opening a connection to the daemon.

*/

#import <Foundation/Foundation.h>

@interface BroadcasterAdminRequest : NSObject
{
    id              broadcasterDaemon;
    NSConnection    *daemonConnection;
}

    // setters
- (void)setDaemonConnection:(NSConnection *)theConnection;
- (void)setBroadcasterDaemon:(id)theBroadcasterDaemon;

    // methods
- (void)processRequest:(NSDictionary *)theQuery;
- (BOOL)makeConnection;
- (void)handleLaunchRequest:(NSDictionary *)theQueryDictionary withResponse:(NSMutableString *)theResponse;
- (void)handleSetupRequest:(BOOL)broadcasterConnected withResponse:(NSMutableString *)theResponse;
- (void)handleBroadcastRequest:(NSDictionary *)theQueryDictionary withResponse:(NSMutableString *)theResponse;
- (void)handleQuitRequest:(NSMutableString *)theResponse;
- (void)outputLaunchResponse:(BOOL)errorLaunching withResponse:(NSMutableString *)theResponse;
- (void)outputSetupResponse:(NSMutableString *)theResponse;
- (void)outputStatisticsResponse:(NSMutableString *)theResponse;
- (void)outputWaitResponse:(NSMutableString *)theResponse;
- (void)outputNotConnectedResponse:(NSMutableString *)theResponse;

    // html generation methods
- (void)addHeaderToResponse:(NSMutableString *)theResponse;
- (void)addCloserToResponse:(NSMutableString *)theResponse;
- (void)addHeaderWithMetaRefreshTagToResponse:(NSMutableString *)theResponse;
- (void)addPageHeader:(NSString *)theString toResponse:(NSMutableString *)theResponse;
- (void)addOpenFormToResponse:(NSMutableString *)theResponse;
- (void)addCloseFormToResponse:(NSMutableString *)theResponse;
- (void)addOpenTableToResponse:(NSMutableString *)theResponse;
- (void)addCloseTableToResponse:(NSMutableString *)theResponse;
- (void)addTableRow:(NSString *)rowTitle withName:(NSString *)theName withList:(NSArray *)theList toResponse:(NSMutableString *)theResponse;
- (void)addTableRow:(NSString *)rowTitle withString:(NSString *)theString toResponse:(NSMutableString *)theResponse;
- (void)addTableRow:(NSString *)rowTitle withTextFieldName:(NSString *)name withValue:(NSString *)value toResponse:(NSMutableString *)theResponse;
- (void)addSubmitButtonWithName:(NSString *)name withValue:(NSString *)value toResponse:(NSMutableString *)theResponse;

@end
```

[Next](Source-BroadcasterAdminCGI-BroadcasterAdminRequest.m.md)[Previous](Source-BroadcasterAdminCGI-BroadcasterAdminHTML.h.md)

