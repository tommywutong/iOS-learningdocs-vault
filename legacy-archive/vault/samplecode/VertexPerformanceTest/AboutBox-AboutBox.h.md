---
title: VertexPerformanceTest
apple_id: DTS10000554
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VertexPerformanceTest/Listings/AboutBox_AboutBox_h.html
archived_at: '2026-07-18T03:27:48.704933Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [VertexPerformanceTest](VertexPerformanceTest.md)


[Next](AboutBox-AboutBox.m.md)[Previous](main.m.md)

# AboutBox/AboutBox.h

```objc
/*
To display the about box add this method to your Controller:

- (IBAction)showAboutBox:(id)sender
{
    [[AboutBox sharedInstance] showPanel:sender];
}

Also hook the About menu item to an action named "showAboutBox" in your Controller
by control-dragging from the menu item to the controller.  Before the Controller's action
will show up as an option for the menu item, you will have to unhook it from it's current
routine.
*/

#import <Cocoa/Cocoa.h>

@interface AboutBox : NSObject
{
    IBOutlet id appNameField;
    IBOutlet id copyrightField;
    IBOutlet id notesField;
    IBOutlet id versionField;
}

+ (AboutBox *)sharedInstance;
- (IBAction)showPanel:(id)sender;
- (void)hiliteAndActivateURLs:(NSTextView*)textView;

@end
```

[Next](AboutBox-AboutBox.m.md)[Previous](main.m.md)

