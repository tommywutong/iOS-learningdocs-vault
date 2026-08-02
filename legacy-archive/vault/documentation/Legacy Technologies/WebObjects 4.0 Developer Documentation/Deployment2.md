---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/Deployment2.html
archived_at: '2026-07-18T01:20:04.383781Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Previous Section](Recording%20Application%20Statistics.md)

## Maintaining a Log File

WOStatisticsStore has the ability to record session information to a log file that can be analyzed by a Common Log File Format (CLFF) standard analysis tool. WOStatisticsStore does not maintain this log file by default. To store information in a log file, you must set the path to the log file early in your application. For example:

```
// Java
public Application() {
    super();

this.statisticsStore().setLogFile("/tmp/WebObjects.log",
1);
    ...
}
```


When a log file is set, WOStatisticsStore records all information returned by __descriptionForResponse:inContext:__ to that log file at the end of each cycle of the request-response loop. Note that __descriptionForResponse:inContext:__ is only invoked during component actions; thus, the log file won't contain entries for direct actions.
Note that descriptions are not saved in the log file in sequential order. A session accumulates descriptions as a user traverses from page to page, and then saves them all at once in the CLFF log file when the session times out. Thus, the WebObjects CLFF log file has a big advantage over a typical HTTP CLFF log file (which saves accesses sequentially): by inspecting it you can clearly see the paths followed by each individual user in your WOApplication. Of course, the WebObjects log file can still be parsed by any web server analysis tool.

[!Table of Contents](Deployment%20and%20Performance%20Issues.md) [!Next Section](Deployment3.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
