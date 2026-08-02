---
title: Quartz Composer WWDC 2005 TextEdit
apple_id: DTS10003654
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzComposer_WWDC_TextEdit/Listings/TextEdit_02_Controller_h.html
archived_at: '2026-07-18T03:21:31.329847Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer WWDC 2005 TextEdit](Quartz%20Composer%20WWDC%202005%20TextEdit.md)


[Next](TextEdit02-Controller.m.md)[Previous](TextEdit01-ScalingScrollView.m.md)

# TextEdit_02/Controller.h

```objc
#import <Cocoa/Cocoa.h>

@interface Controller : NSObject {
    IBOutlet NSPanel *propertiesPanel;
    IBOutlet id keywordsField;
}

/* NSApplication delegate methods */
- (void)application:(NSApplication *)app printFiles:(NSArray *)filenames;
- (void)application:(NSApplication *)app openFiles:(NSArray *)filenames;
- (BOOL)applicationOpenUntitledFile:(NSApplication *)app;
- (NSApplicationTerminateReply)applicationShouldTerminate:(NSApplication *)app;

/* Action methods */
- (void)createNew:(id)sender;
- (void)open:(id)sender;
- (void)saveAll:(id)sender;

@end
```

[Next](TextEdit02-Controller.m.md)[Previous](TextEdit01-ScalingScrollView.m.md)

