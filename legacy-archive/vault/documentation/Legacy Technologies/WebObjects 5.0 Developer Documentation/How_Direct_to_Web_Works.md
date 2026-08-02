---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsOverview/D2W/How_Direct_to_Web_Works.html
archived_at: '2026-07-15T08:15:03.698414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Direct_to_W_pplications.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Developing__Application.md)

## How Direct to Web Works

As you have seen, Direct to Web applications have a fixed
structure. They consist of a set of task pages (for example, query,
list, and edit pages) that work for any type of enterprise object.
These task pages are created using special WebObjects components
called Direct to Web templates.

A Direct to Web template uses information from the entities
of the enterprise objects it displays. An entity is the piece of
the model that specifies how a table maps to a specific enterprise
object. The Direct to Web template takes advantage of the entity's
property information (that is, information about the entity's
attributes and relationships) and determines the properties it needs
to display. For example, a Direct to Web template displaying a list
page for Movie objects can determine that it needs to display the
title, release date, category, and other attributes for each movie
on the page ( [Figure 5-11](#apple-inbeqq2civfes)).

__Figure
5-11 Determining attributes from the entity__

![[image: ../Art/ProductAttributes.gif]](../Art/ProductAttributes.gif)

Direct to Web applications can be configured using a Java
applet called the Direct to Web Assistant. The configuration information
is stored as a database of rules. Rules say something like "if
the task page is a list page and the entity is the Movie entity,
do not display the banner." Each rule has a priority and rules
with higher priority override rules with lower priority. Direct
to Web defines a set of default rules that define the basic application
behavior. You can define higher priority rules that override the
default rules for special cases. This is exactly what the Direct
to Web Assistant does. [Figure 5-12](#apple-krifqusfiyytany) shows the relationship between the Direct to Web
template, the rule system, the rule database, and the Direct to
Web Assistant.

__Figure
5-12 The Direct to Web rule system__

![[image: ../Art/Rules.gif]](../Art/Rules.gif)

Note that when you configure your application with the Direct
to Web Assistant, you don't need to recompile your code to try
your changes. Direct to Web is not a code generation wizard. It
generates Web pages at runtime based on the templates and the rules.

[![Previous](attachments/WebObjectsOverview/Images/previous.gif)](Direct_to_W_pplications.md)[![Next](attachments/WebObjectsOverview/Images/next.gif)](Developing__Application.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
