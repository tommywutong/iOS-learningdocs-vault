---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Protocols/EOEditingContextDelegate.html
archived_at: '2026-07-18T01:28:32.561229Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOClassDescription.ClassDelegate.md)
[!](EOEditingContext.Editor.md)

---

# EOEditingContext.Delegate

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (WebObjects and Yellow Box)

## Interface Description

The EOEditingContext.Delegate interface defines methods that an EOEditingContext can invoke in its delegate. Delegates are not required to provide implementations for all of the methods in the interface, and you don't have to use the __implements__ keyword to specify that the object implements the Delegate interface. Instead, declare and implement any subset of the methods declared in the interface that you need, and use the EOEditingContext method [__setDelegate__](EOEditingContext.md)method to assign your object as the delegate. An editing context can determine if the delegate doesn't implement a delegate method and only attempts to invoke the methods the delegate actually implements.

## Method Types

**Fetching objects**

**- editingContextShouldFetchObjects**

**Invalidating objects**

**- editingContextShouldInvalidateObject (Yellow Box only)**

**Saving changes**

**- editingContextWillSaveChanges**

**Handling failures**

**- editingContextShouldValidateChanges

**- editingContextShouldPresentException

**- editingContextShouldUndoUserActionsAfterFailure (Yellow Box only)******

**Merging changes (Yellow Box only)**

**- editingContextShouldMergeChangesForObject (Yellow Box only)

**- editingContextDidMergeChanges (Yellow Box only)****

## Instance Methods

---

#### editingContextDidMergeChanges

public abstract void __editingContextDidMergeChanges__ (EOEditingContext _anEditingContext_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Invoked once after a batch of objects has been updated in _anEditingContext_'s parent object store (in response to a [ObjectsChangedInStoreNotification](EOEditingContext.md)). A delegate might implement this method to define custom merging behavior, most likely in conjunction with __editingContextShouldMergeChangesForObject__ . It is safe for this method to make changes to the objects in the editing context.

---

#### editingContextShouldFetchObjects

public abstract NSArray __editingContextShouldFetchObjects__ (
EOEditingContext _editingContext_,
EOFetchSpecification _fetchSpecification_)

Invoked from [__objectsWithFetchSpecification__](EOEditingContext.md). If the delegate has appropriate results cached it can return them and the fetch will be bypassed. Returning `null` causes the fetch to be propagated to the parent object store.

---

#### editingContextShouldInvalidateObject

public abstract boolean __editingContextShouldInvalidateObject__ (
EOEditingContext _anEOEditingContext_,
EOEnterpriseObject _anObject_,
EOGlobalID _anEOGlobalID_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Sent when an _object_ identified by _globalID_ has been explicitly invalidated. If the delegate returns __false__ , the invalidation is refused. This allows the delegate to selectively override object invalidations.

__See also:__ `[-](../Classes/EOEditingContext.md)`__invalidateAllObjects__ , `[-](../Classes/EOEditingContext.md)`__revert__

---

#### editingContextShouldMergeChangesForObject

public abstract boolean __editingContextShouldMergeChangesForObject__ (
EOEditingContext _anEditingContext_,
EOEnterpriseObject _object_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

When an EOObjectsChangedInStoreNotification is received, _anEditingContext_ invokes this method in its delegate once for each of the objects that has both uncommitted changes and an update from the EOObjectStore. This method is invoked before any updates actually occur.

If this method returns __true__ , all of the uncommitted changes should be merged into the object after the update is applied, in effect preserving the uncommitted changes (the default behavior). The delegate method __editingContextShouldInvalidateObject__ will not be sent for the object in question.

If this method returns __false__ , no uncommitted changes are applied. Thus, the object is updated to reflect the values from the database exactly. This method should not make any changes to the object since it is about to be invalidated.

If you want to provide custom merging behavior, you need to implement both this method and __editingContextDidMergeChanges__ . You use __editingContextShouldMergeChangesForObject__ to save information about each changed object and return __true__ to allow merging to continue. After the default merging behavior occurs, __editingContextDidMergeChanges__ is invoked, at which point you implement your custom behavior.

---

#### editingContextShouldPresentException

Java Client:

public abstract boolean __editingContextShouldPresentException__ (
EOEditingContext _anEditingContext_,
java.lang.Exception _exception_)

Yellow Box:

public abstract boolean __editingContextShouldPresentException__ (
EOEditingContext _anEditingContext_,
java.lang.Throwable _exception_)

Sent whenever an exception is caught by an EOEditingContext. If the delegate returns __false__ , _exception_ is ignored. Otherwise (if the delegate returns __true__ , if the editing context doesn't have a delegate, or if the delegate doesn't implement this method) _exception_ is passed to the message handler for further processing,

__See also:__ [- __messageHandler__](EOEditingContext.md)

---

#### editingContextShouldUndoUserActionsAfterFailure

public abstract boolean __editingContextShouldUndoUserActionsAfterFailure__ (
EOEditingContext _anEditingContext_)

This method is available for Yellow Box applications only; there is no Java Client equivalent.

Sent when a validation error occurs while processing a [__processRecentChanges__](EOEditingContext.md)message. If the delegate returns __false__ , it disables the automatic undoing of user actions after validation has resulted in an error.

By default, if a user attempts to perform an action that results in a validation failure (such as deleting a department object that has a delete rule stating that the department can't be deleted if it contains employees), the user's action is immediately rolled back. However, if this delegate method returns __false__ , the user action is allowed to stand (though attempting to save the changes to the database without solving the validation error will still result in a failure). Returning __false__ gives the user an opportunity to correct the validation problem so that the operation can proceed (for example, the user might delete all of the department's employees so that the department itself can be deleted).

---

#### editingContextShouldValidateChanges

public abstract boolean __editingContextShouldValidateChanges__ (
EOEditingContext _anEditingContext_)

Sent when an EOEditingContext receives a [__saveChanges__](EOEditingContext.md)message. If the delegate returns __false__ , changes are saved without first performing validation. This method can be useful if the delegate wants to provide its own validation mechanism.

---

#### editingContextWillSaveChanges

public abstract void __editingContextWillSaveChanges__ (EOEditingContext _editingContext_)

Sent when an EOEditingContext receives a [__saveChanges__](EOEditingContext.md)message. The delegate can throw an exception to abort the save operation.

---

[!](EOClassDescription.ClassDelegate.md)
[!](EOEditingContext.Editor.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
