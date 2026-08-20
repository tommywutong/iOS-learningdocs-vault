---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/WOTools/ToolsTechniques.58.html
archived_at: '2026-07-15T08:11:01.246635Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Tools and Techniques

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Direct%20to%20Web.md) [!](The%20Different%20Looks%20for%20WebObjects%20Applications.md)

---

#  Creating a Direct to Web Project

To create a Direct to Web application, begin by using Project Builder to create a WebObjects application project. Follow these steps:

1. 

   Launch Project Builder.
2. 

   Choose Project !
   New.
3. 

   In the New Project panel, choose the Webobjectsapplication project type from the pop-up list and specify the project path where you want to save the project.
   __Note:__

   On Windows NT, the project type and project path appear on different panels.
   
   !
4. 

   Click OK.

   The first screen of the WebObjects application wizard appears.
   
   !
5. 

   Under Available Assistance, select Direct to Web.

   You cannot select a language when the type of WebObjects application is Direct to Web;
   when you create a Direct to Web project, Java is the only available language.
6. 

   Click Next.
   
   !
7. 

   Choose "Open existing model file."

   You can also create a new model file. If you choose "Create new model," you are led through a series of screens that prompt you to create a new model. For more information about creating a new model file, see the chapter "Using EOModeler" in _Enterprise Objects Framework Developer's Guide_
   .

   If the model you add to your project references entities in another model, you must add the other model to your project manually. The wizard doesn't include it automatically.
8. 

   Click Browse, then navigate to the model file you want to use and select it.

   If you are just exploring Direct to Web, you can use a model file from one the Enterprise Objects example projects, such as __Movies.eomodel__
   in the Movies project. This model is used throughout this document.
9. 

   Click Next.

   The next screen offers a selection of user-interface styles ("looks") for your Direct to Web application; see [The Different Looks for WebObjects Applications](The%20Different%20Looks%20for%20WebObjects%20Applications.md#apple-gm2tcojw)
   for more information. Click an item in the browser to select a look.
   
   !
10. 

    Click Next.

    The next screen asks if you would like to launch your application immediately. If you choose not to have the wizard launch your application, see [Using Your Direct to Web Application](Using%20Your%20Direct%20to%20Web%20Application.md#apple-gm3dqmrs)
    , which tells you how to launch your WebObjects application and describes what you see when you launch it.
    !
11. 

    Click Finish to complete the WebObjects application wizard procedure.

#### [The Different Looks for WebObjects Applications](The%20Different%20Looks%20for%20WebObjects%20Applications.md#apple-obtwmslehu4tsojv)

---

© 1999 Apple Computer, Inc. – (Last Updated July 27 99)

[!](WebObjects%20Tools%20and%20Techniques.md) [!](Direct%20to%20Web.md) [!](The%20Different%20Looks%20for%20WebObjects%20Applications.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
