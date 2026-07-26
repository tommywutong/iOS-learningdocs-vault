---
title: UserDefaults
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/userdefaults
source_url: 'https://developer.apple.com/documentation/foundation/userdefaults'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/userdefaults.json'
content_hash: 'sha256:cca056467d7ad6e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# UserDefaults

<sub>Class</sub>

An interface to the user’s defaults database, which stores system-wide and app-specific settings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class UserDefaults
```

## Overview

A `UserDefaults` object provides access to the defaults system, which is a persistent store for app-specific and system-wide settings. You use this system to store nonsensitive information, such as app-specific configuration details. The system also stores configuration details that apply to all apps, such as the current language settings for the device. In your code, you check values from this system and use them to dynamically alter your app’s appearance or behavior. The term _defaults_ refers to the fact that the stored data determines the default startup state and behavior.

> [!important] Important
> Don’t store personal or sensitive information as settings. The defaults system stores information on disk in an unencrypted format. Store personal or sensitive information in the person’s Keychain instead.

To access the defaults system, obtain a `UserDefaults` object and call its methods to read and write values. The [standardUserDefaults](userdefaults/standard.md) object is a shared object you use to read and write your app’s standard settings. You can also create unique `UserDefaults` objects to manage specific sets of settings. For example, you can create a `UserDefaults` object that reads and writes settings your app shares with an app extension. Don’t subclass `UserDefaults`.

Each item you store in a defaults object consists of a key-value pair, where each key is a string that you use to locate the item and each value is a data object. The defaults database supports the same value types found in property list files, including types like [Int](../swift/int.md), [Float](../swift/float.md), [Double](../swift/double.md), [Bool](../swift/bool.md), [String](../swift/string.md), [URL](url.md), [NSNumber](nsnumber.md), [Date](date.md), [Array](../swift/array.md), and [Dictionary](../swift/dictionary.md). To include other types of objects in the defaults database, archive them to a [Data](data.md) object first and store that object instead. Prefer simple types over custom objects whenever possible.

With the exception of managed devices in educational institutions, the system stores defaults locally on the current device. When you write values to a `UserDefaults` object, the object updates its in-memory version of that information right away, and writes the value to disk asynchronously.  When someone backs up their device, the system includes any persistent defaults databases in the backup data. Because the data is device-specific, you don’t use the defaults system to share data between devices. To share data between someone’s devices, use the [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) instead.

> [!warning] Warning
> Don’t access the files of the defaults database directly from the file system. Modifying one of the underlying files directly may cause data loss, a delay in changes being available, or an app crash. In macOS, use the `defaults` command-line utility to safely view or modify the defaults database outside of your app.

While your app is running, the defaults system generates notifications to let you know when values change. To observe changes to individual settings, add a [key-value observer](../swift/using-key-value-observing-in-swift.md) to your `UserDefaults` object, using key names to build the path to the setting you want. To observe changes for all settings, register for a [DidChangeMessage](userdefaults/didchangemessage.md) or [NSUserDefaultsDidChangeNotification](userdefaults/didchangenotification.md) with your `UserDefaults` object.

The `UserDefaults` type is thread-safe, and you can use the same object in multiple threads or tasks simultaneously.

> [!important] Important
> This API has the potential of being misused to access device signals to try to identify the device or user, also known as fingerprinting. Regardless of whether a user gives your app permission to track, fingerprinting is not allowed. When you use this API in your app or third-party SDK (an SDK not provided by Apple), declare your usage and the reason for using the API in your app or third-party SDK’s `PrivacyInfo.xcprivacy` file. For more information, including the list of valid reasons for using the API, see [Describing use of required reason API](../bundleresources/describing-use-of-required-reason-api.md).

### Domains and settings search paths

To integrate settings from different sources, the defaults system organizes them into domains. An app defines its own custom settings, but the system defines settings that apply to all apps. Similarly, you might choose to override a specific setting temporarily to test one of your app’s features. The defaults system provides domains for each of these cases along with several others.

When you request the value of a setting, the `UserDefaults` object searches its domains in a specific order until it finds the value you want. The following table lists the key domains that the defaults system supports and their search order. Some domains might not be present for all apps. For example, the managed domain is present only on administrator-managed devices.

| Domain | Type | Description |
|---|---|---|
| Managed | persistent | This domain contains settings that an administrator provided for a managed device. The system saves these values persistently on the current device. |
| [Argument](userdefaults/argumentdomain.md) | volatile | This domain contains the settings you specified when launching your app from the command-line or Xcode. These keys represent temporary overrides of settings, and the system discards them after the app quits. |
| Educational managed | persistent | For managed devices in an educational institution, this domain contains any settings saved to the iCloud key-value store for that institution. The system saves these settings persistently on a server, not on the device. |
| App | persistent | This domain contains the settings your app saves, either programmatically or using its settings UI. Each `UserDefaults` object writes settings to this group, associating them with the app itself or the app group you used to initialize the object. The system saves these settings persistently on the current device. |
| Suite | persistent | This domain contains custom settings from an app group or other app you specify at runtime. This domain is absent by default, but you can add a suite using the [- addSuiteNamed:](<userdefaults/addsuite(named_).md>) method. The system saves these settings persistently on the current device. |
| [Global](userdefaults/globaldomain.md) | persistent | This domain contains keys present for all apps on the system. The system provides the keys for this domain, and apps can’t write to it. The system saves these settings persistently on the current device. |
| [Registration](userdefaults/registrationdomain.md) | volatile | This domain contains system-provided default values and the default values you register for your app at launch time. Registering a set of default values prevents your code from receiving `nil` values when requesting a setting. The system discards these values when your app quits, so you must register them each time your app launches. |

The system stores data for most persistent domains on the current device, and doesn’t share that data with other devices. To share settings among all of a person’s devices, save them using an [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) object instead.

### Settings in managed environments

If your app supports managed environments, an administrator might configure any managed devices with a default set of settings. For example, in a computer lab or classrom environment, a teacher might set default settings that the lessons require. Apps can’t write to managed domains, so if your app encounters a managed setting, disable or hide any controls that someone might use to change that setting’s value. To determine if a setting is managed, call the [- objectIsForcedForKey:](<userdefaults/objectisforced(forkey_).md>) or [- objectIsForcedForKey:inDomain:](<userdefaults/objectisforced(forkey_indomain_).md>) method of your `UserDefaults` object.

An app running on a managed device can use [NSUbiquitousKeyValueStore](nsubiquitouskeyvaluestore.md) to share small amounts of data with the person’s other devices. Use this store for data that your app can safely share with other instances of itself. For example, a textbook app might save the current page number so that the person can continue reading from the same place on any of their devices.

For more details about managing devices, see [Device Management](../devicemanagement.md).

### Sandbox considerations

A sandboxed app cannot access or modify the settings of another app or process, with the following exceptions:

- An app can modify settings for one of its app extensions.
- An app can modify settings for an app group to which it belongs.

If you use the [- addSuiteNamed:](<userdefaults/addsuite(named_).md>) method to add the identifier for an unrelated app, the method doesn’t give you access to the other app’s settings. Instead, the system writes changes to your app’s settings, not to the third-party app’s settings.

> [!important] Important
> An app that accesses settings in a suite must also have the [App Groups entitlement](../bundleresources/entitlements/com.apple.security.application-groups.md).

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a user defaults object

- [standardUserDefaults](userdefaults/standard.md) — The shared defaults object for the current app.
- [- init](<userdefaults/init().md>) — Creates a new defaults object and initializes it with the app’s current settings.
- [- initWithSuiteName:](<userdefaults/init(suitename_).md>) — Creates a new defaults object and initializes it with the settings from the specified database.

### Registering default settings

- [- registerDefaults:](<userdefaults/register(defaults_).md>) — Specifies the set of default settings and values to use as a fallback in cases where the app domain doesn’t have them.

### Getting the value of a key

- [- boolForKey:](<userdefaults/bool(forkey_).md>) — Returns the Boolean value associated with the specified key.
- [- integerForKey:](<userdefaults/integer(forkey_).md>) — Returns the integer value associated with the specified key.
- [- floatForKey:](<userdefaults/float(forkey_).md>) — Returns the floating-point value associated with the specified key.
- [- doubleForKey:](<userdefaults/double(forkey_).md>) — Returns the double value associated with the specified key.
- [- URLForKey:](<userdefaults/url(forkey_).md>) — Returns the URL associated with the specified key.
- [- stringForKey:](<userdefaults/string(forkey_).md>) — Returns the string associated with the specified key.
- [- stringArrayForKey:](<userdefaults/stringarray(forkey_).md>) — Returns the array of strings associated with the specified key.
- [- dataForKey:](<userdefaults/data(forkey_).md>) — Returns the data object associated with the specified key.
- [- objectForKey:](<userdefaults/object(forkey_).md>) — Returns the object associated with the specified key.
- [- arrayForKey:](<userdefaults/array(forkey_).md>) — Returns the array associated with the specified key.
- [- dictionaryForKey:](<userdefaults/dictionary(forkey_).md>) — Returns the dictionary object associated with the specified key.
- [- dictionaryRepresentation](<userdefaults/dictionaryrepresentation().md>) — Returns a dictionary with the union of all key-value pairs found from all domains.

### Setting the value for a key

- [- setBool:forKey:](<userdefaults/set(__forkey_)-3nn5m.md>) — Sets the value of the specified key to a Boolean value.
- [- setInteger:forKey:](<userdefaults/set(__forkey_)-3v852.md>) — Sets the value of the specified key to an integer.
- [- setFloat:forKey:](<userdefaults/set(__forkey_)-1t5ec.md>) — Sets the value of the specified key to a floating-point number.
- [- setDouble:forKey:](<userdefaults/set(__forkey_)-2w22f.md>) — Sets the value of the specified key to a double.
- [- setURL:forKey:](<userdefaults/set(__forkey_)-2bqjt.md>) — Sets the value of the specified key to a URL.
- [- setObject:forKey:](<userdefaults/set(__forkey_)-8ab6d.md>) — Sets the value of the specified key to a property list object.

### Monitoring settings changes and issues

- [DidChangeMessage](userdefaults/didchangemessage.md) — A message the system sends when a user-defaults setting changes.
- [NSUserDefaultsDidChangeNotification](userdefaults/didchangenotification.md) — Posted when the current process changes the value of a setting.
- [SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md) — A message the system sends when the size of the data in the defaults database exceeds the maximum.
- [NSUserDefaultsSizeLimitExceededNotification](userdefaults/sizelimitexceedednotification.md) — Posted when the amount of data in the defaults database exceeds the allowed maximum.

### Removing settings values

- [- removeObjectForKey:](<userdefaults/removeobject(forkey_).md>) — Removes the value for the specified key from the defaults database.

### Adding and removing search domains

- [- addSuiteNamed:](<userdefaults/addsuite(named_).md>) — Inserts settings for the specified domain into the search list of the current object.
- [- removeSuiteNamed:](<userdefaults/removesuite(named_).md>) — Removes the specified domain from the search list of the current object.

### Getting the domain names

- [NSArgumentDomain](userdefaults/argumentdomain.md) — The identifier for the domain that contains command-line settings.
- [NSGlobalDomain](userdefaults/globaldomain.md) — The identifier for the domain that contains system-specified settings for all apps.
- [NSRegistrationDomain](userdefaults/registrationdomain.md) — The identifier for the domain that contains your app’s registered default values.
- [volatileDomainNames](userdefaults/volatiledomainnames.md) — An array of identifiers for the volatile domains associated with the current object.

### Managing domain-specific values

- [- persistentDomainForName:](<userdefaults/persistentdomain(forname_).md>) — Retrieves the settings from the specified persistent domain.
- [- setPersistentDomain:forName:](<userdefaults/setpersistentdomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- volatileDomainForName:](<userdefaults/volatiledomain(forname_).md>) — Retrieves the settings from the specified volatile domain.
- [- setVolatileDomain:forName:](<userdefaults/setvolatiledomain(__forname_).md>) — Replaces the keys and values in the specified domain with the new keys and values you supply.
- [- removePersistentDomainForName:](<userdefaults/removepersistentdomain(forname_).md>) — Removes the keys and values from the specified persistent domain.
- [- removeVolatileDomainForName:](<userdefaults/removevolatiledomain(forname_).md>) — Removes the keys and values from the specified volatile domain.

### Checking for managed keys

- [- objectIsForcedForKey:](<userdefaults/objectisforced(forkey_).md>) — Returns a Boolean value that indicates whether an administrator provided the value for the specified key.
- [- objectIsForcedForKey:inDomain:](<userdefaults/objectisforced(forkey_indomain_).md>) — Returns a Boolean value that indicates whether an administrator provided the value for the key in the specified domain.

### Deprecated

- [- initWithUser:](<userdefaults/init(user_).md>) — Creates a user defaults object initialized with the defaults for the specified user account. _(deprecated)_
- [- synchronize](<userdefaults/synchronize().md>) — Waits for any pending asynchronous updates to the defaults database and returns; this method is unnecessary and shouldn’t be used.
- [+ resetStandardUserDefaults](<userdefaults/resetstandarduserdefaults().md>) — This method has no effect and shouldn’t be used.
- [- persistentDomainNames](<userdefaults/persistentdomainnames().md>) — Returns an array of the current persistent domain names. _(deprecated)_
- [NSUbiquitousUserDefaultsCompletedInitialSyncNotification](userdefaults/completedinitialcloudsyncnotification.md) — Posted when ubiquitous defaults finish downloading data, either the first time a device is connected to an iCloud account or when a user switches their primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsDidChangeAccountsNotification](userdefaults/didchangecloudaccountsnotification.md) — Posted when the user changes the primary iCloud account. _(deprecated)_
- [NSUbiquitousUserDefaultsNoCloudAccountNotification](userdefaults/nocloudaccountnotification.md) — Posted when a cloud default is set, but no iCloud user is logged in. _(deprecated)_
- [Language-Dependent Information Constants](language-dependent-information-constants.md) — These constants are deprecated and shouldn’t be used.

## See Also

### App-specific settings

- [Accessing settings from your code](accessing-settings-from-your-code.md) — Retrieve or change settings and monitor external changes to those values while your app runs.
