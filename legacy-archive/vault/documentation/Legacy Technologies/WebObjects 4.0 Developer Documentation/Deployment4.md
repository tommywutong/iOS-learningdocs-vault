---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Deployment4.html
archived_at: '2026-07-18T01:20:04.666234Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Deployment3.md)

## Recording Extra Information

There may be occasions when you want to have the WOStatisticsStore object record more information than it usually does. For example, it may be useful to know the value of a certain component variable each time the page is accessed. This is most easily accomplished by overriding __descriptionForResponse:inContext:__ in your component and having it return the desired information.
For example, the HelloWorld example's Hello component could return the value of its __visitorName__ instance variable along with the component name:

```objc
// WebScript Hello.m
- (NSString *)descriptionForResponse:(WOResponse
*)response inContext:(WOContext *)context {
        return [NSString stringWithFormat:@"%@/%@",
            [self name], visitorName];
}
//Java Hello.java
public String descriptionForResponse(WOResponse response,
WOContext context) {
        return new String(this.name() + visitorName);
}
```


The response component receives the __descriptionForResponse:inContext:__ message after it receives the message __appendToResponse:inContext:__. The default implementation of __descriptionForResponse:inContext:__ prints the page name. Unlike other methods invoked during the component action request-response loop, __descriptionForResponse:inContext:__ is not sent to all components and dynamic elements on the page; it is sent only to the top-level response component.
Note that this method receives the response and context objects as arguments, just as __appendToResponse:inContext:__ does. This means you can add such information as the HTTP header keys, or any other information recorded in these objects, to your description string. This description string is then appended to the log file in the CLFF format as discussed in ["Maintaining a Log File"](Deployment2.md#apple-gu4tooa).

When an application is deployed, a session object keeps in memory all these descriptions in the order their components were accessed by the session's user. When the session times out, three things happen:

- All its descriptions are written in the CLFF log file (if any).
- All its descriptions appear in the WOStats page under "Last User's Statistics."
- All its descriptions are added to all previous descriptions, and these totals appear in the WOStats page under "Detailed Statistics."

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Error%20Handling.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
