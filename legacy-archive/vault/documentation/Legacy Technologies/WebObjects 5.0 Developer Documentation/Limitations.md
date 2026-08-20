---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/D2W/Limitations.html
archived_at: '2026-07-15T08:15:04.737395Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Advantages__eb_Approach.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__rect_to_Web.md)

## Limitations

Direct to Web is an HTML-based technology. As a result, Direct
to Web user interfaces are highly portable but suffer the limited
interactivity provided by HTML forms.

Because Direct to Web generates your applications for you,
the applications have a number of additional limitations.

First, the programming model is indirect. You provide a model
and Direct to Web assembles the application for you. The Web page
generation is performed by a "magic box." You don't have to
know what's going on. This makes it really easy to get started programming
with Direct to Web. But for certain customizations, the learning
curve gets very steep very fast.

The machinery for generating Web pages is an entirely new
layer on top of the WebObjects HTML-based application technology.
This layer adds complexity that regular HTML-based applications
don't have, and you might have to learn the details of it to get certain
results. In fact, making fundamental changes to a Direct to Web
application can be a lot of work. Note, however, that you can typically
reuse this work in later applications.

Another disadvantage is that modifying the layout of a Direct
to Web template is more involved and harder to do than laying out
a WebObjects component because Direct to Web templates are more
complex than most WebObjects components.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Advantages__eb_Approach.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Guidelines__rect_to_Web.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
