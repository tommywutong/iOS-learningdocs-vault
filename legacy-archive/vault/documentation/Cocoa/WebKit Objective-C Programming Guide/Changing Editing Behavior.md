---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/ChangingEditingBehavior.html
archived_at: '2026-07-15T07:14:48.765267Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Using%20Undo%20When%20Editing.md)[Previous](Modifying%20the%20Current%20Selection.md)

# Changing Editing Behavior

You can control or augment user editing by implementing a WebView editing delegate, an object that conforms to the WebEditingDelegate protocol. An editing delegate may receive _should_ messages before or _did_ messages after an editing action. Typically, you implement an editing delegate if you want to change the default editing behavior.

You implement should methods if you want to control user editing actions—these messages are initiated by a user action not by simply invoking WebView editing methods programmatically. The should methods are of the form `webView:should...` and may return `YES` to permit an action or `NO` to disallow an action. Optionally, the delegate can take an alternative action and return `NO` so the sender doesn’t take additional action.

For example, you can control the insertion of text by implementing the `webView:shouldInsertText:replacingDOMRange:givenAction:` method. In this example, the user may use the Shift key to alter an insertion:

```objc
- (BOOL)webView:(WebView *)webView shouldInsertText:(NSString *)text replacingDOMRange:(DOMRange *)range givenAction:(WebViewInsertAction)action
{
    if ([self shiftKeyIsDown]) {
        NSString *string = [NSString stringWithFormat:@"Big-%@", text];
        [webView replaceSelectionWithText:string];
        DOMRange *range = [webView selectedDOMRange];
        [range collapse:NO];
        [webView setSelectedDOMRange:range affinity:NSSelectionAffinityUpstream];
        return NO;
    }
    return YES;
}
```


A WebView editing delegate is automatically registered to receive notification of editing actions. The WebView editing delegate is sent a `webViewDid...` notification message—where _sender_ is a WebView object—after the action takes place.

[Next](Using%20Undo%20When%20Editing.md)[Previous](Modifying%20the%20Current%20Selection.md)

