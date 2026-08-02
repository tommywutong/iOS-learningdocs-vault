---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/appendToResponse.html
archived_at: '2026-07-15T07:47:31.362228Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](invokeActionForRequest.md)

# appendToResponse:inContext:

This method is invoked in the phase of the request-response loop during which the application generates HTML for the response page. You can implement this method to add to the response content or otherwise manipulate the HTTP response. For example, you can add or modify the HTTP headers. The following code excerpt sets the "Expires" header in the HTTP response to "0."

```
- appendToResponse:aResponse inContext:aContext
{
  [super appendToResponse:aResponse inContext:aContext];
  [aResponse setHeader:@"0" forKey:@"Expires"];
}
```

The first argument to __appendToResponse:inContext:__ is a WOResponse object. A WOResponse object encapsulates information contained in the generated HTTP response such as the status, response headers, and response content. The second argument is a WOContext object. A WOContext object contains references to application-specific information such as the path to the request component's directory, the version of WebObjects that's running, the name of the application, and the name of the request page.

In a similar manner, you can use __appendToResponse:inContext:__ to append text to the response content. In the following example, a component's __appendToResponse:inContext:__ method appends bold and italic markup elements around a string's value as follows:

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

After you invoke __super__'s __appendToResponse:inContext:__, the application generates the response page. At this point you could do something appropriate for the end of the transaction. For example, the following implementation terminates the current session:

```
- appendToResponse:response inContext:context {
    [super appendToResponse:response inContext:context];
    [[self session] terminate];
}
```

The WOSession method __terminate__ schedules the destruction of state associated with the current session, but termination is deferred until the current transaction concludes. You can explicitly terminate a session anytime, anywhere in a WebObjects application.

[!Table of Contents](RunLoop.book.md)
[!Next Section](Summary.md)
