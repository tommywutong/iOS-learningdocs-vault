---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Protocols/EOEditingContextDelegate.html
archived_at: '2026-07-15T08:11:42.907598Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md) 

# EOEditingContext Delegate

> __(informal protocol)__

> __Declared in:__ : EOControl/EOEditingContext.h

---

## Protocol Description

---

The [EOEditingContext Delegate](#apple-inbecskejfdec) informal
protocol defines methods that an EOEditingContext can invoke in
its delegate. Delegates are not required to provide implementations
for all of the methods in the informal protocol. Instead, declare
and implement any subset of the methods declared in the informal
protocol that you need, and use the EOEditingContext method [setDelegate:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmv2eizlmmvtwc5dfhi) method to assign your
object as the delegate. An editing context can determine if the
delegate doesn't implement a delegate method and only attempts
to invoke the methods the delegate actually implements.

## Method Types

---

> **Fetching objects**
> : [- editingContext:shouldFetchObjectsDescribedByFetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcgmv2gg2cpmjvgky3uoncgk43dojuwezleij4umzlumnufg4dfmnuwm2ldmf2gs33ohi)
>
> **Invalidating objects**
> : [- editingContext:shouldInvalidateObject:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcjnz3gc3djmrqxizkpmjvgky3uhjtwy33cmfwesrb2)
>
> **Saving changes**
> : [- editingContextWillSaveChanges:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2fo2lmnrjwc5tfinugc3thmvztu)
>
> **Handling failures**
> : [- editingContextShouldValidateChanges:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2fg2dpovwgivtbnruwiylumvbwqylom5sxgoq)
> : [- editingContext:shouldPresentException:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcqojsxgzloorcxqy3fob2gs33ohi)
> : [- editingContextShouldUndoUserActionsAfterFailure:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2fg2dpovwgivlomrxvk43fojawg5djn5xhgqlgorsxertbnfwhk4tfhi)
>
> **Merging changes**
> : [- editingContext:shouldMergeChangesForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcnmvzgozkdnbqw4z3fondg64spmjvgky3uhi)
> : [- editingContextDidMergeChanges:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2ei2lejvsxez3finugc3thmvztu)

## Instance Methods

---

### editingContextDidMergeChanges:

`- (void)editingContextDidMergeChanges:(EOEditingContext
*)anEditingContext`

Invoked once after a batch of objects
has been updated in _anEditingContext_'s
parent object store (in response to an [EOObjectsChangedInStoreNotification](EOEditingContext-2.md#apple-ijeuirceifbuu)).
A delegate might implement this method to define custom merging
behavior, most likely in conjunction with [editingContext:shouldMergeChangesForObject:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcnmvzgozkdnbqw4z3fondg64spmjvgky3uhi).
It is safe for this method to make changes to the objects in the
editing context.

---

### editingContext:shouldFetchObjectsDescribedByFetchSpecification:

`- (NSArray *)editingContext:(EOEditingContext
*)editingContext
shouldFetchObjectsDescribedByFetchSpecification:(EOFetchSpecification
*)fetchSpecification`

Invoked from [objectsWithFetchSpecification:editingContext:](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3pmjvgky3uonlws5diizsxiy3iknygky3jmzuwgylunfxw4otfmruxi2lom5bw63tumv4hioq).
If the delegate has appropriate results cached it can return them
and the fetch will be bypassed. Returning nil causes the fetch to
be propagated to the parent object store.

---

### editingContext:shouldInvalidateObject:globalID:

`- (BOOL)editingContext:(EOEditingContext
*)anEditingContext
shouldInvalidateObject:(id)object
globalID:(EOGlobalID *)globalID`

Sent when an _object_ identified
by _globalID_ has been explicitly invalidated.
If the delegate returns NO, the invalidation is refused. This allows
the delegate to selectively override object invalidations.

__See Also:__
[- invalidateAllObjects](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3jnz3gc3djmrqxizkbnrwe6ytkmvrxi4y), [- revert](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3smv3gk4tu)

---

### editingContext:shouldMergeChangesForObject:

`- (BOOL)editingContext:(EOEditingContext
*)anEditingContext
shouldMergeChangesForObject:(id)object`

When an [EOObjectsChangedInStoreNotification](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOObjectStore.html#CJDDGBEC) is
received, _anEditingContext_ invokes
this method in its delegate once for each of the objects that has
both uncommitted changes and an update from the EOObjectStore. This
method is invoked before any updates actually occur.

If this method returns YES, all of the uncommitted changes
should be merged into the object after the update is applied, in
effect preserving the uncommitted changes (the default behavior).
The delegate method [editingContext:shouldInvalidateObject:globalID:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fmruxi2lom5bw63tumv4hiicemvwgkz3borss6zlenf2gs3thinxw45dfpb2du43in52wyzcjnz3gc3djmrqxizkpmjvgky3uhjtwy33cmfwesrb2) will
not be sent for the object in question.

If this method returns NO, no uncommitted changes are applied.
Thus, the object is updated to reflect the values from the database
exactly. This method should not make any changes to the object since
it is about to be invalidated.

If you want to provide custom merging behavior, you need to
implement both this method and __editingContextDidMergeChanges:__.
You use __editingContext:shouldMergeChangesForObject:__ to
save information about each changed object and return YES to allow
merging to continue. After the default merging behavior occurs, __editingContextDidMergeChanges:__ is
invoked, at which point you implement your custom behavior.

---

### editingContext:shouldPresentException:

`- (BOOL)editingContext:(EOEditingContext
*)anEditingContext
shouldPresentException:(NSException
*)exception`

Sent whenever an exception is caught by an EOEditingContext.
If the delegate returns NO, _exception_ is ignored.
Otherwise (if the delegate returns YES, if the editing context doesn't
have a delegate, or if the delegate doesn't implement this method) _exception_ is
passed to the message handler for further processing,

__See Also:__
[- messageHandler](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3nmvzxgylhmvegc3tenrsxe)

---

### editingContextShouldUndoUserActionsAfterFailure:

`- (BOOL)editingContextShouldUndoUserActionsAfterFailure:(EOEditingContext
*)anEditingContext`

Sent when a validation error occurs while
processing a [processRecentChanges](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3qojxwgzltonjgky3fnz2eg2dbnztwk4y) message.
If the delegate returns NO, it disables the automatic undoing of
user actions after validation has resulted in an error.

By default, if a user attempts to perform an action that results
in a validation failure (such as deleting a department object that
has a delete rule stating that the department can't be deleted
if it contains employees), the user's action is immediately rolled
back. However, if this delegate method returns NO, the user action
is allowed to stand (though attempting to save the changes to the
database without solving the validation error will still result
in a failure). Returning NO gives the user an opportunity to correct
the validation problem so that the operation can proceed (for example,
the user might delete all of the department's employees so that
the department itself can be deleted).

---

### editingContextShouldValidateChanges:

`- (BOOL)editingContextShouldValidateChanges:(EOEditingContext
*)anEditingContext`

Sent when an EOEditingContext receives a [saveChanges](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt) message. If the delegate
returns NO, changes are saved without first performing validation.
This method can be useful if the delegate wants to provide its own
validation mechanism.

---

### editingContextWillSaveChanges:

`- (void)editingContextWillSaveChanges:(EOEditingContext
*)editingContext`

Sent when an EOEditingContext receives a [saveChanges](EOEditingContext-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fmruxi2lom5bw63tumv4hil3tmf3gkq3imfxgozlt) message. The delegate
can raise an exception to abort the save operation.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
