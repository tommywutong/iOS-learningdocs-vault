---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeployingWebObjects/Deploying-25.html
archived_at: '2026-07-15T08:04:47.506255Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Deploying WebObjects Applications

[!](Deploying%20With%20Monitor.md) [!](Adding%20a%20Host%20to%20Monitor.md) [!](Creating%20Application%20Instances.md)

---

# Adding and Configuring an Application

To add a new application to Monitor, click the Applications button in the banner. This brings you to the Applications page, which lists all currently-configured applications. In the Add Application text field, enter the name of a new application; this should be the same name as the application project, which is the wrapper name minus the __.woa__
. For the ThinkMovies example application, the entered string would be "ThinkMovies".

When you enter the name of your application and click the Add Application button, Monitor displays the Application Configuration page:

!

Enter the full path to the WebObjects application executable in the Path field, or use the Path Wizard to select the application's executable file (the Path Wizard allows you to browse the filesystem of any configured host computer and select the application's executable). For ThinkMovies you might enter a string similar to the following example:

`/WebObjects/ThinkMovies/ThinkMovies.woa/ThinkMovies.exe`

Be sure that the path specifies the built WebObjects application's executable, including the __.exe__
extension if on Windows NT. You cannot start an instance of an application when the wrong path is specified; Monitor will display "Launch error - path invalid" if you attempt to start such an instance. Click the Update for New Instances button on the bottom of the form to save your changes.

The other fields on this form accept arguments to use when the application instance is run. For descriptions of these fields and as well as the checkboxes and the Update for New and Existing Instances button, see [Setting Command-Line Arguments in Monitor](Setting%20Command-Line%20Arguments%20in%20Monitor.md#apple-gqydsmrz) and [Monitor Option Summary](Monitor%20Option%20Summary.md#apple-ge4tenrs).

---

© 1999 Apple Computer, Inc. – (Last Updated 25 August 99)

[!](Deploying%20With%20Monitor.md) [!](Adding%20a%20Host%20to%20Monitor.md) [!](Creating%20Application%20Instances.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
