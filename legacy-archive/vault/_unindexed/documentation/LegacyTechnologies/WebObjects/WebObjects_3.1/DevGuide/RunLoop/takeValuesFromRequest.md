---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/RunLoop/takeValuesFromRequest.html
archived_at: '2026-07-15T07:47:33.362170Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](RunLoop.book.md)
[!Previous Section](RequestHandlingMethods.md)

# takeValuesFromRequest:inContext:

This method is invoked during the phase of the request-response loop when the application stores user input. When this phase concludes, the request component has been initialized with the bindings made in WebObjects Builder or the assignments made in the declarations file.

The first argument to __takeValuesFromRequest:inContext:__ is a WORequest object. A WORequest object encapsulates information from an HTTP request such as the method line, request headers, URL, and form values. The second argument is a WOContext object. A WOContext object contains references to information specific to the application, such as the path to the request component's directory, the version of WebObjects that's running, the name of the application, and the name of the request page.

It is common to use this method to access request and context information. For example, the following implementation of __takeValuesFromRequest:inContext:__ records the kinds of browsers---user agents---from which requests are made (the "recordUserAgent:" method is assumed to be implemented in the same script):

```
- takeValuesFromRequest:request inContext:context {
    id userAgent = [request headerForKey:@"user-agent"];
    [self recordUserAgent:userAgent];
    [super takeValuesFromRequest:request inContext:context];
}
```

When you invoke __super__'s __takeValuesFromRequest:inContext:__ in your implementation of the same method, the application processes user input. So after the message to __super__ is when you could perform postprocessing of user input. For example, the following implementation takes the values for the __street__, __city__, __state__, and __zipCode__ variables and stores them in __address__ variable formatted as a standard mailing address.

```
- takeValuesFromRequest:request inContext:context {
    [super takeValuesFromRequest:request inContext:context];
    address = [NSString stringWithFormat:@"%@\n%@, %@  %@",
            street, city, state, zipCode];
}
```

[!Table of Contents](RunLoop.book.md)
[!Next Section](invokeActionForRequest.md)
