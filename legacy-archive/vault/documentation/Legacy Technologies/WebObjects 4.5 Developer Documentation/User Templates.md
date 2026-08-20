---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.71.html
archived_at: '2026-07-15T08:11:26.215579Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Generating%20Components.md) [!](Generating%20Templates.md)

---

#   User Templates

Sometimes you need to change the appearance of a Direct to Web page without freezing the component. You might want to change all of the pages for a particular task (list pages for example) without freezing components for every entity. Or you might want to use the Web Assistant to fine-tune pages having your custom appearance.

Direct to Web allows you to generate, modify, and use templates. Templates are WebObjects components that Direct to Web can use to generate pages (list pages for example) for any entity. Direct to Web provides a number of prebuilt templates from which you generate _user templates_
. User templates appear together with the prebuilt templates in the Web Assistant and you can apply them to pages in your project.

The advantages of using templates are:

- 

  You can use a template for any entity.
- 

  You can modify the properties and page appearance with the Web Assistant.
- 

  Since the template is a WebObjects component, you have control over its visual appearance. You can add any static or dynamic HTML elements you like, using a tool such as WebObjects Builder.
- 

  You can add functionality to the template by editing the component's Java code, as well as by editing the bindings of the component's dynamic elements.

Templates are slower than frozen components since Direct to Web generates the pages that the user sees in the browser.

#### [Generating Templates](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.72.html#pgfId=14544)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Generating%20Components.md) [!](Generating%20Templates.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
