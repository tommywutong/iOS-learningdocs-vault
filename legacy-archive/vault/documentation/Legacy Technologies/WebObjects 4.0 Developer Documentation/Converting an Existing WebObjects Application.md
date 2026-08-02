---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/DeltaDoc/NewInWO4.02.html
archived_at: '2026-07-15T07:58:31.310293Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[What's New in WebObjects 4.0](Table%20of%20Contents.md)

[!Table of Contents](Table%20of%20Contents.md) [!Previous Section](Compatibility%20With%20Earlier%20Releases.md)

# Converting an Existing WebObjects Application

To convert a project to WebObjects 4.0, do the following:

- Convert your project's makefiles as described in the document __$___NEXT_ROOT___/Developer/Makefiles/Conversion/DirectoryLayout/ConvertMakefilesReadMe.rtf__.

($NeXT_ROOT is the root installation directory specified when WebObjects was installed.) The project files must change to point to new locations for the build tools. The __ConvertMakefilesReadMe.rtf__ document tells you how to make those changes.

- If your project contains Java code files, convert them as described in [Converting Java Code](NewInWO4.03.md#apple-giytamjx).

__Note:__  The Java APIs have changed considerably. If you've written Java code, you must convert it before you can compile.

- Open your project in Project Builder, and click "Upgrade Now" when prompted.

Among other things, upgrading your project in this fashion will:

- Upgrade your __PB.project__ file to the latest version.
- Upgrade your makefiles to the latest versions.
- Convert your WebObject project suitcases to the new format.
- Convert your project so that it conforms to the new localization scheme. As a result of this, script (__.wos__) and __.api__ files are moved outside of their component (__.wo__) directories. Script files now appear in the Classes suitcase. For more information on the new localization scheme, see the section [Changes to Localization](Changes%20to%20Localization.md#apple-gi4domjv).

- Build. If errors occur during the build, fix them and re-build the project.

The WebObjects Framework contains many new optimizations that should greatly improve your application's performance. However, you may find your code relied on some part of the request-response loop or template parsing code that is no longer always performed.

- Run the project. If your application doesn't run as expected, read the sections [Troubleshooting WebObjects 4.0 Template Parsing](NewInWO4.04.md#apple-giytanbx), [Troubleshooting WebObjects 4.0 Request Handling](NewInWO4.05.md#apple-giytaobr), and [WebScript Changes](NewInWO4.06.md#apple-gm2tmnjr). Among other things, these sections outline the use of WebObjects 3.5 compatibility flags that allow you to revert to the style of template parsing and request handling that was performed in WebObjects 3.5.
- At this stage, if you want, you can remove all usage of deprecated API. WebObjects has been rewritten to be thread-safe, which required deprecating some of the existing APIs. You can still use deprecated API as long as you do not enable multithreading in your application. You'll receive warnings about deprecated API at run-time. For a complete list of what's deprecated, see [Support for Multithreaded Applications](Support%20for%20Multithreaded%20Applications.md#apple-giytknry).

[!Table of Contents](Table%20of%20Contents.md) [!Next Section](NewInWO4.03.md)
