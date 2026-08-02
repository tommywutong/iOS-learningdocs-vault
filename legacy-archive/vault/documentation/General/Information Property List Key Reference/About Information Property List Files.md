---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AboutInformationPropertyListFiles.html
archived_at: '2026-07-15T07:34:58.336338Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Next](Core%20Foundation%20Keys.md)[Previous](About%20Info.plist%20Keys%20and%20Values.md)

# About Information Property List Files

An information property list file is a structured text file that contains essential configuration information for a bundled executable. The file itself is typically encoded using the Unicode UTF-8 encoding and the contents are structured using XML. The root XML node is a dictionary, whose contents are a set of keys and values describing different aspects of the bundle. The system uses these keys and values to obtain information about your app and how it is configured. As a result, all bundled executables (plug-ins, frameworks, and apps) are expected to have an information property list file.

By convention, the name of an information property list file is `Info.plist`. This name of this file is case sensitive and must have an initial capital letter `I`. In iOS apps, this file resides in the top-level of the bundle directory. In macOS bundles, this file resides in the bundle’s `Contents` directory. Xcode typically creates this file for you automatically when you create a project of an appropriate type.

The simplest way to create an information property list file is to let Xcode create it for you. Each new bundle-based project that you create in Xcode comes with a file named _<project>_`-Info.plist`, where _<project>_ is the name of the project. At build time, this file is used to generate the `Info.plist` file that is then included in the resulting bundle.

To edit the contents of your information property list file, select the _<project>_`-Info.plist` file in your Xcode project to display the property list editor. Figure 1 shows the editor for the information property list file of a new Cocoa app project. The file created by Xcode comes preconfigured with keys that every information property list should have.

__Figure 1__  Editing the information property list in Xcode

!!

To edit the value for a specify key, double-click the value in the Xcode property list editor to select it, then type a new value. Most values are specified as strings but Xcode also supports several other scalar types. You can also specify complex types such as an array or dictionary. The property list editor displays an appropriate interface for editing each type. To change the type of a given value, make sure the value is not selected and Control-click it to display its contextual menu. From the Value Type submenu, select the type you want to use for the value.

Because information property lists are usually just text files, you can also edit them using any text editor that supports the UTF-8 file encoding. Because they are XML files, however, editing property list files manually is generally discouraged.

Although the `Info.plist` file provided by Xcode contains the most critical keys required by the system, most apps should typically specify several additional keys. Many subsystems and system apps use the `Info.plist` file to gather information about your app. For example, when the user chooses File > Get Info for your app, the Finder displays information from many of these keys in the resulting information window.

You add keys to your app’s `Info.plist` using the Xcode property list editor. For information about how to use this editor, see “[Edit property lists](http://help.apple.com/xcode/mac/8.0/#/dev3f399a2a6).”

For a list of the recommended keys you should include in a typical app, see [Recommended Info.plist Keys](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjufvjvona).

The values for many keys in an information property list file are human-readable strings that are displayed to the user by the Finder or your own app. When you localize your app, you should be sure to localize the values for these strings in addition to the rest of your app’s content.

Localized values are not stored in the `Info.plist` file itself. Instead, you store the values for a particular localization in a strings file with the name `InfoPlist.strings`. You place this file in the same language-specific project directory that you use to store other resources for the same localization. The contents of the `InfoPlist.strings` file are the individual keys you want localized and the appropriately translated value. The routines that look up key values in the `Info.plist` file take the user’s language preferences into account and return the localized version of the key (from the appropriate `InfoPlist.strings` file) when one exists. If a localized version of a key does not exist, the routines return the value stored in the `Info.plist` file.

For example, the TextEdit app has several keys that are displayed in the Finder and thus should be localized. Suppose your information property list file defines the following keys:

```
<key>CFBundleDisplayName</key>
<string>TextEdit</string>
<key>NSHumanReadableCopyright</key>
<string>Copyright ¬© 1995-2009, Apple Inc.,All Rights Reserved.
</string>
```

The French localization for TextEdit then includes the following strings in the `InfoPlist.strings` file of its `Contents/Resources/French.lproj` directory:

```
CFBundleDisplayName = "TextEdit";
NSHumanReadableCopyright = "Copyright © 1995-2009 Apple Inc.\nTous droits réservés.";
```

For more information about the placement of `InfoPlist.strings` files in your bundle, see _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_. For information about creating strings files, see _[Resource Programming Guide](../../Cocoa/Resource%20Programming%20Guide/About%20Resources.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqga2tc2i)_. For additional information about the localization process, see _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_.

You can designate a key in an `Info.plist` file as applying to a specific platform, a specific device type, or both. To create a platform- or device-specific key variant, combine a root key name with one or two qualifiers, using the following pattern:

_key_root_`-`_<platform>_`~`_<device>_

In this pattern, the _key_root_ portion represents the original name of the key, as you find it in this document. The _<platform>_ and _<device>_ portions are optional and restrict the key’s applicability to a specific platform or device type. Notice that if you employ a platform qualifier, connect it with a hyphen (`-`), and if you employ a device qualifier, connect it with a tilde (`~`).

Use of a device qualifier is much more common than is use of a platform qualifier.

For a device qualifier, you can use one of the following values:

- `iphone` The key applies to iPhone devices only
- `ipod` The key applies to iPod touch devices only
- `ipad` The key applies to iPad devices only

For a platform qualifier, you can specify a value of `iphoneos` or `macos` depending on which of these two platforms you are targeting.

When specifying a key variant, do so in addition to employing a corresponding key without any qualifiers, thereby ensuring you provide a reasonable default value. When the system searches for a key in your app’s `Info.plist` file, it chooses the key that is most specific to the current device and platform. If it does not find a qualified key, it looks for one without qualifiers. For example, to specify support for all device orientations on iPad, and three orientations for iPhone, the Xcode templates specify the corresponding keys in an app’s `Info.plist` file:

```
<key>UISupportedInterfaceOrientations</key>
    <string>UIInterfaceOrientationPortrait</string>
    <string>UIInterfaceOrientationLandscapeLeft</string>
    <string>UIInterfaceOrientationLandscapeRight</string>
<key>UISupportedInterfaceOrientations~ipad</key>
    <string>UIInterfaceOrientationPortrait</string>
    <string>UIInterfaceOrientationPortraitUpsideDown</string>
    <string>UIInterfaceOrientationLandscapeLeft</string>
    <string>UIInterfaceOrientationLandscapeRight</string>
```


iOS and macOS ignore custom keys you include in an `Info.plist` file. If you want to include app-specific configuration information in your `Info.plist` file, you can do so freely as long as your key names do not conflict with the ones Apple uses. When defining custom key names, prefix them with a unique prefix, such as your app’s bundle ID or your company’s domain name, to prevent conflicts.

Each of the Xcode application templates includes an `Info.plist` file, but you can also construct one from scratch. When creating an information property list file, there are several keys you should always include. These keys are almost always accessed by the system and providing them ensures that the system has the information it needs to work with your app effectively.

It is recommended that an iOS app include the following keys in its information property list file. Most are set by Xcode automatically when you create your project.

- [CFBundleDevelopmentRegion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgmydimzq)
- [CFBundleDisplayName](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv)
- [CFBundleExecutable](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytsmbz)
- [CFBundleIconFiles](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjq)
- [CFBundleIdentifier](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanzq)
- [CFBundleInfoDictionaryVersion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdaoby)
- [CFBundlePackageType](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgmrr)
- [CFBundleVersion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdgnru)
- [LSRequiresIPhoneOS](Launch%20Services%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjqfvjvomq)
- [UIMainStoryboardFile](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvooi)

In addition to these keys, there are several that are commonly included:

- [UIRequiredDeviceCapabilities](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomy) (required)
- [UIStatusBarStyle](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomju)
- [UIInterfaceOrientation](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomjt)
- [UIRequiresPersistentWiFi](iOS%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjsfvjvomjs)

For descriptions of these keys, see the other chapters of this book.

It is recommended that a Cocoa app include the following keys in its information property list file. Most are set by Xcode automatically when you create your project but some may need to be added.

- [CFBundleDevelopmentRegion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgmydimzq)
- [CFBundleDisplayName](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv)
- [CFBundleExecutable](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytsmbz)
- [CFBundleIconFile](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanbt)
- [CFBundleIdentifier](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanzq)
- [CFBundleInfoDictionaryVersion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdaoby)
- [CFBundleName](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfuytaojvha2q)
- [CFBundlePackageType](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgmrr)
- [CFBundleShortVersionString](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgnbz)
- [CFBundleVersion](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdgnru)
- [NSHumanReadableCopyright](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfuytcmrygu2c2vcqlbjekrrrge3q)

These keys identify your app to the system and provide some basic information about the services it provides. Cocoa apps should also include the following keys to identify key resources in the bundle:

- [NSMainNibFile](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3temrr)
- [NSPrincipalClass](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfvjvomjr)

For descriptions of these keys, see the other chapters of this book.

In addition to the recommended keys, there are several keys that should be localized and placed in your language-specific `InfoPlist.strings` files:

- [CFBundleDisplayName](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv)
- [CFBundleName](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfuytaojvha2q)
- [CFBundleShortVersionString](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgnbz)
- [NSHumanReadableCopyright](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfuytcmrygu2c2vcqlbjekrrrge3q)

For more information about localizing information property list keys, see [Localizing Property List Values](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjufuytamrsg43a).

[Next](Core%20Foundation%20Keys.md)[Previous](About%20Info.plist%20Keys%20and%20Values.md)

