---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOEditingContextDelegate.html
archived_at: '2026-07-18T01:28:40.908996Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOClassDescriptionClassDelegate.md)
[!](EOEditors.md)

---

# EOEditingContextDelegate

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOEditingContext.h

## Category Description

The EOEditingContextDelegate informal protocol defines methods that an EOEditingContext can invoke in its delegate. Delegates are not required to provide implementations for all of the methods in the informal protocol. Instead, declare and implement any subset of the methods declared in the informal protocol that you need, and use the EOEditingContext method [__setDelegate:__](EOEditingContext-3.md)method to assign your object as the delegate. An editing context can determine if the delegate doesn't implement a delegate method and only attempts to invoke the methods the delegate actually implements.

**Fetching objects**

**- editingContext: shouldFetchObjectsDescribedByFetchSpecification:**

**Invalidating objects**

**- editingContext:shouldInvalidateObject:globalID:**

**Saving changes**

**- editingContextWillSaveChanges:**

**Handling failures**

**- editingContextShouldValidateChanges:

**- editingContext:shouldPresentException:

**- editingContextShouldUndoUserActionsAfterFailure:******

**Merging changes**

**- editingContext:shouldMergeChangesForObject:

**- editingContextDidMergeChanges:****

---

#### editingContextDidMergeChanges:

- (void)`editingContextDidMergeChanges:`(EOEditingContext \*)_anEditingContext_

Invoked once after a batch of objects has been updated in _anEditingContext_'s parent object store (in response to a [EOObjectsChangedInStoreNotification](EOEditingContext-3.md)). A delegate might implement this method to define custom merging behavior, most likely in conjunction with __editingContext:shouldMergeChangesForObject:__ . It is safe for this method to make changes to the objects in the editing context.

---

#### editingContext:shouldFetchObjectsDescribedByFetchSpecification:

- (NSArray \*)`editingContext:`(EOEditingContext \*)_editingContext_ `shouldFetchObjectsDescribedByFetchSpecification:`(EOFetchSpecification \*)_fetchSpecification_

Invoked from [__objectsWithFetchSpecification:editingContext:__](EOEditingContext-3.md). If the delegate has appropriate results cached it can return them and the fetch will be bypassed. Returning `nil` causes the fetch to be propagated to the parent object store.

---

#### editingContext:shouldInvalidateObject:globalID:

- (BOOL)`editingContext:`(EOEditingContext \*)_anEditingContext_
`shouldInvalidateObject:`(id)_object_
`globalID:`(EOGlobalID \*)_globalID_

Sent when an _object_ identified by _globalID_ has been explicitly invalidated. If the delegate returns NO, the invalidation is refused. This allows the delegate to selectively override object invalidations.

__See also:__ `[-](../Classes/EOEditingContext.md)`__invalidateAllObjects__ , `[-](../Classes/EOEditingContext.md)`__revert__

---

#### editingContext:shouldMergeChangesForObject:

- (BOOL)`editingContext:`(EOEditingContext \*)_anEditingContext_
`shouldMergeChangesForObject:`(id)_object_

When an EOObjectsChangedInStoreNotification is received, _anEditingContext_ invokes this method in its delegate once for each of the objects that has both uncommitted changes and an update from the EOObjectStore. This method is invoked before any updates actually occur.

If this method returns YES, all of the uncommitted changes should be merged into the object after the update is applied, in effect preserving the uncommitted changes (the default behavior). The delegate method __editingContext:shouldInvalidateObject:globalID:__ will not be sent for the object in question.

If this method returns NO, no uncommitted changes are applied. Thus, the object is updated to reflect the values from the database exactly. This method should not make any changes to the object since it is about to be invalidated.

If you want to provide custom merging behavior, you need to implement both this method and __editingContextDidMergeChanges:__ . You use __editingContext:shouldMergeChangesForObject:__ to save information about each changed object and return YES to allow merging to continue. After the default merging behavior occurs, __editingContextDidMergeChanges:__ is invoked, at which point you implement your custom behavior.

---

#### editingContext:shouldPresentException:

- (BOOL)`editingContext:`(EOEditingContext \*)_anEditingContext_
`shouldPresentException:`(NSException \*)_exception_

Sent whenever an exception is caught by an EOEditingContext. If the delegate returns NO, _exception_ is ignored. Otherwise (if the delegate returns YES, if the editing context doesn't have a delegate, or if the delegate doesn't implement this method) _exception_ is passed to the message handler for further processing,

__See also:__ [- __messageHandler__](EOEditingContext-3.md)

---

#### editingContextShouldUndoUserActionsAfterFailure:

- (BOOL)`editingContextShouldUndoUserActionsAfterFailure:`(EOEditingContext \*)_anEditingContext_

Sent when a validation error occurs while processing a [__processRecentChanges__](EOEditingContext-3.md)message. If the delegate returns NO, it disables the automatic undoing of user actions after validation has resulted in an error.

By default, if a user attempts to perform an action that results in a validation failure (such as deleting a department object that has a delete rule stating that the department can't be deleted if it contains employees), the user's action is immediately rolled back. However, if this delegate method returns NO, the user action is allowed to stand (though attempting to save the changes to the database without solving the validation error will still result in a failure). Returning NO gives the user an opportunity to correct the validation problem so that the operation can proceed (for example, the user might delete all of the department's employees so that the department itself can be deleted).

---

#### editingContextShouldValidateChanges:

- (BOOL)`editingContextShouldValidateChanges:`(EOEditingContext \*)_anEditingContext_

Sent when an EOEditingContext receives a [__saveChanges__](EOEditingContext-3.md)message. If the delegate returns NO, changes are saved without first performing validation. This method can be useful if the delegate wants to provide its own validation mechanism.

---

#### editingContextWillSaveChanges:

- (void)`editingContextWillSaveChanges:`(EOEditingContext \*)_editingContext_

Sent when an EOEditingContext receives a [__saveChanges__](EOEditingContext-3.md)message. The delegate can raise an exception to abort the save operation.

---

[!](EOClassDescriptionClassDelegate.md)
[!](EOEditors.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
