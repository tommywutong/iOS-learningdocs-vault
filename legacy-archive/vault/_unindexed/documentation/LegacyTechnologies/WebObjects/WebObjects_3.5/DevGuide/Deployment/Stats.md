---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/DevGuide/Deployment/Stats.html
archived_at: '2026-07-15T07:51:25.587229Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](Deployment.md) [!Previous Section](Deployment.md)

# Recording Application Statistics

While your application runs, a WOStatisticsStore object (StatisticsStore in Java) records statistics about the application. It records such information as how many sessions are active, how many requests have been processed, and which pages have been accessed. This section describes how to maintain a log file, access those statistics, and add to them.

## Maintaining a Log File

WOStatisticsStore has the ability to record session information to a log file that can be analyzed by a Common Log File Format (CLFF) standard analysis tool. WOStatisticsStore does not maintain this log file by default. To store information in a log file, you must set the path to the log file early in your application. For example:

```
    // Java
    public Application() {
        super();
        this.statisticsStore().setLogFile("/tmp/WebObjects.log", 1);
        ...
    }
```


When a log file is set, WOStatisticsStore records all information returned by __descriptionForResponse:inContext:__ to that log file at the end of each cycle of the request-response loop.

## Accessing Statistics

If your application has a WOStats page, you can look at the statistics that WOStatisticsStore gathers. WOStats is a reusable component stored in the WOExtensions framework (which WebObjects applications link to by default). While your application is running, you can access the WOStats page with a URL like the following:

```
    http://localhost/cgi-bin/WebObjects/MyWebApp.woa/-/WOStats
```


__Note:__  You can access any component directly using a URL with this form.
[Figure 38](#apple-gyydama) shows a WOStats page.

!Figure 38. WOStats Page 
For more information about the statistics presented on the WOStats page, see [_Serving WebObjects_](../../ServingWebObjects/ServingWebObjectsTOC.md).

If you want access to statistics programmatically, send the WOStatisticsStore a __statistics__ message. For example:

```
    // WebScript
    NSDictionary *myDict = [[[self application] statisticsStore]
        statistics];

    // Java
    ImmutableHashTable myDict =
        this.application().statisticsStore().statistics;
```


For a list of keys to this dictionary, see the WOStatisticsStore class specification in the _[WebObjects Class Reference](../../Reference/Reference.md)_.

## Recording Extra Information

There may be occasions when you want to have the WOStatisticsStore object record more information than it usually does. For example, it may be useful to know the value of a certain component variable each time the page is accessed.
To record extra information about a page, override __descriptionForResponse:inContext:__ in your component.
For example, the HelloWorld example's Hello component could return the value of its __visitorName__ instance variable along with the component name:

```objc
    // WebScript HelloWorld Hello.m
    - (NSString *)descriptionForResponse:(WOResponse *)response
    inContext:(WOContext *)context {
        return [NSString stringWithFormat:@"%@/%@",
            [self name], visitorName];
    }

    //Java HelloWorld Hello.java
    public String descriptionForResponse(Response response, Context context)
    {
        return new String(this.name() + visitorName);
    }
```


The response component receives the __descriptionForResponse:inContext:__ message after it receives the message __appendToResponse:inContext:__. The default implementation of __descriptionForResponse:inContext:__ prints the page name. Unlike other methods invoked during the request-response loop, __descriptionForResponse:inContext:__ is not sent to all components and dynamic elements on the page; it is sent only to the top-level response component.
Note that this method receives the response and context objects as arguments, just as __appendToResponse:inContext:__ does. This means you can add such information as the HTTP header keys, or any other information recorded in these objects, to your description string.

[!Table of Contents](Deployment.md) [!Next Section](ErrorHandling.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
