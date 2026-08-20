---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/WebObjects.framework/Java/Classes/WOSession.html
archived_at: '2026-07-15T08:11:47.112288Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
WebObjects Reference

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md) 

# WOSession

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.webobjects

---

## Class Description

---

WOSession objects represent _sessions_,
periods during which access to a WebObjects application and its
resources is granted to a particular client (typically a browser).
An application can have many concurrent sessions, each with its
own special "view" of the application and its own set
of data values. For instance, one client could be accessing a "catalog"
application, where that client is going from page to page, filling
a virtual shopping cart with items for purchase. Another client
might be accessing the same application at the same time, but that
person might have different items in his or her shopping cart.

Perhaps the most important thing a WOSession object does is
encapsulate state for a session. After the application handles a
request, it stores the WOSession until the next request of the session
occurs. All the information that is important for maintaining continuity
throughout the session is preserved. And the integrity of session
data is maintained as well; the data of a session not only persists
between requests but is kept separate from that of all other sessions.

When you develop an application, you identify data with session-wide
scope by declaring instance variables in your subclass of WOSession
(or, for scripted applications, in __Session.wos__).
Then, before the end of a cycle of the request-response loop, ensure
that the instance variables hold current session values.

The application uses a _session ID_ to
identify a session object. Upon receiving the first request of a session,
the application assigns a session ID (a unique, randomly generated
string) to the session. The session ID appears in the URL between
the application name and the page name.

At the end of each cycle of the request-response loop, the
application stores the WOSession object according to the storage
strategy implemented by the chosen [WOSessionStore](WOSessionStore.md#apple-k5hvgzltonuw63storxxezi). When the application receives
the next request of the session, it restores the WOSession, using
the session ID as key.

To be stored and restored according to any WOSessionStore
strategy, a WOSession must be convertable to an object archive.
WOSessions are therefore asked to serialize and deserialize themselves
prior to being archived and unarchived (in either binary or ASCII
format). To accomplish this, the WOSession should implement the __encodeWithCoder__ and __initWithCoder__ methods
of the NSCoding protocol.

Because storage of sessions in application memory can consume
large amounts of memory over time, WOSession includes methods for
controlling the lifespan of session objects. The [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forkgs3lfj52xi) method
sets a period of inactivity after which the session is terminated.
The [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dfojwws3tborsq) method
explicitly ends a session.

The WOSession class provides several other methods useful
for tasks ranging from localization to database access:

- WOSession objects can interject custom session
  behavior into the request-response loop by implementing the request-handling
  methods ( [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a), [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o), and [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi)) as well as [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylxmfvwk) and [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643mmvsxa).
- For database access, the [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a) method
  gives each WOSession object in an application its own Enterprise
  Objects editing context.
- An object in an application doesn't have to know which instance
  variables its WOSession holds in order to store session values.
  With the [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forhwe2tfmn2em33sjnsxs) and [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc633cnjswg5cgn5zewzlz) methods
  it can store and retrieve values as needed. This mechanism is especially
  useful for reusable components.
- An application's WOSession objects also play a role in localization.
  Through the [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt) method
  you can store a list of the languages supported by the application.
  The sequence of language strings in the list indicates the order
  of language preference for a particular session. Several resource-access
  methods in [WOResourceManager](WOResourceManager.md#apple-k5hvezltn52xey3fjvqw4ylhmvza), [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4), and [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) refer to the [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc63dbnztxkylhmvzq) array
  when they locate such things as localized strings, images, and sounds.
- WOSession objects also allow you to affect load balancing
  with the [setDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle) method; if
  the flag set by this method is false (the default), transactions
  of the session are restricted to a single application instance.
  If this the case, the application instance number as well as the application
  host name are appended to the URL.

## Method Types

---

> **Constructor**
> : [WOSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6v2pknsxg43jn5xa)
>
> **Obtaining attributes**
> : [domainForIDCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdpnvqws3sgn5zesrcdn5xww2lfom)
> : [expirationDateForIDCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zlyobuxeylunfxw4rdborsum33sjfceg33pnnuwk4y)
> : [isDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltiruxg5dsnfrhk5djn5xek3tbmjwgkza)
> : [sessionID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643fonzws33ojfca)
> : [storesIDsInCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643un5zgk42jirzus3sdn5xww2lfom)
> : [storesIDsInURLs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643un5zgk42jirzus3svkjghg)
>
> **Setting attributes**
> : [setDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle)
> : [setStoresIDsInCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forjxi33smvzusrdtjfxeg33pnnuwk4y)
> : [setStoresIDsInURLs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forjxi33smvzusrdtjfxfkusmom)
>
> **Terminating**
> : [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dfojwws3tborsq)
> : [isTerminating](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltkrsxe3ljnzqxi2lom4)
> : [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65djnvsu65lu)
> : [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forkgs3lfj52xi)
>
> **Localization**
> : [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc63dbnztxkylhmvzq)
> : [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt)
>
> **Managing component state**
> : [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forhwe2tfmn2em33sjnsxs)
> : [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc633cnjswg5cgn5zewzlz)
> : [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfnvxxmzkpmjvgky3uizxxes3fpe)
>
> **Managing enterprise objects**
> : [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a)
> : [setDefaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgkztbovwhirlenf2gs3thinxw45dfpb2a)
>
> **Handling requests**
> : [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi)
> : [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylxmfvwk)
> : [context](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6y3pnz2gk6du)
> : [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o)
> : [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643mmvsxa)
> : [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)
>
> **Statistics**
> : [statistics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643umf2gs43unfrxg)
>
> **Debugging**
> : [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33of5sgkytvm5jxi4tjnztq)
> : [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33of5wg6z2torzgs3th)
>
> **Page Management**
> : [savePage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643bozsvaylhmu)
> : [restorePageForContextID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfon2g64tfkbqwozkgn5zeg33oorsxq5cjiq)

## Constructors

---

### WOSession

`public WOSession()`

Returns an initialized WOSession object. Session
time-out is set by default to a very long period. This method throws
exceptions if no session ID has been assigned or if it cannot initialize
the object for any other reason. The __isDistributionEnabled__ flag
is set to __false__, meaning that each transaction
will be assigned to an application instance specified in a configuration
file for load balancing

---

## Static Methods

---

### debugString

`public static void debugString(String aFormatString)`

Prints a message to the standard error device
(stderr), if __WODebuggingEnabled__ is true.
The message can include formatted variable data using String's concatenation
feature.

You control whether this method displays output with
the __WODebuggingEnabled__ user default option.
If __WODebuggingEnabled__ is true, then the __debugString__ messages
display their output. If __WODebuggingEnabled__ is false,
the __debugString__ messages don't display
their output.

---

### logString

`public static void logString(String aString)`

Prints a message to the standard error device
(stderr). The message can include formatted variable data using
String's concatenation feature, for example:
> ```
> int i = 500;
> float f = 2.045;
> WOApplication.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

## Instance Methods

---

### appendToResponse

`public void appendToResponse(
WOResponse aResponse,
WOContext aContext)`

This method is invoked during the phase of the
request-response loop during which the objects associated with a
response page append their HTML content to the response. WOSession's
default implementation of this method forwards the message to the
WOComponent that represents the response page. Then, it records
information about the current transaction by sending [recordStatisticsForResponse](WOStatisticsStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5zgky3pojsfg5dboruxg5djmnzum33skjsxg4dpnzzwk) and
then [descriptionForResponse](WOStatisticsStore.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pkn2gc5djon2gsy3tkn2g64tff5sgk43dojuxa5djn5xem33skjsxg4dpnzzwk) to
the [WOStatisticsStore](WOStatisticsStore.md#apple-k5hvg5dboruxg5djmnzvg5dpojsq) object.

Compiled
or scripted subclasses of WOSession can override this method to
replace or supplement the default behavior with custom logic.

__See
Also:__  [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o), [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)

---

### awake

`public void awake()`

Invoked at the beginning of a WOSession's involvement
in a cycle of the request-response loop, giving the WOSession an
opportunity to initialize its instance variables or perform setup
operations. The default implementation does nothing.

__See
Also:__  [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643mmvsxa)

---

### context

`public WOContext context()`

Returns the WOContext object for the current
transaction.

__See Also:__  [WOContext](WOContext.md#apple-k5hug33oorsxq5a) class

---

### defaultEditingContext

`public com.apple.yellow.eocontrol.EOEditingContext defaultEditingContext()`

Returns the default EOEditingContext object
for the session. The method creates the editing context the first
time that it is invoked and caches it for subsequent invocations.
There is only one unique EOEditingContext instance per session.
The instance's parent object store is initialized to the default parent
object store.

---

### domainForIDCookies

`public String domainForIDCookies()`

Returns the path that is passed when creating
a rendezvous cookie for the application. This path is lazily created
the first time it is used from the current request's __adaptorPrefix__ and
the application name (including the ".woa" extension).

---

### expirationDateForIDCookies

`public NSDate expirationDateForIDCookies()`

Returns when session and instance ID cookies
expire. By default, no expiration date is set and this method returns null.
Override this method if you want to return some other time, such
as the session expiration date.

Different applications can
override this method to enforce different behavior:

- A typical online banking application might use cookies and
  set the timeout to a very short amount of time (two minutes, for
  example), so that if the client doesn't interact with the browser
  and no request is made of the server, the client's session is
  timed out. This could be easily enforced on both the client-by
  setting the cookie timeout-and on the server from within the session
  object.
- A site wishing to personalize its pages based upon a user
  ID might set the timeout far into the distant future so that even
  when a client shuts down his browser, the cookie will still be there
  when he comes back with a bookmarked URL.
- Sites that want you to log in each time you visit could store
  the user ID in a cookie and then set the expiration date on the
  cookie to nil so that the cookie will go away whenever the client
  quits their browser.

---

### invokeAction

`public WOElement invokeAction(
WORequest aRequest,
WOContext aContext)`

WOSession objects receive this message during
the middle phase of the request-response loop. During this phase,
the __invokeAction__ message is propagated
through the objects of an application, most importantly, the WOElement
objects of the request page. The dynamic element on which the user
has acted (by, for example, clicking a button) responds by triggering
the method in the request WOComponent that is bound to the action.
The default behavior of WOSession is to send the message to the
WOComponent object that represents the request. Compiled or scripted
subclasses of WOSession can override this method to replace or supplement
the default behavior with custom logic.

__See
Also:__  [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi), [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)

---

### isDistributionEnabled

`public boolean isDistributionEnabled()`

Returns whether state distribution among multiple
application instances is enabled. Returns __false__ by default
since the default WOSessionStore (state in the server) does not
allow distribution. If this flag is disabled, a specific application
instance (whose identifying number is embedded in the URL) is assigned
to the session.

__See Also:__  [setDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle)

---

### isTerminating

`public boolean isTerminating()`

Returns whether the WOSession object will terminate
at the end of the current request-response loop.

__See
Also:__  [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dfojwws3tborsq)

---

### languages

`public NSArray languages()`

Returns the list of languages supported by the
session. The order of language strings (for example, "French")
indicates the preferred order of languages. This is initialized
from the users's browser preferences unless explicitly set with [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt).
For details, see "Localization" in the WebObjects programming
topics.

__See Also:__  [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt)

---

### objectForKey

`public Object objectForKey(String key)`

Returns an object stored in the session under
a specific key.

__See Also:__  [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forhwe2tfmn2em33sjnsxs)

---

### removeObjectForKey

`public void removeObjectForKey(String key)`

Removes the object stored in the session under
the specified key.

---

### restorePageForContextID

`public WOComponent restorePageForContextID(String contextID)`

Returns a page instance stored in the session
page cache. The key to the stored instance is its context ID, which
derives from the transaction's [WOContext](WOContext.md#apple-k5hug33oorsxq5a) or [WORequest](WORequest.md#apple-k5hvezlrovsxg5a) objects. This method returns null if restoration
is impossible.

__See Also:__  [savePage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643bozsvaylhmu)

---

### savePage

`public void savePage(WOComponent aPage)`

Saves the page instance aPage in the session
page cache. The context ID for the current transaction is made the
key for obtaining this instance in the cache using [restorePageForContextID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfon2g64tfkbqwozkgn5zeg33oorsxq5cjiq).

---

### savePageInPermanentCache

`pubic void savePageInPermanentCache(WOComponent aPage)`

Puts _aPage_ into
a separate page cache. This cache is searched first when attempting
to restore the page the next time its requested. This effectively
makes _aPage_ live for the duration
of the application regardless of the size of your page cache. This
is useful whe you are using frames and its possible for a page of
controls to be bumped from the page cache.

__See
Also:__  [permanentPageCacheSize](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxazlsnvqw4zloorigcz3finqwg2dfknuxuzi) ( [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4)), [setPermanentPageCacheSize](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pifyha3djmnqxi2lpnyxxgzlukbsxe3lbnzsw45cqmftwkq3bmnugku3jpjsq) ( [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4))

---

### sessionID

`public String sessionID()`

Returns the unique, randomly generated string
that identifies the session object. The session ID occurs in the
URL after the request handler key.

---

### setDefaultEditingContext

`public void setDefaultEditingContext(com.apple.yellow.eocontrol.EOEditingContext editingContext)`

Sets the editing context to be returned by [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a). This can be
used to set an editing context initialized with a different parent
object store than the default. This is useful when, for instance, each
session needs its own login to the database. Once a default editing
context has been established, you may not call __setDefaultEditingContext__ again.
Therefore, to provide your own default editing context, you must
call __setDefaultEditingContext__ before
ever calling [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a) since that will
lazily establish an editing context.

__See Also:__  [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a)

---

### setDistributionEnabled

`public void setDistributionEnabled(boolean aFlag)`

Enables or disables the distribution mechanism
that effects load balancing among multiple application instances.
When disabled (the default), generated URLs include the application
instance number; the adaptor uses this number to route the request
to the specific application instance based on information in the
configuration file. When this flag is enabled, generated URLs do
not contain the application instance number, and thus transactions
of a session are handled by whatever application instance is available.

__See
Also:__  [isDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltiruxg5dsnfrhk5djn5xek3tbmjwgkza)

---

### setLanguages

`public void setLanguages(NSArray languages)`

Sets the languages for which the session is
localized. The ordering of language strings in the array determines
the order in which the application will search _languages_.lproj
directories for localized strings, images, and component definitions.

__See
Also:__  [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc63dbnztxkylhmvzq)

---

### setObjectForKey

`public void setObjectForKey(Object anObject,
String key)`

Stores an object within the session under a
given key. This method allows a reusable component to add state
dynamically to any WOSession object. This method eliminates the
need for prior knowledge of the WOSession's instance variables.
A suggested mechanism for generating a unique key prefix for a given
subcomponent is to concatenate the component's name and its element
ID. For a specific component instance, such a prefix should remain
unique and invariant within a session.

__See
Also:__  [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc633cnjswg5cgn5zewzlz)

---

### setStoresIDsInCookies

`public void setStoresIDsInCookies(boolean flag)`

Enables or disables the cookie mechanism. Two
cookies are created for you when enabled: a session ID cookie with
the name "wosid," and an instance ID cookie with the name "woinst."
By default, the cookie mechanism is disabled.

---

### setStoresIDsInURLs

`public void setStoresIDsInURLs(boolean flag)`

Enables or disables the storing of session and
instance IDs in URLs. By default, IDs are stored in URLs.

---

### setTimeOut

`public void setTimeOut(double seconds)`

Set the session timeout in seconds. When a session
remains inactive-that is, the application receives no request
for this session-for a period longer than the time-out setting,
the session will terminate, resulting in the deallocation of the
WOSession object. By default, the session time-out is set from the [WOApplication](WOApplication.md#apple-k5huc4dqnruwgylunfxw4) method [sessionTimeout](WOApplication.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6qlqobwgsy3boruw63rponsxg43jn5xfi2lnmvxxk5a).

__See
Also:__  [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65djnvsu65lu)

---

### sleep

`public void sleep()`

Invoked at the conclusion of each request-response
loop in which the session is involved, giving the WOSession the
opportunity to deallocate objects initialized in the [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylxmfvwk) method. The
default WOSession implementation does nothing.

---

### statistics

`public NSArray statistics()`

Returns a list of the pages accessed by this
session, ordered from first accessed to last. For each page, the
string stored is obtained by sending [descriptionForResponse](WOComponent.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pinxw24dpnzsw45bpmrsxgy3snfyhi2lpnzdg64ssmvzxa33oonsq) to
the WOComponent object. By default, this returns the component's
name. If the application keeps a CLFF log file, this list is recorded in
the log file when the session terminates.

__See
Also:__  [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi)

---

### storesIDsInCookies

`public boolean storesIDsInCookies()`

Returns whether the cookie mechanism for storing
session and instance IDs is enabled. The cookie mechanism is disabled
by default.

---

### storesIDsInURLs

`public boolean storesIDsInURLs()`

Returns whether the URL mechanism for storing
session IDs and instance IDs is enabled. The URL mechanism is enabled
by default.

---

### takeValuesFromRequest

`public void takeValuesFromRequest(
WORequest aRequest,
WOContext aContext)`

WOSession objects receive this message during
the first phase of the request-response loop. During this phase,
the dynamic elements associated with the request page extract any
user input and assign the values to the appropriate component variables.
The default behavior of WOSession is to send the message to the [WOComponent](WOComponent.md#apple-k5hug33nobxw4zlooq) object that represents
the request. Compiled or scripted subclasses of WOSession can override
this method to replace or supplement the default behavior with custom
logic.

__See Also:__  [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi), [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o)

---

### terminate

`public void terminate()`

Causes the session to terminate after the conclusion
of the current request-response loop.

__See
Also:__  [isTerminating](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltkrsxe3ljnzqxi2lom4)

---

### timeOut

`public double timeOut()`

Returns the timeout interval in seconds.

__See
Also:__  [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forkgs3lfj52xi)

---

## Notifications

---

### WOSessionDidCreateNotification

`public static final String WOSessionDidCreateNotification`

Sent at the the end of the session initiation
(including awake). The object of the notification is the session instance

### WOSessionDidRestoreNotification

`public static final String WOSessionDidRestoreNotification`

Sent after the sesion is fully restored
(including awake). The object of the notification is the session instance.

### WOSessionDidTimeOutNotification

`public static final String WOSessionDidTimeOutNotification`

Sent when a session times out but before
it is released. The session ID is the object of the notification.

[![Table of Contents](attachments/images/up.gif)](../WebObjectsTOC.md)
