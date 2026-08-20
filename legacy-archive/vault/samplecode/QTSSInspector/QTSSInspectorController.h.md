---
title: QTSSInspector
apple_id: DTS10001050
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/QTSSInspector/Listings/QTSSInspectorController_h.html
archived_at: '2026-07-18T03:21:19.555774Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSSInspector](QTSSInspector.md)


[Next](QTSSInspectorController.m.md)[Previous](LoginWindowController.m.md)

# QTSSInspectorController.h

```objc
/* QTSSInspectorController */

#import <Cocoa/Cocoa.h>

@interface QTSSInspectorController : NSWindowController
{
    IBOutlet NSOutlineView *myOutlineView;
    NSMutableDictionary *myDataCache;
    NSMutableArray *myStringCache;
    id myAdminProtocolObj;
    IBOutlet NSPanel *myProgressPanel;
    IBOutlet NSTextField *myProgressField;
}

- (NSDictionary *)contentsOfPath:(NSString *)path;
- (NSString *)keepString:(NSString *)theString;
- (id)myAdminProtocolObj;
- (void)setMyAdminProtocolObj:(id)obj;
- (IBAction)refresh:(id)sender;

@end
```

[Next](QTSSInspectorController.m.md)[Previous](LoginWindowController.m.md)

