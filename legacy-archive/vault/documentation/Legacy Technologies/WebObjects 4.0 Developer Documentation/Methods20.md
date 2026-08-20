---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods20.html
archived_at: '2026-07-18T01:20:17.621274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods19.md)

## Generating a Response

The __appendToResponse:inContext:__ method is invoked in the final phase of the request-response loop, during which the application generates HTML for the response page.
__Note:__  Unlike, __takeValuesFromRequest:inContext:__ and __invokeActionForRequest:inContext:__, the __appendToResponse:inContext:__ method may be invoked by the direct action request-response loop. If the direct action method returns a WOComponent object, that component's __appendtoResponse:inContext:__ method is invoked to generate the response.
You can override this method to add to the response content or otherwise manipulate the HTTP response. For example, you can add a cookie to the response as in the following example:

```
- appendToResponse:aResponse inContext:aContext
{
        id aCookie = [WOCookie cookieWithName:@"myCookie"
            value:@"important information goes here"];

        [super appendToResponse:aResponse inContext:aContext];
        [aResponse addCookie:aCookie];
}
```


In a similar manner, you can use __appendToResponse:inContext:__ to add text to the response content. In the following example, a component's __appendToResponse:inContext:__ method adds bold and italic markup elements around a string's value as follows:

```
id value;
id escapeHTML;
id isBold;
id isItalic;

- appendToResponse:aResponse inContext:aContext
{
        id aString = [value description];

        [super appendToResponse:aResponse inContext:aContext];
        [aResponse appendContentHTMLString:@"<p>"];
        if (isBold) {
            [aResponse appendContentHTMLString:@"<b>"];
        }
        if (isItalic) {
            [aResponse appendContentHTMLString:@"<i>"];
        }

        if (escapeHTML) {
            [aResponse appendContentString:aString];
        } else {
            [aResponse appendContentHTMLString:aString];
        }

        if (isItalic) {
            [aResponse appendContentHTMLString:@"</i>"];
        }
        if (isBold) {
            [aResponse appendContentHTMLString:@"</b>"];
        }
}
```


After you invoke __super__'s __appendToResponse:inContext:__, the application generates the response page. At this point you could do something appropriate for the end of the request. For example, the following implementation terminates the current session:

```
public void appendToResponse(WOResponse response,
WOContext context) {
    super.appendToResponse(response, context);
    session().terminate();
}
```


For more details on each phase of the request-response loop, read the chapter ["WebObjects Viewed Through Its Classes"](WebObjects%20Viewed%20Through%20Its%20Classes.md#apple-he2tmmy).

[!Table of Contents](Common%20Methods.md) [!Next Section](Debugging%20a%20WebObjects%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
