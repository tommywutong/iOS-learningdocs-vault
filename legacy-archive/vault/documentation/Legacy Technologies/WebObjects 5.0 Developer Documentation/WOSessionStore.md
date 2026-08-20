---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOSessionStore.html
archived_at: '2026-07-15T08:15:15.880954Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOSessionStore

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOSessionStore, an abstract superclass, offers an object abstraction for storing client state per session. The application object (WOApplication) uses an instance of a concrete WOSessionStore subclass to implement a strategy for storing and retrieving session state. You typically set the WOSessionStore during application initialization through WOApplication's setSessionStore method.

An application first creates a session (WOSession) when it receives a request without a session ID. When this first request has been handled, the application stores the WOSession object under a randomly generated session ID by invoking its own [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss643bozsvgzltonuw63sgn5zeg33oorsxq5a) method. This method by default forwards the message to the chosen WOSessionStore and that WOSessionStore takes care of the details of saving session state. When the next request comes in for that session, the application restores the session by sending itself [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss64tfon2g64tfknsxg43jn5xfo2lunbeui), which by default is forwarded to the application's WOSessionStore. The WOSessionStore then asks the WOContext of the transaction for the session ID of the session. Based on the implementation of the WOSessionStore, the session object is located and returned.

There is one subclass of WOSessionStore implemented for the developer's convenience. A _server_ WOSessionStore (the default) stores session state in the server, in application memory. The [serverSessionStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33okn2g64tff5zwk4twmvzfgzltonuw63storxxezi) method returns this WOSessionStore.

See the chapter "Managing State" in the _WebObjects Developers Guide_ for the purposes, mechanisms, and limitations of session store in the server, page, and cookies.

You can create a custom session store by making a subclass of WOSessionStore. The subclass should properly implement the [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss643bozsvgzltonuw63sgn5zeg33oorsxq5a) and [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss64tfon2g64tfknsxg43jn5xfo2lunbeui) methods (using the session ID as the key for storage) and should have a public method that the application object can use to obtain an instance. Some interesting session stores could be:

- A database session store that stores session data in a database as blobs, with the session ID as the primary key. This kind of WOSessionStore can be shared by many instances of the same WebObjects application, thus distributing the load (requests) among the instances.
- An adaptive session store that stores session state either in cookies or on the server, depending on what the client supports.

If you create your own WOSessionStore class that generates persistent objects, you should implement an algorithm that cleans up session state after the session is inactive for a long time. The server WOSessionStore provided by WebObjects performs this clean-up properly, but the API is not yet public.

## Method Types

---

> **Obtaining a session store**
> : [serverSessionStore](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33okn2g64tff5zwk4twmvzfgzltonuw63storxxezi)
>
> **Checking a session in and out**
> : [checkInSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6y3imvrwwsloknsxg43jn5xem33sinxw45dfpb2a): [checkOutSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6y3imvrwwt3vorjwk43tnfxw4v3joruesra)
>
> **Session utilities**
> : [allSessionIDs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6ylmnrjwk43tnfxw4skeom): [allSessionIDsCheckedOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6ylmnrjwk43tnfxw4skeonbwqzldnnswit3voq): [isSessionIDCheckedOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss62ltknsxg43jn5xesrcdnbswg23fmrhxk5a): [removeSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss64tfnvxxmzktmvzxg2lpnzlws5dijfca)
>
> **Saving and restoring a context**
> : [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss64tfon2g64tfknsxg43jn5xfo2lunbeui): [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss643bozsvgzltonuw63sgn5zeg33oorsxq5a)

## Constructors

---

### WOSessionStore

`public WOSessionStore()`

Description forthcoming.

---

## Static Methods

---

### serverSessionStore

`public static WOSessionStore serverSessionStore()`

Returns a WOSessionStore object that stores session state in application memory. Since this is the default storage strategy, you do not need to explicitly set the session store during application initialization if this is the strategy you want.

State storage in the server is the most secure and is the easiest to implement. You can also easily manage the amount of storage consumed by setting session timeouts, limiting the size of the page-instance cache, and page uniquing. (See "Managing State" in the _WebObjects Developers Guide_ for details on these techniques.)

You may use the coding constructor for the session (WOSession(NSCoder)) to restore session state from the archived data.

---

## Instance Methods

---

### __allSessionIDs__

`public abstract NSArray allSessionIDs()`

This method should be implemented by WOSessionStore subclasses to return an NSArray containing the IDs of all sessions stored within the session store. WOSessionStore's implementation simply throws a RuntimeException.

---

### __allSessionIDsCheckedOut__

`public NSArray allSessionIDsCheckedOut()`

Returns an NSArray containing the session IDs for all sessions currently checked out of the session store.

---

### checkInSessionForContext

`public void checkInSessionForContext(WOContext aContext)`

This method calls [saveSessionForContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss643bozsvgzltonuw63sgn5zeg33oorsxq5a) (implemented in the concrete subclass) to save the session referred to by _aContext_ using whatever storage technique is supported by the receiver. This method also "checks in" the session so that pending (and future) requests for the same session may procede. This method is called by WOApplication to save the session even if the session was not previously checked out via [checkOutSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss6y3imvrwwt3vorjwk43tnfxw4v3joruesra) (that is, the session is a new session which was just created and, therefore, not restored).

---

### checkOutSessionWithID

`public WOSession checkOutSessionWithID( String aSessionID, WORequest aRequest)`

This method returns a session for _aSessionID_ if one is stored. This method calls [restoreSessionWithID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xfg5dpojss64tfon2g64tfknsxg43jn5xfo2lunbeui) (implemented in the concrete subclass) to do the actual session restoration using whatever storage technique is supported by the receiver. If the session is located and restored, this method also "checks out" _aSessionID_ so that simultaneous access to the same session is precluded. If the session is not restored, the _aSessionID_ is not checked out.

---

### isSessionIDCheckedOut

`public boolean isSessionIDCheckedOut(String sessionID)`

Returns `true` if the specified session ID is checked out of the session store.

---

### removeSessionWithID

`public abstract WOSession removeSessionWithID(String sessionID)`

This method should be implemented by WOSessionStore subclasses to remove and return the specified session. WOSessionStore's implementation simply throws a RuntimeException.

---

### restoreSessionWithID

`public abstract WOSession restoreSessionWithID( String aSessionID, WORequest aRequest)`

Implemented by a private concrete subclass to restore the current session object from a particular type of storage.

The default implementation of this method does nothing

---

### saveSessionForContext

`public abstract void saveSessionForContext(WOContext aContext)`

Implemented by a private concrete subclass to save the current session object using a particular strategy for state storage. The default implementation of this method does nothing.

You may use the NSCoding interface method __encodeWithCoder:__ to save session state to archived data.

---

### toString

`public String toString()`

Returns a String containing a string representation of the receiver.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
