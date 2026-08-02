---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/WebScript/RoleOfScripts.html
archived_at: '2026-07-15T07:48:04.916710Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](WebScript.mif.book.md)
[!Previous Section](ModernSyntax.md)

# Using WebScript in a WebObjects Application

This section discusses using WebScript in the context of a WebObjects application. For a detailed discussion of the structure of a WebObjects application, see the chapter "Getting Started."

## The Role of Scripts in a WebObjects Application

In developing WebObjects applications, you usually write your business logic as compiled Objective-C code (though you can write entire applications using just WebScript). You then use WebScript to provide your "interface logic." A WebScript script typically includes the following ingredients:

- Variable declarations
- The instantiation of objects that get bound to HTML elements
- Action methods that define a response to user actions
- Logic for performing page navigation

### Component Scripts

Most scripts are for _components_. A component is a page or a identifiable part of a page that can dynamically generate itself and send action messages when users interact with it. A component contains one or more dynamic HTML elements and usually some static HTML elements as well. Components can exist on the server or on the client browser. (See "Java Client-Side Components" for an example of the latter.)

On the server side, components are instances of a WOComponent subclass. (WOComponent is an abstract class that defines the interface and behavior of WOComponent objects.) At run time, WebObjects creates an instance of a special subclass for each component script and dynamically makes the script code the class implementation. Applications can, and often do, have multiple components.

In most cases, a script for a server-side component has a corresponding declarations file and HTML template. The declarations file provides a mapping between the actions and variables defined in the script, and the HTML elements that will be dynamically generated and then substituted in the HTML template.The three files in a group have the same base name but different extensions; for example, __Main.wos__ (script), __Main.wod__ (declarations), and __Main.html__ (template). These application resources are used by the WOComponent object to prepare responses to user requests.

In a WebObjects application you generally put each group of three files (the script, the declaration, and the HTML template) into a directory that has the same base name and the extension __.wo__. So, for example, you can have a directory __Main.wo__ that contains the files __Main.wos__, __Main.wod__, and __Main.html__. The script associated with a component (in this example, __Main.wos__) is called a _component script_.

!

 ____Figure 1.__  The Contents of a Component Directory__

### The Application and Session Scripts

In addition to having one or more components, a WebScript application can also include an _application script_ and a _session script_. The application script is where you declare and initialize application variables, and where you perform tasks that affect the entire application. The session script is where you declare, initialize, and store variables that persist throughout a session; in a session script you also perform tasks that affect the session as a whole. For more information on application, session, and other variables, see the section "[Variables and Scope](VariablesAndScope.md#apple-kjcumojwgazdo).."

The application script has the name __Application.wos__ and the session script is named __Session.wos__. Both files reside immediately under the application (__.woa__) directory. Similar to component scripts, the script code is dynamically made the implementation code of special WOApplication (__Application.wos__) and WOSession (__Session.wos__) subclasses from which instances are generated at run time.

[!Table of Contents](WebScript.mif.book.md)
[!Next Section](VisitorExample.md)
