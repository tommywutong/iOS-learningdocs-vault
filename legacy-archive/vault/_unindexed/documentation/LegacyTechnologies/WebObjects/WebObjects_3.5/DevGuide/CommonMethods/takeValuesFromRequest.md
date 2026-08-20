---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/CommonMethods/takeValuesFromRequest.html
archived_at: '2026-07-15T07:51:18.497117Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](CommonMethods.md) [!Previous Section](RequestHandlingMethods.md)

## Taking Input Values From a Request

The __takeValuesFromRequest:inContext:__ method is invoked during the first phase of the request-response loop, immediately after all of the objects involved in the request have performed their __awake__ methods. When this phase concludes, the request component has been initialized with the bindings made in WebObjects Builder.
Override __takeValuesFromRequest:inContext:__ when you want to do one of the following:

- Access information from the request or context object.
- Perform postprocessing on user input.

In the first case, you can place your code before the message to __super__. In the second case, you must place your code after the message to __super__. For example, the following implementation of __takeValuesFromRequest:inContext:__ records the kinds of browsers-user agents-from which requests are made:

```
    // WebScript example
    - takeValuesFromRequest:request inContext:context {
        id userAgent = [request headerForKey:@"user-agent"];
        [self recordUserAgent:userAgent];
        [super takeValuesFromRequest:request inContext:context];
    }
```


The following example performs postprocessing. It takes the values for the __street__, __city__, __state__, and __zipCode__ variables and stores them in the __address__ variable formatted as a standard mailing address.

```
    // WebScript example
    - takeValuesFromRequest:request inContext:context {
    [super takeValuesFromRequest:request inContext:context];
    address = [NSString stringWithFormat:@"%@\n%@, %@  %@",
        street, city, state, zipCode];
    }
    // Java example
    public void takeValuesFromRequest(Request request, Context context) {
    super.takeValuesFromRequest(request, context);
    address = street + city + state + zipCode;
    }
```

[!Table of Contents](CommonMethods.md) [!Next Section](invokeActionForRequest.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
