---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Classes/EOApplication.html
archived_at: '2026-07-15T08:13:42.562049Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOApplication

> **__Inherits from:__**
> : [EOController](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhug33oorzg63dmmvza): Object

> **__Package:__**
> : com.webobjects.eoapplication

---

## Class Description

---

Java Client applications typically execute from the command line (often referred to as a "Java application") or as an applet running in a browser. EOApplication insulates the developer from this distinction by serving as an execution-mode-independent repository for application-level client-side logic. The provided JApplet subclass EOApplet simply invokes EOApplication with the HTML arguments as parameters.

Each application has a window observer which keeps track of all of the windows in the application, which window is active, and whether all windows have been closed. The window observer has two notifications: `ActiveWindowChangedNotification` and `LastWindowClosedNotification`, which the __finishInitialization__ method binds to the __activeWindowDidChange__ and __lastWindowDidClose__ methods, respectively.

Each application also has a defaults manager, an EODefaults object, which maintains two dictionaries for application defaults: a transient dictionary whose values are forgotten when the application exits, and a persistent dictionary whose values are stored on the server. The defaults manager implements __valueForKey__ to read the defaults and __setPersistentValueForKey__ and __setTransientValueForKey__ to store the defaults.

EOApplication is used in Java Client application only; there is no equivalent class on the server side.

|  |  |
| --- | --- |
| __XML Tag__ | __Default Rule System Controller Type__ |
| None | None |

## Constants

---

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| ApplicationDidStart | Description forthcoming. |
| ApplicationWillQuit | Description forthcoming. |

## Interfaces Implemented

---

> : NSDisposable: [dispose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwi2ltobxxgzi): : EOKeyValueCodingAdditions (com.webobjects.eocontrol): : EOAction.Enabling: [canPerformActionNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwgylokbsxeztpojwucy3unfxw4ttbnvswi): : EOKeyValueCoding (com.webobjects.eocontrol inherited from EOKeyValueCodingAdditions): : NSKeyValueCoding (inherited from EOKeyValueCoding):

## Method Types

---

> **Accessing the shared instance**
> : [sharedApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlqobwgsy3boruw63rponugc4tfmraxa4dmnfrwc5djn5xa)
>
> **Entering the application**
> : [main](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlqobwgsy3boruw63rpnvqws3q): [startApplication](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qlqobwgsy3boruw63rpon2gc4tuifyha3djmnqxi2lpny)
>
> **Initializing and terminating the application**
> : [canQuit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwgylokf2ws5a): [finishInitialization](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwm2lonfzwqslonf2gsylmnf5gc5djn5xa): [quitsOnLastWindowClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxc5ljorzu63smmfzxiv3jnzsg652dnrxxgzi): [setCanQuit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxgzluinqw4ulvnf2a): [setQuitsOnLastWindowClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxgzlukf2ws5dtj5xeyyltorlws3ten53ug3dponsq)
>
> **Managing the application**
> : [arguments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwc4thovwwk3tuom): [defaults](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwizlgmf2wy5dt): [languages](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwyylom52wcz3fom)
>
> **Managing documents**
> : [documents](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwi33dovwwk3tuom): [documentsForGlobalID](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwi33dovwwk3tuondg64shnrxweylmjfca): [editedDocuments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwkzdjorswirdpmn2w2zloorzq): [hasEditedDocuments](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwqyltivsgs5dfmrcg6y3vnvsw45dt)
>
> **Managing the window observer**
> : [activeWindowDidChange](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwcy3unf3gkv3jnzsg652enfseg2dbnztwk): [lastWindowDidClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwyyltorlws3ten53ui2leinwg643f): [setWindowObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxgzluk5uw4zdpo5hwe43foj3gk4q): [windowObserver](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxo2lomrxxot3consxe5tfoi)
>
> **Methods inherited from Object**
> : [toString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxi32torzgs3th)
>
> **Performing main menu operations**
> : [activatePreviousWindow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwcy3unf3gc5dfkbzgk5tjn52xgv3jnzsg65y): [collectChangesFromServer](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwg33mnrswg5cdnbqw4z3fondhe33nknsxe5tfoi): [defaultActions](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwizlgmf2wy5cbmn2gs33oom): [saveAll](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxgylwmvawy3a): [quit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxc5ljoq)

## Constructors

---

### EOApplication

`public EOApplication()`

Description forthcoming.

---

## Static Methods

---

### main

`public static void main(String[] args[])`

This is the standard entry point for applications started from the command line (not in an applet). The _args_ array contains the application's command-line arguments (for example, `-key1 value1 -key2 value2 ...`), which are stored in a parameter dictionary (NSDictionary). The user must specify an application URL (using the `-applicationURL <application URL>` argument), the name of a distribution channel class (using the `-channelClassName <channel class name>` argument), or both depending on the specific distribution channel. If the user specifies the application URL, he can optionally specify any initial entry page other than Main. After instantiating an EODistributionChannel on the basis of these two parameters, __main__ simply invokes `startApplication`.

---

### sharedApplication

`public static EOApplication sharedApplication()`

Returns the EOApplication instance initialized via the __startApplication__ method, throwing an IllegalStateException if __startApplication__ has not yet been invoked.

---

### startApplication

`public static EOApplication startApplication( NSDictionary parameterDictionary, EOComponentController initialTopComponentController, boolean remoteRequestArguments)`

Creates an EOApplication. An application can execute from the command line or as an applet. EOApplication's parameters are specified using parameterDictionary. If the application is a Java application, the EOApplication's __main__ method reads and parses the parameters from the command line. In addition, it sets _remoteRequestArguments_ to `true`, which triggers __startApplication__ to read additional parameters from the applet at the URL specified on the command line. If the application is started in an applet, all parameters are contained in the HTML. The _initialTopComponentController_ parameter specifies the top-most EOComponentController in the controller hierarchy. For applets, this controller is an EOAppletController. For command line applications, the __main__ method sets _initialTopComponentController_ to `null`, which causes a new EOFrameController to be instantiated and used as the top-most EOComponentController.

---

## Instance Methods

---

### activatePreviousWindow

`public void activatePreviousWindow()`

Activates the previously active window. The user can invoke this method from the Window menu.

---

### activeWindowDidChange

`public void activeWindowDidChange(NSNotification aNSNotification)`

This method is invoked when the user changes the active window in the receiver (usually by clicking in an inactive window). It is invoked via a notification from the receiver's window observer.

---

### arguments

`public NSDictionary arguments()`

Returns all of the receiver's arguments in a dictionary. If the application is a Java application (and not an Applet), the arguments can come from both the command line and the applet at the URL specified on the command line.

---

### canPerformActionNamed

`public boolean canPerformActionNamed(String actionName)`

Conformance to [EOAction.Enabling](EOAction.Enabling.md#apple-ijauissii5eum). See the method description of [canPerformActionNamed](EOAction.Enabling.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpifrxi2lpnyxek3tbmjwgs3thf5rwc3sqmvzgm33snvawg5djn5xe4ylnmvsa) in the interface specification for EOAction.Enabling. An action may be disallowed if it is disabled or is an `activatePreviousWindow` action and the first window is active.

---

### canQuit

`public boolean canQuit()`

Returns whether or not the receiver has a Quit item in the File submenu. Defaults to `true` if the application is run from the command line and `false` if it is started in an applet.

---

### collectChangesFromServer

`public void collectChangesFromServer()`

Updates the receiver's Enterprise Objects to reflect the changes sent to the server from other client applications. By default, the application does not automatically update its objects, however, the user can update the objects manually from the Document menu in Direct to Java Client applications.

---

### defaultActions

`protected NSArray defaultActions()`

Returns an NSArray containing the actions (EOAction objects) the receiver can perform.

---

### defaults

`public EODefaults defaults()`

Returns the receiver's defaults manager (an EODefaults object). If your application requires the user to log in, you should override this method so it returns `null` until the user logs in.

---

### dispose

`public void dispose()`

Prepares the receiver so it is disposed when Java performs garbage collection.

---

### documents

`public NSArray documents()`

Returns an NSArray containing the receiver's visible documents (EODocument objects).

---

### documentsForGlobalID

`public NSArray documentsForGlobalID( com.webobjects.eocontrol.EOGlobalID globalID, String entityName)`

Returns an NSArray containing the receiver's visible documents (EODocument objects) that edit Enterprise Objects with an entity name matching _entityName_ and global ID matching _globalID_.

---

### editedDocuments

`public NSArray editedDocuments()`

Returns an NSArray containing the receiver's visible documents (EODocument objects) that have been edited.

---

### finishInitialization

`protected void finishInitialization()`

This method is invoked after the final event thread is guaranteed to be running. If you subclass EOApplication, use this method to initialize anything relating to the user interface or event-handling. Do not perform such initialization using EOApplication's constructor.

---

### hasEditedDocuments

`public boolean hasEditedDocuments()`

Returns `true` if any of the receiver's documents has been edited. Otherwise returns `false`.

---

### languages

`public NSArray languages()`

Returns an NSArray containing the language names (Strings) for which the application is localized. An example language is `English`.

---

### lastWindowDidClose

`public void lastWindowDidClose(NSNotification aNSNotification)`

This method is invoked when the user closes the last window in the receiver. It is invoked as a notification from the receiver's window observer.

__See Also:__ [quitsOnLastWindowClose](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxxc5ljorzu63smmfzxiv3jnzsg652dnrxxgzi)

---

### quit

`public void quit()`

Causes the receiver to quit (provided `canQuit` is `true`).

__See Also:__ [canQuit](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifyha3djmnqxi2lpnyxwgylokf2ws5a)

---

### quitsOnLastWindowClose

`public boolean quitsOnLastWindowClose()`

Returns whether or not the receiver quits when the user closes all of its windows. Defaults to `true`.

---

### saveAll

`public boolean saveAll()`

Attempts to save all of the receiver's edited documents and returns `true` if it succeeds.

---

### __sessionDidTimeOut__

`public void sessionDidTimeOut()`

Description forthcoming.

---

### setCanQuit

`public void setCanQuit(boolean flag)`

Sets whether or not the application has a quit item in the File menu.

---

### setQuitsOnLastWindowClose

`public void setQuitsOnLastWindowClose(boolean flag)`

Sets whether or not the receiver quits when the user closes all of its windows.

---

### setWindowObserver

`public void setWindowObserver(EOWindowObserver anEOWindowObserver)`

Sets the receiver's window observer to _anEOWindowObserver_. The window observer manages the application's windows: which window is active, how many there are, etc.

---

### toString

`public String toString()`

Returns the receiver as a string that contains the results of the EOController's __toString__ method, the languages the receiver supports, and the status of the `canQuit` and `quitsOnLastWindowClose` flags.

---

### windowObserver

`public EOWindowObserver windowObserver()`

Returns the receiver's window observer.

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
