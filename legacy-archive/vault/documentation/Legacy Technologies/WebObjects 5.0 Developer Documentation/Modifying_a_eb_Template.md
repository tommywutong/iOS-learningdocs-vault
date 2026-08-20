---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Modifying_a_eb_Template.html
archived_at: '2026-07-15T08:12:23.636173Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Creating_a__l_Component.md)[!](Adding_a_Ne_Application.md)

## Modifying a Direct to Web Template

To change the appearance and function of all the pages
Direct to Web generates for a particular task, you need to modify its template.
You can use the Web Assistant to generate the template and WebObjects Builder to
edit it.

To illustrate how to modify a template,
this example shows how to add a hyperlink to the NEUListPage Direct to Web
template. The hyperlink simply redraws the page for now, but in ["Adding a New
Direct to Web Task to Your Application"](Adding_a_Ne_Application.md#apple-ijbusskki5euu) it will be modified to navigate to a
new task page. For this example, it is easiest to start by creating a new
project.

1. Create a Direct to Web application using the
   Movies database. For the look, use the Neutral look. See ["Creating a Direct to Web
   Project"](../WalkThrough/Creating_a__Web_Project.md#apple-ijauessjijeug).
2. Launch your application and run the Web Assistant.
   See ["Using Your Direct to Web
   Application"](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Customizing/Using_Direc_pplications.html#BCIGHACJ) and ["Customizing Your Application
   With the WebAssistant"](../WalkThrough/Customizing_ebAssistant.md#apple-ijbusschjjbeu).
3. Generate a Direct to Web template for
   the list task called "NEUListPage2" using the Web Assistant. ["Generating a
   Template"](../WalkThrough/User_Templates.md#apple-ijauer2jijaug).
4. From Project Builder, double-click
   `NEUListPage2.wo` in the project's Web Components group. This opens
   the Direct to Web template in WebObjects Builder.

   Add a hyperlink after the
   first instance of the metallic Return button. This instance is displayed when the
   list is not empty.

   Add a WOImage inside the hyperlink.

   Bind the
   following attributes to the WOImage:

   __|  |  |
| --- | --- |
| Attribute | Value |__| `filename` | "EditMetalBtn.gif" |
| `framework` | "JavaDirectToWeb" |
| `border` | "0" |

   Add an action called `editList` that returns
   `null`.

   Bind the action to the Edit List hyperlink's
   `action` attribute.
5. Save your template.
6. Build and launch your application. Navigate to a list page. It should now
   appear with an Edit button.

   Since the `editList` action returns
   `null`, the hyperlink just redraws the page. In ["Adding a New
   Direct to Web Task to Your Application"](Adding_a_Ne_Application.md#apple-ijbusskki5euu), you will modify the action to create
   a new task page.

### Freezing Your Modified Direct to Web Template

You can freeze a page based on your
Direct to Web template using the Web Assistant. See ["Generating Components"](Generating_Components.md#apple-ijbusssjjfcek) for
more details. Make sure that your template is selected in the template pop-up
list in the third column of the Web Assistant.

|  |
| --- |
| __Note:__ When you freeze a Direct to Web template, you lose any instance variables and methods you add to it. To avoid an unknown key exception when you display the frozen component, you need to add the same variables and methods to your frozen component. |

In the example above, the
`editList` action is missing from any component created by freezing
the NEUListPage2 template.

Sometimes you add
components to your Direct to Web template that have child components. For
example, tables, WOConditionals, WORepetitions, and any reusable components with
a WOComponentContent dynamic element all have child components. If you add such
components to your Direct to Web template, add an attribute called
`_unroll` and bind it to `YES`. This attribute enables
Direct to Web to include the component's children when you freeze the
template.

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Creating_a__l_Component.md)[!](Adding_a_Ne_Application.md)

© 2001 Apple Computer, Inc.

Shop the [Apple Online Store](http://www.apple.com/store/) (1-800-MY-APPLE), visit an [Apple Retail Store](http://www.apple.com/retail/), or find a [reseller](http://www.apple.com/buy/locator/).

- [Mailing Lists](http://lists.apple.com/)
- [RSS Feeds](https://developer.apple.com/rss/)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
