---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Methods17.html
archived_at: '2026-07-18T01:20:17.251227Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Common%20Methods.md) [!Previous Section](Methods16.md)

## Taking Input Values From a Request

The __takeValuesFromRequest:inContext:__ method is invoked during the first phase of the component action request-response loop, immediately after all of the objects involved in the request have performed their __awake__ methods. When this phase concludes, the request component has been initialized with the bindings made in WebObjects Builder.
You might override __takeValuesFromRequest:inContext:__ if you want to perform post-processing on user input. The following example takes the values for the component's __street__, __city__, __state__, and __zipCode__ instance variables and stores them in __address__ variable formatted as a standard mailing address.

```
// WebScript example
- takeValuesFromRequest:request inContext:context {
    [super takeValuesFromRequest:request inContext:context];
    address = [NSString stringWithFormat:@"%@\n%@, %@  %@",
        street, city, state, zipCode];
}
// Java example
public void takeValuesFromRequest(WORequest request,
WOContext context) {
    super.takeValuesFromRequest(request, context);
    address = street + city + state + zipCode;
}
```


This first phase of the component action request-response loop is only performed if the request has form values to use as input. The first request that an application receives, for example, would not have input values, and thus __takeValuesFromRequest:inContext:__ is not performed for that first request. If you override __takeValuesFromRequest:inContext:__, make sure that your method is only necessary when there are form values; do not override this method to perform something that should occur for every request.
For example, it may be tempting to override __takeValuesFromRequest:inContext:__ when you want access to information contained in the request or context objects. Because you can not guarantee that __takeValuesFromRequest:inContext:__ will be invoked, you should not do this. Instead, you can access the request and context in the __awake__ method this way:

```
- awake {
    id userAgent = [[[self context] request]
        headerForKey:@"user-agent"];
    [self recordUserAgent:userAgent];
}
```

[!Table of Contents](Common%20Methods.md) [!Next Section](Methods18.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
