---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/DeltaDoc/Java_Client.html
archived_at: '2026-07-15T08:04:35.603988Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
What's New in WebObjects

---

[!](What%27s%20New%20in%20WebObjects%204.5.md)

# What's New in Java Client

This chapter describes changes made to Java
Client between WebObjects release 4.0 and release 4.5. Java Client
has been extended considerably, including the following:

- The foundation layer (com.apple.client.foundation)
  contains a new number formatter based on NSNumberFormatter and adds
  an NSUndoManager class, which is analogous to the server side class.
- The control layer (com.apple.client.eocontrol) is more complete.
- The distribution layer (com.apple.client.eodistribution on
  the client side and com.apple.yellow.eodistribution on the server
  side) provides support for encrypted client/server communication
  and for managing user defaults.
- The interface layer (com.apple.client.eointerface) adds support
  for table cell editing and for displaying images and QuickTime media.

Additionally, Java Client now has a new user interface generation
layer, Direct to Java Client, which is comparable to WebObjects'
Direct to Web.

The following sections describe how Java Client has been synchronized
with the rest of EOF, the changes to the procedures for running
Java Client applications, and the new Direct to Java Client technology.

|  |
| --- |
| __Note:__ Java Client applications require some conversion to run on WebObjects 4.5; see the _WebObjects 4.5 Post-Installation Instructions_ for more information on converting your existing applications. |

## Foundation Layer Changes

This section lists some of the new features in the Java Client
Foundation framework (com.apple.client.foundation).

### Number Formatter

The Java Client number formatter has been rewritten; it is
now based on the NSNumberFormatter in the Foundation framework.
It preserves the previous AWT-based API, so it isn't necessary
to convert your code.

The new number formatter supports a subset of the Objective-C
number formatter. It doesn't support attributed strings, but it
does support customized text strings for zero, null, and NaN (Not
a Number).

### New Foundation Layer Classes and Interfaces

The following table lists the classes and interfaces that
have been added in this release.

|  |  |
| --- | --- |
| __Class or Interface__ | __Description__ |
| NSDisposable | An interface that defines a method (`dispose`) for performing any necessary housecleaning in preparation for garbage collection. |
| NSInlineObservable | An interface that observable objects implement. NSNotificationCenters and EOObserverCenters use the interface's two methods (`observerData` and `setObserverData`) to avoid creating uncollectable object references.  Note that this interface is only needed in the absence of weak references; it might be removed in the future when support for weak references is available. |
| NSUndoManager | Analogous to the server side class. |

## Control Layer Changes

The Java Client control layer API is more complete in this
release. Many features that were missing in 4.0 have been ported,
and many of the server-side features added in EOF 4.5 are available
on the client side as well. This section lists the new classes,
interfaces, and methods added to Java Client's control layer (com.apple.client.eocontrol)
as well as classes and methods that have been removed. The purpose
of most of the API changes is to synchronize Java Client's feature
set and API with EOF's. However, some of the new API is exclusive
to Java Client.

### New Control Layer Classes and Interfaces

The following table lists the classes and interfaces that
have been added in this release.

|  |  |
| --- | --- |
| __Class or Interface__ | __Description__ |
| EOFoundationExtras | Exclusive to Java Client. A utility class containing convenience methods for working with classes in the com.apple.client.foundation package. |
| EOKeyValueCoding.KeyBinding | Analogous to the server side class. Corresponds to a new feature in EOF 4.5. See ["Key Value Coding Changes"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorsbizdeq). |
| EOKeyValueCoding.KeyBindingCreation (interface) | Analogous to the server side interface. Corresponds to a new feature in EOF 4.5. See ["Key Value Coding Changes"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorsbizdeq). |
| EOKeyValueCoding.UnknownKeyException | The kind of exception raised by key value coding methods when they encounter an unknown key. |
| EOQualifier.QualifierVariableSubstitutionException | The kind of exception raised when an EOQualifierVariable object requires bindings for all its variables and one or more variable is missing from the bindings. |
| EOQualifierVariable | Analogous to the server side class. |

### New API

The following tables summarize the methods and constants that
have been added to the client side control layer in this release.
Most methods are analogous to methods in the server side control
layer and have been added to synchronize the two layers.

__EOClassDescription__

| __API__ | __Description__ |
| `invalidateClassDescriptionCache` | Analogous to the server side method. |
| `defaultFormatterForKey` | Analogous to the server side method. |
| `defaultFormatterForKeyPath` | Analogous to the server side method. |
| `displayNameForKey` | Analogous to the server side method. |
| `fetchSpecificationNamed` | Analogous to the server side method. |
| `userPresentableDescriptionForObject` | Analogous to the server side method. |

__EOCustomObject__

| __API__ | __Description__ |
| `createKeyValueBindingForKey` | Analogous to the server side method. Conformance to EOKeyValueCoding.KeyBindingCreation, a new feature in EOF 4.5. See ["Key Value Coding Changes"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorsbizdeq). |
| `keyValueBindingForKey` | Analogous to the server side method. Conformance to EOKeyValueCoding.KeyBindingCreation, a new feature in EOF 4.5. See ["Key Value Coding Changes"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorsbizdeq). |
| `observerData`  `setObserverData` | Exclusive to Java Client. Conformance to NSInlineObservable. |

__EODelayedObserver__

| __API__ | __Description__ |
| `observerData`  `setObserverData` | Exclusive to Java Client. Conformance to NSInlineObservable. |

__EOEditingContext__

| __API__ | __Description__ |
| `dispose` | Exclusive to Java Client. Conformance to NSDisposable. |
| `invalidatesObjectsWhenFinalized`  `setInvalidatesObjectsWhenFinalized` | Analogous to the server side method. |
| `lock`  `unlock` | Analogous to the server side method.   Note that multithreaded clients aren't yet supported. All the client-side locks in Java Client application's are no-ops. |
| `observerData`  `setObserverData` | Exclusive to Java Client. Conformance to NSInlineObservable. |
| `redo` | Analogous to the server side method. |
| `refault` | Analogous to the server side method. |
| `refetch` | Analogous to the server side method. |
| `reset` | Analogous to the server side method. |
| `revert` | Analogous to the server side method. |
| `undoManager`  `setUndoManager` | Analogous to the server side method. |
| `undo` | Analogous to the server side method. |

__EOEditingContext.Delegate__

| __API__ | __Description__ |
| `editingContextDidMergeChanges` | Analogous to the server side method. |
| `editingContextShouldInvalidateObject` | Analogous to the server side method. |
| `editingContextShouldMergeChangesForObject` | Analogous to the server side method. |
| `editingContextShouldUndoUserActionsAfterFailure` | Analogous to the server side method. |

__EOEditingContext.MessageHandler__

| __API__ | __Description__ |
| `editingContextPresentErrorMessage` | Analogous to the server side method. |

__EOEnterpriseObject__

| __API__ | __Description__ |
| `changesFromSnapshot` | Analogous to the server side method. |
| `reapplyChangesFromDictionary` | Analogous to the server side method. |
| `userPresentableDescription` | Analogous to the server side method. |

__EOFaultHandler__

| __API__ | __Description__ |
| `eoShallowDescription` | Returns a string that describes the object that receiver's fault represents. Used to prevent faulting an object upon receipt of an `eoShallowDescription` message. |
| `descriptionForObject` | Analogous to the server side method. |

__EOFaulting__

| __API__ | __Description__ |
| `faultHandler` | If the receiver is a fault, returns its EOFaultHandler; otherwise returns `null`. |

__EOFetchSpecification__

| __API__ | __Description__ |
| `fetchSpecificationNamed` | Analogous to the server side method. |
| `fetchSpecificationWithQualifierBindings` | Analogous to the server side method. |

__EOKeyValueCoding__

| __API__ | __Description__ |
| `TargetObjectUserInfoKey`  `UnknownUserInfoKey` | String constants defining the keys in the userInfo dictionary of an EOKeyValueCoding.UnknownKeyException. An UnknownKeyException is raised by key value coding methods when they are invoked with a key that does not correspond to a method or instance variable in the receiving object. The userInfo of the exception contains the target object (`TargetObjectUserInfoKey`) and the key (`UnknownUserInfoKey`). |
| `SetKeyBindingMask` | Analogous to the server side constant. |
| `StoredKeyBindingMask` | Analogous to the server side constant. |

__EOKeyValueCoding.Support (Exclusive to Java Client)__

| __API__ | __Description__ |
| `createKeyValueBindingForKey` | A static method that provides a default implementation of the corresponding EOKeyValueCoding method. |
| `keyValueBindingForKey` | A static method that provides a default implementation of the corresponding EOKeyValueCoding method. |

__EOKeyValueCodingAdditions.Support (Exclusive to Java
Client)__

| __API__ | __Description__ |
| `takeStoredValuesFromDictionary` | A static method that provides a default implementation of the corresponding EOKeyValueCodingAdditions method. |
| `valueForKeyPath` | A static method that provides a default implementation of the corresponding EOKeyValueCodingAdditions method. |

__EOObjectStore__

| __API__ | __Description__ |
| `editingContextDidForgetObjectWithGlobalID` | Analogous to the server side method. Corresponds to a new feature in EOF 4.5. See ["Snapshot Reference Counting"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeorcbijeus). However, note that Java Client doesn't implement snapshot reference counting yet. |
| `faultForRawRow` | Analogous to the server side method. |

__EOQualifier__

| __API__ | __Description__ |
| `qualifierToMatchAllValues` | Analogous to the server side method. |
| `qualifierToMatchAnyValue` | Analogous to the server side method. |
| `addQualifierKeysToSet` | Analogous to the server side method, which is new in EOF 4.5. See ["Miscellaneous API Enhancements"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscfivces). |
| `allQualifierKeys` | Analogous to the server side method, which is new in EOF 4.5. See ["Miscellaneous API Enhancements"](What%27s%20New%20in%20Enterprise%20Objects%20Framework.md#apple-inbeoscfivces). |
| `bindingKeys` | Analogous to the server side method. |
| `keyPathForBindingKey` | Analogous to the server side method. |
| `qualifierWithBindings` | Analogous to the server side method. |
| `validateKeysWithRootClassDescription` | Analogous to the server side method. |

__EOValidation__

| __API__ | __Description__ |
| `validateTakeValueForKeyPath` | Analogous to the server side method. |

### Deleted API

The two interfaces EOKeyValueCoding.KeyValueGetter and EOKeyValueCoding.KeyValueSetter
have been removed. Additionally, the following methods, organized
by class, have been deleted and replaced where appropriate, for compatibility
with the Java wrappers (com.apple.yellow packages).

__EOClassDescription__

| __Deleted API__ | __New API or Workaround__ |
| `registerForName` | `registerClassDescription` |
| `registerForClass` | `registerClassDescription` |

__EOEditingContext__

| __Deleted API__ | __New API or Workaround__ |
| `globalIDsForObjects` | `globalIDForObject` |
| `objectsForGlobalIDs` | `objectForGlobalID` |
| `registeredGlobalIDs` | `registeredObjects` and `globalIDForObject` |

__EOEditingContext.MessageHandler__

| __Deleted API__ | __New API or Workaround__ |
| `editingContextPresentException` | `editingContextPresentErrorMessage` |

### Server-Side Features Not in Java Client

Features added to server-side in the 4.5 release that are _not_ yet
available in Java Client are:

- Shared editing contexts
- Event logging
- Snapshot timestamps
- Snapshot reference counting
- Recursive reader/writer locks

## Distribution Layer Changes

This section describes the changes made to the client and
server sides of the distribution layer for Java Client applications.
They are:

- EODistributionContexts are associated with WOSessions.
   An
  EODistributionContext is now associated with a WOSession, and by
  default, a distribution context's editing context is the session's
  default editing context.
- Client server communication supports encryption.
   Additional
  delegate methods for EODistributionContext and an EODistributionChannel
  delegate provide hooks in which you can encrypt and decrypt data
  being sent between client and server.
- The EODistributedObjectStore method `invokeRemoteMethodWithKeyPath` now
  invokes the method on the server side EODistributionContext if the
  provided key path is `null`.
- User defaults support
   EODistributionContext now sends
  out notifications to load and save user defaults, which can be used
  to manage defaults on a per-user basis.

### New Distribution Layer Classes and Interfaces

The following table lists the classes and interfaces that
have been added in this release.

|  |  |
| --- | --- |
| __Class or Interface__ | __Description__ |
| EODistributionChannel.Delegate | An interface defining methods that allow you to encrypt and decrypt data being sent between client and server |

### Related API Changes

The following tables summarize the updated and new API in
the distribution layer.

__EODistributionContext (Server side; EOJavaClient/EODistributionContext.h)__

| __New or Changed API__ | __Description__ |
| `public EODistributionContext(      WOSession session,      EOEditingContext context)`  `public EODistributionContext(      WOSession session)`  (Java) | Creates a new EODistributionContext for use within the specified session and with the specified editing context, if provided. If an editing context isn't provided, the new distribution context is associated with the session's default editing context. |
| `initWithSession:editingContext:` (Objective-C) | Initializes a new EODistributionContext for use in the specified session and with the specified editing context. |
| `initWithSession:` (Objective-C) | Initializes a new EODistributionContext for use in the specified session and with that session's default editing context. |
| `editingContext` | Returns the EOEditingContext with which the distribution context is associated. |
| `session` | Returns the WOSession with which the distribution context is associated. |
| `LoadUserDefaultsNotification` (Java)  `EOLoadUserDefaultsNotification` (Objective-C) | A string constant defining the name of a notification that's posted whenever a distribution context receives a request for user default values from a client application. Receivers can load default values (from a database, for example) and add them to the mutable dictionary provided in the notification's userInfo. |
| `SaveUserDefaultsNotification` (Java)  `EOSaveUserDefaultsNotification` (Objective-C) | A string constant defining the name of a notification that's posted whenever the distribution context receives user default values from a client application. Receivers can use this notification to store the default values (in a database, for example). The default values are in the notification's userInfo dictionary. |

__EODistributionContext.Delegate (Server side; EOJavaClient/EODistributionContext.h)__

| __New or Changed API__ | __Description__ |
| `distributionContextDidReceiveData` (Java)  `distributionContext:didReceiveData:` (Objective-C) | Invoked after a distribution context has received data. You can use this method and its counterpart, `distributionContextWillSendData`, to implement encryption in client server communication, encrypting in `distributionContextWillSendData` and decrypting in `distributionContextDidReceiveData`. |
| `distributionContextWillSendData` (Java)  `distributionContext:willSendData:` (Objective-C) | Invoked before a distribution context sends data to the client. |

__WOJavaClientApplet (Server side; EOJavaClient/WOJavaClientApplet.h)__

| __New or Changed API__ | __Description__ |
| `EOAllParameterNamesKey` (Objective-C) | A string constant defining a dictionary key used internally to collect the names of all HTML parameters passed to the client (the names of all bindings of the WOJavaClientApplet), including any additional bindings that you add to the applet. |
| `EOSessionIDKey` (Objective-C) | A string constant defining a dictionary key used internally to identify the session with which the server side EODistributionContext is associated. |
| `EOComponentURLKey` (Objective-C) | A string constant defining a dictionary key used internally to identify the WOJavaClientApplet component on the server side which corresponds to the EOApplet on the client side. |

__EODistributionChannel (Client side)__

| __New or Changed API__ | __Description__ |
| `observerData`, `setObserverData` | Conformance to NSInlineObservable. |
| `delegate`, `setDelegate` | Accessing the distribution channel's delegate. |

__EODistributedObjectStore (Client side)__

| __New or Changed API__ | __Description__ |
| `observerData`, `setObserverData` | Conformance to NSInlineObservable. |
| `invokeRemoteMethodWithKeyPath` (Changed behavior) | If the specified key path is `null`, this method now invokes the method on the server side EODistributionContext rather than on the EODistributionContext's invocation target as it did in earlier releases. |

### Deleted API

The following methods have been deleted and replaced where
appropriate, for backwards compatibility with the Java wrappers
(com.apple.yellow packages).

__EODistributionContext (Server side; EODistributionContext.h)__

| __Deleted API__ | __New API or Workaround__ |
| `public EODistributionContext(      EOEditingContext context)` (Java) | `public EODistributionContext(      WOSession session,      EOEditingContext context)` |
| `initWithEditingContext:` (Objective-C) | `initWithSession:editingContext:` |

## Interface Layer Changes

This section describes changes in the interface layer of Java
Client applications, including the following new features:

- Support for table cell editing
- Support for displaying images and QuickTime media
- URL Aspect for Associations
- Changes to string matching behavior in EODisplayGroup

The changes to EODisplayGroup have also been made to WODisplayGroup.
For more information on the changes, see the section ["Other WODisplayGroup Changes"](WebObjects%20Framework%20API%20Changes.md#apple-ijdumscfifees) in
the chapter [WebObjects Framework API Changes](WebObjects%20Framework%20API%20Changes.md#apple-ijdumq2gijdek).

### Support for Table Cell Editing

Swing implements JTable editing using javax.swing.table.TableCellEditor,
a single method interface returning a java.awt.Component to act
as editor. The new Java Client class EOColumnEditor implements this
interface to mediate between the Component it returns and the EOTableColumnAssociation
bound to the edited column. Abstract hooks for component instantiation
and protected methods for editing event communication allow concrete
subclasses such as EOTextColumnEditor to focus purely upon their Component's
specifics.

EOTableColumnAssociation acquires the editors for associated
TableColumns from its TableCellCustomizer, a new static object serving
as the source of both EOColumnEditors and TableCellRenderers. EOTableColumnAssociation's
implementation of `establishConnection` now
sets the editor and renderer of its TableColumn to the objects returned
by this object. Consumers may customize columns by installing their
own TableCellCustomizer.

### QuickTime Association

If you use the QuickTime view and association classes, you
should note the following:

- While you don't have to have the QuickTime
  software or the QuickTime for Java packages installed during development,
  clients must have both installed to view the QuickTime media. If
  one or the other aren't installed, the QuickTime view is simply blank.
- Apple only provides QuickTime for Java on MacOS and Windows, _not_ on
  MacOS X Server.
- EOQuickTimeAssociation doesn't support the `ValueAspect`,
  only `URLAspect`.
- HTTP urls are only supported in QuickTime v4.0.
- The QuickTime association and view aren't supported by the
  Java Client palette in Interface Builder.

### URLAspect for Associations

EOTextAssociation, EOImageAssociation, and EOQuickTimeAssociation
support a new aspect, `URLAspect`.
As opposed to the `ValueAspect`, which
is the raw data for the text, image, or movie, the `URLAspect` is
a url that references data on disk or over the Web. You can bind the `URLAspect` in
Interface Builder. The corresponding values are read only.

### Package Reorganization and Changes

The following classes have been moved from the eointerface
package to the eoapplication package, a new package to support Direct
to Java Client:

- EOApplet
- EOApplication
- EOArchive
- EOInterfaceController

Additionally, the classes EOApplication and EOInterfaceController
have new superclasses, and their APIs have been modified considerably.
EOArchive has also changed, resulting in the requirement that you
open and explicitly save every interface file in your projects.

### New Interface Layer Classes and Interfaces

The following table lists the classes and interfaces that
have been added to the client side interface layer in this release.

|  |  |
| --- | --- |
| __Class or Interface__ | __Description__ |
| EOColumnEditor | An abstract class that implements generalized cell editing management for javax.swing.JTables. See ["Support for Table Cell Editing"](#apple-ijdeurscjfdue). |
| EOImageAssociation | A class whose instances associate the contents of their display groups with EOImageViews. |
| EOImageView | A class whose instances display images (java.awt.Image objects) in Java Client applications. |
| EOQuickTimeAssociation | A class whose instances associate the contents of their display groups with EOQuickTimeViews. |
| EOQuickTimeView | A class whose instances display QuickTime media in Java Client applications. See ["QuickTime Association"](#apple-inbeoq2hifbem). |
| EOTableColumnAssociation. TableColumnCustomizer (interface) | An interface that defines the API an object uses to specify custom editors and renderers for an EOTableColumnAssociation. See ["Support for Table Cell Editing"](#apple-ijdeurscjfdue). |
| EOTextColumnEditor | EOTextColumnEditor is a concrete subclass of EOColumnEditor whose instances mediate between EOTextColumnAssociations and EOTextFields. See ["Support for Table Cell Editing"](#apple-ijdeurscjfdue). |

For more information on these classes and interface, see the
corresponding class and interface specifications.

### Added Methods

The following tables summarize the methods and constants that
have been added to the Java Client interface layer in this release.
The majority of the additions are in EODisplayGroup. Most of the
additions are analogous to API in the server side WODisplayGroup
and have been added to synchronize the classes.

__EOAssociation__

| __New or Changed API__ | __Description__ |
| `URLAspect` (Constant) | A string constant that defines the name of a new aspect. See ["URLAspect for Associations"](#apple-inbeorkcizaus). |
| `dispose` | Conformance to NSDisposable. |
| `isEnabled` | Returns `false` if the receiver has explicitly disabled its display object or if the receiver's `EnabledAspect` (if bound) resolves to `false`; `true` otherwise. |
| `isEnabledAtIndex` | Returns `false` if the receiver has explicitly disabled its display object or if the receiver's `EnabledAspect` (if bound) resolves to `false` for the specified index; `true` otherwise. |
| `isExplicitlyDisabled` | Returns `true` if the receiver has explicitly disabled its display object, `false` otherwise. |
| `setExplicitlyDisabled` | Sets whether or not the receiver is explicitly disabled. This method and its counterpart `isExplicitlyDisabled` are used by Direct to Java Client. An association is "explicitly disabled" when the display object shouldn't be editable, such as in the case where the display object simply displays the results of a search. |

__EOControlActionAdapter__

| __New or Changed API__ | __Description__ |
| `dispose` | Conformance to NSDisposable. |

__EODisplayGroup__

| __New or Changed API__ | __Description__ |
| `globalDefaultForValidatesChangesImmediately`  `setGlobalDefaultFor ValidatesChangesImmediately` | Static methods that return or set the default validation behavior for new display group instances: `true` if they immediately handle validation errors, or `false` if they leave errors for the EOEditingContext to handle when saving changes. |
| `globalDefaultStringMatchFormat`  `setGlobalDefaultStringMatchFormat` | Static methods that return or set the default string match format string used by display group instances. |
| `globalDefaultStringMatchOperator`  `setGlobalDefaultStringMatchOperator` | Static methods that return or set the default string match operator used by display group instances. |
| `awakeFromNib` | Invoked when the receiver is unarchived from a nib file to prepare it for use in an application. |
| `defaultStringMatchFormat`  `setDefaultStringMatchFormat` | Returns or sets the default string match format string used by the receiver. |
| `defaultStringMatchOperator`  `setDefaultStringMatchOperator` | Returns or sets the default string match operator used by the receiver. |
| `delete` | Analogous to WODisplayGroup's method. |
| `dispose` | Conformance to NSDisposable. |
| `editingContextPresentErrorMessage` | Invoked as part of the EOEditingContext.MessageHandlers, to present an attention panel a message to display. |
| `enterQueryMode` | Puts the receiver in query mode. |
| `equalToQueryValues`  `setEqualToQueryValues` | Returns or sets the receiver's dictionary of equalTo query values. Similar to the WODisplayGroup `queryMatch` method. |
| `fetch` | Analogous to the WODisplayGroup method. |
| `finishInitialization` | Invoked from the EODisplayGroup constructor and from `awakeFromNib` to finish initializing a newly created display group. |
| `greaterThanQueryValues`  `setGreaterThanQueryValues` | Returns or sets the receiver's dictionary of greaterThan query values. Similar to the WODisplayGroup `queryMin` method. |
| `inQueryMode`  `setInQueryMode` | Analogous to WODisplayGroup's methods. |
| `insert` | Analogous to the WODisplayGroup method. |
| `insertObjectAtIndex` | Analogous to the WODisplayGroup method `insertNewObjectAtIndex`. |
| `insertedObjectDefaultValues`  `setInsertedObjectDefaultValues` | Analogous to WODisplayGroup's methods. |
| `lessThanQueryValues`  `setLessThanQueryValues` | Returns or sets the receiver's dictionary of lessThan query values. Similar to the WODisplayGroup `queryMax` method. |
| `observerData`  `setObserverData` | Conformance to NSInlineObservable. |
| `qualifierFromQueryValues` | Analogous to the WODisplayGroup method. |
| `qualifyDataSource` | Analogous to the WODisplayGroup method. |
| `qualifyDisplayGroup` | Analogous to the WODisplayGroup method. |
| `queryBindingValues`  `setQueryBindingValues` | Returns or sets a dictionary containing the actual values that the user wants to query upon. |
| `queryOperatorValues`  `setQueryOperatorValues` | Returns or sets a dictionary of operators to use on items in the query dictionaries (`equalToQueryValues`, `greaterThanQueryValues`, and `lessThanQueryValues`). |
| `selectNext` | Analogous to the WODisplayGroup method. |
| `selectObjectsIdenticalToSelectFirstOnNoMatch` | Analogous to the WODisplayGroup method. |
| `selectPrevious` | Analogous to the WODisplayGroup method. |
| `setValueForObjectAtIndex` (Changed arguments) | The position of the integer index argument has been swapped with that of the String value argument. |
| `setValueForObject` (Changed arguments) | The position of the last two arguments has been swapped and the EOKeyValueCodingAdditions argument has been retyped as an Object. |
| `sortOrderings` | Analogous to the WODisplayGroup method. |
| `undoManager` | Returns the receiver's NSUndoManager. |
| `valueForObjectAtIndex` (Changed arguments) | The position of the arguments has been swapped. |
| `valueForObjectKey` | Returns the value in the specified object for the property identified by the specified key. |
| `willChange` | Notifies observers that the receiver will change. |

__EOFormCell__

| __New or Changed API__ | __Description__ |
| `dispose` | Conformance to NSDisposable. |

__EOMasterDetailAssociation__

| __New or Changed API__ | __Description__ |
| `dispose` | Conformance to NSDisposable. |

__EOTable__

| __New or Changed API__ | __Description__ |
| `dispose` | Conformance to NSDisposable. |

__EOTableAssociation__

| __New or Changed API__ | __Description__ |
| `removeColumnAssociation` | Removes the specified column association from the receiver's set of EOTableColumnAssociations. |

__EOTableColumnAssociation__

| __New or Changed API__ | __Description__ |
| `tableColumnCustomizer`  `setTableColumnCustomizer` | Returns and sets the association's table column customizer. |
| `dispose` | Conformance to NSDisposable. |
| `table`  `setTable` (Changed) | Returns and sets the association's EOTable object.   Note that the pre-4.5 `setTable` method had a java.awt.Component as an argument instead of an EOTable (from which you can get Swing table). |

__EOView__

| __New or Changed API__ | __Description__ |
| `dispose` | Conformance to NSDisposable. |

### Deleted API

The following methods, organized by class, have been deleted
and replaced, for backwards compatibility with the Java wrappers
(com.apple.yellow packages):

__EOActionAssociation__

| __Deleted API__ | __New API or Workaround__ |
| `enabled` | `isEnabled` (inherited from EOAssociation) |

__EODisplayGroup__

| __Deleted API__ | __New API or Workaround__ |
| `EODisplayGroup(EODataSource dataSource)` | Invoke the default constructor followed by `setDataSource` with the data source as an argument. |
| `editingContextPresentException` | `editingContextPresentErrorMessage` |
| `insertNewObjectAtIndex(int index);` | `insertObjectAtIndex(int index)` |
| `selectObjectsIdenticalTo` | `selectObjectsIdenticalToSelectFirstOnNoMatch` |
| `sortOrdering` | `sortOrderings`  Note the addition of the "s" in "Orderings" |
| `valueForObject(      String value,      EOKeyValueCodingAdditions object)` | `valueForObjectKey(      EOKeyValueCodingAdditions object,      String value)`  Note that in addition to the method name change, the position of the arguments was swapped. |

__EOViewLayout__

| __Deleted API__ | __New API or Workaround__ |
| `Fixed` (Constant) | For use in `setAutosizingMask`, simply use 0 to mean fixed size. |

## Running Java Client Applications

There are two changes to running Java Client Applications:
the syntax for starting applications has changed and the classpath
requirements have changed for all platforms except Mac OS X Server.

In WebObjects 4.5, there are three ways to run Java Client
applications:

1. As a java application with the command:
   > ```
   > java [-debug] -classpath <classpath>
   >     com.apple.client.eoapplication.EOApplication
   >     -applicationURL <url> [-page <page>]
   > ```

    Note
   that you might have to vary the parameters if you use special distribution channels.

2. As an applet in Applet Viewer with the commands:
   > ```
   > export CLASSPATH=<classpath>  appletviewer [-debug] <url>
   > ```
3. As an applet in a browser

### For Non-Mac OS X Server Users

If you run Java Client applications on non-Mac OS X Server
platforms, you might need to change the classpath you ordinarily
use. If you previously put the awt.jar file ($(NEXT_ROOT)/Library/Frameworks/JavaVM.framework/Classes/awt.jar)
in your classpath, you should remove it. Except on Mac OS X Server,
you can't use the awt.jar.

## Direct To Java Client

Direct to Java Client is an addition to Enterprise Objects
Framework and Java Client. It dynamically generates complete Java
Client applications (or parts of them) from information in a model.
User interface configuration information is stored as a set of rules. You
can use the user interface specified by the default set of rules,
or you can customize the user interface by changing the rules.

The version of Direct to Java Client shipping with WebObjects
4.5 is a technology preview. It is very stable and robust, but its
programming interfaces and generated user interfaces are not guaranteed
to be the same in future releases.

Two new packages have been added to the Java Client technology
to support Direct to Java Client, eoapplication and eogeneration.
The eoapplication package provides application level logic such
as document management and classes for creating advanced user interfaces.
The eogeneration package is for defining applications that are completely dynamic.

The eoapplication and eogeneration packages consists mainly
of __controllers__. A new class, EOController, defines
the basic controller behavior.

|  |
| --- |
| __Note:__ The EOInterfaceController class, which was in the eointerface package in the previous release, has been redefined as a subclass of EOController. In greater detail, EOController is a subclass of EOEntityController, which is subclass of EOComponentController, which is subclass of EOController. |

There are different types of controllers:

- __User interface controllers__ (for
  controlling tabbed panes and windows, for example)
- __Entity level controllers__ (for controlling
  user interfaces that operate at an entity or object level; query
  and editor interfaces, for example)
- __Property level controllers__ (for controlling
  user interface widgets such as text fields, combo boxes, action
  buttons that operate on properties of objects)
- __Application objects__

Controllers are organized in a hierarchy. The root controller
is the shared application object, typically an EOApplication. Children
of the EOApplication object, or the EOApplication's __subcontrollers__,
are usually window or applet controllers which themselves have one
or multiple subcontrollers.

|  |
| --- |
| __Note:__ The eoapplication and eogeneration APIs are preliminary, and might change in future releases. |

To learn more about Direct to Java Client, including how to
create dynamic applications, see the tutorial "Getting Started
with Direct to Java Client".

[!](What%27s%20New%20in%20WebObjects%204.5.md)
