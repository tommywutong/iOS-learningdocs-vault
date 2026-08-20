---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/State/PageWithName.html
archived_at: '2026-07-15T07:47:49.390766Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ManagingState.book.md)
[!Previous Section](PageAwake.md)

# pageWithName: and Page Caching

When the application object receives a __pageWithName:__ message, it creates a new component. For example, in the HelloWorld example a user enters a name in the first page (the Main component), clicks Submit, and is presented with a personal greeting on the second page (the Hello component). Clicking the Submit button in the first page invokes the __sayHello__ method in the Main component. As part of its implementation __sayHello__ sends a __pageWithName:__ message to the application object:

```
id visitorName;

- sayHello {
    id nextPage;

    // Create the next page.
    nextPage = [[self application] pageWithName:@"Hello"];

    // Set state in the Hello page
    [nextPage setVisitorName:visitorName];

    // Return the 'Hello' page.
    return nextPage;
}
```

Each time the __sayHello__ method is invoked, a new Hello component is created. For example, if the user backtracks to the main page and clicks the Submit button again, another Hello page is created. It's unlikely this duplication of components will be a problem for the HelloWorld application, since users quickly tire of its charms. But, depending on design, some applications may benefit by modifying the operation of __pageWithName:__ so that an existing component can be reused.

If you want to extend WebObjects' page caching mechanism to include pages returned by __pageWithName:__, you must implement your own solution. Fortunately, it's easy. One approach is to have the session maintain a dictionary that maps page names to page objects. Here's the code you would add to an application's __Session.wos__ file:

```
id pageDictionary;

- init {
    [super init];
    pageDictionary = [NSMutableDictionary dictionary];
    return self;

}

- pageWithName:aName {
    id aPage = [pageDictionary objectForKey:aName];

    if (!aPage) {
        aPage = [[self application] pageWithName:aName];
        [pageDictionary setObject:aPage forKey:aName];
    }
    return aPage;
}
```

Note that we implement __pageWithName:__ in the session object since we want to cache these pages on a per-session basis. (Overriding the method in the application object would cache pages on a per-application basis.) Since the __pageWithName:__ method that we want to use now resides in the session object, one line in the __sayHello__ method has to change (change in bold):

```
- sayHello {
    id nextPage;
    nextPage = [[self session] pageWithName:@"Hello"];
    [nextPage setVisitorName:visitorName];
    return nextPage;
}
```

[!Table of Contents](ManagingState.book.md)
[!Next Section](ClientCaching.md)
