---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOSession.html
archived_at: '2026-07-18T01:28:54.492329Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOResponse-2.md)
[!](WOSessionStore-2.md)

---

# WOSession

__Inherits From:__
NSObject

__Declared in:__
WebObjects/WOSession.h

---

## Class Description

WOSession objects represent _sessions_, periods during which access to a WebObjects application and its resources is granted to a particular client (typically a browser). An application can have many concurrent sessions, each with its own special "view" of the application and its own set of data values. For instance, one client could be accessing a "catalog" application, where that client is going from page to page, filling a virtual shopping cart with items for purchase. Another client might be accessing the same application at the same time, but that person might have different items in his or her shopping cart.

Perhaps the most important thing a WOSession object does is encapsulate state for a session. After the application handles a request, it stores the WOSession until the next request of the session occurs. All the information that is important for maintaining continuity throughout the session is preserved. And the integrity of session data is maintained as well; the data of a session not only persists between requests but is kept separate from that of all other sessions.

When you develop an application, you identify data with session-wide scope by declaring instance variables in your subclass of WOSession (or, for scripted applications, in __Session.wos__ ). Then, before the end of a cycle of the request-response loop, ensure that the instance variables hold current session values.

The application uses a _session ID_ to identify a session object. Upon receiving the first request of a session, the application assigns a session ID (a unique, randomly generated string) to the session. The session ID appears in the URL between the application name and the page name.

At the end of each cycle of the request-response loop, the application stores the WOSession object according to the storage strategy implemented by the chosen [WOSessionStore](WOSessionStore-2.md). When the application receives the next request of the session, it restores the WOSession, using the session ID as key.

To be stored and restored according to any WOSessionStore strategy, a WOSession must be convertable to an object archive. WOSessions are therefore asked to serialize and deserialize themselves prior to being archived and unarchived (in either binary or ASCII format). To accomplish this, the WOSession should implement the __encodeWithCoder:__  and __initWithCoder:__  methods of the NSCoding protocol.

Because storage of sessions in application memory can consume large amounts of memory over time, WOSession includes methods for controlling the lifespan of session objects. The [__setTimeOut:__](#apple-geztg) method sets a period of inactivity after which the session is terminated. The [__terminate__](#apple-ge2ds) method explicitly ends a session.

The WOSession class provides several other methods useful for tasks ranging from localization to database access:

- WOSession objects can interject custom session behavior into the request-response loop by implementing the request-handling methods ([__takeValuesFromRequest:inContext:__](#apple-ge2dk), [__invokeActionForRequest:inContext:__](#apple-ha2q), and [__appendToResponse:inContext:__](#apple-gyyq)) as well as [__awake__](#apple-gy2q) and [__sleep__](#apple-gezto).
- For database access, the [__defaultEditingContext__](#apple-g43q) method gives each WOSession object in an application its own Enterprise Objects editing context.
- An object in an application doesn't have to know which instance variables its WOSession holds in order to store session values. With the [__setObject:forKey:__](#apple-gi2dgnru) and [__objectForKey:__](#apple-gi2dcnru) methods it can store and retrieve values as needed. This mechanism is especially useful for reusable components.
- An application's WOSession objects also play a role in localization. Through the [__setLanguages:__](#apple-gezdk) method you can store a list of the languages supported by the application. The sequence of language strings in the list indicates the order of language preference for a particular session. Several resource-access methods in [WOResourceManager](WOResourceManager-2.md), [WOApplication](WOApplication-2.md), and [WOComponent](WOComponent-2.md) refer to the [__languages__](#apple-he3q) array when they locate such things as localized strings, images, and sounds.
- WOSession objects also allow you to affect load balancing with the [__setDistributionEnabled:__](#apple-ge3toobw) method; if the flag set by this method is NO (the default), transactions of the session are restricted to a single application instance. If this the case, the application instance number as well as the application host name are appended to the URL.

---

# Adopted Protocols

**NSCoding**

**- encodeWithCoder:

**- initWithCoder:****

**NSCopying**

**- copy

**- copyWithZone:****

---

## Method Types

**Creating**

**[- init](#apple-gi2danru)**

**Obtaining attributes**

**[- domainForIDCookies](#apple-gi2danbz)

**[- expirationDateForIDCookies](#apple-gi2danju)

**[- isDistributionEnabled](#apple-ha4q)

**[- sessionID](#apple-ge2tgmjy)

**[- storesIDsInCookies](#apple-gm2timy)

**[- storesIDsInURLs](#apple-gq3dkny)************

**Setting attributes**

**[- setDistributionEnabled:](#apple-ge3toobw)

**[- setStoresIDsInCookies:](#apple-gm2tcmy)

**[- setStoresIDsInURLs:](#apple-geytgmrs)******

**Terminating**

**[- terminate](#apple-ge2ds)

**[- isTerminating](#apple-hezq)

**[- timeOut](#apple-ge2tg)

**[- setTimeOut:](#apple-geztg)********

**Localization**

**[- languages](#apple-he3q)

**[- setLanguages:](#apple-gezdk)****

**Managing component state**

**[- setObject:forKey:](#apple-gi2dgnru)

**[- objectForKey:](#apple-gi2dcnru)

**[- removeObjectForKey:](#apple-gi2dcnzt)******

**Managing enterprise objects**

**[- defaultEditingContext](#apple-g43q)

**[- setDefaultEditingContext:](#apple-gezdc)****

**Handling requests**

**[- appendToResponse:inContext:](#apple-gyyq)

**[- awake](#apple-gy2q)

**[- context](#apple-gy4q)

**[- invokeActionForRequest:inContext:](#apple-ha2q)

**[- sleep](#apple-gezto)

**[- takeValuesFromRequest:inContext:](#apple-ge2dk)************

**Statistics**

**[- statistics](#apple-ge2dc)**

**Debugging**

**[- debugWithFormat:](#apple-gi2damjt)**

**Page Management**

**[- savePage:](#apple-geytg)

**[- restorePageForContextID:](#apple-geyds)****

---

## Instance Methods

---

### appendToResponse:inContext:

- (void)__appendToResponse:__ (WOResponse \*)_aResponse_ __inContext:__ (WOContext \*)_aContext_

This method is invoked during the phase of the request-response loop during which the objects associated with a response page append their HTML content to the response. WOSession's default implementation of this method forwards the message to the WOComponent that represents the response page. Then, it records information about the current transaction by sending [__recordStatisticsForResponse:inContext:__](WOStatisticsStore-2.md#apple-ha3a) and then [__descriptionForResponse:inContext:__](WOStatisticsStore-2.md#apple-gyza) to the [WOStatisticsStore](WOStatisticsStore-2.md) object.

Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[- __invokeActionForRequest:inContext:__](#apple-ha2q), [- __takeValuesFromRequest:inContext:__](#apple-ge2dk)

---

### awake

- (void)__awake__

Invoked at the beginning of a WOSession's involvement in a cycle of the request-response loop, giving the WOSession an opportunity to initialize its instance variables or perform setup operations. The default implementation does nothing.

__See also:__
[- __sleep__](#apple-gezto)

---

### context

- (WOContext \*)__context__

Returns the WOContext object for the current transaction.

__See also:__
[WOContext](WOContext-2.md) class

---

### debugWithFormat:

- (void)__debugWithFormat:__ (NSString \*)_aFormatString,..._

Prints a message to the standard error device (stderr), if __WODebuggingEnabled__  is YES. The message can include formatted variable data using printf-style conversion specifiers, Note that in WebScript, all variables are objects, so the only conversion specifier allowed is __%@__ . In compiled Objective-C code, all __printf__  conversion specifiers are allowed.

You control whether this method displays output with the __WODebuggingEnabled__  user default option. If __WODebuggingEnabled__  is YES, then the __debugWithFormat:__  messages display their output. If __WODebuggingEnabled__  is NO, the __debugWithFormat:__  messages don\xd5 t display their output.

---

### defaultEditingContext

- (EOEditingContext \*)__defaultEditingContext__

Returns the default EOEditingContext object for the session. The method creates the editing context the first time that it is invoked and caches it for subsequent invocations. There is only one unique EOEditingContext instance per session. The instance is initialized with the default object store coordinator as the parent object store.

---

### domainForIDCookies

- (NSString \*)__domainForIDCookies__

Returns the path that is passed when creating a rendezvous cookie for the application. This path is lazily created the first time it is used from the current request's __adaptorPrefix__  and the application name (including the ".woa" extension).

---

### expirationDateForIDCookies

- (NSDate \*)__expirationDateForIDCookies__

Returns when session and instance ID cookies expire. By default, no expiration date is set and this method returns nil. Override this method if you want to return some other time, such as the session expiration date.

Different applications can override this method to enforce different behavior:

- A typical online banking application might use cookies and set the timeout to a very short amount of time (two minutes, for example), so that if the client doesn't interact with the browser and no request is made of the server, the client's session is timed out. This could be easily enforced on both the client-by setting the cookie timeout-and on the server from within the session object.
- A site wishing to personalize its pages based upon a user ID might set the timeout far into the distant future so that even when a client shuts down his browser, the cookie will still be there when he comes back with a bookmarked URL.
- Sites that want you to log in each time you visit could store the user ID in a cookie and then set the expiration date on the cookie to nil so that the cookie will go away whenever the client quits their browser.

---

### init

- (id)__init__

Initializes a WOSession object. Session timeout is set from the [WOApplication](WOApplication-2.md) method [__sessionTimeout__](WOApplication-2.md#apple-ge3tgnru). This method throws exceptions if no session ID has been assigned or if it cannot initialize the object for any other reason. Override __init__  in compiled subclasses to perform custom initializations; as always, invoke the superclass method as the first thing.

---

### invokeActionForRequest:inContext:

- (WOElement \*)__invokeActionForRequest:__ (WORequest \*)_aRequest___inContext:__ (WOContext \*)_aContext_

WOSession objects receive this message during the middle phase of the request-response loop. During this phase, the __invokeActionForRequest:inContext:__  message is propagated through the objects of an application, most importantly, the WOElement objects of the request page. The dynamic element on which the user has acted (by, for example, clicking a button) responds by triggering the method in the request WOComponent that is bound to the action. The default behavior of WOSession is to send the message to the WOComponent object that represents the request. Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[- __appendToResponse:inContext:__](#apple-gyyq), [- __takeValuesFromRequest:inContext:__](#apple-ge2dk)

---

### isDistributionEnabled

- (BOOL)__isDistributionEnabled__

Returns whether state distribution among multiple application instances is enabled. Returns__false__  by default since the default WOSessionStore (state in the server) does not allow distribution. If this flag is disabled, a specific application instance (whose identifying number is embedded in the URL) is assigned to the session.

__See also:__
[__setDistributionEnabled:__](#apple-ge3toobw)

---

### isTerminating

- (BOOL)__isTerminating__

Returns whether the WOSession object will terminate at the end of the current request-response loop.

__See also:__
[- __terminate__](#apple-ge2ds)

---

### languages

- (NSArray \*)__languages__

Returns the list of languages supported by the session. The order of language strings (for example, "French") indicates the preferred order of languages. This is initialized from the users's browser preferences unless explicitly set with [__setLanguages:__](#apple-gezdk). For details, see "Localization" in the WebObjects programming topics.

__See also:__
[- __setLanguages:__](#apple-gezdk)

---

### objectForKey:

- (id)__objectForKey:__ (NSString \*)_aKey_

Returns an object stored in the session under a specific key.

__See also:__
__[- setObject:forKey:](#apple-gi2dgnru)__

---

### removeObjectForKey:

- (void)__removeObjectForKey:__ (NSString \*)_key_

Removes the object stored in the session under the specified key.

---

### restorePageForContextID:

- (WOComponent \*)__restorePageForContextID:__ (NSString \*)_contextID_

Returns a page instance stored in the session page cache. The key to the stored instance is its context ID, which derives from the transaction's [WOContext](WOContext-2.md) or [WORequest](WORequest-2.md) objects. This method returns __nil__  if restoration is impossible.

__See also:__
[- __savePage:__](#apple-geytg)

---

### savePage:

- (void)__savePage:__ (WOComponent \*)_aPage_

Saves the page instance _aPage_ in the session page cache. The context ID for the current transaction is made the key for obtaining this instance in the cache using [__restorePageForContextID:__](#apple-geyds).

---

### savePageInPermanentCache:

- (void)__savePageInPermanentCache:__ (WOComponent\*)_aPage_

Puts _aPage_ into a separate page cache. This cache is searched first when attempting to restore the page the next time its requested. This effectively makes _aPage_ live for the duration of the application regardless of the size of your page cache. This is useful whe you are using frames and its possible for a page of controls to be bumped from the page cache.

__See also:__
[- __permanentPageCacheSize__](WOApplication-2.md#apple-ge3tinjw) ([WOApplication](WOApplication-2.md)), [- __setPermanentPageCacheSize:__](WOApplication-2.md#apple-ge3tkmjx)
([WOApplication](WOApplication-2.md))

---

### sessionID

- (NSString \*)__sessionID__

Returns the unique, randomly generated string that identifies the session object. The session ID occurs in the URL after the request handler key.

---

### setDefaultEditingContext:

- (void)__setDefaultEditingContext:__ (EOEditingContext \*)_editingContext_

Sets the editing context to be returned by [__defaultEditingContext__](#apple-g43q). This can be used to set an editing context initialized with a different parent object store than the default. This is useful when, for instance, each session needs its own login to the database. Once a default editing context has been established, you may not call __setDefaultEditingContext:__  again. Therefore, to provide your own default editing context, you must call __setDefaultEditingContext:__  before ever calling [__defaultEditingContext__](#apple-g43q) since that will lazily establish an editing context.

__See also:__
[- __defaultEditingContext__](#apple-g43q)

---

### setDistributionEnabled:

- (void)__setDistributionEnabled:__ (BOOL)_aFlag_

Enables or disables the distribution mechanism that effects load balancing among multiple application instances. When disabled (the default), generated URLs include the application instance number; the adaptor uses this number to route the request to the specific application instance based on information in the configuration file. When this flag is enabled, generated URLs do not contain the application instance number, and thus transactions of a session are handled by whatever application instance is available.

__See also:__
[- __isDistributionEnabled__](#apple-ha4q)

---

### setLanguages:

- (void)__setLanguages:__ (NSArray \*)_languages_

Sets the languages for which the session is localized. The ordering of language strings in the array determines the order in which the application will search _languages_.lproj directories for localized strings, images, and component definitions.

__See also:__
[- __languages__](#apple-he3q)

---

### setObject:forKey:

- (void)__setObject:__ (id)_anObject_ __forKey:__ (NSString \*)_aKey_

Stores an object within the session under a given key (_aKey_). This method allows a reusable component to add state dynamically to any WOSession object. This method eliminates the need for prior knowledge of the WOSession's instance variables. A suggested mechanism for generating a unique key prefix for a given subcomponent is to concatenate the component's name and its element ID. For a specific component instance, such a prefix should remain unique and invariant within a session.

__See also:__
__[- objectForKey:](#apple-gi2dcnru)__

---

### setStoresIDsInCookies:

- (void)__setStoresIDsInCookies:__ (BOOL)_flag_

Enables or disables the cookie mechanism. Two cookies are created for you when enabled: a session ID cookie with the name "wosid," and an instance ID cookie with the name "woinst." By default, the cookie mechanism is disabled.

---

### setStoresIDsInURLs:

- (void)__setStoresIDsInCookies:__ (BOOL)_flag_

Enables or disables the storing of session and instance IDs in URLs. By default, IDs are stored in URLs.

---

### setTimeOut:

- (void)__setTimeOut:__ (NSTimeInterval)_seconds_

Set the session timeout in seconds. When a session remains inactive-that is, the application receives no request for this session-for a period longer than the time-out setting, the session will terminate, resulting in the deallocation of the WOSession object. By default, the session time-out is set from the [WOApplication](WOApplication-2.md) method [__sessionTimeout__](WOApplication-2.md#apple-ge3tgnru).

__See also:__
[- __timeOut__](#apple-ge2tg)

---

### sleep

- (void)__sleep__

Invoked at the conclusion of each request-response loop in which the session is involved, giving the WOSession the opportunity to deallocate objects initialized in the [__awake__](#apple-gy2q) method. The default WOSession implementation does nothing.

---

### statistics

- (NSArray \*)__statistics__

Returns a list of the pages accessed by this session, ordered from first accessed to last. For each page, the string stored is obtained by sending [__descriptionForResponse:inContext:__](WOComponent-2.md#apple-ha4q) to the WOComponent object. By default, this returns the component's name. If the application keeps a CLFF log file, this list is recorded in the log file when the session terminates.

__See also:__
[- __appendToResponse:inContext:__](#apple-gyyq)

---

### storesIDsInCookies

- (BOOL)__storesIDsInCookies__

Returns whether the cookie mechanism for storing session and instance IDs is enabled. The cookie mechanism is disabled by default.

---

### storesIDsInURLs

- (BOOL)__storesIDsInURLs__

Returns whether the URL mechanism for storing session IDs and instance IDs is enabled. The URL mechanism is enabled by default.

---

### takeValuesFromRequest:inContext:

- (void)__takeValuesFromRequest:__ (WORequest \*)_aRequest_ __inContext:__ (WOContext \*)_aContext_

WOSession objects receive this message during the first phase of the request-response loop. During this phase, the dynamic elements associated with the request page extract any user input and assign the values to the appropriate component variables. The default behavior of WOSession is to send the message to the [WOComponent](WOComponent-2.md) object that represents the request. Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[- __appendToResponse:inContext:__](#apple-gyyq), [- __invokeActionForRequest:inContext:__](#apple-ha2q)

---

### terminate

- (void)__terminate__

Causes the session to terminate after the conclusion of the current request-response loop.

__See also:__
[- __isTerminating__](#apple-hezq)

---

### timeOut

- (NSTimeInterval)__timeOut__

Returns the timeout interval in seconds.

__See also:__
[- __setTimeOut:__](#apple-geztg)

---

[!](WOResponse-2.md)
[!](WOSessionStore-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
