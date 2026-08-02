---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOResourceManager.html
archived_at: '2026-07-18T01:28:52.285151Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WORequestHandler.md)
[!](WOResponse.md)

---

# WOResourceManager

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WOResourceManager manages an application's resources. It defines methods that retrieve resources from standard directories. Each WebObjects application contains a resource manager object, which you can access by sending [`resourceManager`](WOApplication.md#apple-haydcmq) to the WOApplication class

---

## Method Types

**Retrieving resources**

**[pathForResourceNamed](#apple-gu3q)

**[urlForResourceNamed](#apple-g43q)****

**Retrieving localized strings**

**[stringForKey](#apple-gi2deoi)**

**Managing the application-wide data cache**

**[flushDataCache](#apple-gq4q)

**[setData](#apple-gy2q)****

**Controlling access**

**[lock](#apple-ge4dsmq)

**[unlock](#apple-g4zq)****

---

## Instance Methods

---

### flushDataCache

public void `flushDataCache`()

Removes all data from the image data cache. Use this method if you are storing data in the application-wide cache that you no longer need.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
, [`setData`](#apple-gy2q)

---

### lock

public void `lock`()

Locks access to the WOResourceManager object. When the WOResourceManager is locked, no other threads may access it.

Usually, you don't need to invoke this method in your own code. All messages that you send to a WOResourceManager object lock access to the object at the beginning of the method and unlock access at the end. You only need to use this method if you're subclassing WOResourceManager. In that case, you should lock access to the WOResourceManager object in methods that load resources.

__See also:__
[`unlock`](#apple-g4zq)

---

### pathForResourceNamed

public java.lang.String `pathForResourceNamed`(java.lang.String _aResourceFile_, java.lang.String _aFrameworkName_,
NSArray _languagesList_)

Returns the absolute path for the resource _aResourceFile_. Include the file's extension when specifying _aResourceFile_. If the file is in the application, specify `null` for the framework argument.

This method always returns a path like `/Local/Library/WebObjects/Applications/MyApp.woa/WebServerResources/MyResource`. It does not return the path relative to the HTTP server's document root unless the entire application is located in the document root.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[`urlForResourceNamed`](#apple-g43q)

__removeDataForKey__ public void `removeDataForKey`(java.lang.String _key_, WOSession _aSession_)

Removes the data stored in the data cache under the key _key_. The session argument is currently ignored; specify `null` to have WOResourceManager use the application-wide cache.

This method is used by default when a dynamic element requests an image or embedded object from a database and the `key` attribute is not set for that dynamic element. If the `key` attribute isn't set, the data retrieved from the database is stored in the cache using [`setData`](#apple-gy2q), sent to the dynamic element, and then removed from the cache using `removeDataForKey:session:`. If the `key` attribute is set, `removeDataForKey:session:` is not invoked.

You rarely need to invoke this method yourself. Use it only if you need to limit the amount of memory your application uses, if your application has data stored in the cache, and you know that the data is no longer needed.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[`flushDataCache`](#apple-gq4q)

---

### setData

public void `setData`(NSData _someData_,
java.lang.String _key_,
java.lang.String _mimeType_,
WOSession _aSession_)

Adds the image or embbedded object _someData_ of MIME type _type_ to the data cache for the session specify by _aSession_. The data is stored under the key _key_. The session argument is currently ignored; specify `null` to have WOResourceManager use the application-wide cache.

This method is invoked any time a dynamic element requests an image or embedded object from a database. You rarely need to invoke it yourself.

By default when a dynamic element requests an image from the database, WOResourceManager fetches the image, stores it in the cache using `setData:forKey:mimeType:session:`, sends it to the dynamic element, and then removes it from the cache using `removeDataForKeypublic void removeDataForKey(java.lang.String key, WOSession aSession)`. However, if the dynamic element has a `key` attribute defined, then the image is stored in the database under that key, and it is not removed from the database.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[`flushDataCache`](#apple-gq4q)

---

### stringForKey

public java.lang.String `stringForKey`(java.lang.String _aKey_,
java.lang.String _aTableName_,
java.lang.String _aDefaultValue_,
java.lang.String _aFrameworkName_,
NSArray _languagesList_)

Returns a localized string from string table _aTable_`.strings` using _aKey_ to look it up. If no string value for the key is found in the table, _aDefaultValue_ (optional) is returned. The method first searches the _aTable_`.strings` file, if it exists, in each of the localized (`.lproj`) subdirectories of the application wrapper; searching proceeds in the order specified by the array _languagesList_. If no string value matching the key is found, the search then continues to the _aTable_`.strings` file (if it exists) directly under the Resources directory (inside the directory with the `.woa` extension).

---

### unlock

public void `unlock`()

Removes the lock on the WOResourceManager object, allowing other threads to access it.

Usually, you don't need to invoke this method in your own code. All messages that you send to a WOResourceManager object lock access to the object at the beginning of the method and unlock access at the end. You only need to use this method if you're subclassing WOResourceManager. In that case, you should lock access to the WOResourceManager object in methods that load resources and unlock when the method is finished accessing the WOResourceManager object.

__See also:__
[`lock`](#apple-ge4dsmq)

---

### urlForResourceNamed

public java.lang.String `urlForResourceNamed`(java.lang.String _aResourceFile_, java.lang.String _aFrameworkName_,
NSArray _languagesList_,
WORequest _aRequest_)

Returns the URL associated with a resource named _aResourceFile_. The URL returned is of the following form:

`WebObjects/MyApp.woa/WebServerResources/English.lproj/`_aResourceFile_

Include the file's extension when specifying _aResourceFile_. If the file is in the application, specify `null` for the framework argument.

This method locates resources under the application or framework. The URL returned is computed by concatenating the application's base URL (returned by WOApplication's [`baseURL`](WOApplication.md#apple-g43tcni) method and settable using the WOApplicationBaseURL user default) and the relative path of the resource. This method does not check to see if the file is actually under the document root. For example, if your application is installed in `/Local/Library/WebObjects/Applications`, and the method finds _aResourceFile_ in the `Resources` directory, it returns:

`/WebObjects/MyApp.woa/Resources/`_aResourceFile_

even though the `Resources` directory is not under the document root.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[`pathForResourceNamed`](#apple-gu3q)

****

---

[!](WORequestHandler.md)
[!](WOResponse.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
