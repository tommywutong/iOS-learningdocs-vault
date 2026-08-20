---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/WidgetProjects/WidgetProjects.html
archived_at: '2026-07-15T05:17:47.051813Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md)[Previous](Dual-Product%20Web%20Application%20Tutorial.md)

# Starting a Project

When you start a new project, you base it on a Dashcode template or, in the case of Dashboard widgets, you can also base it on an existing widget. A project encapsulates all the files and resources that Dashcode uses to build a widget or web application for you.

This chapter discusses the options you have when you start a project. It also discusses opening a Dashboard widget in Dashcode, a feature that allows you to forgo Dashcode’s design tools to code, test, and debug an existing widget.

Dashcode creates new projects based on templates. Templates are preconfigured widgets or web applications that include code and graphics that perform common tasks. When you open Dashcode or choose File > New Project after you open it, a dialog appears that offers you a choice of project types. When you choose one of these, the dialog offers you a choice of templates appropriate for the project type. Click a template icon to see a short description of the template’s abilities. If the template matches the task you’re trying to perform, select its icon and click Choose. For more on the templates included with Dashcode, read [Dashcode Templates](Dashcode%20Templates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjvfvjvomi).

In Dashcode version 3.0 and later, you can choose to create a Safari web application or a mobile Safari web application or both. By default, Dashcode creates a single project that produces both products. This allows you to use the same data and much of the same code, but design a different user interface for each product. If you want to create only one type of web application in a project, make sure you deselect the “Develop for:” checkbox for the type of product that you don’t want to develop. The “Develop for:” checkboxes appear between the template icons and their descriptions.

After you choose a template, you may need to provide required values for the widget or web application to work properly. For widgets in particular, make sure to provide the Identity and Properties values, as discussed in [Providing Attributes for a Dashboard Widget](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknlte).

Dashcode can create a new project from an existing widget. If you want to continue work on an existing widget in Dashcode, you should import it. Importing a widget copies it into a new widget project and enables the code generator. When the code generator is active, all of Dashcode’s design and management tools are enabled.

To import a widget, choose File > Import Widget or choose Import from the template chooser dialog.

Once you import your widget into a Dashcode project, use the widget attributes pane, as discussed in [Providing Attributes for a Dashboard Widget](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknlte), to edit your widget’s Identity values.

Each widget project has required values you need to provide for the widget to work properly. You set these values in the widget attributes pane, available when you select Widget Attributes in the navigator. Make sure to provide values in the following sections of the editor, if available:

**_Identity_**
: The values in this section are used to identify a widget.

You need to provide a widget identifier, used by Dashboard to differentiate your widget from others. Widget identifiers are commonly formatted in reverse domain notation, starting with a top-level domain (such as `com`), followed by a company or creator name (such as `apple`), and then a unique product name (such as `my-fabulous-widget`, yielding a name such as `com.apple.my-fabulous-widget`).

Additionally, you need to provide a unique version number. This number is used by Dashboard to differentiate between versions of a widget, so that it’s always running the most recent version.

__Note:__ The widget identifier and version fields correspond to the `CFBundleIdentifier` and `CFBundleVersion` information property list values, as discussed in [Dashboard Info.plist Keys](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/Dashboard_Ref/DashboardPlist/DashboardPlist.html#//apple_ref/doc/uid/TP40001339-CH205).

**_Properties_**
: Template-specific options are in this section. If you’re using an imported or opened widget or the Custom template, this section is absent. For each template’s specific properties, read [Dashcode Templates](Dashcode%20Templates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjvfvjvomi).

Each web application project has values you need to provide for the products to work properly. You set these values in the application attributes pane, available when you select Application Attributes in the navigator. Although only the page title is required, it’s a good idea to set the other values so your web application behaves as you intend.

Some templates include a Properties section in the application attributes pane, in which you set template-specific options. For more information about the options you can set for a template, see the template descriptions in [Web Application Templates](Dashcode%20Templates.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqmjvfvjvomjv).

In Dashcode version 3.0 and later, some application attributes are different, depending on whether you’re developing a Safari web application or a mobile Safari web application. If you’re developing both types of web application, you see a product bar below the toolbar that contains a Safari button and a Mobile Safari button. Click these buttons to switch between the attributes you need to set for each product. If you’re developing only one type of web application (or if you’re using an earlier version of Dashcode to develop a mobile Safari web application), you do not need to switch between attributes for different products, so you do not see the product bar.

To set the application attributes for the Safari web application product of your dual-product project in Dashcode version 3.0 and later, be sure to select the Safari button in the product bar. If you’re using Dashcode version 3.0 and later to develop a Safari web application only, you do not need to do this. If you’re using an earlier version of Dashcode to develop a mobile Safari web application, see [Application Attributes for Mobile Safari Web Applications](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnbnknlts) for information about the attributes you can set.

Provide values in the following section of the application attributes pane:

**_General_**
: The Page Title value in this section is used to identify the Safari web application. In the Page Title field, title your web application by giving it an appropriate, human-readable name. The title you supply is the `<title>` element in your webpage and is displayed in the title bar of the browser.

The Offline Viewing value in this section controls whether users can still use your web application if they lose their network connection. If you select this checkbox, be sure to read [Supporting Offline Usage of a Web Application](Adding%20Source%20Code%20and%20Creating%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnznknltcny) to find out what you need to do to handle offline viewing of your web application.

To set application attributes for the mobile Safari web application product of your dual-product project in Dashcode version 3.0 and later, be sure to select the Mobile Safari button in the product bar. If you’re using Dashcode version 3.0 and later to develop a mobile Safari web application only (or if you’re using an earlier version of Dashcode), you do not need to do this.

Provide values in the following sections of the application attributes pane, if available:

**_General_**
: The Page Title value in this section is used to identify the mobile Safari web application. In the Page Title field, title your web application by giving it an appropriate, human-readable name. The title you supply is the `<title>` element in your webpage and is displayed in the title bar of Safari on iPhone.

**_Viewport_**
: The values in this section control how users can view your mobile Safari web application when they use it on iPhone or iPod touch. When users change the device orientation from portrait to landscape, webpages can get scaled to fit the new screen orientation.

The two options for the Orientation value are:

- “Adjust page width to fit.” When you choose this option, your web application resizes (that is, increases or decreases in width) when the device orientation changes. This option is generally recommended for mobile Safari web applications, because it enhances the user’s perception of the web application as a standalone application and not a webpage.
- "Zoom page to fit.” When you choose this option, the width of your mobile Safari web application does not change when the device orientation changes, but the scale does. In other words, the content of your web application will appear a bit bigger. You might want to choose this option if your web application has a complicated layout that you don’t want to change in width when the device orientation changes.

The Page Zooming value in this section controls whether users can zoom your web application when they view it on iPhone or iPod touch. In general, because you want iPhone and iPod touch users to view your web application as a standalone application and not as a webpage, it’s recommended that you turn off Page Zooming (that is, deselect “Allow users to adjust page zoom”).

**_Web Clip_**
: The values in this section control how your web application can be displayed on iPhone and iPod touch and how your Web Clip icon is created and displayed.

In iOS 2.0 and later you can choose to make your mobile Safari web application available in a full-screen mode, which hides the Safari toolbar and navigation bar. If you want to do this, you must also provide a Web Clip icon, because tapping a Web Clip icon is the only way users can open a web application in full-screen mode (navigating to the application in Safari on iPhone does not open it in full-screen mode). If you choose not to support full-screen mode, you should still consider providing a Web Clip icon so users have a convenient way to open your web application.

To make your mobile Safari web application available in full-screen mode, select the “Show as full screen application (hide Safari toolbar and navigation bar)” checkbox. This allows users to open your web application in full-screen mode when they tap the Web Clip icon. Note that users press the Home button to leave a web application that is running in full-screen mode.

If you selected the “Show as full screen application (hide Safari toolbar and navigation bar)” checkbox, you can also specify one of the following three styles for the status bar:

- Gray
- Black
- Black (Translucent)

Use the pop-up menu to choose the status bar style that best coordinates with the appearance of your web application. You can specify a status bar style only if you selected the “Show as full screen application (hide Safari toolbar and navigation bar)” checkbox. This is because the status bar appearance automatically matches the appearance of the Safari navigation bar when it is visible.

The two options for the Icon value are:

- "Use custom icon.” Choose this option if you want to design your own Web Clip icon to represent your mobile Safari web application. See [Designing a Web Clip Icon for an iPhone Web Application](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojsfvbuqnjnknltk) for more information on how to do this.

  If you choose this option, you can also specify whether you want the shiny glass overlay effect to be added automatically by selecting the “Add glass visual effect” checkbox. Note that you do not have control over a Web Clip icon’s rounded corners and drop shadow; these are always added automatically.
- "Use Safari generated icon.” Choose this option if you want to allow users to create their own Web Clip icon to represent your mobile Safari web application.

If you want to forgo Dashcode’s project management and design tools, you can open an existing widget in Dashcode without importing it into a new project. When Dashcode opens a widget, you have access to its code and all of Dashcode’s debugging tools, but not its design tools.

To open a widget in Dashcode, choose File > Open and select a widget in the Open dialog, or choose File > New Project and click the Open Existing button at the bottom of the template chooser dialog. When you open a widget with Dashcode, the canvas is locked. This means that Dashcode’s design tools, responsible for generating HTML, CSS, and images for a widget, are turned off. When you open an existing widget instead of importing it into a new project, Dashcode displays a lock over the bottom of the canvas.

[Next](Designing%20the%20User%20Interface%20of%20a%20Widget%20or%20Web%20Application.md)[Previous](Dual-Product%20Web%20Application%20Tutorial.md)

