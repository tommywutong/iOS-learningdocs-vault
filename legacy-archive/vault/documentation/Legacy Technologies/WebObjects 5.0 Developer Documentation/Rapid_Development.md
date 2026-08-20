---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/Introduction/Rapid_Development.html
archived_at: '2026-07-15T08:15:08.669872Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Web_Enabled_pplications.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](The_WebObjects_Advantage.md)

## Rapid Development

WebObjects is both powerful and flexible. With that power
and flexibility, however, comes a certain degree of complexity.
For many applications, whether HTML-based or Java Client-based,
it's more important to develop the application quickly than strive
for maximum flexibility or polish. As an example, a simple data-browsing
and editing application, intended only for internal use by a system
administrator, probably wouldn't warrant the same degree of effort
you would put into an Internet-enabled application accessible by
the general public. To simplify the development of applications
like the former, WebObjects includes a set of rapid-development
technologies: Direct to Web and Direct to Java Client.

Direct to Web and Direct to Java Client are similar in approach.
Their primary difference is in how the application interacts with
the end user. Direct to Web creates HTML-based WebObjects applications,
whereas Direct to Java Client creates WebObjects applications that
employ Java Client to partition the application between server and
client. Both are useful not only for "quick and dirty" applications,
but in many situations can also serve as rapid prototyping tools.
Because Direct to Web and Direct to Java Client both allow customization
on various levels, they are well-suited for bootstrapping and creating
your mission-critical applications.

### Direct to Web

Direct to Web is a configurable system for creating HTML-based
WebObjects applications that access a database. All Direct to Web
needs to create the application is a model for the database, which
you can build using EOModeler.

Direct to Web applications are not a set of static Web pages.
Instead, Direct to Web uses information from the model available
at runtime to dynamically generate the pages. Consequently, you
can modify your application's configuration at runtime-using
the Direct to Web Assistant-to hide objects of a particular class,
hide their properties, reorder the properties, and change the way
they are displayed without recompiling or relaunching the application.

Out of the box, Direct to Web generates Web pages for nine
common database tasks, including querying, editing, and listing.
To do this, Direct to Web uses a task-specific component called
a template that can perform the task on any entity. The templates,
in conjunction with a set of developer-configurable rules, are the
essential elements of your Direct to Web application.

Direct to Web is highly customizable. For example, you can
change the appearance of the standard templates, mix traditional
HTML-based WebObjects components with Direct to Web pages, and create
custom components and templates that implement specialized behavior.

### Direct to Java Client

Like Direct to Web, Direct to Java Client generates a user
interface for common database tasks using rules to control program
flow, and it has an Assistant that allows you to modify your applications
at runtime. The primary difference between Direct to Web and Direct
to Java Client is the type of application each produces: Direct
to Java Client produces Java Client applications that have the fast
and rich user interfaces associated with desktop applications. Thus,
Direct to Java Client applications have the same client-side requirements
that other Java Client applications do.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Web_Enabled_pplications.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](The_WebObjects_Advantage.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
