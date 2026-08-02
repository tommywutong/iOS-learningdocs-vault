---
title: Dashboard Programming Topics
apple_id: TP40002837
resource_type: Guide
platform: Safari|macOS
topic: Networking, Internet, & Web
technology: null
published: '2010-02-01'
source_url: https://developer.apple.com/library/archive/documentation/AppleApplications/Conceptual/Dashboard_ProgTopics/Articles/AccessKeys.html
archived_at: '2026-07-15T05:17:17.433054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Dashboard Programming Topics](Introduction%20to%20Dashboard%20Programming%20Topics.md)


[Next](Accessing%20External%20Resources.md)[Previous](Localizing%20Widgets.md)

# Specifying Access Keys

If your widget needs resources that extend beyond your widget's bundle or HTML, CSS, and JavaScript technologies, you need to take Dashboard's Info.plist Access keys into account.

Dashboard allows you to "declare your intentions" when you:

- Access files outside of your widget bundle
- Use a WebKit or standard browser plug-in
- Access network resources
- Run a Java applet
- Run a command-line utility
- Use a widget plug-in

"Declaring your intentions" means that before your widget is run, you specify in your widget’s information property list file which resources you want to use. The keys and their meaning are listed in [Table 17](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztanbyfvjvomi):

__Table 17__  Info.plist Keys for the Widget resource access

| Key | Type | Definition | Example |
| `AllowFileAccessOutsideOfWidget` | Boolean | Access to files across the file system; limited by the user’s permissions. | `<img src="~/Sites/images/macosxlogo.png">` |
| `AllowFullAccess` | Boolean | Access to the file system, WebKit and standard browser plug-ins, Java applets, network resources, and command-line utilities. | N/A |
| `AllowInternetPlugins` | Boolean | Access to WebKit and standard browser plug-ins, such as QuickTime. | `<embed src="http://www.foo.com/bar.mov" type="video/quicktime" width="320" height="256"></embed>` |
| `AllowJava` | Boolean | Access to Java applets. | `<applet code="foo.class" width="320" height="256"></applet>` |
| `AllowNetworkAccess` | Boolean | Access to any resources that are not file-based, including those acquired through the network. | `<img src="http://www.foo.com/bar.png">` |
| `AllowSystem` | Boolean | Access to command-line utilities using the widget script object. | `var s = widget.system("/usr/bin/foo", null);` |
| `Plugin` | String | Specifies a widget plug-in. | `foo.widgetplugin` |

If you attempt to use any of these resources without first specifying them in your widget’s information property list file, your attempt fails.

[Next](Accessing%20External%20Resources.md)[Previous](Localizing%20Widgets.md)

