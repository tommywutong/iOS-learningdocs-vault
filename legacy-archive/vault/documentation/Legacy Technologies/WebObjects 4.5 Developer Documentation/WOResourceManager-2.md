---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/ObjC_classic/Classes/WOResourceManager.html
archived_at: '2026-07-15T08:11:47.723796Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOResourceManager

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  WebObjects/WOResourceManager.h

---

## Class Description

---

WOResourceManager manages an application's resources. It
defines methods that retrieve resources from standard directories.
Each WebObjects application contains a resource manager object,
which you can access by sending [resourceManager](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5zgk43povzggzknmfxgcz3foi) to the WOApplication
class

## Adopted Protocols

---

> NSLocking: [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpnrxwg2y)
> : [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovxgy33dnm)

## Method Types

---

> **Retrieving resources**
> : [- pathForResourceNamed:inFramework:languages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpobqxi2cgn5zfezltn52xey3fjzqw2zlehjuw4rtsmfwwk53pojvtu3dbnztxkylhmvztu)
> : [- urlForResourceNamed:inFramework:languages:request:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovzgyrtpojjgk43povzggzkomfwwkzb2nfxem4tbnvsxo33snm5gyylom52wcz3fom5hezlrovsxg5b2)
>
> **Retrieving localized
> strings**
> : [- stringForKey:inTableNamed:withDefaultValue:inFramework:languages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpon2he2lom5dg64slmv4tu2lokrqwe3dfjzqw2zlehj3ws5diirswmylvnr2fmylmovstu2loizzgc3lfo5xxe2z2nrqw4z3vmftwk4z2)
>
> **Managing the application-wide
> data cache**
> : [- flushDataCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpmzwhk43iirqxiykdmfrwqzi)
> : [- removeDataForKey:session:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpojsw233wmvcgc5dbizxxes3fpe5hgzltonuw63r2)
> : [- setData:forKey:mimeType:session:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rponsxirdborqtuztpojfwk6j2nvuw2zkupfygkottmvzxg2lpny5a)

## Instance Methods

---

### flushDataCache

`- (void)flushDataCache`

Removes all data from the image data cache.
Use this method if you are storing data in the application-wide
cache that you no longer need.

Access to the WOResourceManager
object is locked at the beginning of this method and unlocked at the
end.

__See Also:__  [- removeDataForKey:session:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpojsw233wmvcgc5dbizxxes3fpe5hgzltonuw63r2), [- setData:forKey:mimeType:session:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rponsxirdborqtuztpojfwk6j2nvuw2zkupfygkottmvzxg2lpny5a)

---

### lock

`- (void)lock`

Locks access to the WOResourceManager object.
When the WOResourceManager is locked, no other threads may access
it.

Usually, you don't need to invoke this method in your
own code. All messages that you send to a WOResourceManager object
lock access to the object at the beginning of the method and unlock
access at the end. You only need to use this method if you're
subclassing WOResourceManager. In that case, you should lock access
to the WOResourceManager object in methods that load resources.

__See
Also:__  [- unlock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovxgy33dnm)

---

### pathForResourceNamed:inFramework:languages:

`- (NSString *)pathForResourceNamed:(NSString
*)aResourceFile
inFramework:(NSString *)aFrameworkName
languages:(NSArray *)languagesList`

Returns the absolute path for the resource _aResourceFile_.
Include the file's extension when specifying _aResourceFile_.
If the file is in the application, specify nil for the framework
argument.

This method always returns a path like __/Local/Library/WebObjects/Applications/MyApp.woa/WebServerResources/MyResource__.
It does not return the path relative to the HTTP server's document
root unless the entire application is located in the document root.

Access
to the WOResourceManager object is locked at the beginning of this
method and unlocked at the end.

__See
Also:__  [- urlForResourceNamed:inFramework:languages:request:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpovzgyrtpojjgk43povzggzkomfwwkzb2nfxem4tbnvsxo33snm5gyylom52wcz3fom5hezlrovsxg5b2)

---

### removeDataForKey:session:

`- (void)removeDataForKey:(NSString
*)key
session:(WOSession *)aSession`

Removes the data stored in the data cache under
the key key. The session argument is currently ignored; specify nil to
have WOResourceManager use the application-wide cache.

This
method is used by default when a dynamic element requests an image
or embedded object from a database and the __key__ attribute
is not set for that dynamic element. If the __key__ attribute
isn't set, the data retrieved from the database is stored in the
cache using [setData:forKey:mimeType:session:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rponsxirdborqtuztpojfwk6j2nvuw2zkupfygkottmvzxg2lpny5a),
sent to the dynamic element, and then removed from the cache using __removeDataForKey:session:__.
If the __key__ attribute is set, __removeDataForKey:session:__ is
not invoked.

You rarely need to invoke this method
yourself. Use it only if you need to limit the amount of memory your
application uses, if your application has data stored in the cache,
and you know that the data is no longer needed.

Access
to the WOResourceManager object is locked at the beginning of this
method and unlocked at the end.

__See
Also:__  [- flushDataCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpmzwhk43iirqxiykdmfrwqzi)

---

### setData:forKey:mimeType:session:

`- (void)setData:(NSData
*)someData
forKey:(NSString *)key
mimeType:(NSString *)type
session:(WOSession *)aSession`

Adds the image or embbedded object someData
of MIME type type to the data cache for the session specify by aSession.
The data is stored under the key key. The session argument is currently
ignored; specify nil to have WOResourceManager use the application-wide
cache.

This method is invoked any time a dynamic element requests
an image or embedded object from a database. You rarely need to
invoke it yourself.

By default when a dynamic element
requests an image from the database, WOResourceManager fetches the
image, stores it in the cache using __setData:forKey:mimeType:session:__,
sends it to the dynamic element, and then removes it from the cache
using [removeDataForKey:session:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpojsw233wmvcgc5dbizxxes3fpe5hgzltonuw63r2). However,
if the dynamic element has a __key__ attribute
defined, then the image is stored in the database under that key,
and it is not removed from the database.

Access to
the WOResourceManager object is locked at the beginning of this
method and unlocked at the end.

__See
Also:__  [- flushDataCache](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpmzwhk43iirqxiykdmfrwqzi)

---

### stringForKey:inTableNamed:withDefaultValue:inFramework:languages:

`- (NSString *)stringForKey:(NSString
*)aKey
inTableNamed:(NSString *)aTableName
withDefaultValue:(NSString *)aDefaultValue
inFramework:(NSString *)aFrameworkName
languages:(NSArray *)languagesList`

Returns a localized string from string table _aTable___.strings__ using _aKey_ to
look it up. If no string value for the key is found in the table, _aDefaultValue_ (optional)
is returned. The method first searches the _aTable___.strings__ file,
if it exists, in each of the localized (__.lproj__)
subdirectories of the application wrapper; searching proceeds in
the order specified by the array _languagesList_.
If no string value matching the key is found, the search then continues
to the _aTable___.strings__ file
(if it exists) directly under the Resources directory (inside the
directory with the __.woa__ extension).

---

### unlock

`- (void)unlock`

Removes the lock on the WOResourceManager object,
allowing other threads to access it.

Usually, you don't need
to invoke this method in your own code. All messages that you send
to a WOResourceManager object lock access to the object at the beginning
of the method and unlock access at the end. You only need to use
this method if you're subclassing WOResourceManager. In that case, you
should lock access to the WOResourceManager object in methods that
load resources and unlock when the method is finished accessing
the WOResourceManager object.

__See
Also:__  [- lock](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpnrxwg2y)

---

### urlForResourceNamed:inFramework:languages:request:

`- (NSString *)urlForResourceNamed:(NSString
*)aResourceFile
inFramework:(NSString *)aFrameworkName
languages:(NSArray *)languagesList
request:(WORequest *)aRequest`

Returns the URL associated with a resource named _aResourceFile_.
The URL returned is of the following form:

__WebObjects/MyApp.woa/WebServerResources/English.lproj/___aResourceFile_

Include
the file's extension when specifying _aResourceFile_.
If the file is in the application, specify nil for the framework
argument.

This method locates resources under the
application or framework. The URL returned is computed by concatenating
the application's base URL (returned by WOApplication's [baseURL](WOApplication-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2bobygy2ldmf2gs33of5rgc43fkvjey) method and settable using
the WOApplicationBaseURL user default) and the relative path of
the resource. This method does not check to see if the file is actually
under the document root. For example, if your application is installed
in __/Local/Library/WebObjects/Applications__,
and the method finds _aResourceFile_ in
the __Resources__ directory, it returns:

__/WebObjects/MyApp.woa/Resources/___aResourceFile_

even
though the __Resources__ directory is not under
the document root.

Access to the WOResourceManager
object is locked at the beginning of this method and unlocked at the
end.

__See Also:__  [- pathForResourceNamed:inFramework:languages:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxvot2smvzw65lsmnsu2ylomftwk4rpobqxi2cgn5zfezltn52xey3fjzqw2zlehjuw4rtsmfwwk53pojvtu3dbnztxkylhmvztu)

---

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
