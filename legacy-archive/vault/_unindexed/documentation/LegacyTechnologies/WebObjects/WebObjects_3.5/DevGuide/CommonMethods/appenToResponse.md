---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/appenToResponse.html
archived_at: '2026-07-15T07:51:17.495837Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](invokeActionForRequest.md)

## Generating a Response

The __appendToResponse:inContext:__ method is invoked in the final phase of the request-response loop, during which the application generates HTML for the response page. You can override this method to add to the response content or otherwise manipulate the HTTP response. For example, you can add or modify the HTTP headers as in the following example:

```
    - appendToResponse:aResponse inContext:aContext
    {
        [super appendToResponse:aResponse inContext:aContext];
        [aResponse setHeader:@"True"
            forKey:@"dshttpd-NoAutomaticFooter"];
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
        [aResponse appendContentHTMLAttributeValue:@"<p>"];
        if (isBold) {
            [aResponse appendContentHTMLAttributeValue:@"<b>"];
        }
        if (isItalic) {
            [aResponse appendContentHTMLAttributeValue:@"<i>"];
        }

        if (escapeHTML) {
            [aResponse appendContentString:aString];
        } else {
            [aResponse appendContentHTMLString:aString];
        }

        if (isItalic) {
            [aResponse appendContentHTMLAttributeValue:@"</i>"];
        }
        if (isBold) {
            [aResponse appendContentHTMLAttributeValue:@"</b>"];
        }
    }
```


After you invoke __super__'s __appendToResponse:inContext:__, the application generates the response page. At this point you could do something appropriate for the end of the request. For example, the following implementation terminates the current session:

```
    public void appendToResponse(response, context) {
        super.appendToResponse(response, context);
        session().terminate();
    }
```


For more details on each phase of the request-response loop, read the chapter ["WebObjects Viewed Through Its Classes"](../HowWOWorks/HowWOWorks.md).

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
