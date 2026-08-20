---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb1.html
archived_at: '2026-07-18T01:24:06.805532Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](Direct%20To%20Web.md)

# Creating a Direct to Web Project

To create a Direct to Web application, begin by using Project Builder to create a WebObjects application project. Follow these steps:

- Launch Project Builder.
- Choose Project !New.
- In the New Project panel, choose the WebObjectsApplication project type from the pop-up list and specify the project path where you want to save the project.

!

- Click OK.

The first screen of the WebObjects application wizard appears.

!

- Under Available Assistance, select Direct to Web.

You cannot select a language when the type of WebObjects application is Direct to Web;when you create a Direct to Web project, Java is the only available language.

- Click Next.

!

- Choose "Open existing model file."

You can also create a new model file. If you choose "Create new model," you are led through a series of screens that prompt you to create a new model. For more information about creating a new model file, see the chapter "Using EOModeler" in _Enterprise Objects Framework Developer's Guide_.

If the model you add to your project references entities in another model, you must add the other model to your project manually. The wizard doesn't include it automatically.

- Click Browse, then navigate to the model file you want to use and select it.

If you are just exploring Direct to Web, you can use a model file from one the Enterprise Objects example projects, such as __Movies.eomodel__ in the Movies project.

- Click Next.

The next screen offers a selection of user-interface styles ("looks") for your Direct to Web application; see ["The Different Looks for WebObjects Applications"](DirectToWeb2.md#apple-he4tsni) for more information. Click an item in the browser to select a look.

!

- Click Finish to complete the WebObjects application wizard procedure.

You can now launch the Direct to Web application from Project Builder, in the same way you would launch any other project. ["Using Your Direct to Web Application"](Using%20Your%20Direct%20to%20Web%20Application.md#apple-guzdani) tells you how to launch your WebObjects application and describes what you see when you launch it.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](DirectToWeb2.md)
