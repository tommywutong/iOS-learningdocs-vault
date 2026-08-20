---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOApplication.html
archived_at: '2026-07-18T01:28:45.213097Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOApplet-2.md)
[!](EOArchive-2.md)

---

# EOApplication

__Inherits From:__
com.sun.java.swing.JApplet

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

Java programs typically execute either as either an Applet running in a browser or care of a class implementing the static method [`main`](#apple-gq2tgmy) (often referred to as an "application"). EOApplication insulates the developer from the details of this distinction by serving as an execution-mode-independent repository for application-level client-side logic. The provided JApplet subclass EOApplet is essentially nothing more than an EOApplication-invoking shell.

EOApplication is for use in Java Client applications only; there isn't an equivalent class for Yellow Box.

---

## Constructors

protected `EOApplication`()

This constructor is exposed simply so that subclasses may refer to it without compiler error. EOApplication should always be instantiated through one of the two static initializers.

---

### application

public static com.apple.client.eointerface.EOApplication `application`(com.apple.client.eodistribution.EODistributionChannel _channel_)

One of two [`sharedApplication`](#apple-gq2tmma) initializers, this variant should be invoked in contexts such as [`main`](#apple-gq2tgmy) where the parameters required by the following edition are unavailable and must be requested from a server-side WOJavaClientApplet via _channel_. Once these parameters have been retrieved this method performs the same initialization as the following method.

public static com.apple.client.eointerface.EOApplication `application`(java.lang.String _className_, com.apple.client.eodistribution.EODistributionChannel _channel_com.apple.client.foundation.NSArray _languages_,
java.lang.String _controllerClassName_,
java.awt.container _container_)

Sets [`sharedApplication`](#apple-gq2tmma) to a new instance of the EOApplication with _className_. After initializing an EODistributedObjectStore with _channel_ and establishing it as EOEditingContext's `defaultParentObjectStore`, this method creates an instance of the EOInterfaceController with _controllerClassName_ and runs it in _container_ (see [`createInterfaceController`](#apple-gq2tcny) and [`languages`](#apple-gq2teoa) for further details).

---

## Instance Methods

---

### applicationWillExit

protected boolean `applicationWillExit`()

Invoked whenever the last window registered with the receiver via [`registerWindow`](#apple-gq2tgoa) has been closed in a non-Applet execution context, this method gives custom subclasses an opportunity to perform any necessary cleanup before exit or simply reject EOApplication's window management logic by returning `false` (see [`registerWindow`](#apple-gq2tgoa)). The default implementation returns `true`.

---

### createInterfaceController

public static com.apple.client.eointerface.EOInterfaceController `createInterfaceController`(java.lang.String _className_, java.awt.Container _container_)

This convenience method creates and runs a new instance of the EOInterfaceController with _className_. If _container_ is non-null, it is passed to the new controller's implementation of `runInContainer`, otherwise the "presentation-neutral" method `run` is invoked. Returns the new instance.

---

### finishInitialization

protected void `finishInitialization`()

Invoked as the final step in the receiver's bootstrapping, this method represents a subclass initialization hook somewhat analogous to Applet's [`init`](EOApplet.md#apple-gm2teoa). By the time `finishInitialization` is invoked, EOEditingContext's `defaultParentObjectStore` has been set, connecting the receiver to the server, and any specified EOInterfaceController has been instantiated and run.

---

### languages

public void com.apple.client.foundation.NSArray `languages`()

Returns the array of languages supported by the receiver's localization as defined by developer and retrieved from the server (note that only the first element of this array, typically defined by WOJavaClientApplet's WOAppletLanguageKey, is currently used).

---

### main

public static void `main`(java.lang.String _arguments_)

EOApplication's implementation of this method allows client-side programs to execute from the command line in addition to running as an Applet. The first, required element of _arguments_ must be the same application URL users would enter to access the equivalent EOApplet in a browser. The optional second element should be the name of any initial entry page other than Main. After instantiating an EODistributionChannel on the basis of these two parameters,main simply invokes the channel-driven version of `application`.

---

### registerWindow

public void `registerWindow`(java.awt.Window _window_)

Disposing of all windows in a non-Applet-based user interface launched via `main` does not cause the program to exit because the Java virtual machine continues to run. EOApplication attempts to manage this problem for the consumer by maintaining a registry of all Windows. When the last remaining Window registered with this method is disposed of in a non-Applet execution context, EOApplication invokes `shouldTerminate`. If this method returns `true`, System's `exit` method is invoked with a zero _status_. Also see [`windowRegistryEnabled`](#apple-gq2tmni) and EOInterfaceController's `shouldRegisterWindow`.

Note the use of "disposing" rather than "closing" in the previous paragraph. Despite its name, the AWT WindowListener message `windowClosed` is only sent by java.awt.Window within `dispose`, not `setVisible`. As a result, the exit logic EOApplication provides is only activated by Window disposal.

---

### setLanguages

public void `setLanguages`(com.apple.client.foundation.NSArray _languages_)

Sets the array of languages supported by the receiver's localization as defined by the developer. Note that only the first element of this array is currently referenced.

---

### setWindowRegistryEnabled

public boolean `setWindowRegistryEnabled`(boolean _enabled_)

Sets whether or not the window registration logic described in `registerWindow` should be used by the receiver.

---

### shouldTerminate

protected boolean `shouldTerminate`()

This method acts as a subclass hook for application cleanup logic and refinement of the exit condition described in `registerWindow`. A return value of `false` will inhibit invocation of `exit` when all registered windows have been disposed. The default implementation returns `true`.

---

### sharedApplication

public static void `sharedApplication`()

Returns the EOApplication instance initialized via one the two `application` methods, throwing an IllegalStateException if neither has been invoked.

---

### windowRegistryEnabled

public boolean `windowRegistryEnabled`()

Returns whether or not window registration logic described in `registerWindow` is used by the receiver. The default is `true`, but this may be overridden via `setWindowRegistryEnabled`.

---

[!](EOApplet-2.md)
[!](EOArchive-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
