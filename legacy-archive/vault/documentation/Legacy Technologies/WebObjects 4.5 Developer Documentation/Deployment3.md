---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DevGuide/Deployment3.html
archived_at: '2026-07-15T08:05:21.012991Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Developer's Guide

---

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Deployment2.md)

## Accessing Statistics

If your application has a WOStats page, you can look at the statistics that WOStatisticsStore gathers. WOStats is a reusable component stored in the WOExtensions framework (which WebObjects applications link to by default). While your application is running, you can access the WOStats page with a URL like the following:

```
http://localhost/cgi-bin/WebObjects/MyApp.woa/wa/WOStats
```


__Note:__  You can access any component directly using a URL with this form.
[Figure 37](#apple-gyydama) shows a WOStats page.

!

Figure 37. WOStats Page

The source for the WOStats page is provided, along with the source for all of the components in the WOExtensions framework, in __/System/Developer/Examples/WebObjects/Source/WOExtensions__ (__NeXT_ROOT\Developer\Examples\WebObjects\Source\WOExtensions__ on Windows NT systems).
If you want access to statistics programmatically, send the WOStatisticsStore a __statistics__ message. For example:

```
// WebScript
NSDictionary *myDict = [[[self application]
statisticsStore]
        statistics];
// Java
NSDictionary myDict =
    this.application().statisticsStore().statistics;
```


For a list of keys to this dictionary, see the WOStatisticsStore class specification in the _[WebObjects Class Reference](WebObjects%20Java%20API%20Reference.md)_.
Note that this dictionary is created on demand. It is costly to call this method repeatedly.

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Deployment4.md)
