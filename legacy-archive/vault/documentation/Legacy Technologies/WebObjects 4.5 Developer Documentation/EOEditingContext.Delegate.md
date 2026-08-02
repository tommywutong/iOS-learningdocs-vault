---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Protocols/EOEditingContextDelegate.html
archived_at: '2026-07-15T08:11:38.846160Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOEditingContext.Delegate

> __(informal interface)__

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Interface Description

---

The [EOEditingContext.Delegate](#apple-inbecskejfdec) interface defines
methods that an EOEditingContext can invoke in its delegate. Delegates
are not required to provide implementations for all of the methods
in the interface, and you don't have to use the implements keyword
to specify that the object implements the Delegate interface. Instead,
declare and implement any subset of the methods declared in the interface that
you need, and use the EOEditingContext method [setDelegate](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponsxirdfnrswoylumu) method to assign your
object as the delegate. An editing context can determine if the
delegate doesn't implement a delegate method and only attempts
to invoke the methods the delegate actually implements.

## Method Types

---

> **Fetching objects**
> : [editingContextShouldFetchObjects](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcgmv2gg2cpmjvgky3uom)
>
> **Invalidating objects**
> : [editingContextShouldInvalidateObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcjnz3gc3djmrqxizkpmjvgky3u)
>
> **Saving changes**
> : [editingContextWillSaveChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiv3jnrwfgylwmvbwqylom5sxg)
>
> **Handling failures**
> : [editingContextShouldValidateChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcwmfwgszdborsug2dbnztwk4y)
> : [editingContextShouldPresentException](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcqojsxgzloorcxqy3fob2gs33o)
> : [editingContextShouldUndoUserActionsAfterFailure](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcvnzsg6vltmvzecy3unfxw442bmz2gk4sgmfuwy5lsmu)
>
> **Merging changes**
> : [editingContextShouldMergeChangesForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcnmvzgozkdnbqw4z3fondg64spmjvgky3u)
> : [editingContextDidMergeChanges](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hirdjmrgwk4thmvbwqylom5sxg)

## Instance Methods

---

### editingContextDidMergeChanges

`public abstract void editingContextDidMergeChanges(EOEditingContext anEditingContext)`

Invoked once after a batch of objects
has been updated in _anEditingContext_'s
parent object store (in response to an [ObjectsChangedInStoreNotification](EOEditingContext.md#apple-ijeuirceifbuu)).
A delegate might implement this method to define custom merging
behavior, most likely in conjunction with [editingContextShouldMergeChangesForObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcnmvzgozkdnbqw4z3fondg64spmjvgky3u).
It is safe for this method to make changes to the objects in the
editing context.

---

### editingContextShouldFetchObjects

`public abstract NSArray editingContextShouldFetchObjects(
EOEditingContext editingContext,
EOFetchSpecification fetchSpecification)`

Invoked from [objectsWithFetchSpecification](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpn5rguzldorzvo2lunbdgk5ddnbjxazldnftgsy3boruw63q).
If the delegate has appropriate results cached it can return them
and the fetch will be bypassed. Returning null causes the fetch
to be propagated to the parent object store.

---

### editingContextShouldInvalidateObject

`public abstract boolean editingContextShouldInvalidateObject(
EOEditingContext anEOEditingContext,
EOEnterpriseObject anObject,
EOGlobalID anEOGlobalID)`

Sent when an _object_ identified
by _globalID_ has been explicitly invalidated.
If the delegate returns false, the invalidation is refused. This
allows the delegate to selectively override object invalidations.

__See Also:__
[invalidateAllObjects](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnfxhmylmnfsgc5dfifwgyt3cnjswg5dt), [revert](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpojsxmzlsoq)

---

### editingContextShouldMergeChangesForObject

`public abstract boolean editingContextShouldMergeChangesForObject(
EOEditingContext anEditingContext,
EOEnterpriseObject object)`

When an [ObjectsChangedInStoreNotification](EOObjectStore.md#apple-infeirchijcug) is
received, _anEditingContext_ invokes
this method in its delegate once for each of the objects that has
both uncommitted changes and an update from the EOObjectStore. This
method is invoked before any updates actually occur.

If this method returns true, all of the uncommitted changes
should be merged into the object after the update is applied, in
effect preserving the uncommitted changes (the default behavior).
The delegate method [editingContextShouldInvalidateObject](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5djnztug33oorsxq5boirswyzlhmf2gkl3fmruxi2lom5bw63tumv4hiu3in52wyzcjnz3gc3djmrqxizkpmjvgky3u) will
not be sent for the object in question.

If this method returns false, no uncommitted changes are applied.
Thus, the object is updated to reflect the values from the database
exactly. This method should not make any changes to the object since
it is about to be invalidated.

If you want to provide custom merging behavior, you need to
implement both this method and `editingContextDidMergeChanges`.
You use `editingContextShouldMergeChangesForObject` to
save information about each changed object and return true to allow
merging to continue. After the default merging behavior occurs, `editingContextDidMergeChanges` is
invoked, at which point you implement your custom behavior.

---

### editingContextShouldPresentException

`public abstract boolean editingContextShouldPresentException(
EOEditingContext anEditingContext,
Throwable exception)`

Sent whenever an exception is caught by an EOEditingContext.
If the delegate returns false, _exception_ is
ignored. Otherwise (if the delegate returns true, if the editing
context doesn't have a delegate, or if the delegate doesn't
implement this method) _exception_ is
passed to the message handler for further processing,

__See Also:__
[messageHandler](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpnvsxg43bm5suqylomrwgk4q)

---

### editingContextShouldUndoUserActionsAfterFailure

`public abstract boolean editingContextShouldUndoUserActionsAfterFailure(EOEditingContext anEditingContext)`

Sent when a validation error occurs while
processing a [processRecentChanges](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bpobzg6y3fonzvezldmvxhiq3imfxgozlt) message.
If the delegate returns false, it disables the automatic undoing
of user actions after validation has resulted in an error.

By default, if a user attempts to perform an action that results
in a validation failure (such as deleting a department object that
has a delete rule stating that the department can't be deleted
if it contains employees), the user's action is immediately rolled
back. However, if this delegate method returns false, the user action
is allowed to stand (though attempting to save the changes to the
database without solving the validation error will still result
in a failure). Returning false gives the user an opportunity to
correct the validation problem so that the operation can proceed
(for example, the user might delete all of the department's employees
so that the department itself can be deleted).

---

### editingContextShouldValidateChanges

`public abstract boolean editingContextShouldValidateChanges(EOEditingContext anEditingContext)`

Sent when an EOEditingContext receives a [saveChanges](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom) message. If the delegate
returns false, changes are saved without first performing validation.
This method can be useful if the delegate wants to provide its own
validation mechanism.

---

### editingContextWillSaveChanges

`public abstract void editingContextWillSaveChanges(EOEditingContext editingContext)`

Sent when an EOEditingContext receives a [saveChanges](EOEditingContext.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivsgs5djnztug33oorsxq5bponqxmzkdnbqw4z3fom) message. The delegate
can throw an exception to abort the save operation.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
