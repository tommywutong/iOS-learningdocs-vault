---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/Integrating4.html
archived_at: '2026-07-15T07:46:38.200173Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](Integrating3.md)

## __4. Implement methods for bound actions__

Implement action methods just as you do in other WebObjects scripts or Objective-C implementation methods. Just be sure to return __nil__ instead of __self__ or a response page. This signals to the server-side component that it should synchronize its state with the client applets after completion of the method.

```
- capitalizeString {
    if ([functionSelectedItem isEqualToString:@"1"]) {
        outputString = [inputString lowercaseString];
    } else if ([functionSelectedItem isEqualToString:@"2"]) {
        outputString = [inputString capitalizedString];
    } else if ([functionSelectedItem isEqualToString:@"3"]) {
        if ([inputString length] > 4) {
            outputString = [NSString stringWithFormat:@"%@-diddly-%@",
                [inputString substringToIndex:5],
                [inputString substringFromIndex:3]];
        } else {
            outputString = [inputString stringByAppendingString:@"-eroonie"];
        }
    } else {
        outputString = [inputString uppercaseString];
    }
    return nil;
}
```

### A Note on Backtracking

It is a good idea to have a "welcome" page for applications that use client-side components and, indeed, for all WebObjects applications. Generally the client browser caches URLs and WebObjects caches the corresponding component instances to use as request pages. When the user backtracks through the pages of a session and reaches the first page, a new session will begin and you'll lose all state associated with the lost session. The reason for this is that the first page does not have a URL that includes the session ID, a context ID, and other important information.

In addition to having a "welcome" page as the first page, you can also disable caching by the client, setting the page expiration date to "now." This setting forces the URL request to be sent anew to the WebObjects application, which regenerates the request page. You disable client caching by sending __setPageRefreshOnBacktrackEnabled:__ to the WOApplication object with an argument of YES (this happens automatically with pages that have client-side components on them).

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](MakingOwn0.md)
