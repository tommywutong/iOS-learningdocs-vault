---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOResourceManager.html
archived_at: '2026-07-18T01:28:54.321839Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WORequestHandler-2.md)
[!](WOResponse-2.md)

---

# WOResourceManager

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOResourceManager.h

---

## Class Description

WOResourceManager manages an application's resources. It defines methods that retrieve resources from standard directories. Each WebObjects application contains a resource manager object, which you can access by sending [__resourceManager__](WOApplication-2.md#apple-haydcmq) to the WOApplication class

---

# Adopted Protocols

**NSLocking**

**[- lock](#apple-ge4dsmq)

**[- unlock](#apple-g4zq)****

---

## Method Types

**Retrieving resources**

**[- pathForResourceNamed:inFramework:languages:](#apple-gu3q)

**[- urlForResourceNamed:inFramework:languages:request:](#apple-g43q)****

**Retrieving localized strings**

**[- stringForKey:inTableNamed:withDefaultValue:inFramework:
languages:](#apple-gi2deoi)**

**Managing the application-wide data cache**

**[- flushDataCache](#apple-gq4q)

**[- removeDataForKey:session:](#apple-gyytanq)

**[- setData:forKey:mimeType:session:](#apple-gy2q)******

---

## Instance Methods

---

### flushDataCache

- (void)__flushDataCache__

Removes all data from the image data cache. Use this method if you are storing data in the application-wide cache that you no longer need.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[- __removeDataForKey:session:__](#apple-gyytanq), [- __setData:forKey:mimeType:session:__](#apple-gy2q)

---

### lock

- (void)__lock__

Locks access to the WOResourceManager object. When the WOResourceManager is locked, no other threads may access it.

Usually, you don't need to invoke this method in your own code. All messages that you send to a WOResourceManager object lock access to the object at the beginning of the method and unlock access at the end. You only need to use this method if you're subclassing WOResourceManager. In that case, you should lock access to the WOResourceManager object in methods that load resources.

__See also:__
[- __unlock__](#apple-g4zq)

---

### pathForResourceNamed:inFramework:languages:

- (NSString \*)__pathForResourceNamed:__ (NSString \*)_aResourceFile___inFramework:__ (NSString \*)_aFrameworkName___languages:__ (NSArray \*)_languagesList_

Returns the absolute path for the resource _aResourceFile_. Include the file's extension when specifying _aResourceFile_. If the file is in the application, specify __lnil__  for the framework argument.

This method always returns a path like __/Local/Library/WebObjects/Applications/MyApp.woa/WebServerResources/MyResource__ . It does not return the path relative to the HTTP server's document root unless the entire application is located in the document root.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[- __urlForResourceNamed:inFramework:languages:request:__](#apple-g43q)

---

### removeDataForKey:session:

- (void)__removeDataForKey:__ (NSString \*)_key_ __session:__ (WOSession \*)_aSession_

Removes the data stored in the data cache under the key _key_. The session argument is currently ignored; specify __nil__  to have WOResourceManager use the application-wide cache.

This method is used by default when a dynamic element requests an image or embedded object from a database and the __key__  attribute is not set for that dynamic element. If the __key__  attribute isn't set, the data retrieved from the database is stored in the cache using [__setData:forKey:mimeType:session:__](#apple-gy2q), sent to the dynamic element, and then removed from the cache using __removeDataForKey:session:__ . If the __key__  attribute is set, __removeDataForKey:session:__  is not invoked.

You rarely need to invoke this method yourself. Use it only if you need to limit the amount of memory your application uses, if your application has data stored in the cache, and you know that the data is no longer needed.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[- __flushDataCache__](#apple-gq4q)

---

### setData:forKey:mimeType:session:

- (void)__setData:__ (NSData \*)_someData___forKey:__ (NSString \*)_key___mimeType:__ (NSString \*)_type___session:__ (WOSession \*)_aSession_

Adds the image or embbedded object _someData_ of MIME type _type_ to the data cache for the session specify by _aSession_. The data is stored under the key _key_. The session argument is currently ignored; specify __nil__  to have WOResourceManager use the application-wide cache.

This method is invoked any time a dynamic element requests an image or embedded object from a database. You rarely need to invoke it yourself.

By default when a dynamic element requests an image from the database, WOResourceManager fetches the image, stores it in the cache using __setData:forKey:mimeType:session:__ , sends it to the dynamic element, and then removes it from the cache using [__removeDataForKey:session:__](#apple-gyytanq). However, if the dynamic element has a __key__  attribute defined, then the image is stored in the database under that key, and it is not removed from the database.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[- __flushDataCache__](#apple-gq4q)

---

### stringForKey:inTableNamed:withDefaultValue:inFramework:languages:

- (NSString \*)__stringForKey:__ (NSString \*)_aKey___inTableNamed:__ (NSString \*)_aTableName___withDefaultValue:__ (NSString \*)_aDefaultValue___inFramework:__ (NSString \*)_aFrameworkName_
__languages:__ (NSArray \*)_languagesList_

Returns a localized string from string table _aTable___.strings__  using _aKey_ to look it up. If no string value for the key is found in the table, _aDefaultValue_ (optional) is returned. The method first searches the _aTable___.strings__  file, if it exists, in each of the localized (__.lproj__ ) subdirectories of the application wrapper; searching proceeds in the order specified by the array _languagesList_. If no string value matching the key is found, the search then continues to the _aTable___.strings__  file (if it exists) directly under the Resources directory (inside the directory with the __.woa__  extension).

---

### unlock

- (void)__unlock__

Removes the lock on the WOResourceManager object, allowing other threads to access it.

Usually, you don't need to invoke this method in your own code. All messages that you send to a WOResourceManager object lock access to the object at the beginning of the method and unlock access at the end. You only need to use this method if you're subclassing WOResourceManager. In that case, you should lock access to the WOResourceManager object in methods that load resources and unlock when the method is finished accessing the WOResourceManager object.

__See also:__
[- __lock__](#apple-ge4dsmq)

---

### urlForResourceNamed:inFramework:languages:request:

- (NSString \*)__urlForResourceNamed:__ (NSString \*)_aResourceFile___inFramework:__ (NSString \*)_aFrameworkName___languages:__ (NSArray \*)_languagesList___request:__ (WORequest \*)_aRequest_

Returns the URL associated with a resource named _aResourceFile_. The URL returned is of the following form:

__WebObjects/MyApp.woa/WebServerResources/English.lproj/__ _aResourceFile_

Include the file's extension when specifying _aResourceFile_. If the file is in the application, specify__l__  __nil__  for the framework argument.

This method locates resources under the application or framework. The URL returned is computed by concatenating the application's base URL (returned by WOApplication's [__baseURL__](WOApplication-2.md#apple-g43tcni) method and settable using the WOApplicationBaseURL user default) and the relative path of the resource. This method does not check to see if the file is actually under the document root. For example, if your application is installed in __/Local/Library/WebObjects/Applications__ , and the method finds _aResourceFile_ in the __Resources__  directory, it returns:

__/WebObjects/MyApp.woa/Resources/__ _aResourceFile_

even though the __Resources__  directory is not under the document root.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See also:__
[- __pathForResourceNamed:inFramework:languages:__](#apple-gu3q)

****

---

[!](WORequestHandler-2.md)
[!](WOResponse-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
