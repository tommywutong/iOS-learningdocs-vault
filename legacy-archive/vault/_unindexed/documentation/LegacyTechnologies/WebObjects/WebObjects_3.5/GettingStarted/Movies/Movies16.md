---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/GettingStarted/Movies/Movies16.html
archived_at: '2026-07-15T07:54:15.691394Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](MoviesTOC.md) [!Previous Section](Movies15.md)

### Bindings in the Query Part

In the query part of the component, __movieDisplayGroup.queryMatch.title__ is bound to the Title text field. There are similar bindings to the Category and Rating text fields. The __queryMatch__ bindings allow users to specify search criteria to use when __movieDisplayGroup__ next fetches movies. The Match button is bound to __movieDisplayGroup.qualifyDataSource__, which actually performs the fetch.
For example, to display only R-rated comedies, a user types "Comedy" in the Category text field, types "R" in the Rating text field, and clicks the Match button. __movieDisplayGroup__ then refetches, selecting only movies whose __category__ values are set to Comedy and whose __rating__ values are set to R.!

[!Table of Contents](MoviesTOC.md) [!Next Section](Movies17.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
