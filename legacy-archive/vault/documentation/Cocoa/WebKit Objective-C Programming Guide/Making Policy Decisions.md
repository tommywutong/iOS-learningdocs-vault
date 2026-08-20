---
title: WebKit Objective-C Programming Guide
apple_id: 10000164i
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2012-11-09'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/DisplayWebContent/Tasks/PolicyDecisions.html
archived_at: '2026-07-15T07:14:53.225411Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Objective-C Programming Guide](Introduction%20to%20WebKit%20Objective-C%20Programming%20Guide.md)


[Next](Enabling%20Editing.md)[Previous](Managing%20History.md)

# Making Policy Decisions

You can make decisions about what web content to display in a WebView by implementing a policy delegate that conforms to the WebPolicyDelegate protocol.

The protocol is very flexible, allowing you to make a wide range of policy decisions. For example, you can implement a policy delegate to log URL requests, check for patterns you might not permit, block certain websites, block types of files, and even block IP addresses. The protocol provides the hooks for you to intercept requests—you implement the actual policy decisions.

For example, follow these steps to modify the MiniBrowser application located in `/Developer/Examples/WebKit` to ignore selected URLs:

1. Open `MyDocument.nib` using Interface Builder and set the WebView’s `policyDelegate` outlet to `File’s Owner` (the MyDocument instance).
2. Implement `webView:decidePolicyForNavigationAction:request:frame:decisionListener:` to filter the URL requests. In this example, URL requests with host names ending in `company.com` are ignored.

```objc
- (void)webView:(WebView *)sender decidePolicyForNavigationAction:(NSDictionary *)actionInformation
        request:(NSURLRequest *)request frame:(WebFrame *)frame decisionListener:(id)listener {
    NSString *host = [[request URL] host];
    if ([host hasSuffix:@"company.com"])
        [listener ignore];
    else
        [listener use];
}
```

[Next](Enabling%20Editing.md)[Previous](Managing%20History.md)

