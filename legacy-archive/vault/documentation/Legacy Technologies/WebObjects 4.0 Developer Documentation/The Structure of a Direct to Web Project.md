---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/DirectToWeb3.html
archived_at: '2026-07-18T01:24:57.620442Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](DirectToWeb2.md)

# The Structure of a Direct to Web Project

A Direct to Web project has a structure similar to other WebObjects application projects. A newly created project contains two components:

!

- __Main.wo__ is the main component, representing the login page of the application.
- __PageWrapper.wo__ is a reusable component that wraps the content of the pages of the application (except for __Main.wo__). It contains the header and footer text and elements common to these pages. The header, by default, consists of control buttons that are displayed at the top of each page (or the left side of the page in the WebObjects look). If you choose, you can add text or other elements to the header and footer areas of __PageWrapper.wo__.

As you run your application, Direct to Web creates additional pages, using information in your model file and the settings specified in the WebAssistant. These pages do not show up as components in your project. Rather, Direct to Web creates them dynamically using a set of reusable components in the Direct to Web framework. However, you can save any page as a component. When you do that, you are then able to modify the component just as you would with any other WebObjects component. See ["Generating Components"](Generating%20Components.md#apple-gezdanjw) for more information.

In your project's Classes suitcase, you'll see a Java file for each of the components, as well as the Session and Application objects. You can add code to any of these files to extend their functionality. See ["Modifying Your Application's Code"](Modifying%20Your%20Application%27s%20Code.md#apple-haytioa) for more information on the Direct to Web API.

!

The Resources suitcase contains the model file you specified when you created the project (in this example, __Movies.eomodeld__). It also contains __user.d2wmodel__, which stores the preferences you have specified using the WebAssistant (you should never need to edit this file directly). The Resources suitcase also holds files specifying the exported keys, both optional and required, for each type of component used in the application; these files have an extension of __.api__.

!

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Using%20Your%20Direct%20to%20Web%20Application.md)
