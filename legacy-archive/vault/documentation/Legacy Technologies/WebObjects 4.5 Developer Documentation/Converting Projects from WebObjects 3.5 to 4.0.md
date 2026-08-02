---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/PostInstall/PostInstall.3e.html
archived_at: '2026-07-15T08:09:40.408972Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Post Install Guide

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Converting%20Direct%20To%20Web%20Projects.md) [!](Converting%20Java%20Code%20From%20WebObjects%203.5.md)

---

#   Converting Projects from WebObjects 3.5 to 4.0

Prior to conversion, make sure you have the latest patches for WebObjects 4.0. Check the Tech Info Library at http://til.info.apple.com/techinfo.nsf/artnum/n70037 for the most up-to-date list. In particular, on Windows NT systems make sure you've obtained and installed the NSTimeZone bug workaround.

To convert a project to WebObjects 4 from an earlier version of WebObjects, do the following:

1. 

   Make a backup copy of your application, and save that backup copy somewhere other than in the base directory.
2. 

   Convert your project's makefiles as described in the document _$NEXT_ROOT_

   /Developer/Makefiles/Conversion/DirectoryLayout/ConvertMakefilesReadMe.rtf.

   (_$NEXT_ROOT_
   is the root installation directory specified when WebObjects was installed.) The project files must change to point to new locations for the build tools.
   ConvertMakefilesReadMe.rtf
   tells you how to make those changes.
3. 

   If your project contains Java code files, convert them as described in [Converting Java Code From WebObjects 3.5](Converting%20Java%20Code%20From%20WebObjects%203.5.md#apple-gm3dknrz)
   .

   The Java APIs changed considerably between WebObjects 3.5 and 4. If you've written Java code, you must convert it before you can compile.
4. 

   Open your project in Project Builder, and click "Upgrade Now" when prompted.

   Among other things, upgrading your project in this fashion will:

   - Upgrade your
   PB.project
   file to the latest version.

   - Upgrade your makefiles to the latest versions.

   - Convert your WebObject project suitcases to the new format.

   - Convert your project so that it conforms to the WebObjects 4 localization scheme. As a result of this, script (.wos) and .api files are moved outside of their component (.wo) directories. Script files now appear in the Classes suitcase.
5. 

   Build. If errors occur during the build, fix them and re-build the project.

   The WebObjects Framework contains many optimizations that should greatly improve your application's performance. However, you may find your code relied on some part of the request-response loop or template parsing code that is no longer always performed.
6. 

   Run the project. If your application doesn't run as expected, see the following sections:

   -

   [Troubleshooting WebObjects 4 Template Parsing](Troubleshooting%20WebObjects%204%20Template%20Parsing.md#apple-gizdmnzy)

   -

   [Troubleshooting WebObjects 4 Request Handling](Troubleshooting%20WebObjects%204%20Request%20Handling.md#apple-gm4tonjz)

   -

   [WebScript Changes](WebScript%20Changes.md#apple-gqzdmnzr)

   Also check the _What's New in WebObjects_
   document for a list of differences between the current release and the previous one.
7. 

   At this stage, if you want, you can remove all usage of deprecated API. WebObjects has been rewritten to be thread-safe, which required deprecating some of the existing APIs. You can still use deprecated API as long as you do not enable multithreading in your application. You'll receive warnings about deprecated API at run-time. For a complete list of what's deprecated, see the "Deprecated API" file that's included as part of each framework's reference documentation.
8. 

   Make the following changes as appropriate for your system:

   -

   Convert dynamic elements to use
   escapeHTML
   and
   displayString
   (WOBrowser, WOPopUpButton, WOCheckBoxList, WONestedList).

   -

   Replace EOFetchSpecification hints with the appropriate new methods (see the EOFetchSpecification class reference).

Changes in both WebObjects template parsing and request handling may require you to make additional, manual adjustments to your WebObjects 3.5 applications. Refer to [Troubleshooting WebObjects 4 Template Parsing](Troubleshooting%20WebObjects%204%20Template%20Parsing.md#apple-gizdmnzy)
and [Troubleshooting WebObjects 4 Request Handling](Troubleshooting%20WebObjects%204%20Request%20Handling.md#apple-gm4tonjz)
for details.

---

© 1999 Apple Computer, Inc. – (Last Updated 19 Oct 99)

[!](Converting%20Projects%20From%20Earlier%20Releases.md) [!](Converting%20Direct%20To%20Web%20Projects.md) [!](Converting%20Java%20Code%20From%20WebObjects%203.5.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
