---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/WalkThrough/User_Templates.html
archived_at: '2026-07-15T08:12:31.618987Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Generating_Components.md)[![Next](attachments/DirectToWeb/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/index.html)

## User Templates

Sometimes you need to change the appearance of a Direct to
Web page without freezing the component. You might want to change
all of the pages for a particular task (list pages for example)
without freezing components for every entity. Or you might want
to use the Web Assistant to fine-tune pages having your custom appearance.

Direct to Web allows you to generate, modify, and use templates.
Templates are WebObjects components that Direct to Web can use to
generate pages (list pages for example) for any entity. Direct to
Web provides a number of prebuilt templates from which you generate _user
templates_. User templates appear together with the prebuilt templates
in the Web Assistant and you can apply them to pages in your project.

These are the advantages of using templates:

- You can use
  a template for any entity.
- You can modify the properties and page appearance with the
  Web Assistant.
- Since the template is a WebObjects component, you have control
  over its visual appearance. You can add any static or dynamic HTML
  elements you like, using a tool such as WebObjects Builder.
- You can add functionality to the template by editing the component's
  Java code, as well as by editing the bindings of the component's
  dynamic elements.

Templates are slower than frozen components since Direct to
Web generates the pages that the user sees in the browser.

### Generating a Template

Follow these steps to generate a template:

1. Click Expert
   Mode at the bottom of the Web Assistant window to enter Expert mode.
2. Click the Generation tab at the top of the WebAssistant.
   ![[image: ../Art/wageneratetemplate.gif]](../Art/wageneratetemplate.gif)
3. Select the task corresponding to the page you want to generate.
4. Select "\*all\*" in the Entities pop-up list.

   You must
   select "\*all\*" for the entities because the template is independent
   of the entity. You cannot select "\*all\*" for the task to generate
   multiple templates. You must generate the templates one at a time.
5. Make sure the "Use DirectToWeb or User Template" radio
   button is selected.
6. Click Generate Template.

   The Generate Template window
   appears. It contains a text field with a default name for your template.
   You can edit the name if you choose.
7. Click the Ok button.

   Direct to Web copies a component
   (with extension `.wo`)
   and a corresponding `.java` file from
   a predefined template and adds them to your project. You may have
   to wait a few moments for this process to complete. Your settings
   are automatically saved.
8. Rebuild and run your project, and restart the WebAssistant.

After you generate the template and rebuild your project,
you can use the Web Assistant to apply the template to a Direct
to Web page. See ["Customizing Pages"](Customizing_Pages.md#apple-ijbusrscizdei).

[![Previous](attachments/DirectToWeb/Images/previous.gif)](Generating_Components.md)[![Next](attachments/DirectToWeb/Images/next.gif)](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/DirectToWeb/Architecture/index.html)

© 2001 Apple Computer, Inc.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
