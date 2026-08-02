---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOInterfaceController.html
archived_at: '2026-07-18T01:28:43.294336Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOInterface Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOInterface.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOGenericControlAssociation.md)
[!](EOMasterCopyAssociation.md)

---

# EOInterfaceController

__Inherits From:__
java.lang.Object

EOKeyValueCodingAdditions (EOControl)
EOObserving (EOControl)
java.awt.event.WindowListener

__Inherits From:__
com.apple.client.eointerface

---

## Class Description

EOInterfaceController serves as a convenient base class for logic related to the interface of client-side applications. When the WebObjectsApplication wizard in Project Builder creates a new client-side interface, it adds to the client-side subproject an Interface Builder nib file representing this interface and a skeletal EOInterfaceController subclass defined as the nib file's root object or "owner."

In an application constructed in conformance to the Model-View-Controller paradigm, EOInterfaceController plays the role of controller. It has four special outlets: its [`editingContext`](#apple-gm3tqmq), its [`component`](#apple-gm2tgoa), its [`masterDisplayGroup`](#apple-gm4dqna), and its [`controllerDisplayGroup`](#apple-gm2tioa), all of which you can configure using Interface Builder. The object identified by __component__  is an AWT Component that functions as the view, since it is the main entry point into the user interface. Because an enterprise objects must always inhabit an editing context, __editingContext__  and its contents serve as the "model." The __masterDisplayGroup__  is an EODisplayGroup containing the "master" enterprise objects manipulated by the controller's user interface (which may well involve many other display groups). The __controllerDisplayGroup__  is a convenience instance containing nothing but the interface controller itself.

---

## Constructors

public `EOInterfaceController`()

public `EOInterfaceController`(com.apple.client.eocontrol.EOEditingContext _substitutionContext_)

public `EOInterfaceController`(com.apple.client.eocontrol.EOEditingContext _substitutionContext_, java.lang.String _archiveName_)

The two-argument constructor is EOInterfaceController's designated constructor. It initializes a new instance and then attempts to load the associated EOArchive indentified by _archiveName_, using _substitutionContext_ as EOEditingContext's substitution editing context during the load. Archive loading results in the restoration of any controller outlets such as [`editingContext`](#apple-gm3tqmq) and [`component`](#apple-gm2tgoa) connected within InterfaceBuilder. The remaining constructors are convenience constructions that invoke the designated constructor with `null`s substituted for the missing arguments. These `null` values are passed along in the calls to [`loadArchive`](#apple-gu3tcmq) and EOEditingContext's `setSubstitutionEditingContext` .

---

## Instance Methods

---

### closeWindow

public void `closeWindow`()

Puts any window created through the [`runInFrame`](#apple-gm4tmmq) or [`runInModalDialog`](#apple-gm4tomq) methods offscreen and disposes of the window once the Component has been removed.

__See also:__
[`component`](#apple-gm2tgoa)

---

### collectChangesFromServer

public void `collectChangesFromServer`()

Updates the receiver's editing context to reflect any changes to enterprise objects pending on the server.

---

### component

public java.awt.Component `component`()

Returns the main entry point into the receiver's user interface, which is always an AWT Component.

---

### controllerDisplayGroup

public EODisplayGroup `controllerDisplayGroup`()

Returns an EODisplayGroup containing nothing but the receiver (EOInterfaceController implements EOKeyValueCodingAdditions). You typically instantiate and connect this display group with Interface Builder. This display group facilitates the use of the receiver with EOAssociations, as any properties defined in a controller subclass may then be used as association aspect keys.

For example, to enable or disable the entire user interface, you could add a "uiEnabled" property to an EOInterfaceController subclass and bind the "enabled" aspect of any EOAssociation with display objects in its component to the key of the controller display group.

---

### displayGroupDidChangeDataSource

public void `displayGroupDidChangeDataSource`(EODisplayGroup _aDisplayGroup_)

Overriden by subclasses to respond to a change in _aDisplayGroup_'s data source. In the [`setMasterDisplayGroup`](#apple-gqydonq) and [`setControllerDisplayGroup`](#apple-gqydkmq) methods EOInterfaceController sets itself as the delegate of its master and controller display groups if no other object has claimed delegate status. The default implementation of this delegation method simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq).

---

### displayGroupDidChangeSelection

public void `displayGroupDidChangeSelection`(EODisplayGroup _aDisplayGroup_)

Overriden by subclasses to respond to a selection change in _aDisplayGroup_. In the [`setMasterDisplayGroup`](#apple-gqydonq) and [`setControllerDisplayGroup`](#apple-gqydkmq) methods EOInterfaceController sets itself as the delegate of its master and controller display groups if no other object has claimed delegate status. The default implementation of this delegation method simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq).

---

### displayGroupDidDeleteObject

public void `displayGroupDidDeleteObject`(EODisplayGroup _aDisplayGroup_, java.lang.Object _anObject_)

Overriden by subclasses to respond to the deletion of _anObject_ in _aDisplayGroup_. In the [`setMasterDisplayGroup`](#apple-gqydonq) and [`setControllerDisplayGroup`](#apple-gqydkmq) methods EOInterfaceController sets itself as the delegate of its master and controller display groups if no other object has claimed delegate status. The default implementation of this delegation method simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq).

---

### displayGroupDidFetchObjects

public void `displayGroupDidFetchObjects`(EODisplayGroup _aDisplayGroup_, NSArray _anArray_)

Overriden by subclasses to respond to the fetch of objects in _anArray_ by _aDisplayGroup_. In the [`setMasterDisplayGroup`](#apple-gqydonq) and [`setControllerDisplayGroup`](#apple-gqydkmq) methods EOInterfaceController sets itself as the delegate of its master and controller display groups if no other object has claimed delegate status. The default implementation of this delegation method simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq).

---

### displayGroupDidInsertObject

public void `displayGroupDidInsertObject`(EODisplayGroup _aDisplayGroup_, java.lang.Object _anObject_)

Overriden by subclasses to respond to the insertion of object _anObject_ into _aDisplayGroup_. In the [`setMasterDisplayGroup`](#apple-gqydonq) and [`setControllerDisplayGroup`](#apple-gqydkmq) methods EOInterfaceController sets itself as the delegate of its master and controller display groups if no other object has claimed delegate status. The default implementation of this delegation method simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq).

---

### displayGroupDidSetValueForObject

public void `displayGroupDidSetValueForObject`(EODisplayGroup _aDisplayGroup_, java.lang.Object _anObject_, java.lang.Object _anObject_, java.lang.String _aString_)

Overriden by subclasses to _aDisplayGroup_. In the [`setMasterDisplayGroup`](#apple-gqydonq) and [`setControllerDisplayGroup`](#apple-gqydkmq) methods EOInterfaceController sets itself as the delegate of its master and controller display groups if no other object has claimed delegate status. The default implementation of this delegation method simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq).

---

### editingContext

public com.apple.client.eocontrol.EOEditingContext `editingContext`()

Returns the EOEditingContext established through [`setEditingContext`](#apple-gqydmna), which should also be that of the master display group's data source. All manipulation of enterprise objects must occur within an editing context.

__See also:__
[`masterDisplayGroup`](#apple-gm4dqna)

---

### handleEditingContextChanges

public void `handleEditingContextChanges`(NSNotification _aNotification_)

Implemented by observers of EOEditingContext's ObjectsChangedInEditingContext and EditingContextDidSaveChanges notifications; when [`setEditingContext`](#apple-gqydmna) is invoked, the receiver is automatically registered as an observer. The default implementation simply invokes [`redisplayControllerDisplayGroup`](#apple-gm4tenq) and [`updateWindowTitle`](#apple-gqzdgma).

---

### handleWindowClosing

protected void `handleWindowClosing`()

Invoked when the window containing the receiver's component is about to close. The default implementation invokes [`saveIfUserConfirmsAndCloseWindow`](#apple-gqydgma).

__See also:__
[`component`](#apple-gm2tgoa)

---

### insertIntoControllerDisplayGroup

protected void `insertIntoControllerDisplayGroup`()

Makes the receiver the only object in the controller display group and selects it. This method is invoked whenever [`setControllerDisplayGroup`](#apple-gqydkmq) is invoked.

---

### isEdited

public boolean `isEdited`()

Returns whether the receiver's editing contexthas changes and thus whether the receiver is "dirty."

__See also:__
[`editingContext`](#apple-gm3tqmq)

---

### isRunning

public boolean `isRunning`()

Returns whether [`component`](#apple-gm2tgoa) currently has a parent.

---

### isRunningInContainer

public boolean `isRunningInContainer`()

Returns `true` if no JFrame or JDialog has been instantiated by the receiver but [`component`](#apple-gm2tgoa) still has a parent.

---

### isRunningInFrame

public boolean `isRunningInFrame`()

Returns `true` if [`runInFrame`](#apple-gm4tmmq) has previously been invoked but [`closeWindow`](#apple-gm2teoa) has not.

---

### isRunningInModalDialog

public boolean `isRunningInModalDialog`()

Returns `true` if [`runInModalDialog`](#apple-gm4tomq) has previously been invoked but [`closeWindow`](#apple-gm2teoa) has not.

---

### loadArchive

protected void `loadArchive`()

Convenience method equivalent invoking the following form with a null parameter.

protected void __loadArchive__ (java.lang.String _archiveName_)

Loads a new instance of the EOArchive named _archiveName_ with the receiver as its owner and a null archive package name, throwing if the attempt fails (see EOArchive's __loadArchiveNamed__ ). If _archiveName_ is null the name of the receiver's class will be used instead.

---

### locateWindow

protected void `locateWindow`(java.awt.Window _window_)

Invoked within [`runInFrame`](#apple-gm4tmmq) and [`runInModalDialog`](#apple-gm4tomq), this method positions _window_ at its appropriate initial location, center screen in the default implementation.

---

### masterDisplayGroup

public EODisplayGroup `masterDisplayGroup`()

Returns an EODisplayGroup containing the "master" enterprise objects primarily manipulated by the receiver's user interface (the EOArchive associated with the receiver may well contain additional display groups).

A component containing a display of Studios, for example, might contain additional displays of Movies the selected Studio has produced and Talent in its stable, but the Studio EODisplayGroup would drive these details and therefore be the "master."

---

### masterObject

public com.apple.client.eocontrol.EOEnterpriseObject `masterObject`()

Returns that single enterprise object currently selected in the receiver's [`masterDisplayGroup`](#apple-gm4dqna).

---

### masterObjectGlobalID

public com.apple.client.eocontrol.EOGlobalID `masterObjectGlobalID`()

Returns the EOGlobalID of the [`masterObject`](#apple-gm4dsna).

---

### objectWillChange

public void `objectWillChange`(java.lang.Object _object_)

Actually EOObserverCenter's notification hook, this method is implemented by EOInterfaceController in order to invoke [`redisplayControllerDisplayGroup`](#apple-gm4tenq) whenever _object_ is the receiver.

---

### redisplayControllerDisplayGroup

public void `redisplayControllerDisplayGroup`()

Invoked whenever the contents or selection of [`controllerDisplayGroup`](#apple-gm2tioa) changes (see [`objectWillChange`](#apple-gm4tcna)), this method sends the display group a __redisplay__  message.

---

### run

public void `run`()

A "presentation-neutral" form of the following three more specific editions, this method is intended to be invoked when the consumer is content to leave [`component`](#apple-gm2tgoa) presentation details to the receiver. The default implementation invokes [`runInFrame`](#apple-gm4tmmq).

---

### runInContainer

public void `runInContainer`(java.awt.Container _container_)

Adds the receiver's [`component`](#apple-gm2tgoa) to _container_.

---

### runInFrame

public void `runInFrame`()

Instantiates a JFrame containing the receiver's [`component`](#apple-gm2tgoa) and makes it visible atop the window stack.

---

### runInModalDialog

public void `runInModalDialog`()

Instantiates a modal JDialog containing the receiver's [`component`](#apple-gm2tgoa) and makes it visible atop the window stack.

---

### save

public boolean `save`()

Sends [`editingContext`](#apple-gm3tqmq) a __saveChanges__  message with the receiver as its sender and presents an error dialog containing any exception if this invocation fails. Returns `true` if __saveChanges__  succeeds, `false` otherwise.

---

### saveAndCloseWindow

public boolean `saveAndCloseWindow`()

Invokes [`save`](#apple-gm4tqmq) and, upon success, [`closeWindow`](#apple-gm2teoa), returning `save`'s result.

---

### saveIfUserConfirms

public boolean `saveIfUserConfirms`()

Convenience method invoking the following two parameter form with a null _dialogTitle_ and _message_.

public boolean `saveIfUserConfirms`(java.lang.String _dialogTitle_, java.lang.String _message_)

Invokes [`save`](#apple-gm4tqmq) once the user has confirmed this operation in a dialog titled _dialogTitle_ containing _message_ (both arguments take on default values if null). Returns `true` if the operation is confirmed and succeeds, `false` otherwise.

---

### saveIfUserConfirmsAndCloseWindow

public boolean `saveIfUserConfirmsAndCloseWindow`()

Invokes the two parameter form of `saveIfUserConfirms` with the _dialogTitle_ "Close" and a null _message_. If the operation is confirmed, `closeWindow` is invoked. Returns the result of __saveIfUserConfirms__ .

---

### setComponent

public void `setComponent`(java.awt.Component _component_)

Establishes _component_ as the main entry point into the receiver's user interface. If component is a Window or RootPaneContainer, the receiver's [`component`](#apple-gm2tgoa) will actually wind up being a new EOView containing its subcomponents rather than _component_, as the appropriate root container will be determined by which __run...__  method is subsequently invoked. If _component_ is not a Window it will be removed from any existing parent.

---

### setControllerDisplayGroup

public void `setControllerDisplayGroup`(EODisplayGroup _displayGroup_)

Typically invoked only by EOArchive in re-establishing a connection made in the receiver's corresponding InterfaceBuilder document, this method establishes _displayGroup_ as the EODisplayGroup which will vend the receiver's keys (also see [`controllerDisplayGroup`](#apple-gm2tioa)). The default implementation invokes [`insertIntoControllerDisplayGroup`](#apple-gu3dkmy) before making the receiver both an observer of _displayGroup_ and its delegate in the absence of any other.

---

### setEditingContext

public void `setEditingContext`(com.apple.client.eocontrol.EOEditingContext _editingContext_)

Typically invoked only by EOArchive in re-establishing a connection made in the receiver's corresponding InterfaceBuilder document, this method establishes _editingContext_ as the EOEditingContext for any manipulated enterprise objects (also see [`editingContext`](#apple-gm3tqmq)). This should be the same as that of [`masterDisplayGroup`](#apple-gm4dqna)'s __dataSource__ . The default implementation adds the receiver as a recipient of ObjectsChangedInEditingContext and EditingContextDidSaveChanges notifications sent to [`handleEditingContextChanges`](#apple-gm3tsmq).

---

### setMasterDisplayGroup

public void `setMasterDisplayGroup`(EODisplayGroup _displayGroup_)

Establishes _displayGroup_ as the EODisplayGroup containing the "master" enterprise objects manipulated in [`component`](#apple-gm2tgoa) (also see [`masterDisplayGroup`](#apple-gm4dqna)).

---

### setMasterWithGlobalID

public void `setMasterWithGlobalID`(com.apple.client.eocontrol.EOGlobalID _gid_)

Attempts to retrieve that enterprise object with _gid_ from the EOEditingContext of [`masterDisplayGroup`](#apple-gm4dqna)'s __dataSource__ . If successful, this object is set as `masterDisplayGroup`'s new contents and selection. If not, the `masterDisplayGroup` will be emptied.

---

### setMasterWithObject

public void `setMasterWithObject`(com.apple.client.eocontrol.EOEnterpriseObject _anEO_)

Retrieves _anEO_'s EOGlobalID from its editing context and invokes [`setMasterWithGlobalID`](#apple-gqydqoa).

---

### setTitle

public void `setTitle`(java.lang.String _title_)

Sets the receiver's title to _title_. Note that this value will be used in constructing the receiver's [`windowTitle`](#apple-gu4tkmy). Invocations of this method will have no effect on window titles until changes occur in the receiver's editing context.

---

### showWindow

public void `showWindow`()

If the receiver's root container is a Window, this method makes it visible atop the window stack.

---

### title

public java.lang.String `title`()

Returns any title explicitly set for the receiver via [`setTitle`](#apple-gqytcnq).

---

### updateWindowTitle

public void `updateWindowTitle`()

Sets the title of any Window created by the receiver to the current value of [`windowTitle`](#apple-gu4tkmy).

---

### window

public java.awt.Window `window`()

Returns the Window created to contain the receiver's [`component`](#apple-gm2tgoa), which will only be non-null if [`runInFrame`](#apple-gm4tmmq) or [`runInModalDialog`](#apple-gm4tomq) have previously been invoked.

---

### windowTitle

protected java.lang.String `windowTitle`()

Returns [`title`](#apple-gqzdaoa) if it has been explicitly set or an de-packaged, prettified edition of the receiver's class name. Both will be prefixed by an asterisk if [`isEdited`](#apple-gm4dgma) currently returns `true`.

---

[!](EOGenericControlAssociation.md)
[!](EOMasterCopyAssociation.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
