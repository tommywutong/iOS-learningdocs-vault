---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/GettingStarted/GettingStarted.36.html
archived_at: '2026-07-18T01:29:44.061319Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Getting Started With WebObjects

---

[!](Examining%20the%20Bindings.md) [!](Examining%20the%20Bindings.md) [!](Bindings%20in%20the%20Repetition%20Part.md)

---

#  Bindings in the Query Part

In the query part of the component, __movieDisplayGroup.queryMatch.title__ is bound to the title text field. There are similar bindings to the category text fields. The __queryMatch__ bindings allow users to specify search criteria to use when __movieDisplayGroup__ next fetches movies. The Match button is bound to __movieDisplayGroup.qualifyDataSource__, which actually performs the fetch.

For example, to display all comedies, a user types "Comedy" in the Category text field, and clicks the Match button. __movieDisplayGroup__ then refetches, selecting only movies whose __category__ values are set to Comedy.!

---

© 1999 Apple Computer, Inc. – (Last Updated 24 Aug 99)

[!](Examining%20the%20Bindings.md) [!](Examining%20the%20Bindings.md) [!](Bindings%20in%20the%20Repetition%20Part.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
