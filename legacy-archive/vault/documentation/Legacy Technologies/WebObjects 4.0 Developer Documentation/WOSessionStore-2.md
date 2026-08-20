---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOSessionStore.html
archived_at: '2026-07-18T01:28:54.599988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOSession-2.md)
[!](WOStatisticsStore-2.md)

---

# WOSessionStore

__Inherits From:__
NSObject

__Declared in:__
WebObjects/WOSessionStore.h

---

## Class Description

WOSessionStore, an abstract superclass, offers an object abstraction for storing client state per session. The application object ([WOApplication](WOApplication-2.md)) uses an instance of a concrete WOSessionStore subclass to implement a strategy for storing and retrieving session state. You typically set the WOSessionStore during application initialization through WOApplication's [__setSessionStore:__](WOApplication-2.md#apple-haytenq) method.

An application first creates a session ([WOSession](WOSession-2.md)) when it receives a request without a session ID. When this first request has been handled, the application stores the WOSession object under a randomly generated session ID by invoking its own [__saveSessionForContext:__](#apple-gy4q) method. This method by default forwards the message to the chosen WOSessionStore and that WOSessionStore takes care of the details of saving session state. When the next request comes in for that session, the application restores the session by sending itself [__restoreSessionWithID:request:__](#apple-ge4timi), which by default is forwarded to the application's WOSessionStore. The WOSessionStore then asks the [WOContext](WOContext-2.md) of the transaction for the session ID of the session. Based on the implementation of the WOSessionStore, the session object is located and returned.

There is one subclass of WOSessionStore implemented for the developer's convenience. A _server_ WOSessionStore (the default) stores session state in the server, in application memory. The [__serverSessionStore__](#apple-gu3dqmq) method returns this WOSessionStore.

See the chapter "Managing State" in the _WebObjects Developers Guide_ for the purposes, mechanisms, and limitations of session store in the server, page, and cookies.

You can create a custom session store by making a subclass of WOSessionStore. The subclass should properly implement the [__saveSessionForContext:__](#apple-gy4q) and [__restoreSessionWithID:request:__](#apple-ge4timi) methods (using the session ID as the key for storage) and should have a public method that the application object can use to obtain an instance. Some interesting session stores could be:

- A database session store that stores session data in a database as blobs, with the session ID as the primary key. This kind of WOSessionStore can be shared by many instances of the same WebObjects application, thus distributing the load (requests) among the instances.
- An adaptive session store that stores session state either in cookies or on the server, depending on what the client supports.

If you create your own WOSessionStore class that generates persistent objects, you should implement an algorithm that cleans up session state after the session is inactive for a long time. The server WOSessionStore provided by WebObjects performs this clean-up properly, but the API is not yet public.

---

## Method Types

**Obtaining a session store**

**[+ serverSessionStore](#apple-gu3dqmq)**

**Checking a session in and out**

**[- checkinSessionForContext:](#apple-gm3tmna)

**[- checkoutSessionWithID:request:](#apple-gu3toni)****

**Saving and restoring a context**

**[- restoreSessionWithID:request:](#apple-ge4timi)

**[- saveSessionForContext:](#apple-gy4q)****

---

## Class Methods

---

### serverSessionStore

+ (WOSessionStore \*)__serverSessionStore__

Returns a WOSessionStore object that stores session state in application memory. Since this is the default storage strategy, you do not need to explicitly set the session store during application initialization if this is the strategy you want.

State storage in the server is the most secure and is the easiest to implement. You can also easily manage the amount of storage consumed by setting session timeouts, limiting the size of the page-instance cache, and page uniquing. (See "Managing State" in the _WebObjects Developers Guide_ for details on these techniques.)

You may use WOSession's __initWithCoder:__  method to restore session state from the archived data.

---

## Instance Methods

---

### checkinSessionForContext:

- (void)__checkinSessionForContext:__ (WOContext \*)_aContext_

This method calls [__saveSessionForContext:__](#apple-gy4q) (implemented in the concrete subclass) to save the session referred to by _aContext_ using whatever storage technique is supported by the receiver. This method also "checks in" the session so that pending (and future) requests for the same session may procede. This method is called by [WOApplication](WOApplication-2.md) to save the session even if the session was not previously checked out via [__checkoutSessionWithID:request:__](#apple-gu3toni) (that is, the session is a new session which was just created and, therefore, not restored).

---

### checkoutSessionWithID:request:

- (WOSession\*)__checkoutSessionWithID:__ (NSString \*)_aSessionID_ __request:__ (WORequest \*)_aRequest_

This method returns a session for _aSessionID_ if one is stored. This method calls [__restoreSessionWithID:request:__](#apple-ge4timi) (implemented in the concrete subclass) to do the actual session restoration using whatever storage technique is supported by the receiver. If the session is located and restored, this method also "checks out" _aSessionID_ so that simultaneous access to the same session is precluded. If the session is not restored, the _aSessionID_ is not checked out.

---

### restoreSessionWithID:request:

- (WOSession \*)__restoreSessionWithID:__ (NSString \*)_aSessionID_ __request:__ (WORequest \*)_aRequest_

Implemented by a private concrete subclass to restore the current session object from a particular type of storage.

The default implementation of this method does nothing

---

### saveSessionForContext:

- (void)__saveSessionForContext:__ (WOContext \*)_aContext_

Implemented by a private concrete subclass to save the current session object using a particular strategy for state storage. The default implementation of this method does nothing.

You may use the method __encodeWithCoder:__  to save session state to archived data.

---

[!](WOSession-2.md)
[!](WOStatisticsStore-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
