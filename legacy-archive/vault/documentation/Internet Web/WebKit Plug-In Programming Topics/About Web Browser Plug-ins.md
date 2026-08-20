---
title: WebKit Plug-In Programming Topics
apple_id: TP40001521
resource_type: Guide
platform: macOS
topic: Networking, Internet, & Web
technology: WebKit
published: '2011-05-17'
source_url: https://developer.apple.com/library/archive/documentation/InternetWeb/Conceptual/WebKit_PluginProgTopic/Concepts/AboutPlugins.html
archived_at: '2026-07-15T07:44:14.152987Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebKit Plug-In Programming Topics](Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md)


[Next](Creating%20Plug-ins%20with%20the%20Netscape%20API.md)[Previous](Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md)

# About Web Browser Plug-ins

Web browser plug-ins are considered extensions to existing web browsers. By installing them locally on your machine, you can “teach” your web browsers to support alternative content types—perhaps even custom types you design yourself—or to perform additional tasks that a ready-made browser cannot do.

The WebKit framework natively supports the Netscape-style plug-in API, which is based off a common cross-platform API. This API is described futher in [Creating Plug-ins with the Netscape API](Creating%20Plug-ins%20with%20the%20Netscape%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgi2talkciffeosskifea).

Plug-ins can be stored in one of two places on an OS X system:

- Plug-ins stored in `/Library/Internet Plug-ins` can be shared by all users on the computer.
- Plug-ins stored in `~/Library/Internet Plug-ins` will be available only to the user whose home directory contains them.

In addition, the WebKit-based plug-ins can be stored inside the bundle of _any_ application that uses the WebKit, by storing it in:

```
    AppName/Contents/Plug-ins
```

where `AppName` is the actual application’s executable bundle.

Plug-ins are generally reloaded on each application start.

Content that your plug-ins will view needs to be embedded within HTML. Most browsers do this with an `EMBED` tag, but others require the `OBJECT` tag. For maximum compatibility, you can tune your page to support both. The example in Listing 1 is specific to the QuickTime plug-in provided by Apple, and you can tune these parameters to your own mode of business.

__Listing 1__  Embedding a movie into an HTML page

```
<OBJECT CLASSID="clsid:02BF25D5-8C17-4B23-BC80-D3488ABDDC6B"
 WIDTH="160"
 HEIGHT="144"
 CODEBASE="http://www.apple.com/qtactivex/qtplugin.cab">
 <PARAM name="SRC" VALUE="sample.mov">
 <PARAM name="AUTOPLAY" VALUE="true">
 <PARAM name="CONTROLLER" VALUE="false">
<EMBED SRC="sample.mov"
WIDTH="160"
HEIGHT="144"
AUTOPLAY="true"
CONTROLLER="false"
PLUGINSPAGE="http://www.apple.com/quicktime/download/">
 </EMBED>
</OBJECT>
```

The variables for the Active X controls will change based on your plug-in’s behavior. Read Apple’s _[HTML Scripting Guide for QuickTime](../../Quick%20Time/HTML%20Scripting%20Guide%20for%20QuickTime/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytkmrv)_ tutorial for more information.

[Next](Creating%20Plug-ins%20with%20the%20Netscape%20API.md)[Previous](Introduction%20to%20WebKit%20Plug-in%20Programming%20Topics.md)

