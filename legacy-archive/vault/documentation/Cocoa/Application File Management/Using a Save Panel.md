---
title: Application File Management
apple_id: 10000056i
resource_type: Guide
platform: macOS
topic: Data Management
technology: AppKit
published: '2011-05-25'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AppFileMgmt/Tasks/UsingASavePanel.html
archived_at: '2026-07-15T05:25:38.373765Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Application File Management](Introduction%20to%20Application%20File%20Management.md)


[Next](Using%20an%20Open%20Panel.md)[Previous](Working%20With%20Directory%20Wrappers.md)

# Using a Save Panel

Typically, you access an `NSSavePanel` by invoking the [savePanel](https://developer.apple.com/documentation/appkit/nssavepanel/1539016-savepanel) class method. A typical programmatic use of NSSavePanel requires you to:

- Invoke `savePanel`
- Configure the panel (for instance, set its title or add a custom view)
- Run the panel in a modal loop
- Test the result; if successful, save the file under the chosen name and in the chosen directory

The following Objective-C code fragment demonstrates this sequence. (Two objects in this example, _newView_ and _textData_, are assumed to be defined and created elsewhere.)

```
NSSavePanel *sp;
int runResult;

/* create or get the shared instance of NSSavePanel */
sp = [NSSavePanel savePanel];

/* set up new attributes */
[sp setAccessoryView:newView];
[sp setRequiredFileType:@"txt"];

/* display the NSSavePanel */
runResult = [sp runModal];

/* if successful, save file under designated name */
if (runResult == NSOKButton) {
    if (![textData writeToFile:[sp filename] atomically:YES])
         NSBeep();
}
```

When the class receives a `savePanel` message, it tries to reuse an existing panel rather than create a new one. When a panel is reused its attributes are reset to the default values so the effect is the same as receiving a new panel. Because a Save panel may be reused, you shouldn't modify the instance returned by `savePanel` except through the methods of the [NSSavePanel](https://developer.apple.com/documentation/appkit/nssavepanel) class. For example, you can set the panel’s title and required file type, but not the arrangement of the buttons within the panel.

[Next](Using%20an%20Open%20Panel.md)[Previous](Working%20With%20Directory%20Wrappers.md)

