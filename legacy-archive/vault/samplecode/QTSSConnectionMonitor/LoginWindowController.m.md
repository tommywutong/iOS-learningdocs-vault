---
title: QTSSConnectionMonitor
apple_id: DTS10001049
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSConnectionMonitor/Listings/LoginWindowController_m.html
archived_at: '2026-07-18T03:21:18.527139Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSConnectionMonitor](QTSSConnectionMonitor.md)


[Next](QTSSStatusController.h.md)[Previous](LoginWindowController.h.md)

# LoginWindowController.m

```objc
#import "LoginWindowController.h"
#import "AdminProtocolAccessObj.h"
#import "QTSSStatusController.h"

@implementation LoginWindowController

+ (BOOL)checkLoginForString:(NSString *)theString
{
    NSRange range = [theString rangeOfString:@"qtssusername"];

    if ((range.location < 0) || (range.location > [theString length]))
        return YES;
    else
        return NO;
}

- (void)awakeFromNib
{    
    [myWindow center];
}

- (void)openProgressPanelForString:(NSString *)progressString
{
    [myProgressField setStringValue:progressString];
    [[NSApplication sharedApplication] beginSheet:myProgressPanel
                                   modalForWindow:myWindow
                                    modalDelegate:self
                                   didEndSelector:nil
                                      contextInfo:nil];

}

- (IBAction)login:(id)sender
{
    NSString *hostname = [hostField stringValue];
    NSString *username = [usernameField stringValue];
    NSString *password = [passwordField stringValue];
    id authServerObj;

    [self openProgressPanelForString:@"Logging inÉ"];

    authServerObj = [[AdminProtocolAccessObj alloc] initWithUsername:username password:password host:hostname];

    [myProgressPanel close];
    [[NSApplication sharedApplication] endSheet:myProgressPanel];

    if (authServerObj) {
        [myStatusController setMyAdminProtocolObj:authServerObj];
        [myWindow close];
        [myStatusController start];
    }
    else
        NSBeginAlertSheet(@"Invalid Password",
                          @"OK",
                          nil, nil,
                          myWindow,
                          nil, nil, nil, nil,
                          @"The username or password you entered is not recognized. Please try again.");
}

@end
```

[Next](QTSSStatusController.h.md)[Previous](LoginWindowController.h.md)

