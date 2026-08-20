---
title: Dashcode User Guide
apple_id: TP40004692
resource_type: Guide
platform: Safari|Xcode Developer Tools
topic: Xcode
technology: null
published: '2012-02-16'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashcode_UserGuide/Contents/Resources/en.lproj/Advanced/Advanced.html
archived_at: '2026-07-15T05:17:34.822417Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashcode User Guide](Introduction%20to%20Dashcode%20User%20Guide.md)


[Next](Dashcode%20Templates.md)[Previous](Testing%20and%20Sharing.md)

# Advanced Topics for Widgets

In addition to the core tasks of designing, coding, and testing a widget, Dashcode offers additional, advanced features that help you develop a widget that fits your users’ needs. This chapter covers localization techniques and how to include a plug-in written in Objective-C.

You supply localized strings for your widget in the Localization section of the widget attributes pane. To show the widget attributes pane, click Widget Attributes in the navigator.

To localize your widget for other languages, click the plus (+) button and choose the language. Next to the language name in the first table, you provide a localized name for your widget. This name is used for your widget in the Finder and in the widget bar in Dashboard.

The table on the right shows all the strings used in your widget. In this table, you double-click a term in the Value column and provide localized versions of your widget’s strings. You add key-value combinations for localization by clicking the plus button, providing a unique key name, and entering the localized version of the string next to its key.

When you add a language for localization, a language project folder is added to the widget. In addition to the strings, you can place any localized resources, such as style sheets or images, in a language project folder. To show the language project folder, choose View > Files and look for the folders that end with the `.lproj` extension. For more information on widget localization, read [Localizing Widgets](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/Localization.html#//apple_ref/doc/uid/TP40003047) in _[Dashboard Programming Topics](../Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_.

To make it easy to test your widget’s localization, choose View > Customize Toolbar. In the dialog, drag the Language pop-up menu to the project window’s toolbar, then click Done. Now you can choose a language from the Language pop-up menu to see your widget in that language. If you click Run in the toolbar, your widget runs in the selected language.

Dashcode offers a place to associate a widget plug-in with your widget. If you’ve built a custom widget plug-in with Xcode and want to include it with your widget, select Widget Attributes from the navigator and, in the Widget Plugin section, click the Choose button and select a built widget plug-in.

For more information about widget plug-ins, read [Creating a Widget Plug-in](https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/WidgetPlugin.html#//apple_ref/doc/uid/TP40003051) in _[Dashboard Programming Topics](../Dashboard%20Programming%20Topics/Introduction%20to%20Dashboard%20Programming%20Topics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmzx)_.

[Next](Dashcode%20Templates.md)[Previous](Testing%20and%20Sharing.md)

