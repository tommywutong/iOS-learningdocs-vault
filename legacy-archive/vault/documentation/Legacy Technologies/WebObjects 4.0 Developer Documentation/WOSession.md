---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOSession.html
archived_at: '2026-07-18T01:28:52.480378Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOResponse.md)
[!](WOSessionStore.md)

---

# WOSession

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WOSession objects represent _sessions_, periods during which access to a WebObjects application and its resources is granted to a particular client (typically a browser). An application can have many concurrent sessions, each with its own special "view" of the application and its own set of data values. For instance, one client could be accessing a "catalog" application, where that client is going from page to page, filling a virtual shopping cart with items for purchase. Another client might be accessing the same application at the same time, but that person might have different items in his or her shopping cart.

Perhaps the most important thing a WOSession object does is encapsulate state for a session. After the application handles a request, it stores the WOSession until the next request of the session occurs. All the information that is important for maintaining continuity throughout the session is preserved. And the integrity of session data is maintained as well; the data of a session not only persists between requests but is kept separate from that of all other sessions.

When you develop an application, you identify data with session-wide scope by declaring instance variables in your subclass of WOSession (or, for scripted applications, in `Session.wos`). Then, before the end of a cycle of the request-response loop, ensure that the instance variables hold current session values.

The application uses a _session ID_ to identify a session object. Upon receiving the first request of a session, the application assigns a session ID (a unique, randomly generated string) to the session. The session ID appears in the URL between the application name and the page name.

At the end of each cycle of the request-response loop, the application stores the WOSession object according to the storage strategy implemented by the chosen [WOSessionStore](WOSessionStore.md). When the application receives the next request of the session, it restores the WOSession, using the session ID as key.

To be stored and restored according to any WOSessionStore strategy, a WOSession must be convertable to an object archive. WOSessions are therefore asked to serialize and deserialize themselves prior to being archived and unarchived (in either binary or ASCII format). To accomplish this, the WOSession should implement the `encodeWithCoder:` and `initWithCoder:` methods of the NSCoding protocol.

Because storage of sessions in application memory can consume large amounts of memory over time, WOSession includes methods for controlling the lifespan of session objects. The [`setTimeOut`](#apple-geztg) method sets a period of inactivity after which the session is terminated. The [`terminate`](#apple-ge2ds) method explicitly ends a session.

The WOSession class provides several other methods useful for tasks ranging from localization to database access:

- WOSession objects can interject custom session behavior into the request-response loop by implementing the request-handling methods ([`takeValuesFromRequest`](#apple-ge2dk), [`invokeAction`](#apple-ha2q), and [`appendToResponse`](#apple-gyyq)) as well as [`awake`](#apple-gy2q) and [`sleep`](#apple-gezto).
- For database access, the [`defaultEditingContext`](#apple-g43q) method gives each WOSession object in an application its own Enterprise Objects editing context.
- An application's WOSession objects also play a role in localization. Through the [`setLanguages`](#apple-gezdk) method you can store a list of the languages supported by the application. The sequence of language strings in the list indicates the order of language preference for a particular session. Several resource-access methods in [WOResourceManager](WOResourceManager.md), [WOApplication](WOApplication.md), and [WOComponent](WOComponent.md) refer to the [`languages`](#apple-he3q) array when they locate such things as localized strings, images, and sounds.
- WOSession objects also allow you to affect load balancing with the [`setDistributionEnabled`](#apple-ge3toobw) method; if the flag set by this method is `false` (the default), transactions of the session are restricted to a single application instance. If this the case, the application instance number as well as the application host name are appended to the URL.

---

## Method Types

**Constructor**

**[WOSession](#apple-gi2dmmby)**

**Obtaining attributes**

**[isDistributionEnabled](#apple-ha4q)

**[sessionID](#apple-ge2tgmjy)

**[storesIDsInCookies](#apple-gm2timy)

**[storesIDsInURLs](#apple-gq3dkny)********

**Setting attributes**

**[setDistributionEnabled](#apple-ge3toobw)

**[setStoresIDsInCookies](#apple-gm2tcmy)

**[setStoresIDsInURLs](#apple-geytgmrs)******

**Terminating**

**[terminate](#apple-ge2ds)

**[isTerminating](#apple-hezq)

**[timeOut](#apple-ge2tg)

**[setTimeOut](#apple-geztg)********

**Localization**

**[languages](#apple-he3q)

**[setLanguages](#apple-gezdk)****

**Managing enterprise objects**

**[defaultEditingContext](#apple-g43q)

**[setDefaultEditingContext](#apple-gezdc)****

**Handling requests**

**[appendToResponse](#apple-gyyq)

**[awake](#apple-gy2q)

**[context](#apple-gy4q)

**[invokeAction](#apple-ha2q)

**[sleep](#apple-gezto)

**[takeValuesFromRequest](#apple-ge2dk)************

**Statistics**

**[statistics](#apple-ge2dc)**

**Page Management**

**[savePage](#apple-geytg)

**[restorePageForContextID](#apple-geyds)****

---

## Constructors

---

### WOSession

public `WOSession`()

Returns an initialized WOSession object. Session time-out is set by default to a very long period. This method throws exceptions if no session ID has been assigned or if it cannot initialize the object for any other reason. The `isDistributionEnabled` flag is set to `false`, meaning that each transaction will be assigned to an application instance specified in a configuration file for load balancing

---

## Instance Methods

---

### appendToResponse

public void `appendToResponse`(WOResponse _aResponse_, WOContext _aContext_)

This method is invoked during the phase of the request-response loop during which the objects associated with a response page append their HTML content to the response. WOSession's default implementation of this method forwards the message to the WOComponent that represents the response page. Then, it records information about the current transaction by sending [`recordStatisticsForResponse`](WOStatisticsStore.md#apple-ha3a) and then [`descriptionForResponse`](WOStatisticsStore.md#apple-gyza) to the [WOStatisticsStore](WOStatisticsStore.md) object.

Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[`invokeAction`](#apple-ha2q), [`takeValuesFromRequest`](#apple-ge2dk)

---

### awake

public void `awake`()

Invoked at the beginning of a WOSession's involvement in a cycle of the request-response loop, giving the WOSession an opportunity to initialize its instance variables or perform setup operations. The default implementation does nothing.

__See also:__
[`sleep`](#apple-gezto)

---

### context

public WOContext `context`()

Returns the WOContext object for the current transaction.

__See also:__
[WOContext](WOContext.md) class

---

### defaultEditingContext

public com.apple.yellow.eocontrol.EOEditingContext `defaultEditingContext`()

Returns the default EOEditingContext object for the session. The method creates the editing context the first time that it is invoked and caches it for subsequent invocations. There is only one unique EOEditingContext instance per session. The instance is initialized with the default object store coordinator as the parent object store.

---

### invokeAction

public WOElement `invokeAction`(WORequest _aRequest_, WOContext _aContext_)

WOSession objects receive this message during the middle phase of the request-response loop. During this phase, the `invokeActionForRequest:inContext:` message is propagated through the objects of an application, most importantly, the WOElement objects of the request page. The dynamic element on which the user has acted (by, for example, clicking a button) responds by triggering the method in the request WOComponent that is bound to the action. The default behavior of WOSession is to send the message to the WOComponent object that represents the request. Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[`appendToResponse`](#apple-gyyq), [`takeValuesFromRequest`](#apple-ge2dk)

---

### isDistributionEnabled

public boolean `isDistributionEnabled`()

Returns whether state distribution among multiple application instances is enabled. Returns`false` by default since the default WOSessionStore (state in the server) does not allow distribution. If this flag is disabled, a specific application instance (whose identifying number is embedded in the URL) is assigned to the session.

__See also:__
[`setDistributionEnabled`](#apple-ge3toobw)

---

### isTerminating

public boolean `isTerminating`()

Returns whether the WOSession object will terminate at the end of the current request-response loop.

__See also:__
[`terminate`](#apple-ge2ds)

---

### languages

public NSArray `languages`()

Returns the list of languages supported by the session. The order of language strings (for example, "French") indicates the preferred order of languages. This is initialized from the users's browser preferences unless explicitly set with [`setLanguages`](#apple-gezdk). For details, see "Localization" in the WebObjects programming topics.

__See also:__
[`setLanguages`](#apple-gezdk)

---

### restorePageForContextID

public WOComponent `restorePageForContextID`(java.lang.String _contextID_)

Returns a page instance stored in the session page cache. The key to the stored instance is its context ID, which derives from the transaction's [WOContext](WOContext.md) or [WORequest](WORequest.md) objects. This method returns `null` if restoration is impossible.

__See also:__
[`savePage`](#apple-geytg)

---

### savePage

public void `savePage`(WOComponent _aPage_)

Saves the page instance _aPage_ in the session page cache. The context ID for the current transaction is made the key for obtaining this instance in the cache using [`restorePageForContextID`](#apple-geyds).

---

### savePageInPermanentCache

pubic void `savePageInPermanentCache`(WOComponent _aPage_)

Puts _aPage_ into a separate page cache. This cache is searched first when attempting to restore the page the next time its requested. This effectively makes _aPage_ live for the duration of the application regardless of the size of your page cache. This is useful whe you are using frames and its possible for a page of controls to be bumped from the page cache.

__See also:__
[`permanentPageCacheSize`](WOApplication.md#apple-ge3tinjw) ([WOApplication](WOApplication.md)), [`setPermanentPageCacheSize`](WOApplication.md#apple-ge3tkmjx) ([WOApplication](WOApplication.md))

---

### sessionID

public java.lang.String `sessionID`()

Returns the unique, randomly generated string that identifies the session object. The session ID occurs in the URL after the request handler key.

---

### setDefaultEditingContext

public void `setDefaultEditingContext`(EOEditingContext _editingContext_)

Sets the editing context to be returned by [`defaultEditingContext`](#apple-g43q). This can be used to set an editing context initialized with a different parent object store than the default. This is useful when, for instance, each session needs its own login to the database. Once a default editing context has been established, you may not call `setDefaultEditingContext:` again. Therefore, to provide your own default editing context, you must call `setDefaultEditingContext:` before ever calling [`defaultEditingContext`](#apple-g43q) since that will lazily establish an editing context.

__See also:__
[`defaultEditingContext`](#apple-g43q)

---

### setDistributionEnabled

public void `setDistributionEnabled`(boolean _aFlag_)

Enables or disables the distribution mechanism that effects load balancing among multiple application instances. When disabled (the default), generated URLs include the application instance number; the adaptor uses this number to route the request to the specific application instance based on information in the configuration file. When this flag is enabled, generated URLs do not contain the application instance number, and thus transactions of a session are handled by whatever application instance is available.

__See also:__
[`isDistributionEnabled`](#apple-ha4q)

---

### setLanguages

public void `setLanguages`(NSArray _languages_)

Sets the languages for which the session is localized. The ordering of language strings in the array determines the order in which the application will search _languages_.lproj directories for localized strings, images, and component definitions.

__See also:__
[`languages`](#apple-he3q)

---

### setStoresIDsInCookies

public void `setStoresIDsInCookies`(boolean _flag_)

Enables or disables the cookie mechanism. Two cookies are created for you when enabled: a session ID cookie with the name "wosid," and an instance ID cookie with the name "woinst." By default, the cookie mechanism is disabled.

---

### setStoresIDsInURLs

public void `setStoresIDsInCookies`(boolean _flag_)

Enables or disables the storing of session and instance IDs in URLs. By default, IDs are stored in URLs.

---

### setTimeOut

public void `setTimeOut`(double _seconds_)

Set the session timeout in seconds. When a session remains inactive-that is, the application receives no request for this session-for a period longer than the time-out setting, the session will terminate, resulting in the deallocation of the WOSession object. By default, the session time-out is set from the [WOApplication](WOApplication.md) method [`sessionTimeout`](WOApplication.md#apple-ge3tgnru).

__See also:__
[`timeOut`](#apple-ge2tg)

---

### sleep

public void `sleep`()

Invoked at the conclusion of each request-response loop in which the session is involved, giving the WOSession the opportunity to deallocate objects initialized in the [`awake`](#apple-gy2q) method. The default WOSession implementation does nothing.

---

### statistics

public NSArray `statistics`()

Returns a list of the pages accessed by this session, ordered from first accessed to last. For each page, the string stored is obtained by sending [`descriptionForResponse`](WOComponent.md#apple-ha4q) to the WOComponent object. By default, this returns the component's name. If the application keeps a CLFF log file, this list is recorded in the log file when the session terminates.

__See also:__
[`appendToResponse`](#apple-gyyq)

---

### storesIDsInCookies

public boolean `storesIDsInCookies`()

Returns whether the cookie mechanism for storing session and instance IDs is enabled. The cookie mechanism is disabled by default.

---

### storesIDsInURLs

public boolean `storesIDsInURLs`()

Returns whether the URL mechanism for storing session IDs and instance IDs is enabled. The URL mechanism is enabled by default.

---

### takeValuesFromRequest

public void `takeValuesFromRequest`(WORequest _aRequest_, WOContext _aContext_)

WOSession objects receive this message during the first phase of the request-response loop. During this phase, the dynamic elements associated with the request page extract any user input and assign the values to the appropriate component variables. The default behavior of WOSession is to send the message to the [WOComponent](WOComponent.md) object that represents the request. Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[`appendToResponse`](#apple-gyyq), [`invokeAction`](#apple-ha2q)

---

### terminate

public void `terminate`()

Causes the session to terminate after the conclusion of the current request-response loop.

__See also:__
[`isTerminating`](#apple-hezq)

---

### timeOut

public double `timeOut`()

Returns the timeout interval in seconds.

__See also:__
[`setTimeOut`](#apple-geztg)

---

# Notifications

---

### WOSessionDidCreateNotification

public static final java.lang.String `WOSessionDidCreateNotification`

Sent at the the end of the session initiation (including awake). The object of the notification is the session instance

---

### WOSessionDidRestoreNotification

public static final java.lang.String `WOSessionDidCreateNotification`

Sent after the sesion is fully restored (including awake). The object of the notification is the session instance.

---

### WOSessionWillTimeoutNotification

public static final java.lang.String `WOSessionDidCreateNotification`

Sent when a session times out but before it is released. The session ID is the object of the notification.

---

[!](WOResponse.md)
[!](WOSessionStore.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
