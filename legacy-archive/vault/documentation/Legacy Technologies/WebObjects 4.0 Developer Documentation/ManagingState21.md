---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DevGuide/ManagingState21.html
archived_at: '2026-07-18T01:20:14.773474Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Developer's Guide](The%20WebObjects%20Developer%27s%20Guide.md)

[!Table of Contents](Managing%20State.md) [!Previous Section](ManagingState20.md)

### Page Refresh and WODisplayGroup

If you're using a WODisplayGroup object in your application, you must enable page refresh so that the application and the client browser stay in agreement about which objects are being displayed.
A WODisplayGroup holds a set of objects (generally enterprise objects fetched from a database) and provides "batched" access to these objects. For example, if a user submits a query (such as, "Show me the movies released in 1996.") to a Movies application, a WODisplayGroup might return 10 records at a time to the user's browser. The application would offer controls to let the user display the next and previous batches of 10 movie titles. When the user decides to order one of the movies, the WODisplayGroup needs to know which batch the item comes from.
As the user presses the Next Ten Movies or Previous Ten Movies buttons, the WODisplayGroup updates its record of which 10 movies are being displayed. When the user decides to order the second movie in the list, the WODisplayGroup can determine the actual record since it knows which batch is being displayed and which record is number 2 in that batch. But if the user backtracks to a previous page (with page refresh disabled) and chooses the second record, the WODisplayGroup will erroneously pick the second record from its current batch. By enabling page refresh, the WODisplayGroup is alerted each time the user backtracks and can update its notion of the current batch, eliminating this problem.

[!Table of Contents](Managing%20State.md) [!Next Section](Deployment%20and%20Performance%20Issues.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
