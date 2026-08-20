---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/WOComponent.html
archived_at: '2026-07-18T01:28:51.146283Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](WOAssociation.md)
[!](WOContext.md)

---

# WOComponent

__Inherits From:__
[WOElement](WOElement.md) : NSObject

__Inherits From:__
com.apple.yellow.webobjects

---

## Class Description

WOComponent objects dynamically render web pages (or sections of pages) at run time. They provide custom navigation and other logic for the page, provide a framework for organizing constituent objects (static and dynamic HTML elements and subcomponents), and enable the attribute bindings of dynamic elements.

The WOComponent class has many methods that have the same names as methods of the [WOApplication](WOApplication.md) class. However, the scope of the WOComponent methods is limited to a component rather than being application-wide. For example, you can control component-definition caching on a per-component basis using [`setCachingEnabled`](#apple-ge2tg), which has a WOApplication counterpart. When this kind of caching is enabled for a component, the application parses the contents of the component directory the first time the component is requested, creates the component definition, stores this object in memory, and restores it for subsequent requests.

WOComponent objects also respond to [`awake`](#apple-g4zq), [`sleep`](#apple-ge3dc), and the three request-handling messages: [`takeValuesFromRequest`](#apple-ge3tg), [`invokeActionForRequest`](#apple-geytg),and [`appendToResponse`](#apple-geydgmq). You can override these methods in your compiled subclasses, and thereby integrate your custom behavior into the request-response loop. (You can also override these methods in component scripts using WebScript.)

---

### Subcomponents

A WOComponent object can represent a dynamic fragment of a Web page as well as an entire page. Such _subcomponents_, or _reusable components_, are nested within a parent component representing the page _or_ another subcomponent. Each component keeps track of its parent and subcomponents-when a component receives a request-handling message, such as [`takeValuesFromRequest`](#apple-ge3tg), it forwards that message to its subcomponents

The WOComponent class also provides a child-parent callback mechanism to allow a child component to communicate with its parent. In the parent's declaration file, bind an arbitrary attribute of the child to an action method of the parent. Then, as the last step in the child's action method, invoke [`performParentAction`](#apple-ge2dk) with the argument being the arbitrary attribute, returning the object received back as the response page. See the method description for [`performParentAction`](#apple-ge2dk) for details.

---

## Method Types

**Constructors**

**[WOComponent](#apple-ge4dgmry)**

**Obtaining attributes**

**[application](#apple-gy4q)

**[baseURL](#apple-g43q)

**[context](#apple-hayq)

**[frameworkName](#apple-hezq)

**[hasSession](#apple-geydk)

**[name](#apple-gezds)

**[pageWithName](#apple-geztg)

**[path](#apple-geydgnzr)

**[session](#apple-ge2ds)******************

**Caching**

**[isCachingEnabled](#apple-geyto)

**[setCachingEnabled](#apple-ge2tg)****

**Managing resources**

**[templateWithName](#apple-ge3to)

**[pathForResource](#apple-ge2dc)****

**Handling requests**

**[appendToResponse](#apple-geydgmq)

**[awake](#apple-g4zq)

**[invokeActionForRequest](#apple-geytg)

**[sleep](#apple-ge3dc)

**[takeValuesFromRequest](#apple-ge3tg)**********

**Logging**

**[debugString](#apple-ge4dgmzx)

**[logString](#apple-ge4dgnjq)****

**Template parsing**

**[templateWithHTMLString](#apple-gyyq)**

**Components statistics**

**[descriptionForResponse](#apple-ha4q)**

**Invoking actions**

**[parent](#apple-gezto)

**[performParentAction](#apple-ge2dk)****

**Synchronizing components**

**[hasBinding:](#apple-geydc)

**[setValue:forBinding:](#apple-ge2to)

**[synchronizesVariablesWithBindings](#apple-ge3ds)

**[valueForBinding:](#apple-gqztmmy)********

**Other**

**[generateResponse](#apple-he3q)**

---

## Constructors

---

### WOComponent

public `WOComponent`()

WebObjects Builder archive file exists in the component directory, it initializes component variables from this archive. This constructor throws exceptions if it cannot determine the name of the component or if it cannot initialize the object for any other reason. Override `WOComponent`() in compiled subclasses to perform custom initializations; as always, invoke `super`'s default constructor as the first thing.

#

---

### debugString

public static void `debugString`(java.lang.String _aString_)

Like [`logString`](#apple-ge4dgnjq), prints a message to the standard error device (stderr), but only prints the message if the WODebuggingEnabled user default option is `true`. If WODebuggingEnabled is `false`, the [`debugString`](#apple-ge4dgmzx) messages aren't printed. See [`logString`](#apple-ge4dgnjq) for information on the format of _aString_.

---

### logString

public static void `logString`(java.lang.String _aString_)

Prints a message to the standard error device (stderr). The message can include formatted variable data using String's concatenation feature, for example:

> ```
> int i = 500;
> ```

> ```
> float f = 2.045;
> ```

> ```
> WOComponent.logString("Amount = " + i + ", Rate = " + f ", Total = " + i*f);
> ```

---

### templateWithHTMLString

public static WOElement `templateWithHTMLString`(java.lang.String _anHTMLString_, java.lang.String _aDeclarationString,_ NSArray _languages_)

Programmatically creates the component's template using _anHTMLString_ as the HTML template contents and _aDeclarationString_ as the declarations file contents. Returns (as a WOElement object) the graph of static and dynamic elements build by parsing the HTML and declaration strings. You can then use the returned WOElement as the component's template.

__See also:__
[`templateWithName`](#apple-ge3to)

---

## Instance Methods

---

### appendToResponse

public void `appendToResponse`(WOResponse _aResponse_, WOContext _aContext_)

Component objects associated with a response receive this message during the last phase of the request-response loop. In the append-to-response phase, the application objects (particularly the response page instance itself) generate the HTML content of the page. WOComponent's default implementation of this method forwards the message to the root [WOElement](WOElement.md) object of the component template. Compiled or scripted subclasses of WOComponent can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[`invokeActionForRequest`](#apple-geytg), [`takeValuesFromRequest`](#apple-ge3tg)

---

### application

public WOApplication `application`()

Returns the WOApplication object for the current application.

__See also:__
[WOApplication](WOApplication.md) class, [`context`](#apple-hayq), `[session](#apple-ge2ds)`

---

### awake

public void `awake`()

Invoked at the beginning of a WOComponent's involvement in a cycle of the request-response loop, giving the WOComponent an opportunity to initialize its instance variables or perform setup operations. The default implementation does nothing.

__See also:__
, `[sleep](#apple-ge3dc)`

---

### baseURL

public java.lang.String `baseURL`()

Returns the component URL relative to the server's document root, for example: "/WebObjects/MyApp.woa/Resources/Main.wo"

__See also:__
[`name`](#apple-gezds), [`path`](#apple-geydgnzr)

---

### context

public WOContext `context`()

Returns the WOContext object for the current transaction.

__See also:__
[WOContext](WOContext.md) class, [`application`](#apple-gy4q), [`session`](#apple-ge2ds)

---

### descriptionForResponse

public java.lang.String `descriptionForResponse`(WOResponse _aResponse_, WOContext _aContext_)

Records information about the component if it is the response component in the current request-response loop transaction. The default implementation records the component's name. You might override this method if you want to record more information about the component. For example, you might want to record the values of some instance variables as well as the component name.

This message is sent only to the top-level response component, that is, the one representing the entire page. Components nested inside of that top-level component do not receive this message.

If a CLFF log file is kept for this application, the string returned by this method is recorded in that log file. Thus, you must ensure that the string you return can be analyzed by a CLFF-analysis tool.

__See also:__
[WOStatisticsStore](WOStatisticsStore.md) class

---

### frameworkName

public java.lang.String `frameworkName`()

If the component is stored in a framework, this method returns the name of that framework. For example, if the component is in the framework _NeXT_ROOT_`/System/Library/Frameworks/WOExtensions.framework`, then this method returns the string "WOExtensions".

If the component is not stored in a framework, this method returns `null`.

__See also:__
[WOResourceManager](WOResourceManager.md) class

---

### generateResponse

public WOResponse `generateResponse`()

Returns a newly-created WOResponse object. WOComponent's implementation of this method translates the receiving component into a WOResponse object by sending iteself an [`appendToResponse`](#apple-geydgmq) message.

---

### hasBinding:

public boolean `hasBinding`(java.lang.String _aBindingName_)

Returns whether the component has a binding named _aBindingName_.

---

### hasSession

public boolean `hasSession`()

Returns whether the component is already in a session. For example, in direct actions, sessions are lazily created and you can avoid creating another one unnecessarily by calling [`hasSession`](#apple-geydk) before [`session`](#apple-ge2ds).

__See also:__
[`session`](#apple-ge2ds)

---

### invokeActionForRequest

public WOElement `invokeAction`(WORequest _aRequest_, WOContext _aContext_)

WOComponent objects associated with a request page receive this message during the middle phase of request handling. In this middle phase, the [`invokeActionForRequest`](#apple-geytg) message is propagated through the [WOElement](WOElement.md) objects of the page; the dynamic element on which the user has acted (by, for example, clicking a button) responds by triggering the method in the request component that is bound to the action. WOComponent's default implementation of this method forwards the message to the root WOElement object of the component template.Compiled or scripted subclasses of WOComponent can override this method to replace or supplement the default behavior with custom logic. (Scripted subclasses must use the Objective-C form of this method: `invokeActionForRequest:inContext:`).

__See also:__
[`appendToResponse`](#apple-geydgmq), [`takeValuesFromRequest`](#apple-ge3tg)

---

### isCachingEnabled

public boolean `isCachingEnabled`()

Returns whether component-definition caching is enabled for this component. `false` is the default.

__See also:__
[`setCachingEnabled`](#apple-ge2tg)

---

### name

public java.lang.String `name`()

Returns the name of the component, which includes a path of all directories under _DOCUMENTROOT_/`WebObjects` and is minus the ".wo" extension; for example "Main" is a typical component name.

__See also:__
[`baseURL`](#apple-g43q), `[path](#apple-geydgnzr)`

---

### pageWithName

public WOComponent `pageWithName`(java.lang.String _aName_)

Returns a new page instance (a WOComponent object) identified by _aName_. If _aName_ is `null`, the "Main" component is assumed. If the method cannot create a valid page instance, it throws an exception.

__See also:__
[`restorePageForContextID`](WOSession.md#apple-geyds) (WOSession), [`savePage`](WOSession.md#apple-geytg) (WOSession)

---

### parent

public WOComponent `parent()`

Returns the parent component of the receiver.

---

### path

public java.lang.String `path`()

Returns the file-system path of the component, which is an absolute path and includes the ".wo" extension; for example "C:\Apple\Library\WOApps\MyApp.woa\Resources\Main.wo" is a typical path.

__See also:__
[`baseURL`](#apple-g43q), [`name`](#apple-gezds)

---

### pathForResource

public java.lang.String `pathForResource`(java.lang.String _aName_, java.lang.String _aType_)

Returns the absolute path to the component resource having the name of _aName_ and an extension of _aType_. The method searches all localized ".lproj" directories of the component before searching directly under the ".wo" component directory for a non-localized resource of the given name and extension.

This method is provided for backwards compatibility only. For WebObjects 3.5 and above, you should use the [WOResourceManager](WOResourceManager.md) API to retrieve resources. WOResourceManager is not able to retrieve resources stored inside component directories.

---

### performParentAction

public java.lang.Object `performParentAction`(java.lang.String _anActionName_)

Allows a subcomponent to invoke an action method of its parent component bound to the child component (_attribute_). Parent and child components are "synchronized" when this method returns: the variables that are bound by a declaration of the child component in the parent component's declaration file have the same value.

An example best illustrates this mechanism. Let's say you have a Palette subcomponent, and this WOComponent is nested in a parent component with a "displaySelection" action method. When the user selects an item in the palette (perhaps a color), you want to invoke "displaySelection" to show the result of the new selection (perhaps a car in the new color). The declaration in the parent's ".wod" file would look like this:

> ```
> PALETTE: Palette {
> ```

> ```
> selection = number;
> ```

> ```
> callBack = "displaySelection";
> ```

> ```
> };
> ```

The "callBack" item is an arbitrary attribute of the child component bound in this declaration to the parent component's "displaySelection" method.The `performParentAction:` method is used to activate this binding. Let's assume the child component has an action method called "click"; the implementation would look like this:

> ```
> public WOComponent click() {             /* this is the child's action */
> ```

> ```
> selection = /* some value */;
> ```

> ```
> /* now invoke the parent's action */
> ```

> ```
> return performParentAction(callBack);
> ```

> ```
> }
> ```

---

### session

public WOSession `session`()

Returns the current WOSession object. This method creates a new one if there isn't one.

__See also:__
[WOSession](WOSession.md) class, [`application`](#apple-gy4q), [`context`](#apple-hayq), [`hasSession`](#apple-geydk)

---

### setCachingEnabled

public void `setCachingEnabled`(boolean _flag_)

Enables or disables the caching of component definitions for the receiving component. WOComponent definitions contain templates and other common information related to components, and are used to generate instances of those components.When this attribute is set to `true`, the application parses the HTML template and the declaration (".wod") file of a component once and then stores the resulting component definition for future requests. By default, this kind of caching is disabled so that you can edit a _scripted_ component without having to relaunch the application every time to check the results.(Note that this does not apply to Java subclasses of WOComponent; in this case, you still have to kill and relaunch the application.)

With [WOApplication](WOApplication.md)'s method of the same name, you can turn component-definition caching off globally. You can then control caching of individual component definitions using WOComponent's version of this method. Selective caching is an especially valuable technique for very large applications where only the most frequently requested components should be cached.

__See also:__
`[isCachingEnabled](#apple-geyto)`

---

### setValue:forBinding:

public void `setValueForBinding`(java.lang.Object _aValue_, java.lang.String _aBindingName_)

Sets the value of the binding specified by _aBindingName_ in the parent component to _aValue_. If the parent doesn't provide _aBindingName_ in its declarations file, this method attempts to set the value in the current component using `takeValueForKey:`. If the current component doesn't define this key, this method silently returns.

__See also:__
[`synchronizesVariablesWithBindings`](#apple-ge3ds), [`valueForBinding:`](#apple-gqztmmy)

---

### sleep

public void `sleep`()

Invoked at the conclusion of a request-handling cycle to give component the opportunity for deallocating objects created and initialized in its [`awake`](#apple-g4zq) method. The default implementation does nothing.

---

### synchronizesVariablesWithBindings

public boolean `synchronizesVariablesWithBindings`()

Returns whether a nested component pulls all values down from its parent and pushes all values to its parent before and after each phase of the request-response loop. By default, this method returns `true`. Override this method to create a non-synchronizing component.

__See also:__
[`setValue:forBinding:`](#apple-ge2to), [`valueForBinding:`](#apple-gqztmmy)

---

### takeValuesFromRequest

public void `takeValuesFromRequest`(WORequest _aRequest_, WOContext _aContext_)

WOComponent objects associated with a request receive this message during the first phase of the request-response loop. The default WOComponent behavior is to send the message to the root object of the component's template.In this phase, each dynamic element in the template extracts any entered data or changed state (such as a check in a check box) associated with an attribute and assigns the value to the component variable bound to the attribute.Compiled or scripted subclasses of Component can override this method to replace or supplement the default behavior with custom logic. (Scripted subclasses must use the Objective-C form of this method: `takeValuesFromRequest:inContext:`).

__See also:__
[`appendToResponse`](#apple-geydgmq), [`invokeActionForRequest`](#apple-geytg)

---

### templateWithName

public WOElement `templateWithName`(java.lang.String _aName_)

Returns the root object of the graph of static and dynamic HTML elements and subcomponents that is used to graphically render the component identified by _aName_. This template is constructed from the ".html" and ".wod" file found in the component directory. You identify the template by specifying the component directory, which consists of the component name plus the "wo" extension: for example, "HelloWorld.wo." If the template is not cached, the application will parse the HTML and declaration files of the specified component to create the template.

__See also:__
[`setCachingEnabled`](#apple-ge2tg)

__validationFailedWithException__ public void `validationFailedWithException`(java.lang.Throwable _exception_,
java.lang.Object _value_, java.lang.String _keyPath_)

Called when an Enterprise Object or formatter failed validation during an assignment. The default implementation ignores the error. Subclassers can override to record the error and possibly return a different page for the current action.

---

### valueForBinding:

public java.lang.Object `valueForBinding`(java.lang.String _aBindingName_)

Gets the value for the specified binding from the parent component. If the parent doesn't provide _aBindingName_ in its delcarations file, this method attempts to get the value from the current component using `valueForKey`.If the current component doesn't define this key, this method returns null. This cascading lookup makes it easy to provide default values for optional bindings.

__See also:__
[`setValue:forBinding:`](#apple-ge2to), [`synchronizesVariablesWithBindings`](#apple-ge3ds)

****

---

[!](WOAssociation.md)
[!](WOContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
