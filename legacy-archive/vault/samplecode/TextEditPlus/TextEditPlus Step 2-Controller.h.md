---
title: TextEditPlus
apple_id: DTS10004025
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2006-07-28'
source_url: https://developer.apple.com/library/archive/samplecode/TextEditPlus/Listings/TextEditPlus_Step_2_Controller_h.html
archived_at: '2026-07-18T03:26:36.469854Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [TextEditPlus](TextEditPlus.md)


[Next](TextEditPlus%20Step%202-Controller.m.md)[Previous](TextEditPlus%20Step%202-AppleScriptKit.sdef.md)

# TextEditPlus Step 2/Controller.h

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

[Next](TextEditPlus%20Step%202-Controller.m.md)[Previous](TextEditPlus%20Step%202-AppleScriptKit.sdef.md)

