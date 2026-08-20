---
title: Quartz Composer WWDC 2005 TextEdit
apple_id: DTS10003654
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: Quartz
published: '2005-06-01'
source_url: https://developer.apple.com/library/archive/samplecode/QuartzComposer_WWDC_TextEdit/Listings/TextEdit_03_Controller_h.html
archived_at: '2026-07-18T03:21:32.833779Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Quartz Composer WWDC 2005 TextEdit](Quartz%20Composer%20WWDC%202005%20TextEdit.md)


[Next](TextEdit03-Controller.m.md)[Previous](TextEdit02-ScalingScrollView.m.md)

# TextEdit_03/Controller.h

```objc
#import <Cocoa/Cocoa.h>
#import <Quartz/Quartz.h>

@interface Controller : NSObject {
    IBOutlet NSPanel *propertiesPanel;
    IBOutlet id keywordsField;

/************ BEGIN QUARTZ COMPOSER *************/

    IBOutlet QCView *qcView;

/************* END QUARTZ COMPOSER **************/
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

[Next](TextEdit03-Controller.m.md)[Previous](TextEdit02-ScalingScrollView.m.md)

