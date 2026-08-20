---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/SettingUp/Convert.htm
archived_at: '2026-07-15T07:57:37.024906Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](SetUpTOC.md) [!Previous Section](Install.md)

# Converting Old Projects

Under version 3.5 of WebObjects, projects are organized differently than under previous versions. This section describes how to convert your old projects to the new organization so that you can work with them in WebObjects 3.5 and beyond.
If your existing project is already a WebObjectsApplication project (that is, it was created by Project Builder and has a __PB.project__ file), you can use Project Builder to convert your project. If your project does not have a __PB.project__ file, you must create a new project and add your existing files to the appropriate suitcases.
In version 3.5, the __.woa__ extension is reserved for the application wrapper. Previously, the project directory itself had the __.woa__ extension. Before converting your project, you should rename its folder to remove the __.woa__ extension.

## Performing the Conversion

To convert your project, open it in Project Builder. (It's a good idea to create a backup of your project before converting.) If your project was created prior to WebObjects 3.5, Project Builder detects that a conversion needs to be done. It reassigns the files in your project to new suitcases, as appropriate. It uses the file extension to determine what action to take; if there are files whose extensions it doesn't recognize, it reports these at the end of the conversion, and you must manually assign those files to the appropriate suitcases.
The following list summarizes the conversions that take place:

- Components (with a __.wo__ extension) are added to the Web Components suitcase. __Note:__ Only components found in the top level of the project and each subproject are moved automatically.
- Java code (__.java__) files are moved from the components into the Classes suitcase and stored at the top level of the project on disk. __Note:__ Keep in mind that this may affect your source/revision control system.

In addition, you are asked if you want to add two optional subprojects (ClientSideJava and CommonJava) to your project. You can use these to divide your Java code into client-side, server-side or common Java. See ["Subprojects"](Subproj.md#apple-gyydeoi) for more information.

- Resources (previously in the Other Resources suitcase) are put into two new suitcases. Images with known extensions are assigned to the Web Server Resources suitcase. Other resources are assigned to the Resources suitcase. Files with unrecognized extensions are left out and you are notified.
- __WOProject.plist__ is no longer used and is deleted if it is in the project.
- Several new makefile variables have been added and are appended to your existing __Makefile.preamble__ with default values assigned.
- All existing subprojects are recursively converted in the same manner as the top-level project.

In the conversion process, you are prompted to confirm each type of operation. In general, you should accept the default action for each prompt; otherwise, you will have to perform the action manually.
Once the conversion has begun, there is no way to cancel it. If you choose not to convert at all, you may not be able to view some of your files, since they are assigned to suitcases that aren't visible.

## Moving Your Images

After the project is converted, there are additional changes you may want to make in order to take advantage of the new features of WebObjects 3.5. In previous versions, images were stored inside the components themselves. To support the new "split installation" procedure, images should be stored in the Web Server Resources suitcase, so that the web server can access them at run time. (When you build your project, the items in this suitcase are copied to the __WebServerResources__ directory inside the application wrapper.)
When using the dynamic elements WOImage and WOActiveImage, you use their __filename__ attribute to reference images inside the __WebServerResources__ directory. You may also have images in a framework that can be shared by multiple applications. To access these images, use the __framework__ attribute to specify the framework name. See ["Working With Dynamic Elements"](../DynamicElements/DynElTOC.md#apple-gqytc) in this document and the [_Dynamic Elements Reference_](../../Reference/DynamicElements/DynamicElementsTOC.md)for more information.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
