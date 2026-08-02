---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOResourceManager.html
archived_at: '2026-07-15T08:15:15.792738Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOResourceManager

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOResourceManager manages an application's resources. It defines methods that retrieve resources from standard directories. Each WebObjects application contains a resource manager object, which you can access by sending resourceManager to the WOApplication class

## Method Types

---

> **Retrieving resources**
> : [bytesForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5rhs5dfondg64ssmvzw65lsmnsu4ylnmvsa): [contentTypeForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5rw63tumvxhivdzobsum33skjsxg33vojrwkttbnvswi): [errorMessageUrlForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5sxe4tpojgwk43tmftwkvlsnrdg64ssmvzw65lsmnsu4ylnmvsa): [inputStreamForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5uw44dvorjxi4tfmfwum33skjsxg33vojrwkttbnvswi): [pathForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5ygc5diizxxeutfonxxk4tdmvhgc3lfmq): [urlForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf52xe3cgn5zfezltn52xey3fjzqw2zle)
>
> **Retrieving localized strings**
> : [stringForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zxi4tjnztum33sjnsxs)
>
> **Managing the application-wide data cache**
> : [flushDataCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5tgy5ltnbcgc5dbinqwg2df): [removeDataForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zgk3lpozsuiylumfdg64slmv4q): [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zwk5cemf2gc)
>
> **Other**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf52g6u3uojuw4zy)

## Constructors

---

### WOResourceManager

`protected WOResourceManager()`

Description forthcoming.

---

## Instance Methods

---

### bytesForResourceNamed

`public byte[] bytesForResourceNamed( String aResourceName, String aFrameworkName, NSArray aLanguagesList)`

Returns, as a Java byte array, the contents of the specified resource. When calling this method you must provide the name of the resource (including the filename extension) specified by_aResourceName_, the name of the framework in which the resource resides (or `null` if the resource resides within the application) specified by _aFrameworkName_, and an NSArray of String objects identifying the order in which the language-specific resources should be searched (supply `null` for this third argument specified by _aLanguageList_ if the default order is sufficient).

---

### contentTypeForResourceNamed

`public String contentTypeForResourceNamed(String aResourcePath)`

Returns a String containing the HTTP content type for the named resource specified by _aResourcePath_. The content type is determined based upon the filename extension; if the resource's filename supplied to this method has no extension or the extension isn't one of those listed in System/Library/Frameworks/JavaWebObjects/Resources/MIME.plist, this method returns "text/plain".

---

### errorMessageUrlForResourceNamed

`public String errorMessageUrlForResourceNamed( String aResourceName, String aFrameworkName)`

Returns a String containing an error URL for the resource name specified by _aResourceName_ and framework name specified by _aFrameworkName_. If a resource name is not supplied (that is, if `null` is passed as the first parameter), the error message will contain "null" in place of the resource name. If a framework name is passed as the second parameter, the error message will have the following form: `/ERROR/NOT_FOUND/framework=frameworkName/filename=resourceName`. If `null` is passed as the second parameter, the error message will include the application name instead of a framework name and will have the following form: `/ERROR/NOT_FOUND/app=applicationName/filename=resourceName`.

---

### flushDataCache

`public void flushDataCache()`

Removes all data from the image data cache. Use this method if you are storing data in the application-wide cache that you no longer need.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See Also:__ [removeDataForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zgk3lpozsuiylumfdg64slmv4q), [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zwk5cemf2gc)

---

### inputStreamForResourceNamed

`public java.io.InputStream inputStreamForResourceNamed( String aResourceName, String aFrameworkName, NSArray aLanguagesList)`

Returns a `java.io.InputStream` which you can use to read the contents of the specified resource. When calling this method you must provide the name of the resource (including the filename extension) specified by _aResourceName_, the name of the framework in which the resource resides (or `null` if the resource resides within the application) specified by _aFrameworkName_, and an NSArray of String objects identifying the order in which the language-specific resources should be searched (supply `null` for this third argument if the default order is sufficient) specified by _aLanguageList_.

---

### pathForResourceNamed

`public String pathForResourceNamed( String aResourceFile, String aFrameworkName, NSArray languagesList)`

Returns the absolute path for the resource _aResourceFile_. Include the file's extension when specifying _aResourceFile_. If the file is in the application, specify null for the framework argument.

This method always returns a path like __/Local/Library/WebObjects/Applications/MyApp.woa/WebServerResources/MyResource__. It does not return the path relative to the HTTP server's document root unless the entire application is located in the document root.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See Also:__ [urlForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf52xe3cgn5zfezltn52xey3fjzqw2zle)

---

### removeDataForKey

`public void removeDataForKey( String key, WOSession aSession)`

Removes the data stored in the data cache under the key key. The session argument is currently ignored; specify null to have WOResourceManager use the application-wide cache.

This method is used by default when a dynamic element requests an image or embedded object from a database and the __key__ attribute is not set for that dynamic element. If the __key__ attribute isn't set, the data retrieved from the database is stored in the cache using [setData](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zwk5cemf2gc), sent to the dynamic element, and then removed from the cache using __removeDataForKey__. If the __key__ attribute is set, __removeDataForKey__ is not invoked.

You rarely need to invoke this method yourself. Use it only if you need to limit the amount of memory your application uses, if your application has data stored in the cache, and you know that the data is no longer needed.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See Also:__ [flushDataCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5tgy5ltnbcgc5dbinqwg2df)

---

### setData

`public void setData( NSData someData, String key, String mimeType, WOSession aSession)`

Adds the image or embbedded object someData of MIME type type to the data cache for the session specify by aSession. The data is stored under the key key. The session argument is currently ignored; specify null to have WOResourceManager use the application-wide cache.

This method is invoked any time a dynamic element requests an image or embedded object from a database. You rarely need to invoke it yourself.

By default when a dynamic element requests an image from the database, WOResourceManager fetches the image, stores it in the cache using __setData__, sends it to the dynamic element, and then removes it from the cache using [removeDataForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5zgk3lpozsuiylumfdg64slmv4q). However, if the dynamic element has a __key__ attribute defined, then the image is stored in the database under that key, and it is not removed from the database.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See Also:__ [flushDataCache](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5tgy5ltnbcgc5dbinqwg2df)

---

### stringForKey

`public String stringForKey( String aKey, String aTableName, String aDefaultValue, String aFrameworkName, NSArray languagesList)`

Returns a localized string from string table _aTable___.strings__ using _aKey_ to look it up. If no string value for the key is found in the table, _aDefaultValue_ (optional) is returned. The method first searches the _aTable___.strings__ file, if it exists, in each of the localized (__.lproj__) subdirectories of the application wrapper; searching proceeds in the order specified by the array _languagesList_. If no string value matching the key is found, the search then continues to the _aTable___.strings__ file (if it exists) directly under the Resources directory (inside the directory with the __.woa__ extension).

---

### __toString__

`public String toString()`

Returns a String representation of the receiver suitable for debugging purposes.

---

### urlForResourceNamed

`public String urlForResourceNamed( String aResourceFile, String aFrameworkName, NSArray languagesList, WORequest aRequest)`

Returns the URL associated with a resource named _aResourceFile_. The URL returned is of the following form:

__WebObjects/MyApp.woa/WebServerResources/English.lproj/___aResourceFile_

Include the file's extension when specifying _aResourceFile_. If the file is in the application, specify null for the framework argument.

This method locates resources under the application or framework. The URL returned is computed by concatenating the application's base URL (returned by WOApplication's baseURL method and settable using the WOApplicationBaseURL user default) and the relative path of the resource. This method does not check to see if the file is actually under the document root. For example, if your application is installed in __/Local/Library/WebObjects/Applications__, and the method finds _aResourceFile_ in the __Resources__ directory, it returns:

__/WebObjects/MyApp.woa/Resources/___aResourceFile_

even though the __Resources__ directory is not under the document root.

Access to the WOResourceManager object is locked at the beginning of this method and unlocked at the end.

__See Also:__ [pathForResourceNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkjsxg33vojrwktlbnzqwozlsf5ygc5diizxxeutfonxxk4tdmvhgc3lfmq)

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
