---
title: WebObjects Java Client Programming Guide
apple_id: TP30001017
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/DesktopApplications/DocumentHistory/DocumentHistory.html
archived_at: '2026-07-18T02:17:44.502175Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Java Client Programming Guide](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)


[Next](Controllers%20and%20Actions%20Reference.md)[Previous](Building%20a%20Login%20Window.md)

# Document Revision History

This table describes the changes to _WebObjects Java Client Programming Guide_.

| __Date__ | __Notes__ |
| 2005-08-11 | Changed the title from "Java Client Desktop Applications." |
| 2002-11-01 | Updated for WebObjects 5.2. |
|  | Added information on layout hints and levels enhancements to the dynamic user-interface generation, [Widgets Pane](Inside%20Assistant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgewviucykjcumnbw) |
|  | Added information on the new security contract for remote method invocations in the distribution layer, [Business Logic](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcummzv) and [Delegates](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcumnbr) |
|  | Added information on how to implement SSL in the distribution layer, [Using SSL](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcumnbu) |
|  | Added information about delegates in the distribution layer, [Delegates](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcumnbr), and how to set them [Setting the Delegate](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwueqkcirceiqkb) |
|  | Added information on how to deploy the client application, [Deploying Client Applications](Deploying%20Client%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqg4wviubr) |
|  | Added information on new controllers and new arguments, [Controllers and Actions Reference](Controllers%20and%20Actions%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgmwviubr) |
|  | Added information on how to package client applications as Mac OS X desktop applications, [Desktop Applications](Deploying%20Client%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqg4wueqkcincegrki) |
|  | Added information on how to implement the new continuous change notification feature in certain controllers, [Continuous Change Notification](Common%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgiwueqkcizauersd) |
|  | Added information on how to build the WOComponent in [Write the Action (Build a WOComponent)](Enhancing%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgmwviucykjcummjtgy) |
|  | Added [Building Custom Controllers With XML](Building%20Custom%20Controllers%20With%20XML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqguwviubr) |
|  | Added [Using HTML on the Client](Using%20HTML%20on%20the%20Client.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgawviubr) |
|  | Added [Development Process Overview](Development%20Process%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmrzhawviubr) |
|  | Added [Using Nib Actions When Mixing](Mixing%20Static%20and%20Dynamic%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgqwugsceinduiscc) |
|  | Separated information on the Direct to Java Client Assistant into its own chapter, [Inside Assistant](Inside%20Assistant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgewviubr) |
|  | Adapted task chapters more closely to the JCRealEstatePhotos example |
|  | Changed the title of the chapter “Using the Controller Factory Programmatically” to [Generating Controllers With the Controller Factory](Generating%20Controllers%20With%20the%20Controller%20Factory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhewviubr) |
|  | Removed "Task:" in the title of the task chapters |
|  | Updated [Controllers and Actions Reference](Controllers%20and%20Actions%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgmwviubr) for WebObjects 5.2 |
|  | Moved information on different deployment strategies from the introduction to [Deploying Client Applications](Deploying%20Client%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqg4wviubr) |
|  | D2WContext key `languages` is now `locales`, [Localizing Property Labels](Localizing%20Dynamic%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrhawugrkhivceussi) |
|  | The security contract in the distribution layer changed, [Business Logic](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcummzv) and [Delegates](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcumnbr) |
|  | The package `com.webobjects.eogeneration.client` changed to `com.webobjects.eogeneration` |
|  | Web Start is now integrated with Java Client, [Web Start](Deploying%20Client%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqg4wueqkcjfbemssk) and [Server Files (Application Server Target)](Building%20a%20Simple%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgawviucykjcummrs) |
|  | Removed most information about deploying as applets, as applet support is now deprecated |
|  | It’s no longer necessary to set the class of File’s Owner in nib files, [Prepare the Nib File](Nondirect%20Java%20Client%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgqwviucykjcumnbq) |
|  | MouseInputAdapter class is now correctly named, [Make EOImageView Accept Clicks](Using%20Custom%20Views%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrguwviucykjcummzw) |
| 2002-05-01 | Updated for WWDC. |
|  | Added [Restricting Access to an Application](Restricting%20Access%20to%20an%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhawviubr) |
|  | Added [Generating Controllers With the Controller Factory](Generating%20Controllers%20With%20the%20Controller%20Factory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhewviubr) |
|  | Added [Adding Custom Menu Items](Adding%20Custom%20Menu%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgawviubr) |
|  | Added [Adding Custom Actions to Controllers](Adding%20Custom%20Actions%20to%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgewviubr) |
|  | Added [Common Rules](Common%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgiwviubr) |
|  | Added [Freezing XML User Interfaces](Freezing%20XML%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgmwviubr) |
|  | Added [Mixing Static and Dynamic User Interfaces](Mixing%20Static%20and%20Dynamic%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgqwviubr) |
|  | Added [Using Custom Views in Nib Files](Using%20Custom%20Views%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrguwviubr) |
|  | Added [Localizing Dynamic Components](Localizing%20Dynamic%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrhawviubr) |
|  | Added [Building Custom List Controllers](Building%20Custom%20List%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrhewviubr) |
|  | Added [Using and Extending Image Views in Nib Files](Using%20and%20Extending%20Image%20Views%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgywviubr) |
|  | Added [Using Pop-up Menus in Nib Files](Using%20Pop-up%20Menus%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrg4wviubr) |
|  | Added [Building a Login Window](Building%20a%20Login%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgewviubr) |

[Next](Controllers%20and%20Actions%20Reference.md)[Previous](Building%20a%20Login%20Window.md)

