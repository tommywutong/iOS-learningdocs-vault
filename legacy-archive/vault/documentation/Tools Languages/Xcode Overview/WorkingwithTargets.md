---
title: Xcode Overview
apple_id: TP40010215
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-10-27'
source_url: https://developer.apple.com/library/archive/documentation/ToolsLanguages/Conceptual/Xcode_Overview/WorkingwithTargets.html
archived_at: '2026-07-27T06:57:07.913860Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Xcode Overview](index.md)


[Next](WorkingonRelatedProjects.md)[Previous](CreatingProjects.md)

## Working with Targets

Every project contains at least one target. A target specifies a product to build, such as an iOS, watchOS, or OS X app. Select a target in the project editor to view and modify the target’s settings. In the screenshot below, the _Adventure iOS target_ of the _Adventure project_ is selected in the _project navigator,_ and the _Adventure iOS target_ is selected in the _project editor_. The project editor displays the General pane for the target.

（原归档配图未能恢复：`TargetSettings_2x.png`）

### Applying App-Specific Target Settings

The General pane for a target shows basic settings that you occasionally check and possibly edit. You typically assign values for these settings elsewhere during the app development process, for example, in dialogs that appear when you create a new project.

For an iOS app, the General pane contains target settings for:

- The bundle identifier, a string that identifies the app to the operating system and to the App Store
- The version number under which to publish the app
- The build number, which identifies a particular build of the app
- The name of your Apple Developer Program development team
- The deployment target, which is the earliest iOS version on which the app runs
- The devices for which to build the app
- The main user interface file to load when the app launches
- The user interface orientations (portrait, upside down, landscape left, landscape right) that the app supports

For a watchOS app, the General pane contains target settings for:

- The display name of the app
- The bundle identifier
- The version number
- The build number
- The source for the app icon

For a WatchKit extension, the General pane contains target settings for:

- The bundle identifier
- The version number
- The build number
- The complication configuration including data source class, supported families, and groups
- A list of embedded binaries
- A list of linked frameworks and libraries
- Possibly other information depending on what the extension does

For an OS X app, the General pane contains target settings for:

- The application category, for classifying the app on the Mac App Store
- The bundle identifier
- The version number
- The build number
- An option to code sign the app for the Mac App Store, to code sign the app with a developer ID for distribution outside the Mac App Store, or to leave the code unsigned
- The deployment target, which is the earliest OS X version on which the app will run
- The icon that OS X uses to identify the app to the user

Specifying debug or release builds is done elsewhere. See [Managing Schemes](ManagingSchemes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqnjwfvjvomi).

### Adding Technology Features to a Target

To add various Apple technologies—such as iCloud, Game Center, In-App Purchase, and Maps—to your app, select its target in the project editor and click Capabilities. Add a capability by setting a switch to On. Xcode adds the necessary entitlements file to your project and links the target to the necessary frameworks. In some cases, Xcode might encounter issues enabling a capability. If so, that information will be displayed in the information area for that capability.

You can show or hide detail for a capability by clicking the disclosure triangle to the left of the capability name. For capabilities that are off, this area describes the capability and actions that occur when the capability is turned on. For capabilities that are on, use this area to view or update any associated configuration and to identify issues that need fixing.

（原归档配图未能恢复：`Capabilities_2x.png`）

For more information on adding capabilities, see Adding Capabilities.

### Adding On-Demand Resource Tags to a Target

_On-demand resources_ are app contents that you download only when needed. They are hosted on the App Store separately from the app bundle downloaded by the user. You can use on-demand resources to enable smaller apps, faster downloads, and richer app content. You use tags to identify and manage the on-demand resources in a target.

The Resource Tags pane shows the list of tags and the associated resources. You can use it to add and remove tags as well as to move resources between tags.

（原归档配图获取待重试：`ODR_Resource_Tags_Pane_All_2x.png`）

For more information on adding and using on-demand resources, see _[On-Demand Resources Guide](../../File%20Management/On-Demand%20Resources%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2taobt)_.

### Adding File Type and Service Information to a Target

The Info pane for a target shows properties associated with your app, file types that your app can create or open, and for OS X, services provided by your app. Most of the custom target properties are modified in other parts of the Xcode interface (such as the bundle identifier, version, and build number set in the General pane). The screenshot shows the Info pane for the iOS target of the Adventure app.

（原归档配图未能恢复：`XC_O_target_info_pane_2x.png`）

The Document Types setting specifies the document types you can create and edit in your app and provides a custom icon displayed for that document type by iOS or the Mac OS.

Add exported and imported UTIs for any file types your app can export or import. Unlike document types, which are usually unique to your app, UTIs specify general formats like plain text or `.png`. For example, UTIs support copying and pasting to and from the Clipboard between apps. See _[Uniform Type Identifiers Reference](../../Miscellaneous/Uniform%20Type%20Identifiers%20Reference/Introduction%20to%20Uniform%20Type%20Identifiers%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjx)_ for more information and a list of supported types.

The URL Types setting lets you specify custom schemas for exchanging data with other apps by using custom protocols. For example, some existing schemas include `http`, `mailto`, and `sms`. For more information, see [Using URL Schemes to Communicate with Apps](../../iPhone/App%20Programming%20Guide%20for%20iOS/Inter-App%20Communication.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tanzsfvbuqnrnknltc) (iOS) or _[Launch Services Programming Guide](../../Carbon/Launch%20Services%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojz)_ (Mac OS).

Mac OS apps use the Services item to add items that appear in the Services menu. For more information, see _[Services Implementation Guide](../../Cocoa/Services%20Implementation%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeydc2i)_.

### Overriding Build Settings for a Target

A target contains instructions—in the form of build settings and build phases—for building a product. A target inherits the project’s build settings. Although most developers seldom need to change these settings, you can override any of the project’s build settings by specifying different settings at the target level. Select a target in the project editor to modify the target settings in the Info, Build Settings, or Build Phases pane.

[Working with Projects](CreatingProjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmzrfvjvomi)

[Working on Related Projects](WorkingonRelatedProjects.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmztfvjvomi)

Copyright © 2018 Apple Inc. All rights reserved.
[Terms of Use](http://www.apple.com/legal/terms/site.html) |
[Privacy Policy](http://www.apple.com/privacy/) |
[Updated: 2016-10-27](RevisionHistory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydemjvfvbuqmrsfvjvomi)

[Next](WorkingonRelatedProjects.md)[Previous](CreatingProjects.md)
