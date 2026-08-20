---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/EnablingEditing.html
archived_at: '2026-07-15T07:14:51.217808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Saving%20and%20Loading%20Web%20Content.md)[Previous](Making%20Policy%20Decisions.md)

# Enabling Editing

By setting the editable attribute of a WebView object you can make all the web content displayed in that view editable. Editing the content will change the underlying Document Object Model (DOM). However, setting the editable attribute to `YES` does not modify the editing attributes of the DOM objects—the WebView attribute setting overrides the DOM attributes.

For example, to modify the MiniBrowser application located in `/Developer/Examples/WebKit`, set the editable attribute to `YES` after the nib file is loaded in MyDocument’s [windowControllerDidLoadNib:](https://developer.apple.com/documentation/appkit/nsdocument/1515221-windowcontrollerdidloadnib) method as follows:

```objc
- (void)windowControllerDidLoadNib:(NSWindowController *) aController
{
    [super windowControllerDidLoadNib:aController];
    ...
    // Set editable flag
    [webView setEditable:YES];
}
```

Now when you build and run the application, you can add, delete, and modify the HTML content displayed in a WebView object. See [Saving and Loading Web Content](Saving%20and%20Loading%20Web%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytinzsfvbuuqsfjbaucry) for how to get the HTML source from the DOM.

[Next](Saving%20and%20Loading%20Web%20Content.md)[Previous](Making%20Policy%20Decisions.md)

