---
title: Information Property List Key Reference
apple_id: TP40009247
resource_type: Guide
platform: watchOS|tvOS|iOS|macOS
topic: General
technology: null
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/AppExtensionKeys.html
archived_at: '2026-07-15T07:34:59.111815Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Information Property List Key Reference](About%20Info.plist%20Keys%20and%20Values.md)


[Next](Document%20Revision%20History.md)[Previous](watchOS%20Keys.md)

# App Extension Keys

App extensions enable you to provide features to other apps in iOS and macOS. Each app extension type defines keys that let you declare to the system information about an app extension's capabilities and intents.

Keys for app extensions follow a particular hierarchical structure, with the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) dictionary at the top. Most app extension types employ an [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) dictionary as an immediate child of the NSExtension key. Here is a typical structure of the keys for an app extension:

```
<key>NSExtension</key>
<dict>
  <key>NSExtensionAttributes</key>
  <dict>
    <key>NSExtensionJavaScriptPreprocessingFile</key>
    <string>Action</string>
  </dict>
  <key>NSExtensionPointIdentifier</key>
  <string>com.apple.ui-services</string>
  <key>NSExtensionPrincipalClass</key>
  <string>MyActionRequestHandler</string>
</dict>
```

The NSExtensionPointIdentifier key uniquely identifies the type of app extension, such as _Action_ or _Custom Keyboard_. For a complete list of the available values for the extension point identifier key, see [NSExtensionPointIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjv).

For more information about configuring the information property-list file of an app extension, see _[App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)_.

Table 1 is an alphabetical list of app extension keys, brief descriptions, and availability by platform and version. See later sections in this chapter for detailed information on each of these keys.

__Table 1__  Summary of app extension keys

| Key | Extension point and description | Availability |
| IsASCIICapable | Custom Keyboard: A Boolean value that specifies whether a custom keyboard supports the [UIKeyboardTypeASCIICapable](https://developer.apple.com/documentation/uikit/uikeyboardtype/uikeyboardtypeasciicapable) keyboard type trait. See [IsASCIICapable](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooa) for details. | iOS 8 and later |
| NSExtension | General: A dictionary of keys and values that describe an app extension. See [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) for details. | iOS 8 and later  macOS 10.10 and later |
| NSExtensionActionWantsFullScreenPresentation | Action: A Boolean value that specifies whether the Action extension should be presented in full screen. See [NSExtensionActionWantsFullScreenPresentation](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzv) for details. | iOS 8 and later |
| NSExtensionActivationDictionaryVersion | Share, Action: An integer that specifies the activation dictionary version to employ. See [NSExtensionActivationDictionaryVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzw) for details. | iOS 9 and later  macOS 10.11 and later |
| NSExtensionActivationRule | Share, Action: A dictionary that specifies the semantic data types that a Share or Action extension supports. See [NSExtensionActivationRule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjq) for details. | iOS 8 and later |
| NSExtensionActivationUsesStrictMatching | Share, Action: See [NSExtensionActivationUsesStrictMatching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzx) for details. | iOS 9 and later  macOS 10.11 and later |
| NSExtensionAttributes | General: A dictionary of keys and values that specify aspects of an app extension. See [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) for details. | iOS 8 and later  macOS 10.10 and later |
| NSExtensionFileProviderDocumentGroup | Document Picker: A string that specifies the identifier of a shared container that can be accessed by a document picker and its associated file provider. See [NSExtensionFileProviderDocumentGroup](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjs) for details. | iOS 8 and later |
| NSExtensionJavaScriptPreprocessingFile | Share, Action: A string that specifies the name of a JavaScript file supplied by a Share extension or an Action extension. See [NSExtensionJavaScriptPreprocessingFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrx) for details. | iOS 8 and later  macOS 10.10 and later |
| NSExtensionMainStoryboard | General: A string that specifies the name of the app extension’s main storyboard file, minus the `.storyboard` filename extension. See [NSExtensionMainStoryboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomju) for details. | iOS 8 and later  macOS 10.10 and later |
| NSExtensionOverridesHostUIAppearance | General: A Boolean value that specifies whether the app extension should ignore appearance updates made by the host app. See [NSExtensionOverridesHostUIAppearance](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonjt) for details. | iOS 10 and later |
| NSExtensionPointIdentifier | General: A string that specifies the extension point that supports an app extension, in reverse-DNS notation. See [NSExtensionPointIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjv) for details. | iOS 8 and later  macOS 10.10 and later |
| NSExtensionPrincipalClass | General: A string that specifies the name of the custom class that implements an app extension’s primary view or functionality. See [NSExtensionPrincipalClass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjw) for details. | iOS 8 and later  macOS 10.10 and later |
| NSExtensionServiceAllowsToolbarItem | Action: A Boolean value that specifies whether an Action extension can display a toolbar button in a window’s toolbar. See [NSExtensionServiceAllowsToolbarItem](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjx) for details. | macOS 10.10 and later |
| NSExtensionServiceRoleType | Action: A string that specifies the type of task an Action extension can perform. See [NSExtensionServiceRoleType](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjy) for details. | macOS 10.10 and later |
| NSExtensionServiceToolbarIconFile | Action: A string that species the icon file for an OS X Action extension’s toolbar button. See [NSExtensionServiceToolbarIconFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjz) for details. | macOS 10.10 and later |
| NSExtensionServiceToolbarPaletteLabel | Action: A string that specifies the toolbar item title that gets displayed in the toolbar customization dialog for an Action extension. See [NSExtensionServiceToolbarPaletteLabel](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrq) for details. | macOS 10.10 and later |
| PHSupportedMediaTypes | Photo Editing: An array that specifies the types of assets a Photo Editing extension can edit. See [PHSupportedMediaTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrr) for details. | iOS 8 and later |
| PrefersRightToLeft | Custom Keyboard: A Boolean value that specifies whether a custom keyboard is for a right-to-left language. See [PrefersRightToLeft](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrs) for details. | iOS 8 and later |
| PrimaryLanguage | Custom Keyboard: A string conforming to [BCP 47 - Tags for Identifying Languages](http://tools.ietf.org/html/bcp47), that specifies the primary language for custom keyboard. See [PrimaryLanguage](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrt) for details. | iOS 8 and later |
| RequestsOpenAccess | Custom Keyboard: A Boolean value that specifies whether a custom keyboard wants to use a shared container and wants network access. See [RequestsOpenAccess](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomru) for details. | iOS 8 and later |
| SFSafariContentScript | Safari: An array used to add content scripts to the extension. Each value in the array is a dictionary, providing the filename for a content script. See [SFSafariContentScript](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbq) for details. | Safari 10 in macOS 10.11.5 and later |
| SFSafariContextMenu | Safari: An array used to add items to Safari’s context menu. See [SFSafariContextMenu](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbu)for details. | Safari 10 in macOS 10.11.5 and later |
| SFSafariStyleSheet | Safari: An array used to add style sheets to the extension. Each value in the array is a dictionary, providing the filename for a content script. See [SFSafariStyleSheet](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbw) for details. | Safari 10 in macOS 10.11.5 and later |
| SFSafariToolbarItem | Safari: A dictionary used to add a toolbar item to Safari windows. See [SFSafariToolbarItem](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonby) for details. | Safari 10 in macOS 10.11.5 and later |
| SFSafariWebsiteAccess | Safari: An optional dictionary that specifies which webpages the Safari app extension can access, if any. See [SFSafariWebsiteAccess](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonjq) for details. | Safari 10 in macOS 10.11.5 and later |
| UIDocumentPickerModes | Document Picker: An array that specifies the supported document picker modes. See [UIDocumentPickerModes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrv) for details. | iOS 8 and later |
| UIDocumentPickerSupportedFileTypes | Document Picker: An array that specifies the supported Uniform Type Identifiers (UTIs) for a document picker. See [UIDocumentPickerSupportedFileTypes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrw) for details. | iOS 8 and later |

The keys in this section pertain to all app extensions.

`Dictionary` - iOS, macOS. Keys and values that describe an app extension. Any other app extension key used for an app extension must be placed within this dictionary.

The supported direct children of this key are the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr), [NSExtensionMainStoryboard](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomju), [NSExtensionPointIdentifier](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjv), and [NSExtensionPrincipalClass](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjw) keys.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`Dictionary` - iOS, macOS. Keys and values that specify aspects of an app extension. This key, if used, must be placed as an immediate child of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`String` - iOS, macOS. Specifies the name of the app extension’s main storyboard file, minus the `.storyboard` filename extension. This key, if used, must be placed as an immediate child of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`Boolean` - iOS. Specifies whether the app extension can ignore appearance changes that the host app makes. To ignore appearance changes made by the host app, you must include this key as an immediate child of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key and give it the value `YES`.

This key is supported in iOS 10 and later.

`String` - iOS, macOS. Specifies the extension point that supports an app extension, in reverse-DNS notation. This key is required for every app extension, and must be placed as an immediate child of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key. Each Xcode app extension template is preconfigured with the appropriate extension point identifier key. Valid values are shown in Table 2.

__Table 2__  Values for the `NSExtensionPointIdentifier` key

| Extension point | Platforms | Extension point identifier |
| Action (UI) | iOS, macOS | `com.apple.ui-services` |
| Action (non-UI) | iOS | `com.apple.services` |
| Broadcast Upload, Broadcast Upload UI, Broadcast UI | tvOS | `com.apple.broadcast-services` |
| Custom Keyboard | iOS | `com.apple.keyboard-service` |
| Document Picker | iOS | `com.apple.fileprovider-ui` |
| File Provider | iOS | `com.apple.fileprovider-nonui` |
| File Provider Actions | iOS | `com.apple.fileprovider-actionsui` |
| Finder Sync | macOS | `com.apple.FinderSync` |
| Message Filter | iOS | `com.apple.identitylookup.message-filter` |
| Photo Editing | iOS | `com.apple.photo-editing` |
| Share | iOS, macOS | `com.apple.share-services` |
| Today | iOS, macOS | `com.apple.widget-extension` |
| TV Services | tvOS | `com.apple.tv-services` |
| Watch App | iOS, watchOS | `com.apple.watchkit` |

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`String` - iOS, macOS. Specifies the name of the custom class that implements an app extension’s primary view or functionality. This key, if used, must be placed as an immediate child of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

The keys in this section pertain to app extensions employing the Action extension point. These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key, unless noted otherwise.

`Boolean` - iOS. Specifies whether an iOS Action extension should be presented in full screen. This key, if used, must be placed as an immediate child of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key.

If the value of this key is `YES`, the modal presentation style of the extension’s view controller is [UIModalPresentationFullScreen](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/fullscreen); otherwise, the modal presentation style is [UIModalPresentationFormSheet](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle/formsheet).

This key is supported in iOS 8 and later.

`Dictionary` - iOS, macOS. Also supported in a Share extension. Specifies the semantic data types that an app extension supports. Each key in the dictionary represents a data type, such as _image_, _video_, or _web URL_. Add a key to this dictionary, and provide a nonzero value, if your app extension can handle files of the corresponding data type.

Table 3 lists the keys that you can include in the dictionary associated with the `NSExtensionActivationRule` dictionary. The value for each key is an integer that specifies the maximum number of files of the corresponding data type that your extension can handle.

__Table 3__  Keys for the `NSExtensionActivationRule` dictionary

| Key | Description |
| `NSExtensionActivationSupportsAttachmentsWithMaxCount` | Include this key to indicate to the system and to other apps that your app supports a maximum number of attachments. |
| `NSExtensionActivationSupportsAttachmentsWithMinCount` | Include this key to indicate to the system and to other apps that your app supports a minimum number of attachments. |
| `NSExtensionActivationSupportsFileWithMaxCount` | Include this key to indicate to the system and to other apps that your app supports files in general. |
| `NSExtensionActivationSupportsImageWithMaxCount` | Include this key to indicate to the system and to other apps that your app supports image files. |
| `NSExtensionActivationSupportsMovieWithMaxCount` | Include this key to indicate to the system and to other apps that your app supports movie files. |
| `NSExtensionActivationSupportsText` | Include this key to indicate to the system and to other apps that your app supports text. |
| `NSExtensionActivationSupportsWebURLWithMaxCount` | Include this key to indicate to the system and to other apps that your app supports web URLs. |
| `NSExtensionActivationSupportsWebPageWithMaxCount` | Include this key to indicate to the system and to other apps that your app supports web pages. |

If these predefined keys cannot express the activation rule you need, you can provide an entry to the NSExtensionActivationRule dictionary that is a string representing a predicate. The system evaluates the predicate against dictionary representations of [NSItemProvider](https://developer.apple.com/documentation/foundation/nsitemprovider) objects. (To learn more about creating a predicate statement for an activation rule, see [Declaring Supported Data Types for a Share or Action Extension](../App%20Extension%20Programming%20Guide/ExtensionScenarios.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjufvbuqmrrfvjvooa).)

The NSExtensionActivationRule dictionary can also contain the [NSExtensionActivationDictionaryVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzw) and [NSExtensionActivationUsesStrictMatching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzx) keys.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`Number` - iOS, macOS. Also supported in a Share extension. Specifies the activation dictionary version for an app extension. This key appears within a [NSExtensionActivationRule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjq) dictionary.

In iOS 9 and macOS 10.11, this key impacts only one thing: the matching between the set of asset types provided by a host app in an item provider, on the one hand, and the set of asset types handled by an Action or Share extension, on the other. The value of this key can be either `1` or `2`, which indicates activation dictionary version 1 or 2. Specifically, the value of the key determines the conditions under which an app extension is eligible to appear in an activity view controller, as follows:

- __Activation dictionary version 1__ Only when the app extension handles _all_ of the asset types being offered by a host app item provider
- __Activation dictionary version 2__ When the app extension handles _at least one_ of the asset types being offered by a host app item provider

For example, say an item provider in a host app is offering an image asset and a text asset, and a Share extension is capable of handling only text assets. If the app extension’s `Info.plist` file does not have this key, or has this key and its value is set to `1`, the extension _will not_ appear in the activity view controller when the user taps the Action button in the host app. However, if the app extension’s `Info.plist` file has this key and its value is `2`, the extension _will_ appear.

This key is supported in iOS 9 and later and in macOS 10.11 and later.

See also [NSExtensionActivationUsesStrictMatching](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzx).

`Boolean` - iOS, macOS. Specifies whether you want to use strict or fuzzy matching when determining the asset types an app extension can handle. This key appears within a [NSExtensionActivationRule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjq) dictionary.

If you need strict matching, set this key to `YES` (that is, `1`). For example, if you need strict matching and your app extension runs in iOS 9 and later, setting [NSExtensionActivationDictionaryVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzw) to `2` and NSExtensionActivationUsesStrictMatching to `1` helps you future-proof your code in case new versions are added.

This key is supported in iOS 9 and later and in macOS 10.11 and later.

See also [NSExtensionActivationDictionaryVersion](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomzw).

`String` - iOS, macOS. Also supported in a Share extension. Specifies the name of a JavaScript file supplied by a Share extension. If you provide a JavaScript file, Safari runs the functions in the file when your Share extension starts and stops. You might want to include a JavaScript file in your Share extension if you want to get information from a webpage to display in your extension, or update a webpage when your extension completes its task.

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`Boolean` - macOS. Specifies whether an Action extension can display a toolbar button in a window’s toolbar. When a toolbar allows extension items, an enabled Action extension can appear in the toolbar customization dialog.

This key is supported in macOS 10.10 and later.

`String` - macOS. specifies the type of task an Action extension can perform. The available values for this key are shown in Table 4.

__Table 4__  Values for the `NSExtensionServiceRoleType` key

| Value | Description |
| `NSExtensionServiceRoleTypeEditor` | Indicates an Action extension that supports user editing and returns edited content to the host app. |
| `NSExtensionServiceRoleTypeViewer` | Indicates an Action extension that supports viewing of content but not editing. |

This key is supported in macOS 10.10 and later.

`String` - macOS. Species the icon file for an OS X Action extension’s toolbar button. If this key is not present, the toolbar button uses the icon specified by the app extension’s [CFBundleIconFile](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgazdanbt) key.

This key is supported in macOS 10.10 and later.

`String` - macOS. Specifies the toolbar item title that gets displayed in the toolbar customization dialog for an Action extension. If this key is not present, the toolbar customization dialog displays the title specified by the app extension’s [CFBundleDisplayName](Core%20Foundation%20Keys.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambrgqztcljrgeydomrv) key.

This key is supported in macOS 10.10 and later.

The keys in this section pertain to app extensions employing the Custom Keyboard extension point (iOS only). These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`Boolean` - iOS. Specifies whether a custom keyboard supports the [UIKeyboardTypeASCIICapable](https://developer.apple.com/documentation/uikit/uikeyboardtype/uikeyboardtypeasciicapable) keyboard type trait.

This key is supported in iOS 8 and later.

`Boolean` - iOS. Specifies whether a custom keyboard is for a right-to-left language.

This key is supported in iOS 8 and later.

`String` - iOS. Specifies the primary language for a custom keyboard, using a string that conforms to [BCP 47 - Tags for Identifying Languages](http://tools.ietf.org/html/bcp47). The system uses this value to indicate the keyboard language in Settings and in the system globe key.

This key is supported in iOS 8 and later.

`Boolean` - iOS. Specifies whether a custom keyboard wants access to such resources as a shared container (shared with the containing app) and network access. Default value is `NO`. If you set this key’s value to `YES`, your keyboard gains a variety of capabilities:

- Network access, supporting server-side processing of keystrokes
- Shared container access with the keyboard’s containing app, supporting features such as an editing interface for the keyboard’s custom autocorrect lexicon
- Access to Location Services and the Address Book database, with user approval
- Via containing app, ability to participate in Game Center and In-App Purchase
- Ability to to work with managed apps, if custom keyboard supports mobile device management (MDM)

This key is supported in iOS 8 and later.

The keys in this section pertain to app extensions employing the Document Picker or File Provider extension points (iOS only). These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`String` - iOS. Specifies the identifier of a shared container that can be accessed by a Document Picker and its associated File Provider.

This key is supported in iOS 8 and later.

`Array` - iOS. Defines custom actions for a File Provider extension. Your project must contain both a File Provider extension and a File Provider UI extension.

Set this to an array of dictionaries. Each dictionary represents a separate action, and contains the following keys:

__Table 5__  Keys for the `NSExtensionFileProviderActions` dictionaries

| Key | Type | Description |
| `NSExtensionFileProviderActionIdentifier` | `String` | A unique identifier for the action. |
| `NSExtensionFileProviderActionName` | `String` (Localizable) | The localized name that appears in the context menu. |
| `NSExtensionFileProviderActionActivationRule` | `Predicate` | A predicate that determines whether the action appears in the context menu.  The value must be a valid predicate format string. The system passes the resulting predicate a dictionary with a single `fileproviderItems` key. The value is an array of [NSFileProviderItem](https://developer.apple.com/documentation/fileprovider/nsfileprovideritem) objects representing the selected items.  If the action should always appear in the context menu, set the value to `TRUEPREDICATE`. |

These actions appear in the context menu when the user long presses an item while browsing the File Provider's content.

This key is supported in iOS 11 and later.

`Boolean` - iOS. Determines whether the File Provider can enumerate its content. On iOS 11 and later, set this value to `YES` to provide content for the Files app and the [UIDocumentBrowserViewController](https://developer.apple.com/documentation/uikit/uidocumentbrowserviewcontroller) class.

This key is supported in iOS 11 and later.

`Array` - iOS. Specifies the supported document picker modes.The available values for this key are shown in [Table 6](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomry).

__Table 6__  Values for the `UIDocumentPickerModes` key

| Value | Description |
| `UIDocumentPickerModeImport` | Indicates that the document picker can import files. |
| `UIDocumentPickerModeOpen` | Indicates that the document picker can open files. |
| `UIDocumentPickerModeExportToService` | Indicates that the document picker can export files. |
| `UIDocumentPickerModeMoveToService` | Indicates that the document picker can move files. |

This key is supported in iOS 8 and later.

`Array` - iOS. Specifies the supported file Uniform Type Identifiers (UTIs) for a document picker. The app extension is included in a document menu only if one of the requested UTIs matches one of the UTIs in this array. The move and export modes of a document picker operate only on files with supported UTIs.

This key is supported in iOS 8 and later.

The keys in this section pertain to iMessage apps and sticker packs.

`Array` - iOS. Specifies the contexts an iMessage app or sticker pack supports. Takes an array containing the following strings:

- `MSMessagesAppPresentationContextMessages` - Can be included by itself or combined with `MSMessagesAppPresentationContextMedia`.
- `MSMessagesAppPresentationContextMedia` - Cannot be included by itself. Must be combined with `MSMessagesAppPresentationContextMessages`.

Example 1: Messages only

```
<key>MSSupportedPresentationContexts</key>
<array>
  <string>MSMessagesAppPresentationContextMessages</string>
</array>
```

Example 2: Messages and media

```
<key>MSSupportedPresentationContexts</key>
<array>
  <string>MSMessagesAppPresentationContextMessages</string>
  <string>MSMessagesAppPresentationContextMedia</string>
</array>
```

This key is supported in iOS 12 and later.

The keys in this section pertain to app extensions employing the Message Filter extension point (iOS only). These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`String` - iOS. Optional. Specifies the associated server to which a Message Filter app extension may defer a query.

This key is supported in iOS 11 and later.

The keys in this section pertain to app extensions employing the Notification Content extension point (iOS only). These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`String` or `Array` - iOS. Required. Specifies the identifier of a category declared by the app using the [UNNotificationCategory](https://developer.apple.com/documentation/usernotifications/unnotificationcategory) class.

This key is supported in iOS 10 and later.

`Number` - iOS. Required. Represents the initial size of your view controller’s view expressed as a ratio of its height to its width. The system uses this value to set the initial size of the view controller while your extension is loading. (You can change the size of your view controller after your extension loads.)

This key is supported in iOS 10 and later.

`Boolean` - iOS. Optional. When set to `YES`, the system displays only your custom view controller in the notification interface. When set to `NO`, the system displays the default notification content in addition to your view controller’s content. Custom action buttons and the Dismiss button are always displayed, regardless of this setting. If you do not specify this key, the default value is set to `NO`.

This key is supported in iOS 10 and later.

`Boolean` - iOS. Optional. When set to `YES`, the system uses the `title` property of your view controller as the title of the notification. When set to `NO`, the system sets the notification's title to the name of your app. If you do not specify this key, the default value is set to `NO`.

This key is supported in iOS 10 and later.

`Boolean` - iOS. Optional. When set to `YES`, enables user interactions in a custom notification. This lets you add interactive controls, such as buttons and switches to your custom interface. For additional information, see [Customizing the Appearance of Notifications](https://developer.apple.com/documentation/usernotificationsui/customizing_the_appearance_of_notifications).

This key is supported in iOS 12 and later.

The key in this section pertains to app extensions employing the Photo Editing extension point (iOS only). These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`Array` - iOS. Specifies the types of assets a Photo Editing extension can edit. The available values for this key are `Image` (which is the default value) and `Video`.

This key is supported in iOS 8 and later.

The keys in this section pertain to app extensions employing the Safari app extension point, `com.apple.Safari.extension`, for macOS. These keys, if used, must be placed as immediate children of the [NSExtension](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvooi) key. These keys are supported in Safari 10.0 and later in macOS 10.11.5 and later. For more on Safari App Extensions, see _[Safari App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternetWeb/Conceptual/SafariAppExtension_PG/index.html#//apple_ref/doc/uid/TP40017319)_.

Listing 1 represents the overall structure of a typical NSExtension dictionary when you are providing a Safari app extension. Keep this structure in mind as you configure each element of your extension.

__Listing 1__  Structure for a Safari App Extension

```
<dict>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.Safari.extension</string>
    <key>NSExtensionPrincipalClass</key>
    <string>SafariExtensionHandler</string>
     <key>SFSafariToolbarItem</key>
    <dict>
        <key>Action</key>
        <string>Command</string>
        <key>Identifier</key>
        <string>Button</string>
        <key>Image</key>
        <string>ToolbarItemIcon.pdf</string>
        <key>Label</key>
        <string>Your Button</string>
    </dict>
   <key>SFSafariContextMenu</key>
    <array>
        <dict>
            <key>Text</key>
            <string>Search for selected text in MyApplication</string>
            <key>Command</key>
            <string>Search</string>
        </dict>
        <dict>
            <key>Text</key>
            <string>Add entry for selected text in MyApplication</string>
            <key>Command</key>
            <string>Add</string>
        </dict>
    </array>
    <key>SFSafariContentScript</key>
    <array>
        <dict>
            <key>Script</key>
            <string>script.js</string>
        </dict>
    </array>
    <key>SFSafariStyleSheet</key>
    <array>
        <dict>
            <key>Style Sheet</key>
            <string>script.js</string>
        </dict>
    </array>
    <key>SFSafariWebsiteAccess</key>
    <dict>
        <key>Allowed Domains</key>
        <array>
            <string>*.webkit.org</string>
        </array>
        <key>Level</key>
        <string>Some</string>
    </dict>
</dict>
```

In addition to the NSExtension keys, the `Info.plist` lets you add an `NSHumanReadableDescription` key for your Safari app extension. When the app extension is installed, the string value of this key appears in Safari Extensions Preferences.

`Array` - macOS. An array used to add content scripts to the app extension. Each value in the array is a dictionary, providing the filename for a content script.

This key is supported in macOS 10.11.5 and later.

Content scripts and style sheets have similar functionality. Content scripts (as `.js` files) are injected, and style sheets (as `.css` files) are applied to webpages to customize web content. Scripts and styles have the same access privileges as the scripts and styles executed from the webpage’s host. Scripts can also send messages to, and receive messages from, a Safari app extension.

For details on the `SFSafariContentScript` subkeys, see [Creating URL Patterns](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbt). Similar subkeys for `SFSafariStyleSheet` are shown in [Table 7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbr). For details on the URL Patterns subkeys for scripts and styles, see [URL Patterns for Scripts and Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbs).

__Table 7__  `SFSafariContentScript` subkeys

| Subkey | Type | Description |
| `Script` | String | Required. A string that specifies the path to the content script relative to the Resources folder in the extension's bundle; for example: `script.js`. |
| `Allowed URL Patterns` | Array | Optional. An array of URL patterns that describe which pages the script should be injected into. |
| `Excluded URL Patterns` | Array | Optional. An array of URL patterns that describe which pages the script cannot be injected into. |

For both `SFSafariContentScript` and `SFSafariStyleSheet`, the key’s `Allowed URL Patterns` and `Excluded URL Patterns` subkeys work in conjunction with the `SFSafariWebsiteAccess` key to specify the accessible webpages. First, access is limited by the `SFSafariWebsiteAccess` values, then the `Allowed URL Patterns` and `Excluded URL Patterns` keys are applied. Here’s how these keys work:

- If you do not specify either key, the file is injected into any website.
- If you specify the `Allowed URL Patterns` key, the value for this key is an array of domain patterns. The file is injected only into webpages whose URL matches one of these patterns.
- If you specify the `Excluded URL Patterns` key, the value for this key is an array of domain patterns. The file is not injected into any webpages whose URL matches any of these patterns.

If you specify `Some` access for your app extension, for example, you have access only to the domains matching your provided domain patterns. Items in your `Allowed URL Patterns` and `Excluded URL Patterns` create additional restrictions within those domains. Be sure all the items in your `Allowed URL Patterns` are within a domain you have access to.

A URL pattern takes the form _Scheme://Domain/Path_.

- _Scheme_ can be `http` or `https`.
- _Domain_ is the host domain, such as `developer.apple.com` or `www.example.co.jp`.
- _Path_ is the directory or webpage, such as `safari/` or `safari/library/navigation/index.html`.

A URL pattern can include the asterisk (\*) character to match any string. This allows you to specify all pages in a particular domain, for example, without having to create an exhaustive list.

The \* character can be used anywhere in the domain or path, but not in the scheme. Here are some examples:

- `http://*/*`—Matches all HTTP URLs.
- `http://*.example.com/*`—Matches all webpages from `example.com`.
- `http://subdomain.example.com/*`—Matches all webpages from `subdomain.example.com`.
- `http://www.example.com/thepath/thepage.html`—Matches one webpage.
- `https://*/*`—Matches all webpages that are delivered over HTTPS.
- `https://secure.example.com/accounts/*`—Matches all webpages from the `accounts` directory of `secure.example.com` that are delivered over HTTPS.

`Array` - macOS. An array used to add items to Safari’s context menu.

This key is supported in macOS 10.11.5 and later.

The `SFSafariContextMenu` key lets app your app extension add items to the context menu shown in webpages. For available subkeys, see Listing 1.

__Table 8__  `SFSafariContextMenu` subkeys

| Subkey | Type | Description |
| `Text` | String | Required. A string that specifies the text to display for the context menu item. |
| `Command` | String | Required. A string that the context menu item sends when activated. |

`Array` - macOS. An array used to add style sheets to the app extension. Each value in the array is a dictionary, providing the filename for a content script.

This key is supported in macOS 10.11.5 and later.

Content scripts and style sheets have similar functionality. Content scripts (as `.js` files) are injected and style sheets (as `.css` files) are applied to webpages to customize web content. Scripts and styles have the same access privileges as the scripts and styles executed from the webpage’s host. The scripts can also send messages to, and receive messages from, the extension.

For details on the `SFSafariContentScript` subkeys, see [Creating URL Patterns](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbt). Similar subkeys for `SFSafariStyleSheet` are shown in [Table 7](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbr). For details on the URL Patterns subkeys for scripts and styles, see [URL Patterns for Scripts and Styles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvonbs).

__Table 9__  `SFSafariStyleSheet` subkeys

| Subkey | Type | Description |
| `Style Sheet` | String | Required. A string that specifies the path to the style sheet relative to the Resources folder in the extension's bundle |
| `Allowed URL Patterns` | Array | Optional. An array of URL patterns that describe which pages the style sheet should be injected into. |
| `Excluded URL Patterns` | Array | Optional. An array of URL patterns that describe which pages the style sheet cannot be injected into. |

`Dictionary` - macOS. A dictionary used to add a toolbar item to Safari windows.

This key is supported in macOS 10.11.5 and later.

The `SFSafariToolbarItem` dictionary adds a toolbar item to Safari windows. Each app extension can have only one toolbar item. For available subkeys, see SFSafariContentScript.

__Table 10__  `SFSafariToolbarItem` subkeys

| Subkey | Type | Description |
| `Identifier` | String | Required. A string identifier for the toolbar item. |
| `Label` | String | Required. A string that is shown in the overflow menu, in the customize palette, and on hover. |
| `Image` | String | Required. A string specifying the filename of a scalable PDF image. The image must be transparent. See Toolbar Items. |
| `Action` | String | Required. A string specifying the command to send when the toolbar item is clicked. Available actions are `Command` and `Popover`. |

`Dictionary` - macOS. An optional dictionary that specifies which webpages the Safari app extension can access, if any.

This key is supported in macOS 10.11.5 and later.

The `SFSafariWebsiteAccess` dictionary specifies the webpages your app extension has access to. Only the webpages you choose have your app extension’s content injected into them, and only those webpages can be manipulated using the [SFSafariPageProperties](https://developer.apple.com/documentation/safariservices/sfsafaripageproperties) object. For available subkeys, see Safari App Extension Keys.

__Table 11__  `SFSafariWebsiteAccess` subkeys

| Subkey | Type | Description |
| `Level` | String | Required. A string that specifies the extent of the app extension’s website access. Available values are `All`, `None`, `Some`. |
| `Allowed Domains` | Array | If `Level` is `Some`, the `Allowed Domains` subkey is required and lists the allowed domains. Each domain in the array is specified as a string. |

Use the `Level` subkey to restrict your extension’s website access. Available values are as follows:

- `None`—Your app extension cannot access any webpages.
- `All`—Your app extension has access to all webpages.
- `Some`—Your app extension can access webpages from a list of domains. If you set your access to `Some`, and do not specify any domain patterns, your app extension cannot access any webpages.

  Each domain is specified as a string. For example: `developer.apple.com` or `www.example.org.jp`. Do _not_ include a scheme (such as `http://`) in the domain pattern.

  A leading `*` character matches all subdomains of the allowed domain. For example: `*.apple.com` matches `www.apple.com`, `developer.apple.com`, or any host name in the `apple.com` domain. Similarly, `*.co.jp` matches all `co.jp` domains, and `*.jp` matches all `.jp` domains.

Use the `SFSafariExtensionBundleIdentifiersToUninstall` key to specify any Safari extensions that you want to remove when your Safari app extension is loaded. The value for this key should be an array of strings. Each string is the bundle identifier of a Safari extension that should be removed. The Safari extensions must have been created by the same developer account that was used to create the Safari app extension.

When your app is installed, the Safari app extension is automatically installed and the Safari extensions you identified are removed from Safari. If any of the Safari extensions you listed are enabled when the upgrade occurs, the Safari app extension is enabled automatically.

The keys in this section pertain to app extensions employing the Share extension point. These keys, if used, must be placed as immediate children of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`Dictionary` - iOS, macOS. Also supported in an Action extension. Specifies the semantic data types that an app extension supports. For complete information, see [NSExtensionActivationRule](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjq).

This key is supported in iOS 8 and later and in macOS 10.10 and later.

`String` - iOS, macOS. Also supported in an Action extension. Specifies the name of a JavaScript file supplied by a Share extension. For complete information, see [NSExtensionJavaScriptPreprocessingFile](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomrx).

This key is supported in iOS 8 and later and in macOS 10.10 and later.

The key in this section pertains to app extensions employing the Unwanted Communication Reporting extension point. This key, if used, must be placed as an immediate child of the [NSExtensionAttributes](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2demjsfvjvomjr) key.

`String` - iOS. Contains a destination SMS number for reports. When the user reports an SMS or call, the system generates an SMS message and sends it to this phone number.

```
<dict>
    <key>NSExtensionAttributes</key>
    <dict>
        <key>ILClassificationExtensionSMSReportDestination</key>
        <string>[PHONE NUMBER]</string>
    </dict>
    <key>NSExtensionMainStoryboard</key>
    <string>MainInterface</string>
    <key>NSExtensionPointIdentifier</key>
    <string>com.apple.identitylookup.classification-ui</string>
</dict>
```

This key is supported in iOS 12.0 and later.

[Next](Document%20Revision%20History.md)[Previous](watchOS%20Keys.md)

