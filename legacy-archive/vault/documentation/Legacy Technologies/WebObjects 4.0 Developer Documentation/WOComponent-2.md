---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/WOComponent.html
archived_at: '2026-07-18T01:28:53.502313Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Framework Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/WebObjects.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](WOAssociation-2.md)
[!](WOContext-2.md)

---

# WOComponent

__Inherits From:__
[WOElement](WOElement-2.md) : NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
WebObjects/WOComponent.h

---

## Class Description

WOComponent objects dynamically render web pages (or sections of pages) at run time. They provide custom navigation and other logic for the page, provide a framework for organizing constituent objects (static and dynamic HTML elements and subcomponents), and enable the attribute bindings of dynamic elements.

The WOComponent class has many methods that have the same names as methods of the [WOApplication](WOApplication-2.md) class. However, the scope of the WOComponent methods is limited to a component rather than being application-wide. For example, you can control component-definition caching on a per-component basis using [__setCachingEnabled:__](#apple-ge2tg), which has a WOApplication counterpart. When this kind of caching is enabled for a component, the application parses the contents of the component directory the first time the component is requested, creates the component definition, stores this object in memory, and restores it for subsequent requests.

WOComponent objects also respond to [__awake__](#apple-g4zq), [__sleep__](#apple-ge3dc), and the three request-handling messages: [__takeValuesFromRequest:inContext:__](#apple-ge3tg), [__invokeActionForRequest:inContext:__](#apple-geytg),and [__appendToResponse:inContext:__](#apple-geydgmq). You can override these methods in your compiled subclasses, and thereby integrate your custom behavior into the request-response loop. (You can also override these methods in component scripts using WebScript.)

[Perhaps rewrite this to talk about Java serialization?] [this constructor doesn't exist]By implementing the NSCoding interface (__encodeWithCoder__ ) and the WOComponent(next.util.Coder) constructor protocol (__encodeWithCoder:__  and __initWithCoder:__  methods), WOComponent objects can serialize their state in an object archive. This capability makes WOComponent objects persistent across sessions when they and their "owning" session (which initiates the archiving) are stored in the page or in cookies. These methods are automatically implemented for scripted components.

---

### Subcomponents

A WOComponent object can represent a dynamic fragment of a Web page as well as an entire page. Such _subcomponents_, or _reusable components_, are nested within a parent component representing the page _or_ another subcomponent. Each component keeps track of its parent and subcomponents-when a component receives a request-handling message, such as [__takeValuesFromRequest:inContext:__](#apple-ge3tg), it forwards that message to its subcomponents

The WOComponent class also provides a child-parent callback mechanism to allow a child component to communicate with its parent. In the parent's declaration file, bind an arbitrary attribute of the child to an action method of the parent. Then, as the last step in the child's action method, invoke [__performParentAction:__](#apple-ge2dk) with the argument being the arbitrary attribute, returning the object received back as the response page. See the method description for [__performParentAction:__](#apple-ge2dk) for details.

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

Someone needs to double check these categories.

**Creation**

**[- init](#apple-ge4donrr)**

**Obtaining attributes**

**[- application](#apple-gy4q)

**[- baseURL](#apple-g43q)

**[- context](#apple-hayq)

**[- frameworkName](#apple-hezq)

**[- hasSession](#apple-geydk)

**[- name](#apple-gezds)

**[- pageWithName:](#apple-geztg)

**[- path](#apple-geydgnzr)

**[- session](#apple-ge2ds)******************

**Caching**

**[- isCachingEnabled](#apple-geyto)

**[- setCachingEnabled:](#apple-ge2tg)****

**Managing resources**

**[- templateWithName:](#apple-ge3to)

**[- pathForResourceNamed:ofType:](#apple-ge2dc)****

**Handling requests**

**[- appendToResponse:inContext:](#apple-geydgmq)

**[- awake](#apple-g4zq)

**[- invokeActionForRequest:inContext:](#apple-geytg)

**[- sleep](#apple-ge3dc)

**[- takeValuesFromRequest:inContext:](#apple-ge3tg)**********

**Logging**

**[- debugWithFormat:](#apple-ge4dmojv)

**[- logWithFormat:](#apple-ge4doojz)

**[- logWithFormat:arguments:](#apple-ge4dqmjq)

**[- validationFailedWithException:value:keyPath:](#apple-ge4dsnjt)********

**Template parsing**

**[+ templateWithHTMLString:declarationString:languages:](#apple-gyyq)**

**Components statistics**

**[- descriptionForResponse:inContext:](#apple-ha4q)**

**Invoking actions**

**[- parent](#apple-gezto)

**[- performParentAction:](#apple-ge2dk)****

**Synchronizing components**

**[- hasBinding:](#apple-geydc)

**[- setValue:forBinding:](#apple-ge2to)

**[- synchronizesVariablesWithBindings](#apple-ge3ds)

**[- valueForBinding:](#apple-gqztmmy)********

**Other**

**[- generateResponse](#apple-he3q)**

[This constructor doesn't exist.]The __WOComponent__ (next.util.Coder) constructor returns a WOComponent object after initializing it from an object archive. You can override this constructor to unarchive and reinitialize the state of instances derived from custom WOComponent subclasses. This constructor, which decodes archived state, must, be implemented in conjunction with the __encodeWithCoder__  interface method (next.util.Coding), which you must implement to encode the archived state. Decoding of objects and other data must follow the same sequence as was used in encoding. Use next.util.Coder methods to do the encoding and decoding. The default implementation of this constructor decodes all subcomponents, thereby causing their implementations of this constructor to be invoked.

__See also:__
Coder class, Coding interface

---

## Class Methods

---

### templateWithHTMLString:declarationString:languages:

+ (WOElement \*)__templateWithHTMLString:__ (NSString \*)_anHTMLString_ __declarationString:__ (NSString \*)_aDeclarationString_ __languages:__ (NSArray\*)_languages_

Programmatically creates the component's template using _anHTMLString_ as the HTML template contents and _aDeclarationString_ as the declarations file contents. Returns (as a WOElement object) the graph of static and dynamic elements build by parsing the HTML and declaration strings. You can then use the returned WOElement as the component's template.

__See also:__
[- __templateWithName:__](#apple-ge3to)

---

## Instance Methods

---

### appendToResponse:inContext:

- (void)__appendToResponse:__ (WOResponse \*)_aResponse_ __inContext:__ (WOContext \*)_aContext_

Component objects associated with a response receive this message during the last phase of the request-response loop. In the append-to-response phase, the application objects (particularly the response page instance itself) generate the HTML content of the page. WOComponent's default implementation of this method forwards the message to the root [WOElement](WOElement-2.md) object of the component template. Compiled or scripted subclasses of WOComponent can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[- __invokeActionForRequest:inContext:__](#apple-geytg), [- __takeValuesFromRequest:
inContext:__](#apple-ge3tg)

---

### application

- (WOApplication \*)__application__

Returns the WOApplication object for the current application.

__See also:__
[WOApplication](WOApplication-2.md) class, [- __context__](#apple-hayq), __[- session](#apple-ge2ds)__

---

### awake

- (void)__awake__

Invoked at the beginning of a WOComponent's involvement in a cycle of the request-response loop, giving the WOComponent an opportunity to initialize its instance variables or perform setup operations. The default implementation does nothing.

__See also:__
[- __init__](#apple-ge4donrr), __[- sleep](#apple-ge3dc)__

---

### baseURL

- (NSString \*)__baseURL__

Returns the component URL relative to the server's document root, for example: "/WebObjects/MyApp.woa/Resources/Main.wo"

__See also:__
[- __name__](#apple-gezds), [- __path__](#apple-geydgnzr)

---

### context

- (WOContext \*)__context__

Returns the WOContext object for the current transaction.

__See also:__
[WOContext](WOContext-2.md) class, [- __application__](#apple-gy4q), [- __session__](#apple-ge2ds)

---

### debugWithFormat:

- (void)__debugWithFormat:__ (NSString \*)_aFormatString,..._

Like [__logWithFormat:__](#apple-ge4doojz), prints a message to the standard error device (stderr), but only prints the message if the WODebuggingEnabled user default option is YES. If WODebuggingEnabled is NO, the [__debugWithFormat:__](#apple-ge4dmojv) messages aren't printed. See [__logWithFormat:__](#apple-ge4doojz) for information on the format of _aFormatString_.

__See also:__
[- __logWithFormat:arguments:__](#apple-ge4dqmjq)

---

### descriptionForResponse:inContext:

- (NSString \*)__descriptionForResponse:__ (WOResponse \*)_aResponse___inContext:__ (WOContext \*)_aContext_

Records information about the component if it is the response component in the current request-response loop transaction. The default implementation records the component's name. You might override this method if you want to record more information about the component. For example, you might want to record the values of some instance variables as well as the component name.

This message is sent only to the top-level response component, that is, the one representing the entire page. Components nested inside of that top-level component do not receive this message.

If a CLFF log file is kept for this application, the string returned by this method is recorded in that log file. Thus, you must ensure that the string you return can be analyzed by a CLFF-analysis tool.

__See also:__
[WOStatisticsStore](WOStatisticsStore-2.md) class

---

### frameworkName

- (NSString \*)__frameworkName__

If the component is stored in a framework, this method returns the name of that framework. For example, if the component is in the framework _NeXT_ROOT___/System/Library/Frameworks/WOExtensions.framework__ , then this method returns the string "WOExtensions".

If the component is not stored in a framework, this method returns __nil__ .

__See also:__
[WOResourceManager](WOResourceManager-2.md) class

---

### generateResponse

- (WOResponse \*)__generateResponse__

Returns a newly-created WOResponse object. WOComponent's implementation of this method translates the receiving component into a WOResponse object by sending iteself an [__appendToResponse:inContext:__](#apple-geydgmq) message.

__See also:__
[- __generateResponse__](WOResponse-2.md#apple-ge3dgnry) (WOResponse)

---

### hasBinding:

- (BOOL)__hasBinding:__ (NSString \*)_aBindingName_

Returns whether the component has a binding named _aBindingName_.

---

### hasSession

- (BOOL)__hasSession__

Returns whether the component is already in a session. For example, in direct actions, sessions are lazily created and you can avoid creating another one unnecessarily by calling [__hasSession__](#apple-geydk) before [__session__](#apple-ge2ds).

__See also:__
[- __session__](#apple-ge2ds)

---

### init

- (id)__init__

Initializes a WOComponent object. If a WebObjects Builder archive file exists in the component directory, it initializes component variables from this archive. An exception is thrown if the method cannot determine the name of the component or if it cannot initialize the object for any other reason. Override [__init__](#apple-ge4donrr) in compiled subclasses to perform custom initializations; as always, invoke __super__ 's __init__  method as the first thing.

__See also:__
__[- awake](#apple-g4zq)__

---

### invokeActionForRequest:inContext:

- (WOElement \*)__invokeActionForRequest:__ (WORequest \*)_aRequest___inContext:__ (WOContext \*)_aContext_

WOComponent objects associated with a request page receive this message during the middle phase of request handling. In this middle phase, the [__invokeActionForRequest:inContext:__](#apple-geytg) message is propagated through the [WOElement](WOElement-2.md) objects of the page; the dynamic element on which the user has acted (by, for example, clicking a button) responds by triggering the method in the request component that is bound to the action. WOComponent's default implementation of this method forwards the message to the root WOElement object of the component template.Compiled or scripted subclasses of WOComponent can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[- __appendToResponse:inContext:__](#apple-geydgmq), [- __takeValuesFromRequest:inContext:__](#apple-ge3tg)

---

### isCachingEnabled

- (BOOL)__isCachingEnabled__

Returns whether component-definition caching is enabled for this component. NO is the default.

__See also:__
[- __setCachingEnabled:__](#apple-ge2tg)

---

### logWithFormat:

- (void)__logWithFormat:__ (NSString \*)_aFormat,..._

Prints a message to the standard error device (stderr). The message can include formatted variable data using __printf__ -style conversion specifiers, for example:

> ```
> id i = 500;
> ```

> ```
> id f = 2.045;
> ```

> ```
> [self logWithFormat:@"Amount = %@, Rate = %@, Total = %@",
> ```

> ```
> i, f, i*f];
> ```

Note that in WebScript, all variables are objects, so the only conversion specifier allowed is %@ as shown above. In compiled Objective-C code, all __printf__  conversion specifiers are allowed. The equivalent method in Java is __logString__ .

---

### logWithFormat:arguments:

- (void)__logWithFormat:__ (NSString \*)_aFormat_ __arguments:__ (va_list)_someArguments_

Prints a message to the standard error device (stderr). This method is used by [__logWithFormat:__](#apple-ge4doojz).

---

### name

- (NSString \*)__name__

Returns the name of the component minus the ".wo" extension; for example "Main" is a typical component name.

__See also:__
[- __baseURL__](#apple-g43q), __[- path](#apple-geydgnzr)__

---

### pageWithName:

- (WOComponent \*)__pageWithName:__ (NSString \*)_aName_

Returns a new page instance (a WOComponent object) identified by _aName_. If _aName_ is __nil__ , the "Main" component is assumed. If the method cannot create a valid page instance, it raises an exception.

__See also:__
[- __restorePageForContextID:__](WOSession-2.md#apple-geyds) (WOSession), [- __savePage:__](WOSession-2.md#apple-geytg) (WOSession)

---

### parent

- (WOComponent \*)__parent__

Returns the parent component of the receiver.

---

### path

- (NSString \*)__path__

Returns the file-system path of the component, which is an absolute path and includes the ".wo" extension; for example "C:\Apple\Library\WOApps\MyApp.woa\Resources\Main.wo" is a typical path.

__See also:__
[- __baseURL__](#apple-g43q), [- __name__](#apple-gezds)

---

### pathForResourceNamed:ofType:

- (NSString \*)__pathForResourceNamed:__ (NSString \*)_aName_ __ofType:__ (NSString \*)_aType_

Returns the absolute path to the component resource having the name of _aName_ and an extension of _aType_. The method searches all localized ".lproj" directories of the component before searching directly under the ".wo" component directory for a non-localized resource of the given name and extension.

This method is provided for backwards compatibility only. For WebObjects 3.5 and above, you should use the [WOResourceManager](WOResourceManager-2.md) API to retrieve resources. WOResourceManager is not able to retrieve resources stored inside component directories.

---

### performParentAction:

- (id)__performParentAction:__ (NSString \*)_anActionName_

Allows a subcomponent to invoke an action method of its parent component bound to the child component (_attribute_). Parent and child components are "synchronized" when this method returns: the variables that are bound by a declaration of the child component in the parent component's declaration file have the same value.

An example best illustrates this mechanism. Let's say you have a Palette subcomponent, and this WOComponent is nested in a parent component with a "displaySelection" action method. When the user selects an item in the palette (perhaps a color), you want to invoke "displaySelection" to show the result of the new selection (perhaps a car in the new color). The declaration in the parent's ".wod" file would look like this:

> ```
> PALETTE: Palette {
> ```

> ```
>    selection = number;
> ```

> ```
>    callBack = "displaySelection";
> ```

> ```
> };
> ```

The "callBack" item is an arbitrary attribute of the child component bound in this declaration to the parent component's "displaySelection" method.The __performParentAction:__  method is used to activate this binding. Let's assume the child component has an action method called "click"; the implementation would look like this:

> ```
> - click {             /* this is the child's action */
> ```

> ```
> 	selection = /* some value */;
> ```

> ```
> 	/* now invoke the parent's action */
> ```

> ```
> 	return [self performParentAction:callBack];
> ```

> ```
> }
> ```

---

### session

- (WOSession \*)__session__

Returns the current WOSession object. This method creates a new one if there isn't one.

__See also:__
[WOSession](WOSession-2.md) class, [- __application__](#apple-gy4q), [- __context__](#apple-hayq), [- __hasSession__](#apple-geydk)

---

### setCachingEnabled:

- (void)__setCachingEnabled:__ (BOOL)_flag_

Enables or disables the caching of component definitions for the receiving component. WOComponent definitions contain templates and other common information related to components, and are used to generate instances of those components.When this attribute is set to YES, the application parses the HTML template and the declaration (".wod") file of a component once and then stores the resulting component definition for future requests. By default, this kind of caching is disabled so that you can edit a _scripted_ component without having to relaunch the application every time to check the results.(Note that this does not apply to Java subclasses of WOComponent; in this case, you still have to kill and relaunch the application.)

With [WOApplication](WOApplication-2.md)'s method of the same name, you can turn component-definition caching off globally. You can then control caching of individual component definitions using WOComponent's version of this method. Selective caching is an especially valuable technique for very large applications where only the most frequently requested components should be cached.

__See also:__
__[- isCachingEnabled](#apple-geyto)__

---

### setValue:forBinding:

- (void)__setValue:__ _aValue_ __forBinding:__ (NSString \*)_aBindingName_

Sets the value of the binding specified by _aBindingName_ in the parent component to _aValue_. If the parent doesn't provide _aBindingName_ in its declarations file, this method attempts to set the value in the current component using __takeValue:forKey:__ . If the current component doesn't define this key, this method silently returns.

__See also:__
[- __synchronizesVariablesWithBindings__](#apple-ge3ds), [- __valueForBinding:__](#apple-gqztmmy), "Non-Synchronizing
Components" in the Class Description<<Find this cross-ref>>?

---

### sleep

- (void)__sleep__

Invoked at the conclusion of a request-handling cycle to give component the opportunity for deallocating objects created and initialized in its [__awake__](#apple-g4zq) method. The default implementation does nothing.

---

### synchronizesVariablesWithBindings

- (BOOL)__synchronizesVariablesWithBindings__

Returns whether a nested component pulls all values down from its parent and pushes all values to its parent before and after each phase of the request-response loop. By default, this method returns YES. Override this method to create a non-synchronizing component.

__See also:__
[- __setValue:forBinding:__](#apple-ge2to), [- __valueForBinding:__](#apple-gqztmmy), "Non-Synchronizing Components" in the Class
Description<<Find this cross-ref>>

---

### takeValuesFromRequest:inContext:

- (void)__takeValuesFromRequest:__ (WORequest \*)_aRequest_ __inContext:__ (WOContext \*)_aContext_

WOComponent objects associated with a request receive this message during the first phase of the request-response loop. The default WOComponent behavior is to send the message to the root object of the component's template.In this phase, each dynamic element in the template extracts any entered data or changed state (such as a check in a check box) associated with an attribute and assigns the value to the component variable bound to the attribute.Compiled or scripted subclasses of Component can override this method to replace or supplement the default behavior with custom logic.

__See also:__
[- __appendToResponse:inContext:__](#apple-geydgmq), [- __invokeActionForRequest:inContext:__](#apple-geytg)

---

### templateWithName:

- (WOElement \*)__templateWithName:__ (NSString \*)_aName_

Returns the root object of the graph of static and dynamic HTML elements and subcomponents that is used to graphically render the component identified by _aName_. This template is constructed from the ".html" and ".wod" file found in the component directory. You identify the template by specifying the component directory, which consists of the component name plus the "wo" extension: for example, "HelloWorld.wo." If the template is not cached, the application will parse the HTML and declaration files of the specified component to create the template.

__See also:__
[- __setCachingEnabled:__](#apple-ge2tg)

---

### validationFailedWithException:value:keyPath:

- (void)__validationFailedWithException:__ (NSException \*)_exception_
__value:__ (id)_value_
__keyPath:__ (NSString \*)_keyPath_

Called when an Enterprise Object or formatter failed validation during an assignment. The default implementation ignores the error. Subclassers can override to record the error and possibly return a different page for the current action.

---

### valueForBinding:

- __valueForBinding:__ (NSString \*)_aBindingName_

Gets the value for the specified binding from the parent component. If the parent doesn't provide _aBindingName_ in its delcarations file, this method attempts to get the value from the current component using __valueForKey:__ .If the current component doesn't define this key, this method returns nil. This cascading lookup makes it easy to provide default values for optional bindings.

__See also:__
[- __setValue:forBinding:__](#apple-ge2to), [- __synchronizesVariablesWithBindings__](#apple-ge3ds), "Non-Synchronizing
Components" in the Class Description. <<Find this cross-ref>>

****

---

[!](WOAssociation-2.md)
[!](WOContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
