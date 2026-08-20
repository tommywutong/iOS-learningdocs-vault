---
title: NameAndAddress
apple_id: DTS10000703
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: Foundation
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/NameAndAddress/Listings/NameAndAddress_h.html
archived_at: '2026-07-18T03:16:50.685110Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [NameAndAddress](NameAndAddress.md)


[Next](NameAndAddress.m.md)[Previous](NameAndAddress.md)

# NameAndAddress.h

```objc
/*
    File:       NameAndAddress.h

    Contains:   Public header for the NameAndAddress class.

    Written by: Guy @Werk

    Created:    June 1997

    Copyright:  (c)1997-2000 by Apple Computer, Inc., all rights reserved.

    Change History (most recent first):
                June  2000 - Updated to Project Builder on DP4
        March 1998 - HI changes - DG
        April 1997 -- Created for the initial Rhapsody training.

    You may incorporate this sample code into your applications without
    restriction, though the sample code has been provided "AS IS" and the
    responsibility for its operation is 100% yours.  However, what you are
    not permitted to do is to redistribute the source as "DSC Sample Code"
    after having made changes. If you're going to re-distribute the source,
    we require that you make it clear in the source that the code was
    descended from Apple Sample Code, but that you've made changes.
*/

#import <AppKit/AppKit.h>

@interface NameAndAddress : NSObject
{
    // O U T L E T S
    id hostNameButton;
    id hostNameField;
    id IPAddressButton;
    id IPAddressField;
}

// A C T I O N S
- (void)getHostName:(id)sender;
- (void)getIPAddress:(id)sender;

@end
```

[Next](NameAndAddress.m.md)[Previous](NameAndAddress.md)

