---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CoreFoundationKeys.html
archived_at: '2026-07-15T07:34:59.227821Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Next](Launch%20Services%20Keys.md)[Previous](About%20Information%20Property%20List%20Files.md)

# Core Foundation Keys

The Core Foundation framework provides the underlying infrastructure for bundles, including the code used at runtime to load bundles and parse their structure. As a result, many of the keys recognized by this framework are fundamental to the definition of bundles themselves and are instrumental in determining the contents of a bundle.

Core Foundation keys use the prefix `CF` to distinguish them from other keys. For more information about Core Foundation, see _[Core Foundation Framework Reference](https://developer.apple.com/documentation/corefoundation)_.

Table 1 contains an alphabetical listing of Core Foundation keys, the corresponding name for that key in the Xcode property list editor, a high-level description of each key, and the platforms on which you use it. Detailed information about each key is available in later sections.

__Table 1__  Summary of Core Foundation keys

| Key | Xcode name | Summary | Platforms |
| CFAppleHelpAnchor | “Help file” | The bundle’s initial HTML help file. See [CFAppleHelpAnchor](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga3taobv) for details. | macOS |
| CFBundleAllowMixedLocalizations | “Localized resources can be mixed” | Used by Foundation tools to retrieve localized resources from frameworks. See [CFBundleAllowMixedLocalizations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgmydimjy) for details. | iOS, macOS |
| CFBundleDevelopmentRegion | “Localization native development region” | (Recommended) The default language and region for the bundle, as a language ID. See [CFBundleDevelopmentRegion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgmydimzq) for details. | iOS, macOS |
| CFBundleDisplayName | “Bundle display name” | (Required, Localizable) The user-visible name of the bundle; used by Siri and visible on the Home screen in iOS. See [CFBundleDisplayName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv) for details. | iOS, macOS |
| CFBundleDocumentTypes | “Document types” | An array of dictionaries describing the document types supported by the bundle. See [CFBundleDocumentTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv) for details. | iOS, macOS |
| CFBundleExecutable | “Executable file” | (Recommended) Name of the bundle’s executable file. See [CFBundleExecutable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytsmbz) for details. | iOS, macOS |
| CFBundleHelpBookFolder | “Help Book directory name” | The name of the folder containing the bundle’s help files. See [CFBundleHelpBookFolder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdambt) for details. | macOS |
| CFBundleHelpBookName | “Help Book identifier” | The name of the help file to display when Help Viewer is launched for the bundle. See [CFBundleHelpBookName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdamrr) for details. | macOS |
| CFBundleIconFile | “Icon file” | A legacy way to specify the app’s icon. Use the [CFBundleIcons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjt) or [CFBundleIconFiles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjq) keys instead. See [CFBundleIconFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanbt) for details. | iOS, macOS |
| CFBundleIconName | “Icon Name” | The name of the asset, from the bundle’s Asset Catalog, that represents the icon for the bundle. If you do not specify this key, [CFBundleIconFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanbt) is used to identify the file containing the icon. | macOS 10.13 and later |
| CFBundleIconFiles | “Icon files” | A top-level key for specifying the file names of the bundle’s icon image files. See [CFBundleIconFiles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjq) for details.  See also [CFBundleIcons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjt) as an alternative to this key. | iOS 3.2 and later |
| CFBundleIcons | None | File names of the bundle’s icon image files. See [CFBundleIcons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjt) for details. | iOS 5.0 and later, tvOS 9 and later |
| CFBundleIdentifier | “Bundle identifier” | (Recommended) An identifier string that specifies the app type of the bundle. The string should be in reverse DNS format using only the Roman alphabet in upper and lower case (A–Z, a–z), the dot (“.”), and the hyphen (“-”). See [CFBundleIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanzq) for details. | iOS, macOS |
| CFBundleInfoDictionaryVersion | “InfoDictionary version” | (Recommended) Version information for the `Info.plist` format. See [CFBundleInfoDictionaryVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdaoby) for details. | iOS, macOS |
| CFBundleLocalizations | “Localizations” | Contains localization information for an app that handles its own localized resources. See [CFBundleLocalizations](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrga4tknjs) for details. | iOS, macOS |
| CFBundleName | “Bundle name” | (Recommended, Localizable) The short name of the bundle. See [CFBundleName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfuytaojvha2q) for details. | iOS, macOS |
| CFBundlePackageType | “Bundle OS Type code” | The four-letter code identifying the bundle type. See [CFBundlePackageType](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgmrr) for details. | iOS, macOS |
| CFBundleShortVersionString | “Bundle versions string, short” | (Localizable) The release-version-number string for the bundle. See [CFBundleShortVersionString](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeytgnbz) for details. | iOS, macOS |
| CFBundleSpokenName | "Accessibility bundle name” | The spoken name of the app. See [CFBundleSpokenName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomy) for details. | iOS, macOS |
| CFBundleURLTypes | “URL types” | An array of dictionaries describing the URL schemes supported by the bundle. See [CFBundleURLTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdembx) for details. | iOS, macOS |
| CFBundleVersion | “Bundle version” | (Recommended) The build-version-number string for the bundle. See [CFBundleVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdgnru) for details. | iOS, macOS |
| CFPlugInDynamicRegistration | “Plug-in should be registered dynamically” | If YES, register the plug-in dynamically; otherwise, register it statically. See [CFPlugInDynamicRegistration](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgizdknjx) for details. | macOS |
| CFPlugInDynamicRegistrationFunction | Plug-in dynamic registration function name” | The name of the custom, dynamic registration function. See [CFPlugInDynamicRegisterFunction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfuytemrvg42q) for details. | macOS |
| CFPlugInFactories | “Plug-in factory interfaces” | For static registration, this dictionary contains a list of UUIDs with matching function names. See [CFPlugInFactories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgizdkojt) for details. | macOS |
| CFPlugInTypes | “Plug-in types” | For static registration, the list of UUIDs [CFPlugInTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgizdmmjr) for details. | macOS |
| CFPlugInUnloadFunction | “Plug-in unload function name” | The name of the custom function to call when it’s time to unload the plug-in code from memory. See [CFPlugInUnloadFunction](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfuytemrwgmzq) for details. | macOS |

`CFAppleHelpAnchor` (`String` - macOS) identifies the name of the bundle’s initial HTML help file, minus the `.html` or `.htm` extension. This file must be located in the bundle’s localized resource directories or, if the help is not localized, directly under the `Resources` directory.

`CFBundleAllowMixedLocalizations` (`Boolean` - iOS, macOS) specifies whether the bundle supports the retrieval of localized strings from frameworks. This key is used primarily by Foundation tools that link to other system frameworks and want to retrieve localized resources from those frameworks.

`CFBundleDevelopmentRegion` (`String` - iOS, macOS) specifies the default language and region for the bundle, as a language ID. For example, English for Australia has the language ID `en-AU`. The system uses this value if it cannot locate a resource for the user’s preferred language.

For more information, see [Language IDs](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/Language%20and%20Locale%20IDs.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2jninedcnjnknltm) in _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_. For details on how a bundle finds localized resources, see [The Bundle Search Pattern](../../Core%20Foundation/Bundle%20Programming%20Guide/Accessing%20a%20Bundle%E2%80%99s%20Contents.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2jninedcmbufvjvony) in _[Bundle Programming Guide](../../Core%20Foundation/Bundle%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdg2i)_.

`CFBundleDisplayName` (`String` - iOS, macOS) specifies the display name of the bundle, visible to users and used by Siri. If you support localized names for your bundle, include this key in your app’s `Info.plist` file and in the `InfoPlist.strings` files of your app’s language subdirectories. If you localize this key, include a localized version of the [CFBundleName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfuytaojvha2q) key as well.

Because Siri uses the value of this key, always provide a value, whether or not you localize your app.

In macOS, before displaying a localized name for your bundle, the Finder compares the value of this key against the actual name of your bundle in the file system. If the two names match, the Finder proceeds to display the localized name from the appropriate `InfoPlist.strings` file of your bundle. If the names do not match, the Finder displays the file-system name.

For more information about display names in macOS, see _[File System Programming Guide](../../File%20Management/File%20System%20Programming%20Guide/About%20Files%20and%20Directories.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeydmnzs)_.

`CFBundleDocumentTypes` (`Array` - iOS, macOS) contains an array of dictionaries that associate one or more document types with your app. Each dictionary is called a type-definition dictionary and contains keys used to define the document type. Table 2 lists the keys that are supported in these dictionaries.

__Table 2__  Keys for type-definition dictionaries

| Key | Xcode name | Type | Description | Platforms |
| __CFBundleTypeExtensions__ | “Document Extensions” | `Array` | This key contains an array of strings. Each string contains a filename extension (minus the leading period) to map to this document type. To open documents with any extension, specify an extension with a single asterisk “`*`”. (In OS X v10.4, this key is ignored if the `LSItemContentTypes` key is present.) Deprecated in OS X v10.5. | macOS |
| __CFBundleTypeIconFile__ | “Icon File Name” | `String` | This key contains a string with the name of the icon file (`.icns`) to associate with this macOS document type. For more information about specifying document icons, see [Document Icons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvooi). | macOS |
| __CFBundleTypeIconFiles__ | None | `Array` | An array of strings containing the names of the image files to use for the document icon in iOS. For more information about specifying document icons, see [Document Icons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvooi). | iOS |
| __CFBundleTypeMIMETypes__ | “Document MIME types” | `Array` | Contains an array of strings. Each string contains the MIME type name you want to map to this document type. (In OS X v10.4, this key is ignored if the `LSItemContentTypes` key is present.) Deprecated in OS X v10.5. | macOS |
| __CFBundleTypeName__ | “Document Type Name” | `String` | This key contains the abstract name for the document type and is used to refer to the type. This key is required and can be localized by including it in an `InfoPlist.strings` files. This value is the main way to refer to a document type. If you are concerned about this key being unique, you should consider using a uniform type identifier (UTI) for this string instead. If the type is a common Clipboard type supported by the system, you can use one of the standard types listed in the `NSPasteboard` class description. | iOS, macOS |
| __CFBundleTypeOSTypes__ | “Document OS Types” | `Array` | This key contains an array of strings. Each string contains a four-letter type code that maps to this document type. To open documents of any type, include four asterisk characters (`****`) as the type code. These codes are equivalent to the legacy type codes used by Mac OS 9. (In OS X v10.4, this key is ignored if the `LSItemContentTypes` key is present.) Deprecated in OS X v10.5. | macOS |
| __CFBundleTypeRole__ | “Role” | `String` | This key specifies the app’s role with respect to the type. The value can be `Editor`, `Viewer`, `Shell`, or `None`. This key is required. | macOS |
| __LSItemContentTypes__ | “Document Content Type UTIs” | `Array` | This key contains an array of strings. Each string contains a UTI defining a supported file type. The UTI string must be spelled out explicitly, as opposed to using one of the constants defined by Launch Services. For example, to support PNG files, you would include the string “`public.png`“ in the array. When using this key, also add the `NSExportableTypes` key with the appropriate entries. In macOS 10.5 and later, this key (when present) takes precedence over these type-identifier keys: `CFBundleTypeExtensions`, `CFBundleTypeMIMETypes`, `CFBundleTypeOSTypes`. | iOS, macOS |
| __LSHandlerRank__ | “Handler rank” | `String` | Determines how Launch Services ranks this app among the apps that declare themselves editors or viewers of files of this type. The possible values are: `Owner` (this app is the primary creator of files of this type), `Default` (this app is an opener of files of this type; this value is also used if no rank is specified), `Alternate` (this app is a secondary viewer of files of this type), and `None` (this app is never selected to open files of this type, but it accepts drops of files of this type). Launch Services uses the value of `LSHandlerRank` to determine the app to use to open files of this type. The order of precedence is: `Owner`, `Default`, `Alternate`. This key is available in macOS 10.5 and later and iOS 3.0 and later. | iOS, macOS |
| __LSTypeIsPackage__ | “Document is a package or bundle” | `Boolean` | Specifies whether the document is distributed as a bundle. If set to true, the bundle directory is treated as a file. (In macOS 10.4 and later, this key is ignored if the `LSItemContentTypes` key is present.) | macOS |
| __NSDocumentClass__ | “Cocoa NSDocument Class” | `String` | This key specifies the name of the `NSDocument` subclass used to instantiate instances of this document. This key is used by Cocoa apps only. | macOS |
| __NSUbiquitousDocumentUserActivityType__ | None | `String` | This key specifies the activity type of the [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) object associated with this document. | iOS, macOS |
| __NSExportableAs__ | “Exportable As Document Type Names” | `Array` | This key specifies an array of strings. Each string contains the name of another document type, that is, the value of a `CFBundleTypeName` property. This value represents another data format to which this document can export its content. This key is used by Cocoa apps only. Deprecated in OS X v10.5. | macOS |
| __NSExportableTypes__ | None | `Array` | This key specifies an array strings. Each string should contain a UTI defining a supported file type to which this document can export its content. Each UTI string must be spelled out explicitly, as opposed to using one of the constants defined by Launch Services. For example, to support PNG files, you would include the string “`public.png`“ in the array. This key is used by Cocoa apps only. Available in macOS 10.5 and later. | macOS |

The way you specify icon files in macOS and iOS is different because of the supported file formats on each platform. In iOS, each icon resource file is typically a PNG file that contains only one image. Therefore, it is necessary to specify different image files for different icon sizes. However, when specifying icons in macOS, you use an icon file (with extension `.icns`), which is capable of storing the icon at several different resolutions.

This key is supported in iOS 3.2 and later and all versions of macOS. For detailed information about UTIs, see _[Uniform Type Identifiers Overview](../../File%20Management/Uniform%20Type%20Identifiers%20Overview/Introduction%20to%20Uniform%20Type%20Identifiers%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytgmjz)_.

An app can take one of the following roles for any given document type:

- __Editor__. The app can read, manipulate, and save the type.
- __Viewer__. The app can read and present data of that type.
- __Shell__. The app provides runtime services for other processes—for example, a Java applet viewer. The name of the document is the name of the hosted process (instead of the name of the app), and a new process is created for each document opened.
- __None__. The app does not understand the data, but is just declaring information about the type (for example, the Finder declaring an icon for fonts).

The role you choose applies to all of the concrete formats associated with the document or Clipboard type. For example, the Safari app associates itself as a viewer for documents with the “.html”, “.htm”, “shtml, or “jhtml” filename extensions. Each of these extensions represents a concrete type of document that falls into the overall category of HTML documents. This same document can also support MIME types and legacy 4-byte OS types.

In iOS, the `CFBundleTypeIconFiles` key contains an array of strings with the names of the image files to use for the document icon. Table 3 lists the icon sizes you can include for each device type. You can name the image files however you want but the file names in your `Info.plist` file must match the image resource filenames exactly. (For iPhone and iPod touch, the usable area of your icon is actually much smaller.) For more information on how to create these icons, see _iOS Human Interface Guidelines_.

__Table 3__  Document icon sizes for iOS

| Device | Sizes |
| iPad | 64 x 64 pixels  320 x 320 pixels |
| iPhone and iPod touch | 22 x 29 pixels  44 x 58 pixels (high resolution) |

In macOS, the `CFBundleTypeIconFile` key contains the name of an icon resource file with the document icon. An icon resource file contains multiple images, each representing the same document icon at different resolutions. If you omit the filename extension, the system looks for your file with the extension `.icns`. You can create icon resource files using the Icon Composer app that comes with Xcode Tools.

The entry for each document type should contain the following keys:

- `CFBundleTypeIconFile`
- `CFBundleTypeName`
- `CFBundleTypeRole`

In addition to these keys, it must contain at least one of the following keys:

- `LSItemContentTypes`
- `CFBundleTypeExtensions`
- `CFBundleTypeMIMETypes`
- `CFBundleTypeOSTypes`

If you do not specify at least one of these keys, no document types are bound to the type-name specifier. You may use all three keys when binding your document type, if you so choose. In macOS 10.4 and later, if you specify the `LSItemContentTypes` key, the other keys are ignored. You can continue to include the other keys for compatibility with older versions of the system, however.

`CFBundleExecutable` (`String` - iOS, macOS) identifies the name of the bundle’s main executable file. For an app, this is the app executable. For a loadable bundle, it is the binary that will be loaded dynamically by the bundle. For a framework, it is the shared library for the framework. Xcode automatically adds this key to the information property list file of appropriate projects.

For frameworks, the value of this key is required to be the same as the framework name, minus the `.framework` extension. If the keys are not the same, the target system may incur some launch-performance penalties. The value should not include any extension on the name.

`CFBundleHelpBookFolder` (`String` - macOS) identifies the folder containing the bundle’s help files. Help is usually localized to a specific language, so the folder specified by this key represents the folder name inside the `.lproj` directory for the selected language.

`CFBundleHelpBookName` (`String` - macOS) identifies the main help page for your app. This key identifies the name of the Help page, which may not correspond to the name of the HTML file. The Help page name is specified in the `CONTENT` attribute of the help file’s `META` tag.

`CFBundleIconFile` (`String` - iOS, macOS) identifies the file containing the icon for the bundle. The filename you specify does not need to include the extension, although it may. The system looks for the icon file in the main resources directory of the bundle.

If your Mac app uses a custom icon and the asset name for the icon isn’t set in `CFBundleIconName`, you must specify the `CFBundleIconFile` property. If you do not specify this property, the system (and other apps) display your bundle with a default icon.

`CFBundleIconFiles` (`Array` - iOS) contains an array of strings identifying the icon files for the bundle. (It is recommended that you always create icon files using the PNG format.) When specifying your icon filenames, it is best to omit any filename extensions. Omitting the filename extension lets the system automatically detect high-resolution (`@2x`) versions of your image files using the standard-resolution image filename. If you include filename extensions, you must specify all image files (including the high-resolution variants) explicitly. The system looks for the icon files in the main resources directory of the bundle.

The [CFBundleIcons](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjt) key takes precedence over this key in iOS 5.0 and later. This key takes precedence over the [CFBundleIconFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanbt) key.

This key is supported in iOS 3.2 and later only and an app may have differently sized icons to support different types of devices and different screen resolutions. In other words, an app icon is typically 57 x 57 pixels on iPhone or iPod touch but is 72 x 72 pixels on iPad. Icons at other sizes may also be included. The order of the items in this array does not matter. The system automatically chooses the most appropriately sized icon based on the usage and the underlying device type.

For information about how to create icons for your apps, including the size information for each one, see _iOS Human Interface Guidelines_.

`CFBundleIcons` (`Dictionary` - iOS, tvOS) contains information about all of the icons used by the app. This key allows you to group icons based on their intended usage and specify multiple icon files together with specific keys for modifying the appearance of those icons. This dictionary can contain the following keys:

- __CFBundlePrimaryIcon__—This key identifies the primary icon for the Home screen and Settings app among others. The value for this key is described in [Contents of the CFBundlePrimaryIcon Dictionary Entry](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjy).
- __CFBundleAlternateIcons__—This key identifies alternate icons for the Home screen and Settings app among others. The value for this key is described in [Contents of the CFBundleAlternateIcons Dictionary Entry](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomju).
- __UINewsstandIcon__—This key identifies default icons to use for apps presented from Newsstand. The value for this key is a dictionary whose contents are described in [Contents of the UINewsstandIcon Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjv).

The `CFBundleIcons` key is supported in iOS 5.0 and later and in tvOS 9.0 and later. In iOS, you can combine this key with the [CFBundleIconFiles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenbzfvjvomjq) and [CFBundleIconFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanbt) keys but in iOS 5.0 and later, this key takes precedence.

The value of the `CFBundlePrimaryIcon` key is different in iOS and tvOS:

- In tvOS, the value of this key is a string. The value of the string is the name of an icon file in your app. For information about the icon file for your tvOS app, see [“Icons and Images”](https://developer.apple.com/tvos/human-interface-guidelines/icons-and-images/) in [Apple TV Human Interface Guidelines](https://developer.apple.com/tvos/human-interface-guidelines/)
- In iOS, the value of the key is a dictionary. Table 4 lists the keys and values that you include in this dictionary.

__Table 4__  Keys for the `CFBundlePrimaryIcon` dictionary

| Key | Value | Description |
| __CFBundleIconName__ | String | (Recommended for iOS 11 and later.) The name of the asset, from the bundle’s Asset Catalog, that represents the app icon. If you use this key, you should also include at least one item in `CFBundleIconFiles` so non-iOS systems, like Configurator and MDM solutions, can show the icon. |
| __CFBundleIconFiles__ | Array of strings | (Required if targeting iOS 10 or earlier.) Each string in the array contains the name of an icon file. You can include multiple icons of different sizes to support iPhone, iPad, and universal apps.  For a list of the icons, including their sizes, that you can include in your app bundle, see the section on app icons in [Providing the Required Resources](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/ExpectedAppBehaviors/ExpectedAppBehaviors.html#//apple_ref/doc/uid/TP40007072-CH3-SW9) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_. For information about how to create icons for your apps, see _iOS Human Interface Guidelines_. |
| __UIPrerenderedIcon__ | Boolean | This key specifies whether the icon files already incorporate a shine effect. If your icons already incorporate this effect, include the key and set its value to `YES` to prevent the system from adding the same effect again. If you do not include this key, or set its value to `NO`, the system applies a shine effect to the icon files listed in the `CFBundleIconFiles` key in this dictionary. |

When specifying icon filenames, it is best to omit any filename extensions. Omitting the filename extension lets the system automatically detect high-resolution (`@2x`) versions of your image files using the standard-resolution image filename. If you include filename extensions, you must specify all image files (including the high-resolution variants) explicitly. The system looks for the icon files in the main resources directory of the bundle.

The value of the `CFBundleAlternateIcons` key is different in iOS and tvOS:

- In tvOS, the value of the key is an array of strings. The value of each string is the name of an icon file in your app. For information about the icon file for your tvOS app, see [“Icons and Images”](https://developer.apple.com/tvos/human-interface-guidelines/icons-and-images/) in [Apple TV Human Interface Guidelines](https://developer.apple.com/tvos/human-interface-guidelines/)
- In iOS, the value of the key is a dictionary. The key for each dictionary entry is the name of the alternate icon, which is also the string you pass to the [setAlternateIconName:completionHandler:](https://developer.apple.com/documentation/uikit/uiapplication/2806818-setalternateiconname) method of `UIApplication` when changing icons. The value for each key is a dictionary containing the keys in Table 5.

__Table 5__  Keys for the `CFBundleAlternateIcons` dictionary in iOS

| Key | Value | Description |
| __CFBundleIconFiles__ | Array of strings | (Required) Each string in the array contains the name of an icon file. You can include multiple icons of different sizes to support iPhone, iPad, and universal apps.  For a list of the icons, including their sizes, that you can include in your app bundle, see _iOS Human Interface Guidelines_. |
| __UIPrerenderedIcon__ | Boolean | This key specifies whether the icon files already incorporate a shine effect. If your icons already incorporate this effect, include the key and set its value to `YES` to prevent the system from adding the same effect again. If you do not include this key, or set its value to `NO`, the system applies a shine effect to the icon files listed in the `CFBundleIconFiles` key in this dictionary. |

When specifying icon filenames, it is best to omit any filename extensions. Omitting the filename extension lets the system automatically detect high-resolution (`@2x`) versions of your image files using the standard-resolution image filename. If you include filename extensions, you must specify all image files (including the high-resolution variants) explicitly. The system looks for the icon files in the main resources directory of the bundle.

The value for the `UINewsstandIcon` key is a dictionary that identifies the default icons and style options to use for apps displayed in Newsstand. Table 6 lists the keys that you can include in this dictionary and their values.

__Table 6__  Keys for the `UINewsstandIcon` dictionary

| Key | Value | Description |
| __CFBundleIconFiles__ | Array of strings | (Required) Each string in the array contains the name of an icon file. You use this key to specify a set of standard icons for your app when presented in the Newsstand. This icon is used when no cover art is available for a downloaded issue.  For a list of the icons, including their sizes, that you can include in your app bundle, see the section on app icons in [App-Related Resources](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Inter-AppCommunication/Inter-AppCommunication.html#//apple_ref/doc/uid/TP40007072-CH6) in _[App Programming Guide for iOS](https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/iPhoneOSProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40007072)_. For information about how to create icons for your apps, see _iOS Human Interface Guidelines_. |
| __UINewsstandBindingType__ | String | This key provides information about how to stylize any Newsstand art. The value of this key is one of the following strings:   - `UINewsstandBindingTypeMagazine` - `UINewsstandBindingTypeNewspaper` |
| __UINewsstandBindingEdge__ | String | This key provides information about how to stylize any Newsstand art. The value of this key is one of the following strings:   - `UINewsstandBindingEdgeLeft` - `UINewsstandBindingEdgeRight` - `UINewsstandBindingEdgeBottom` |

When specifying icon filenames, it is best to omit any filename extensions. Omitting the filename extension lets the system automatically detect high-resolution (`@2x`) versions of your image files using the standard-resolution image filename. If you include filename extensions, you must specify all image files (including the high-resolution variants) explicitly. The system looks for the icon files in the main resources directory of the bundle.

`CFBundleIdentifier` (`String` - iOS, macOS) uniquely identifies the bundle. Each distinct app or bundle on the system must have a unique bundle ID. The system uses this string to identify your app in many ways. For example, the preferences system uses this string to identify the app for which a given preference applies; Launch Services uses the bundle identifier to locate an app capable of opening a particular file, using the first app it finds with the given identifier; in iOS, the bundle identifier is used in validating the app’s signature.

The bundle ID string must be a uniform type identifier (UTI) that contains only alphanumeric (`A`-`Z`,`a`-`z`,`0`-`9`), hyphen (`-`), and period (`.`) characters. The string should also be in reverse-DNS format. For example, if your company’s domain is `Ajax.com` and you create an app named Hello, you could assign the string `com.Ajax.Hello` as your app’s bundle identifier.

`CFBundleInfoDictionaryVersion` (`String` - iOS, macOS) identifies the current version of the property list structure. This key exists to support future versioning of the information property list file format. Xcode generates this key automatically when you build a bundle and you should not change it manually. The value for this key is currently 6.0.

`CFBundleLocalizations` (`Array` - iOS, macOS) identifies the localizations handled manually by your app. If your executable is unbundled or does not use the existing bundle localization mechanism, you can include this key to specify the localizations your app does handle.

Each entry in this property’s array is a string identifying the language name or ISO language designator of the supported localization. See “Language and Locale Designations” in _[Internationalization and Localization Guide](../../Mac%20OSX/Internationalization%20and%20Localization%20Guide/About%20Internationalization%20and%20Localization.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tc2i)_ in Internationalization Documentation for information on how to specify language designators.

`CFBundleName` (`String` - iOS, macOS) specifies the short name of the bundle, which may be displayed to users in situations such as the absence of a value for [CFBundleDisplayName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv). This name should be less than 16 characters long.

See also [CFBundleDisplayName](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv).

`CFBundlePackageType` (`String` - iOS, macOS) identifies the type of the bundle and is analogous to the Mac OS 9 file type code. The value for this key consists of a four-letter code. The type code for apps is `APPL`; for frameworks, it is `FMWK`; for loadable bundles, it is `BNDL`. For loadable bundles, you can also choose a type code that is more specific than `BNDL` if you want.

All bundles should provide this key. However, if this key is not specified, the bundle routines use the bundle extension to determine the type, falling back to the `BNDL` type if the bundle extension is not recognized.

`CFBundleShortVersionString` (`String` - iOS, macOS) specifies the release version number of the bundle, which identifies a released iteration of the app.

The release version number is a string composed of three period-separated integers. The first integer represents major revision to the app, such as a revision that implements new features or major changes. The second integer denotes a revision that implements less prominent features. The third integer represents a maintenance release revision.

The value for this key differs from the value for [CFBundleVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdgnru), which identifies an iteration (released or unreleased) of the app.

This key can be localized by including it in your `InfoPlist.strings` files.

See also [NSHumanReadableCopyright](Cocoa%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjrfuytcmrygu2c2vcqlbjekrrrge3q).

`CFBundleSpokenName` (`String` - iOS, macOS) contains a suitable replacement for the app name when performing text-to-speech operations. Include this key in your app bundle when the spelling of your app might be mispronounced by the speech system. For example, if the name of your app is “MyApp123”, you might set the value of this key to “My app one two three”.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`CFBundleURLTypes` (`Array` - iOS, macOS) contains an array of dictionaries, each of which describes the URL schemes (`http`, `ftp`, and so on) supported by the app. The purpose of this key is similar to that of [CFBundleDocumentTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgaytmobv), but it describes URL schemes instead of document types. Each dictionary entry corresponds to a single URL scheme. Table 7 lists the keys to use in each dictionary entry.

__Table 7__  Keys for CFBundleURLTypes dictionaries

| Key | Xcode name | Type | Description | Platforms |
| __CFBundleTypeRole__ | “Document Role” | `String` | This key specifies the app’s role with respect to the URL type. The value can be `Editor`, `Viewer`, `Shell`, or `None`. This key is required. | iOS, macOS |
| __CFBundleURLIconFile__ | “Document Icon File Name” | `String` | This key contains the name of the icon image file (minus the extension) to be used for this URL type. | iOS, macOS |
| __CFBundleURLName__ | “URL identifier” | `String` | This key contains the abstract name for this URL type. This is the main way to refer to a particular type. To ensure uniqueness, it is recommended that you use a Java-package style identifier. This name is also used as a key in the `InfoPlist.strings` file to provide the human-readable version of the type name. | iOS, macOS |
| __CFBundleURLSchemes__ | “URL Schemes” | `Array` | This key contains an array of strings, each of which identifies a URL scheme handled by this type. For example, specifying the URL scheme `feed` makes other apps aware that this app is capable of viewing RSS content. Types of URL schemes include `http`, `ftp`, `mailto`, and so on. | iOS, macOS |

To learn about the converse operation in iOS of declaring the URL schemes an app can open, read the description of the [LSApplicationQueriesSchemes](Launch%20Services%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tenjqfvjvomju) key.

`CFBundleVersion` (`String` - iOS, macOS) specifies the build version number of the bundle, which identifies an iteration (released or unreleased) of the bundle.

The build version number should be a string comprised of three non-negative, period-separated integers with the first integer being greater than zero—for example, `3.1.2`. The string should only contain numeric (`0`-`9`) and period (`.`) characters. Leading zeros are truncated from each integer and will be ignored (that is, `1.02.3` is equivalent to `1.2.3`). The meaning of each element is as follows:

- The first number represents the most recent major release and is limited to a maximum length of four digits.
- The second number represents the most recent significant revision and is limited to a maximum length of two digits.
- The third number represents the most recent minor bug fix and is limited to a maximum length of two digits.

If the value of the third number is `0`, you can omit it and the second period.

While developing a new version of your app, you can include a suffix after the number that is being updated; for example `3.1.3a1`. The character in the suffix represents the stage of development for the new version. For example, you can represent _development_, _alpha_, _beta_, and _final candidate_, by `d`, `a`, `b`, and `fc`. The final number in the suffix is the build version, which cannot be `0` and cannot exceed `255`. When you release the new version of your app, remove the suffix.

`CFPlugInDynamicRegistration` (`String` - macOS) specifies whether how host loads this plug-in. If the value is `YES`, the host attempts to load this plug-in using its dynamic registration function. If the value is `NO`, the host uses the static registration information included in the [CFPlugInFactories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgizdkojt), and [CFPlugInTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgizdmmjr) keys.

For information about registering plugins, see “Plug-in Registration” in _[Plug-in Programming Topics](../../Core%20Foundation/Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_.

`CFPlugInDynamicRegisterFunction` (`String` - macOS) identifies the function to use when dynamically registering a plug-in. Specify this key if you want to specify one of your own functions instead of implement the default `CFPlugInDynamicRegister` function.

For information about registering plugins, see “Plug-in Registration” in _[Plug-in Programming Topics](../../Core%20Foundation/Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_.

`CFPlugInFactories` (`Dictionary` - macOS) is used for static plug-in registration. It contains a dictionary identifying the interfaces supported by the plug-in. Each key in the dictionary is a universally unique ID (UUID) representing the supported interface. The value for the key is a string with the name of the plug-in factory function to call.

For information about registering plugins, see “Plug-in Registration” in _[Plug-in Programming Topics](../../Core%20Foundation/Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_.

`CFPlugInTypes` (`Dictionary` - macOS) is used for static plug-in registration. It contains a dictionary identifying one or more groups of interfaces supported by the plug-in. Each key in the dictionary is a universally unique ID (UUID) representing the group of interfaces. The value for the key is an array of strings, each of which contains the UUID for a specific interface in the group. The UUIDs in the array corresponds to entries in the [CFPlugInFactories](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgizdkojt) dictionary.

For information about registering plugins, see “Plug-in Registration” in _[Plug-in Programming Topics](../../Core%20Foundation/Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_.

`CFPlugInUnloadFunction` (`String` - macOS) specifies the name of the function to call when it is time to unload the plug-in code from memory. This function gives the plug-in an opportunity to clean up any data structures it allocated.

For information about registering plugins, see “Plug-in Registration” in _[Plug-in Programming Topics](../../Core%20Foundation/Plug-in%20Programming%20Topics/Introduction%20to%20Plug-ins.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgezdq2i)_.

[Next](Launch%20Services%20Keys.md)[Previous](About%20Information%20Property%20List%20Files.md)

