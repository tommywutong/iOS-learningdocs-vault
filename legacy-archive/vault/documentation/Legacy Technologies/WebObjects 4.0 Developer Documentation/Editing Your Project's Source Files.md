---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/WOTools/SettingUp12.html
archived_at: '2026-07-18T01:27:33.539435Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Tools and Techniques](WebObjects%20Tools%20and%20Techniques.md)

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Previous Section](SettingUp11.md)

# Editing Your Project's Source Files

Every component in your project has a code file whose name is the name of the component followed by the appropriate extension (__.java__ for Java, __.m__ for Objective-C, and __.wos__ for WebScript). Your project may use different languages for different components.
Each component's code specifies the component's behavior. Each component is actually a subclass of WOComponent. This class has standard methods (such as __awake__ and __init__) that you may want to override (see [_WebObjects Developer's Guide_](The%20WebObjects%20Developer%27s%20Guide.md) for more information on these methods). You can also write your own methods and bind them to dynamic elements in your component (see ["Working With Dynamic Elements"](Working%20With%20Dynamic%20Elements.md#apple-gqytc), as well as the [_Dynamic Elements Reference_](Dynamic%20Element%20Specifications.md), for information on binding dynamic elements).

In addition to the component's code, each project has an _application code file_ (__Application.java__, __Application.m__, or __Application.wos__) and a _session code file_ (__Session.java__, __Session.m__, or __Session.wos__). These files implement your applications custom subclasses of WOApplication and WOSession.
When you first create your project using the Wizard, you specify the language you want to use (see ["Choosing the Programming Language"](SettingUp4.md#apple-he2tsna)). This language applies to the application and session code, as well as to the code for your initial component, Main. Other components may be written in different languages.

Regardless of the language you select, all source code for classes appear in the Classes suitcase. On disk, they are located at the top level of the project directory.

!

To save changes in your code, choose File !Save.
__Note:__ WebObjects Builder gets information from Project Builder about variables and methods in your code. If you add or delete a variable or method, WebObjects Builder doesn't get the updated information until you save the file.

[!Table of Contents](WebObjects%20Tools%20and%20Techniques.md) [!Next Section](Editing%20Your%20Component%27s%20HTML%20and%20Declarations%20Files.md)
