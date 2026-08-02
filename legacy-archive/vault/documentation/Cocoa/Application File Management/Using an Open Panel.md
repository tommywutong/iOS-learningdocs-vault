---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/Tasks/UsingAnOpenPanel.html
archived_at: '2026-07-15T05:25:38.872817Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application File Management](Introduction%20to%20Application%20File%20Management.md)


[Next](Getting%20the%20Current%20Selection.md)[Previous](Using%20a%20Save%20Panel.md)

# Using an Open Panel

Typically, you access an NSOpenPanel by invoking the `openPanel` method. When the class receives an `openPanel` message, it tries to reuse an existing panel rather than create a new one. If a panel is reused, its attributes are reset to the default values so that the effect is the same as receiving a new panel. Because Open panels may be reused, you shouldn’t modify the instance returned by `openPanel` except through the methods declared by the [NSOpenPanel](https://developer.apple.com/documentation/appkit/nsopenpanel) class inherited from [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel). For example, you can set the panel’s title and whether it allows multiple selection, but not the arrangement of the buttons within the panel.

The following Objective-C code example shows the NSOpenPanel displaying only files with extensions of “.td” and allowing multiple selection. If the user makes a selection and clicks the OK button (that is, `runModalInDirectoryrunModalForDirectory:file:types:` returns `NSOKButton`), this method opens each selected file:

```objc
- (void)openDoc:(id)sender
{
    int result;
    NSArray *fileTypes = [NSArray arrayWithObject:@"td"];
    NSOpenPanel *oPanel = [NSOpenPanel openPanel];

    [oPanel setAllowsMultipleSelection:YES];
    result = [oPanel runModalForDirectory:NSHomeDirectory()
                    file:nil types:fileTypes];
    if (result == NSOKButton) {
        NSArray *filesToOpen = [oPanel filenames];
        int i, count = [filesToOpen count];
        for (i=0; i<count; i++) {
            NSString *aFile = [filesToOpen objectAtIndex:i];
            id currentDoc = [[ToDoDoc alloc] initWithFile:aFile];
        }
    }
}
```

NSOpenPanel can accept file types specified as either filename extensions or encoded HFS file types. To encode an HFS file type into an acceptable NSString use the function `NSFileTypeForHFSTypeCode`. (See [HFS File Types](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/LowLevelFileMgmt/Articles/HFSFileTypes.html#//apple_ref/doc/uid/20000779) for details.) When specifying file types for NSOpenPanel, you should include any allowed HFS file types as well as the filename extensions. For example, if you want to open text files, specify a file types array like this:

```
NSArray *fileTypes = [NSArray arrayWithObjects: @"txt", @"text",
                        NSFileTypeForHFSTypeCode( 'TEXT' ), nil];
```

[Next](Getting%20the%20Current%20Selection.md)[Previous](Using%20a%20Save%20Panel.md)

