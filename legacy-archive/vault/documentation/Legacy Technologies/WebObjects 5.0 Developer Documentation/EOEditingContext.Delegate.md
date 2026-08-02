---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Protocols/EOEditingContext.Delegate.html
archived_at: '2026-07-15T08:13:47.816533Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md) 

# EOEditingContext.Delegate

> __(informal interface)__

> **__Package:__**
> : com.webobjects.eocontrol

---

## Interface Description

---

The [EOEditingContext. Delegate](#apple-inbecskejfdec) interface defines methods that an EOEditingContext can invoke in its delegate. Delegates are not required to provide implementations for all of the methods in the interface, and you don't have to use the implements keyword to specify that the object implements the Delegate interface. Instead, declare and implement any subset of the methods declared in the interface that you need, and use the EOEditingContext method setDelegate method to assign your object as the delegate. An editing context can determine if the delegate doesn't implement a delegate method and only attempts to invoke the methods the delegate actually implements.

## Method Types

---

> **Fetching objects**
> : editingContextShouldFetchObjects
>
> **Invalidating objects**
> : editingContextShouldInvalidateObject
>
> **Saving changes**
> : editingContextWillSaveChanges
>
> **Handling failures**
> : editingContextShouldValidateChanges: editingContextShouldPresentException: editingContextShouldUndoUserActionsAfterFailure
>
> **Merging changes**
> : editingContextShouldMergeChangesForObject: editingContextDidMergeChanges

## Instance Methods

---

### editingContextDidMergeChanges

`public abstract void editingContextDidMergeChanges(EOEditingContext anEditingContext)`

Invoked once after a batch of objects has been updated in _anEditingContext_'s parent object store (in response to an ObjectsChangedInStoreNotification). A delegate might implement this method to define custom merging behavior, most likely in conjunction with editingContextShouldMergeChangesForObject. It is safe for this method to make changes to the objects in the editing context.

---

### editingContextShouldFetchObjects

`public abstract NSArray editingContextShouldFetchObjects( EOEditingContext editingContext, EOFetchSpecification fetchSpecification)`

Invoked from objectsWithFetchSpecification. If the delegate has appropriate results cached it can return them and the fetch will be bypassed. Returning null causes the fetch to be propagated to the parent object store.

---

### editingContextShouldInvalidateObject

`public abstract boolean editingContextShouldInvalidateObject( EOEditingContext anEOEditingContext, EOEnterpriseObject anObject, EOGlobalID anEOGlobalID)`

Sent when an _object_ identified by _globalID_ has been explicitly invalidated. If the delegate returns false, the invalidation is refused. This allows the delegate to selectively override object invalidations.

__See Also:__ invalidateAllObjects, reset

---

### editingContextShouldMergeChangesForObject

`public abstract boolean editingContextShouldMergeChangesForObject( EOEditingContext anEditingContext, EOEnterpriseObject object)`

When an ObjectsChangedInStoreNotification is received, _anEditingContext_ invokes this method in its delegate once for each of the objects that has both uncommitted changes and an update from the EOObjectStore. This method is invoked before any updates actually occur.

If this method returns true, all of the uncommitted changes should be merged into the object after the update is applied, in effect preserving the uncommitted changes (the default behavior). The delegate method editingContextShouldInvalidateObject will not be sent for the object in question.

If this method returns false, no uncommitted changes are applied. Thus, the object is updated to reflect the values from the database exactly. This method should not make any changes to the object since it is about to be invalidated.

If you want to provide custom merging behavior, you need to implement both this method and __editingContextDidMergeChanges__. You use __editingContextShouldMergeChangesForObject__ to save information about each changed object and return true to allow merging to continue. After the default merging behavior occurs, __editingContextDidMergeChanges__ is invoked, at which point you implement your custom behavior.

---

### editingContextShouldPresentException

`public abstract boolean editingContextShouldPresentException( EOEditingContext anEditingContext, Throwable exception)`

Sent whenever an exception is caught by an EOEditingContext. If the delegate returns false, _exception_ is ignored. Otherwise (if the delegate returns true, if the editing context doesn't have a delegate, or if the delegate doesn't implement this method) _exception_ is passed to the message handler for further processing,

__See Also:__ messageHandler

---

### editingContextShouldUndoUserActionsAfterFailure

`public abstract boolean editingContextShouldUndoUserActionsAfterFailure(EOEditingContext anEditingContext)`

Sent when a validation error occurs while processing a processRecentChanges message. If the delegate returns false, it disables the automatic undoing of user actions after validation has resulted in an error.

By default, if a user attempts to perform an action that results in a validation failure (such as deleting a department object that has a delete rule stating that the department can't be deleted if it contains employees), the user's action is immediately rolled back. However, if this delegate method returns false, the user action is allowed to stand (though attempting to save the changes to the database without solving the validation error will still result in a failure). Returning false gives the user an opportunity to correct the validation problem so that the operation can proceed (for example, the user might delete all of the department's employees so that the department itself can be deleted).

---

### editingContextShouldValidateChanges

`public abstract boolean editingContextShouldValidateChanges(EOEditingContext anEditingContext)`

Sent when an EOEditingContext receives a saveChanges message. If the delegate returns false, changes are saved without first performing validation. This method can be useful if the delegate wants to provide its own validation mechanism.

---

### editingContextWillSaveChanges

`public abstract void editingContextWillSaveChanges(EOEditingContext editingContext)`

Sent when an EOEditingContext receives a saveChanges message. The delegate can throw an exception to abort the save operation.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
