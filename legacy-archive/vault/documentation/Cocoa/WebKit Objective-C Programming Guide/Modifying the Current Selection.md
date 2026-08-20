---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/CurrentSelection.html
archived_at: '2026-07-15T07:14:49.238277Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Changing%20Editing%20Behavior.md)[Previous](Saving%20and%20Loading%20Web%20Content.md)

# Modifying the Current Selection

There are a number of WebView editing methods that allow you to modify the current selection. For example, you can replace the current selection with plain text as follows:

```
[webView replaceSelectionWithText:@”SomeString”];
```

You can replace the current selection with a styled string as follows:

```
NSString *markupString = [NSString stringWithFormat:
    @"<span style='color: red; font-style: italic'>%@</span>",
    @”SomeString”];
[webView replaceSelectionWithMarkupString:markupString];
```

[Next](Changing%20Editing%20Behavior.md)[Previous](Saving%20and%20Loading%20Web%20Content.md)

