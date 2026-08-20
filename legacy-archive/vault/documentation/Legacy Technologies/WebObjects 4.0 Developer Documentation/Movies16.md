---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/GettingStarted/Movies/Movies16.html
archived_at: '2026-07-18T01:22:04.775838Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Getting Started With WebObjects](Getting%20Started.md)

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Previous Section](Movies15.md)

### Bindings in the Query Part

In the query part of the component, __movieDisplayGroup.queryMatch.title__ is bound to the Title text field. There are similar bindings to the Category text fields. The __queryMatch__ bindings allow users to specify search criteria to use when __movieDisplayGroup__ next fetches movies. The Match button is bound to __movieDisplayGroup.qualifyDataSource__, which actually performs the fetch.
For example, to display all comedies, a user types "Comedy" in the Category text field, and clicks the Match button. __movieDisplayGroup__ then refetches, selecting only movies whose __category__ values are set to Comedy.

!

[!Table of Contents](Creating%20a%20WebObjects%20Database%20Application.md) [!Next Section](Movies17.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
