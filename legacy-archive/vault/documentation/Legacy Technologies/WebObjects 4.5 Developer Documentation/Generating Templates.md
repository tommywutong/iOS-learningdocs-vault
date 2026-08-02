---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.72.html
archived_at: '2026-07-15T08:11:26.235403Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](User%20Templates.md) [!](User%20Templates.md)

---

#  Generating Templates

To generate a template:

1. 

   Click the Expert Mode button at the bottom of the Web Assistant to enter Expert mode.
2. 

   Click the Generate tab at the top of the Web Assistant.
   
   !
3. 

   Select the task corresponding to the page you want to generate. In the Select "\*all\*" in the Entities pop-up list.

   You must select "\*all\*" for the entities because the template is independent of the entity. You cannot select "\*all\*" for the task to generate multiple templates. You must generate the templates one at a time.
4. 

   Make sure the "Use DirectToWeb or User Template" radio button is selected.
5. 

   Click Generate Template.

   The Generate Template window appears. It contains a text field with a default name for your template. You can edit the name if you choose.
   
   !
6. 

   Click the Ok button.

   Direct to Web copies a component (with extension __.wo__
   ) and a corresponding __.java__
   file from a predefined template and adds them to your project. You may have to wait a few moments for this process to complete. Your settings are automatically saved.
7. 

   Rebuild your project.

After you generate the template and rebuild your project, you can use the Web Assistant to apply the template to a Direct to Web page. See [Customizing Pages](Customizing%20Pages.md#apple-gqytgoju)
.

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](User%20Templates.md) [!](User%20Templates.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
