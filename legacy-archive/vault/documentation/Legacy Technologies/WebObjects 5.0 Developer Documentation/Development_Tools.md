---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/Introduction/Development_Tools.html
archived_at: '2026-07-15T08:13:19.792841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](WebObjects_Features.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/IntroductionToWO/index.html)

## Development Tools

For the most part you interact with the WebObjects development
environment via three tools: Project Builder, WebObjects Builder,
and EOModeler.

### Project Builder

![[image: ../Art/projectbuildericon.gif]](../Art/projectbuildericon.gif)

Project Builder is your primary WebObjects development tool.
It provides an integrated development environment that allows you
to edit code, organize resources, and compile your project, as well
as facilitate your work with other programs like WebObjects Builder when
you edit your WebObjects components. Project Builder is described
in ["Project Builder"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/IntroductionToWO/iProject_Builder.html).

### WebObjects Builder

![[image: ../Art/wobicon.gif]](../Art/wobicon.gif)

WebObjects Builder is a specialized application for editing
WebObjects components. It handles editing the HTML file as well
as the WOD (WebObjects data) file that controls the connection between
your HTML components and your Java code. WebObjects Builder is introduced
in ["The Main Component"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/DynamicContent/iThe_Main_Component.html).

### EOModeler

![[image: ../Art/eomodelericon.gif]](../Art/eomodelericon.gif)

EOModeler is a tool for constructing a __model__ that
relates your database structure to Java objects. As such, it's
only used in WebObjects programs that perform database access. With EOModeler
you can create a model in two ways:

- Reverse-engineer
  an existing database schema.

  EOModeler reads your database's
  schema and creates a model from it.
- Create the model from scratch.

  You can create a new model
  from scratch by defining the entities, attributes, and relationships
  that represent your data model. You can then have EOModeler create
  the underlying tables. This is the approach used in ["Creating the Authors Model"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOMBasics/iThe_Authors_Application.html).

Constructing a good model is a very important part of developing
a database-enabled WebObjects application. With a properly constructed
model, an application practically writes itself. See ["The Model"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/EOFArchitecture/iThe_Model.html) for more
information.

[![Previous](attachments/DiscoveringWO/Images/previous.gif)](WebObjects_Features.md)[![Next](attachments/DiscoveringWO/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DiscoveringWO/IntroductionToWO/index.html)

---

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
