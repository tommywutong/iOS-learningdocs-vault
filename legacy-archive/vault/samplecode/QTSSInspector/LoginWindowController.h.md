---
title: QTSSInspector
apple_id: DTS10001050
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSInspector/Listings/LoginWindowController_h.html
archived_at: '2026-07-18T03:21:19.473088Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSInspector](QTSSInspector.md)


[Next](LoginWindowController.m.md)[Previous](ImageAndTextCell.m.md)

# LoginWindowController.h

```objc
/* LoginWindowController */

#import <Cocoa/Cocoa.h>

@interface LoginWindowController : NSObject
{
    IBOutlet NSTextField *hostField;
    IBOutlet NSTextField *passwordField;
    IBOutlet NSTextField *usernameField;
    IBOutlet NSWindow *myWindow;
    IBOutlet NSPanel *myProgressPanel;
    IBOutlet NSTextField *myProgressField;
    id myInspectorController;
    id myOutlineView;
}

+ (BOOL)checkLoginForString:(NSString *)theString;
- (void)openProgressPanelForString:(NSString *)progressString;
- (IBAction)login:(id)sender;

@end
```

[Next](LoginWindowController.m.md)[Previous](ImageAndTextCell.m.md)

