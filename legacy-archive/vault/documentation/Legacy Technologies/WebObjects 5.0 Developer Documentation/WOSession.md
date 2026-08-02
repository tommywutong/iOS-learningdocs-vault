---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/WebObjectsRef/Java/Classes/WOSession.html
archived_at: '2026-07-15T08:15:15.844584Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# WOSession

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : Cloneable: Serializable: NSKeyValueCoding: NSKeyValueCoding.ErrorHandling NSKeyValueCodingAdditions

> **__Package:__**
> : com.webobjects.appserver

---

## Class Description

---

WOSession objects represent _sessions_, periods during which access to a WebObjects application and its resources is granted to a particular client (typically a browser). An application can have many concurrent sessions, each with its own special "view" of the application and its own set of data values. For instance, one client could be accessing a "catalog" application, where that client is going from page to page, filling a virtual shopping cart with items for purchase. Another client might be accessing the same application at the same time, but that person might have different items in his or her shopping cart.

Perhaps the most important thing a WOSession object does is encapsulate state for a session. After the application handles a request, it stores the WOSession until the next request of the session occurs. All the information that is important for maintaining continuity throughout the session is preserved. And the integrity of session data is maintained as well; the data of a session not only persists between requests but is kept separate from that of all other sessions.

When you develop an application, you identify data with session-wide scope by declaring instance variables in your subclass of WOSession (or, for scripted applications, in __Session.wos__). Then, before the end of a cycle of the request-response loop, ensure that the instance variables hold current session values.

The application uses a _session ID_ to identify a session object. Upon receiving the first request of a session, the application assigns a session ID (a unique, randomly generated string) to the session. The session ID appears in the URL between the application name and the page name.

At the end of each cycle of the request-response loop, the application stores the WOSession object according to the storage strategy implemented by the chosen WOSessionStore. When the application receives the next request of the session, it restores the WOSession, using the session ID as key.

To be stored and restored according to any WOSessionStore strategy, a WOSession must be convertible to an object archive. WOSessions are therefore asked to serialize and deserialize themselves prior to being archived and unarchived (in either binary or ASCII format). To accomplish this, the WOSession should implement the __encodeWithCoder:__ and __initWithCoder:__ methods of the NSCoding protocol.

Because storage of sessions in application memory can consume large amounts of memory over time, WOSession includes methods for controlling the lifespan of session objects. The [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forkgs3lfj52xi) method sets a period of inactivity after which the session is terminated. The [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dfojwws3tborsq) method explicitly ends a session.

The WOSession class provides several other methods useful for tasks ranging from localization to database access:

- WOSession objects can interject custom session behavior into the request-response loop by implementing the request-handling methods ( [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a), [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o), and [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi)) as well as [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylxmfvwk) and [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643mmvsxa).
- For database access, the [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a) method gives each WOSession object in an application its own Enterprise Objects editing context.
- An object in an application doesn't have to know which instance variables its WOSession holds in order to store session values. With the [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forhwe2tfmn2em33sjnsxs) and [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc633cnjswg5cgn5zewzlz) methods it can store and retrieve values as needed. This mechanism is especially useful for reusable components.
- An application's WOSession objects also play a role in localization. Through the [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt) method you can store a list of the languages supported by the application. The sequence of language strings in the list indicates the order of language preference for a particular session. Several resource-access methods in WOResourceManager, WOApplication, and WOComponent refer to the [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc63dbnztxkylhmvzq) array when they locate such things as localized strings, images, and sounds.
- WOSession objects also allow you to affect load balancing with the [setDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle) method; if the flag set by this method is false (the default), transactions of the session are restricted to a single application instance. If this the case, the application instance number as well as the application host name are appended to the URL.

## Interfaces Implemented

---

> : NSKeyValueCoding: [takeValueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsum33sjnsxs): [valueForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65tbnr2wkrtpojfwk6i): : NSKeyValueCodingAdditions: [takeValueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsum33sjnsxsudborua): [valueForKeyPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65tbnr2wkrtpojfwk6kqmf2gq): : NSKeyValueCoding.ErrorHandling: [handleQueryWithUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62dbnzsgyzkrovsxe6kxnf2gqvlomjxxk3tejnsxs): [handleTakeValueForUnboundKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62dbnzsgyzkumfvwkvtbnr2wkrtpojkw4ytpovxgis3fpe): [unableToSetNullForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65lomfrgyzkun5jwk5coovwgyrtpojfwk6i):

## Method Types

---

> **Constructor**
> : [WOSession](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6v2pknsxg43jn5xa)
>
> **Obtaining attributes**
> : [domainForIDCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdpnvqws3sgn5zesrcdn5xww2lfom): [expirationDateForIDCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zlyobuxeylunfxw4rdborsum33sjfceg33pnnuwk4y): [isDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltiruxg5dsnfrhk5djn5xek3tbmjwgkza): [sessionID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643fonzws33ojfca): [storesIDsInCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643un5zgk42jirzus3sdn5xww2lfom): [storesIDsInURLs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643un5zgk42jirzus3svkjghg)
>
> **Setting attributes**
> : [allowedToViewStatistics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylmnrxxozlekrxvm2lfo5jxiylunfzxi2ldom): [setDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle): [setStoresIDsInCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forjxi33smvzusrdtjfxeg33pnnuwk4y): [setStoresIDsInURLs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forjxi33smvzusrdtjfxfkusmom)
>
> **Terminating**
> : [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dfojwws3tborsq): [isTerminating](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltkrsxe3ljnzqxi2lom4): [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65djnvsu65lu): [timeOutMillis](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65djnvsu65lujvuwy3djom): [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forkgs3lfj52xi)
>
> **Localization**
> : [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc63dbnztxkylhmvzq): [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt)
>
> **Managing component state**
> : [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forhwe2tfmn2em33sjnsxs): [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc633cnjswg5cgn5zewzlz): [removeObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfnvxxmzkpmjvgky3uizxxes3fpe)
>
> **Managing enterprise objects**
> : [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a): [setDefaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgkztbovwhirlenf2gs3thinxw45dfpb2a)
>
> **Handling requests**
> : [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi): [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylxmfvwk): [context](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6y3pnz2gk6du): [finalize](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ztjnzqwy2l2mu): [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o): [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643mmvsxa): [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)
>
> **Statistics**
> : [statistics](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643umf2gs43unfrxg)
>
> **Debugging**
> : [debugString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33of5sgkytvm5jxi4tjnztq): [logString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33of5wg6z2torzgs3th)
>
> **Page Management**
> : [savePage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643bozsvaylhmu): [restorePageForContextID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfon2g64tfkbqwozkgn5zeg33oorsxq5cjiq)
>
> **Validation**
> : [validateEventsLogin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65tbnruwiylumvcxmzloorzuy33hnfxa): [validateStatisticsLogin](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65tbnruwiylumvjxiylunfzxi2ldongg6z3jny): [validationFailedWithException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65tbnruwiylunfxw4rtbnfwgkzcxnf2gqrlymnsxa5djn5xa)
>
> **Other**
> : [allowedToViewEvents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylmnrxxozlekrxvm2lfo5cxmzloorzq): [canAccessFieldsDirectly](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5lu6u3fonzws33of5rwc3sbmnrwk43tizuwk3deoncgs4tfmn2gy6i): [timeOutForIDCookies](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65djnvsu65luizxxeskeinxw623jmvzq)

## Constructors

---

### WOSession

`public WOSession()`

Returns an initialized WOSession object. Session time-out is set by default to a very long period. This method throws exceptions if no session ID has been assigned or if it cannot initialize the object for any other reason. The __isDistributionEnabled__ flag is set to __false__, meaning that each transaction will be assigned to an application instance specified in a configuration file for load balancing

`public WOSession(String aSessionID)`

This constructor initializes a newly-instantiated session object with the provided session ID (pass the session ID as a String). This constructor throws a RuntimeException if a session ID isn't provided or if the session object cannot be properly initialized.

---

## Static Methods

---

### __canAccessFieldsDirectly__

`public static boolean canAccessFieldsDirectly()`

WOSession's implementation of this static method returns `true`, indicating that key/value coding is allowed to access fields in this object if an appropriate method isn't present.

---

### debugString

`public static void debugString(String aFormatString)`

Prints a message to the standard error device (stderr), if __WODebuggingEnabled__ is true. The message can include formatted variable data using String's concatenation feature.

You control whether this method displays output with the __WODebuggingEnabled__ user default option. If __WODebuggingEnabled__ is true, then the __debugString__ messages display their output. If __WODebuggingEnabled__ is false, the __debugString__ messages don't display their output.

---

### logString

`public static void logString(String aString)`

Prints a message to the standard error device (stderr). The message can include formatted variable data using String's concatenation feature, for example:
> ```
> int i = 500;
> float f = 2.045;
> WOApplication.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

## Instance Methods

---

### __allowedToViewStatistics__

`public boolean allowedToViewStatistics()`

Returns `true` if clients of this session are allowed to view session statistics. If statistics aren't being gathered, or if a password must be supplied prior to viewing those statistics and the client hasn't supplied the proper password, this method returns `false`. By default, sessions don't allow statistics to be viewed.

---

### allowedToViewEvents

`public boolean allowedToViewEvents()`

Description forthcoming.

---

### appendToResponse

`public void appendToResponse( WOResponse aResponse, WOContext aContext)`

This method is invoked during the phase of the request-response loop during which the objects associated with a response page append their HTML content to the response. WOSession's default implementation of this method forwards the message to the WOComponent that represents the response page. Then, it records information about the current transaction by sending recordStatisticsForResponse and then descriptionForResponse to the WOStatisticsStore object.

Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See Also:__ [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o), [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)

---

### awake

`public void awake()`

Invoked at the beginning of a WOSession's involvement in a cycle of the request-response loop, giving the WOSession an opportunity to initialize its instance variables or perform setup operations. The default implementation does nothing.

__See Also:__ [sleep](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643mmvsxa)

---

### __clone__

`public Object clone()`

Conformance to Cloneable.

---

### context

`public WOContext context()`

Returns the WOContext object for the current transaction.

__See Also:__ WOContext class

---

### defaultEditingContext

`public com.webobjects.eocontrol.EOEditingContext defaultEditingContext()`

Returns the default EOEditingContext object for the session. The method creates the editing context the first time that it is invoked and caches it for subsequent invocations. There is only one unique EOEditingContext instance per session. The instance's parent object store is initialized to the default parent object store.

---

### domainForIDCookies

`public String domainForIDCookies()`

Returns the path that is passed when creating a rendezvous cookie for the application. This path is lazily created the first time it is used from the current request's __adaptorPrefix__ and the application name (including the ".woa" extension).

---

### expirationDateForIDCookies

`public NSTimestamp expirationDateForIDCookies()`

This method is deprecated. Do not use it.

---

### finalize

`public void finalize() throws Throwable`

WOSession's finalizer. This method disposes of the session's editing context, if it has one. It throws Throwable if a non-recoverable error occurs during the disposal of the editing context.

---

### handleQueryWithUnboundKey

`public Object handleQueryWithUnboundKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### handleTakeValueForUnboundKey

`public void handleTakeValueForUnboundKey(Object value, String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### invokeAction

`public WOActionResults invokeAction( WORequest aRequest, WOContext aContext)`

WOSession objects receive this message during the middle phase of the request-response loop. During this phase, the __invokeAction__ message is propagated through the objects of an application, most importantly, the WOElement objects of the request page. The dynamic element on which the user has acted (by, for example, clicking a button) responds by triggering the method in the request WOComponent that is bound to the action. The default behavior of WOSession is to send the message to the WOComponent object that represents the request. Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See Also:__ [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi), [takeValuesFromRequest](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dbnnsvmylmovsxgrtsn5wvezlrovsxg5a)

---

### isDistributionEnabled

`public boolean isDistributionEnabled()`

Returns whether state distribution among multiple application instances is enabled. Returns __false__ by default since the default WOSessionStore (state in the server) does not allow distribution. If this flag is disabled, a specific application instance (whose identifying number is embedded in the URL) is assigned to the session.

__See Also:__ [setDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forcgs43uojuwe5lunfxw4rlomfrgyzle)

---

### isTerminating

`public boolean isTerminating()`

Returns whether the WOSession object will terminate at the end of the current request-response loop.

__See Also:__ [terminate](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65dfojwws3tborsq)

---

### languages

`public NSArray languages()`

Returns the list of languages supported by the session. The order of language strings (for example, "French") indicates the preferred order of languages. This is initialized from the users's browser preferences unless explicitly set with [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt). For details, see "Localization" in the WebObjects programming topics.

__See Also:__ [setLanguages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forggc3thovqwozlt)

---

### objectForKey

`public Object objectForKey(String key)`

Returns an object stored in the session under a specific key.

__See Also:__ [setObjectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forhwe2tfmn2em33sjnsxs)

---

### removeObjectForKey

`public void removeObjectForKey(String key)`

Removes the object stored in the session under the specified key.

---

### restorePageForContextID

`public WOComponent restorePageForContextID(String contextID)`

Returns a page instance stored in the session page cache. The key to the stored instance is its context ID, which derives from the transaction's WOContext or WORequest objects. This method returns null if restoration is impossible.

__See Also:__ [savePage](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643bozsvaylhmu)

---

### savePage

`public void savePage(WOComponent aPage)`

Saves the page instance aPage in the session page cache. The context ID for the current transaction is made the key for obtaining this instance in the cache using [restorePageForContextID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc64tfon2g64tfkbqwozkgn5zeg33oorsxq5cjiq).

---

### savePageInPermanentCache

`pubic void savePageInPermanentCache(WOComponent aPage)`

Puts _aPage_ into a separate page cache. This cache is searched first when attempting to restore the page the next time its requested. This effectively makes _aPage_ live for the duration of the application regardless of the size of your page cache. This is useful when you are using frames and its possible for a page of controls to be bumped from the page cache.

__See Also:__ permanentPageCacheSize (WOApplication), setPermanentPageCacheSize (WOApplication)

---

### sessionID

`public String sessionID()`

Returns the unique, randomly generated string that identifies the session object. The session ID occurs in the URL after the request handler key.

---

### setDefaultEditingContext

`public void setDefaultEditingContext( com.webobjects.eocontrol.EOEditingContext editingContext)`

Sets the editing context to be returned by [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a). This can be used to set an editing context initialized with a different parent object store than the default. This is useful when, for instance, each session needs its own login to the database. Once a default editing context has been established, you may not call __setDefaultEditingContext__ again. Therefore, to provide your own default editing context, you must call __setDefaultEditingContext__ before ever calling [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a) since that will lazily establish an editing context.

__See Also:__ [defaultEditingContext](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6zdfmzqxk3duivsgs5djnztug33oorsxq5a)

---

### setDistributionEnabled

`public void setDistributionEnabled(boolean aFlag)`

Enables or disables the distribution mechanism that effects load balancing among multiple application instances. When disabled (the default), generated URLs include the application instance number; the adaptor uses this number to route the request to the specific application instance based on information in the configuration file. When this flag is enabled, generated URLs do not contain the application instance number, and thus transactions of a session are handled by whatever application instance is available.

__See Also:__ [isDistributionEnabled](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltiruxg5dsnfrhk5djn5xek3tbmjwgkza)

---

### setLanguages

`public void setLanguages(NSArray languages)`

Sets the languages for which the session is localized. The ordering of language strings in the array determines the order in which the application will search _languages_.lproj directories for localized strings, images, and component definitions.

__See Also:__ [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc63dbnztxkylhmvzq)

---

### setObjectForKey

`public void setObjectForKey(Object anObject, String key)`

Stores an object within the session under a given key. This method allows a reusable component to add state dynamically to any WOSession object. This method eliminates the need for prior knowledge of the WOSession's instance variables. A suggested mechanism for generating a unique key prefix for a given subcomponent is to concatenate the component's name and its element ID. For a specific component instance, such a prefix should remain unique and invariant within a session.

__See Also:__ [objectForKey](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc633cnjswg5cgn5zewzlz)

---

### setStoresIDsInCookies

`public void setStoresIDsInCookies(boolean flag)`

Enables or disables the cookie mechanism. Two cookies are created for you when enabled: a session ID cookie with the name "wosid," and an instance ID cookie with the name "woinst." By default, the cookie mechanism is disabled.

---

### setStoresIDsInURLs

`public void setStoresIDsInURLs(boolean flag)`

Enables or disables the storing of session and instance IDs in URLs. By default, IDs are stored in URLs.

---

### setTimeOut

`public void setTimeOut(double seconds)`

Set the session timeout in seconds. When a session remains inactive-that is, the application receives no request for this session-for a period longer than the time-out setting, the session will terminate, resulting in the deallocation of the WOSession object. By default, the session time-out is set from the WOApplication method sessionTimeout..

__See Also:__ [timeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc65djnvsu65lu)

---

### sleep

`public void sleep()`

Invoked at the conclusion of each request-response loop in which the session is involved, giving the WOSession the opportunity to deallocate objects initialized in the [awake](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylxmfvwk) method. The default WOSession implementation does nothing.

---

### statistics

`public NSArray statistics()`

Returns a list of the pages accessed by this session, ordered from first accessed to last. For each page, the string stored is obtained by sending descriptionForResponse to the WOComponent object. By default, this returns the component's name. If the application keeps a CLFF log file, this list is recorded in the log file when the session terminates.

__See Also:__ [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi)

---

### storesIDsInCookies

`public boolean storesIDsInCookies()`

Returns whether the cookie mechanism for storing session and instance IDs is enabled. The cookie mechanism is disabled by default.

---

### storesIDsInURLs

`public boolean storesIDsInURLs()`

Returns whether the URL mechanism for storing session IDs and instance IDs is enabled. The URL mechanism is enabled by default.

---

### takeValueForKey

`public void takeValueForKey(Object value, String key)`

Conformance to NSKeyValueCoding.

---

### takeValueForKeyPath

`public void takeValueForKeyPath(Object value, String keyPath)`

Conformance to NSKeyValueCodingAdditions.

---

### takeValuesFromRequest

`public void takeValuesFromRequest( WORequest aRequest, WOContext aContext)`

WOSession objects receive this message during the first phase of the request-response loop. During this phase, the dynamic elements associated with the request page extract any user input and assign the values to the appropriate component variables. The default behavior of WOSession is to send the message to the WOComponent object that represents the request. Compiled or scripted subclasses of WOSession can override this method to replace or supplement the default behavior with custom logic.

__See Also:__ [appendToResponse](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc6ylqobsw4zcun5jgk43qn5xhgzi), [invokeAction](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62loozxwwzkbmn2gs33o)

---

### terminate

`public void terminate()`

Causes the session to terminate after the conclusion of the current request-response loop.

__See Also:__ [isTerminating](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc62ltkrsxe3ljnzqxi2lom4)

---

### timeOut

`public double timeOut()`

Returns the timeout interval in seconds.

__See Also:__ [setTimeOut](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6v2pknsxg43jn5xc643forkgs3lfj52xi)

---

### timeOutForIDCookies

`public int timeOutForIDCookies()`

This method is deprecated. Do not use it.

---

### __timeOutMillis__

`public long timeOutMillis()`

Returns the session timeout, in milliseconds, as a long.

---

### __toString__

`public String toString()`

Returns a String description of the WOSession object that enumerates a number of the more important aspects of the session.

---

### unableToSetNullForKey

`public void unableToSetNullForKey(String key)`

Conformance to NSKeyValueCoding.ErrorHandling.

---

### validateEventsLogin

`public void validateEventsLogin ( String password, String username)`

Description forthcoming.

---

### validateStatisticsLogin

`public void validateStatisticsLogin ( String password, String username)`

Description forthcoming.

---

### validationFailedWithException

`public void validationFailedWithException ( Throwable aThrowable, Object value, String keyPath, WOComponent aComponent)`

Description forthcoming.

---

### valueForKey

`public Object valueForKey(String key)`

Conformance to NSKeyValueCoding.

---

### valueForKeyPath

`public Object valueForKeyPath(String keyPath)`

Conformance to NSKeyValueCodingAdditions.

---

## Notifications

---

### WOSessionDidCreateNotification

`public static final String WOSessionDidCreateNotification`

Sent at the the end of the session initiation (including awake). The object of the notification is the session instance

### WOSessionDidRestoreNotification

`public static final String WOSessionDidRestoreNotification`

Sent after the sesion is fully restored (including awake). The object of the notification is the session instance.

### WOSessionDidTimeOutNotification

`public static final String WOSessionDidTimeOutNotification`

Sent when a session times out but before it is released. The session ID is the object of the notification.

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/WebObjectsRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
