---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/Direct_to_W_rchitecture.html
archived_at: '2026-07-15T08:12:22.015444Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/iUser_Templates.html)[![Next](attachments/DirectToWeb/Images/next.gif)](Direct_to_Web_Components.md)

# Direct to Web Architecture

The Direct to Web framework works together
with the WebObjects framework to generate web pages for nine database
tasks including querying, editing, and listing. To do this, Direct
to Web uses a task-specific component called a _Direct
to Web template_ that can perform the task on any entity.
Direct to Web also translates the information that Enterprise Objects
Framework provides about the entity into values the Direct to Web template
needs to render the page.

This chapter discusses the Direct to Web architecture and
how Direct to Web generates a page. More specifically, it describes

- the different
  types of components that Direct to Web uses to render the pages
- the _Direct to Web context_, an instance
  of the D2WContext class that resolves the bindings in the Direct
  to Web template's binding file
- the _Direct to Web factory_, an instance
  of the D2W class that creates the Direct to Web pages
- how Direct to Web generates a query page
- the Direct to Web rule system, which contains application
  configuration information

[![Previous](attachments/DirectToWeb/Images/previous.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/iUser_Templates.html)[![Next](attachments/DirectToWeb/Images/next.gif)](Direct_to_Web_Components.md)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
