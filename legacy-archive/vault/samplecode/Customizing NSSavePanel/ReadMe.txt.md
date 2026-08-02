---
title: Customizing NSSavePanel
apple_id: DTS10004201
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2014-03-14'
source_url: https://developer.apple.com/library/archive/samplecode/CustomSave/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:05:38.532499Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Customizing NSSavePanel](Customizing%20NSSavePanel.md)


[Next](main.m.md)[Previous](Customizing%20NSSavePanel.md)

# ReadMe.txt

```objc
### CustomSave ###

================================================================================
DESCRIPTION:

"CustomSave" is a Cocoa sample application that demonstrates how to customize the NSSavePanel class.  Customization is achieved by implementing -

NSDocument
- (BOOL)prepareSavePanel:(NSSavePanel *)savePanel;
This will set the initial directory, add a custom accessory view, set the required extension, set the name field label and dialog message.

NSSavePanelDelegate
- (BOOL)panel:(id)sender isValidFilename:(NSString *)filename;
- (NSString*)panel:(id)sender userEnteredFilename:(NSString*)filename confirmed:(BOOL)okFlag;
- (void)panel:(id)sender willExpand:(BOOL)expanding;
- (void)panel:(id)sender directoryDidChange:(NSString *)path;
- (void)panelSelectionDidChange:(id)sender;

As a delegate to the NSSavePanel, this sample provides sound feedback for navigation, allows navigating inside packages, and overrides how a file's saved name is determined.

================================================================================
BUILD REQUIREMENTS:

OS X SDK 10.9 or later

================================================================================
RUNTIME REQUIREMENTS:

OS X 10.8 or later

===========================================================================
CHANGES FROM PREVIOUS VERSIONS:

1.2 - Upgraded for OS X 10.9 SDK
1.1 - corrected ReadMe info
1.0 - first version

================================================================================
Copyright © 2007-2014 Apple Inc. All rights reserved.
```

[Next](main.m.md)[Previous](Customizing%20NSSavePanel.md)

