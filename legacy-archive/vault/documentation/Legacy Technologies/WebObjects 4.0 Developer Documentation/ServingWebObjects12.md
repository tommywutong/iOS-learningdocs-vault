---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjects12.html
archived_at: '2026-07-18T01:23:35.197102Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[Serving WebObjects](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html)

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Previous Section](ServingWebObjects11.md)

## Adding and Configuring an Application

To add a new application to Monitor, click the Application button in the banner. This brings you to the Applications page, which lists all configured applications. In the Add Application text field, enter the name of a new application; this should be the same name as the application project, or the wrapper name minus the __.woa__. For the ElementTour example application, the entered string would be "ElementTour".
When you enter the name of your new application and click the Add Application button, Monitor displays the Application Configuration page:

!

First enter the full path to the WebObjects application in the Path field. For ElementTour running on Windows NT you might enter a string similar to the following example:

```
C:/Apple/Developer/Examples/WebObjects/Java/ElementTour/ElementTour.woa
```


Be sure that the path specifies the built WebObjects application, including the __.woa__ extension. You cannot start an instance of an application when the wrong path is specified, and Monitor will not provide feedback when you attempt to start such an instance. The executable name must be the name of the application-in this case "ElementTour" (or, on Windows NT, "ElementTour.exe"). Click the Update for New Instances button on the bottom of the form to save your changes.
The other fields on this form accept arguments to use when the application instance is run. For descriptions of these fields and as well as the checkboxes and the Update for New and Existing Instances button, see "[Setting Command-Line Arguments in Monitor](ServingWebObjects22.md#apple-gy3tmoa)" .

[!Table of Contents](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/ServingWebObjects/ServingWebObjectsTOC.html) [!Next Section](ServingWebObjects13.md)
