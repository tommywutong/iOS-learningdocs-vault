---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/The_Structu_Web_Project.html
archived_at: '2026-07-15T08:12:31.600543Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Creating_a__Web_Project.md)[!](Using_Your__Application.md)

## The Structure of a Direct to Web Project

A Direct to Web project has a structure similar to other
WebObjects application projects. A newly created project contains three
components, each enclosed in a subgroup, which you can access if you disclose the
contents of the Web Components group in the Groups & Files list in Project
Builder's main window.

- `MenuHeader.wo` is a
  reusable component that contains the header with the control buttons on the left
  side of each page (or the top of the page in the Basic look.) You can add text or
  other elements to this component if you choose.
- `Main.wo` is the main component, representing the login page of
  the application.
- `PageWrapper.wo` is a reusable
  component that wraps the content of the pages of the application (except for
  `Main.wo`). It contains a header, the menu header component
  (`MenuHeader.wo`), and footer text and elements common to these pages.
  If you want to customize the headers and footers for all pages of your
  application, you can add text or other elements to this component.

You can add code to the `.java` files
corresponding to each component to extend their functionality. See "Modifying
Your Application's Code" (page 130) for more information on the Direct to Web
API.

Each of the subgroups that contains a
component also holds the component's `.api` file. This file specifies
the exported keys, both optional and required, for each the component.

As you run your application, Direct to Web creates
additional pages, using information in your model file and the settings specified
in the WebAssistant. These pages do not show up as components in your project.
Rather, Direct to Web creates them dynamically using a set of reusable components
in the Direct to Web framework. However, you can generate components or user
templates. When you do that, you can modify the resulting components just as you
would with any other WebObjects components. See ["Generating
Components"](Generating_Components.md#apple-ijbusssjjfcek) and ["User
Templates"](User_Templates.md#apple-ijbusrsejjaue) for more information.

The
Resources group contains the model file you specified when you created the
project (in this example, `Movies.eomodeld`). It also contains
`user.d2wmodel`, which stores the preferences you have specified using
the WebAssistant. Advanced users can edit this file; see ["The Rule System"](The_Rule_System.md#apple-ijauurcbifbeu) for
more information about the rule file.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Creating_a__Web_Project.md)[!](Using_Your__Application.md)

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
