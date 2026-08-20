---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/WorkingWithNested.html
archived_at: '2026-07-15T08:01:37.166253Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Using Nested Editing Contexts

##  Synopsis

Describes how to use nested editing contexts as a working area for complex edit screens.

##  Discussion

EOEditingContexts can be viewed as working areas into which objects are fetched and modified. By default, every session is given its own _defaultEditingContext_
as a means of separating different user's objects.

When changes are made to objects within an editing context, the editing context tracks the changes for future saving. When the editing context sends the message _saveChanges_
, it hands off the changes to its parent EOObjectStore. Normally, the parent is the EOObjectStoreCoordinator which in turn hands off the changes to the appropriate EODatabaseContext for each entity. The EODatabaseContext then saves the changes to the database.

Since an EOEditingContext is itself an EOObjectStore, you can nest EOEditingContexts, thereby making different levels of working areas that can _saveChanges_
to its parent level. With a little bit of effort, this feature of EOF can be used within WebObjects applications to provide scratch areas where users can make changes, submit forms, update EOs, submit more forms, and then decide if all the changes should be saved to the session's _defaultEditingContext_
or completely forgotten.

This more complicated approach to editing is necessary because the Web permits users to edit on a special edit page and, without saving or canceling, hyperlink directly to another page, leaving the _defaultEditingContext_
with incomplete or inconsistent EOs. This action can be disastrous unless care is taken to prevent the partial or undesired changes from being saved by accident.

To better illustrate this issue, assume you create a special object edit page that uses multiple Submit buttons to switch between sections of data to be edited. Also, assume that the WOTextfields, WOPopuplists, and so on, are bound directly to the object via key paths. As soon as you edit the data on the first section, and switch to see the data on a different section, the object will be changed to reflect any changes you made in the first section. Assume further that the user clicks a hyperlink in a different frame and jumps to a completely different screen. The user subsequently edits another object and finishes by selecting the Save button. The changes from the first edit screen will alsobe applied to the database! This is undesirable because the user never acknowledged a save for those changes.

There are two possible workarounds for this problem.

1. Create a temporary instance variable for every data element that might be changed. Initialize the temporary variables upon entering the edit page. Update the real variables only during the actual _saveChanges_
action.

2. Create a nested EOEditingContext and fault in the object to be edited. The relationships will automatically be faulted into this temporary nested work area as needed. Bind the new editing instance of the object directly to the page's components. When _saveChanges_
is invoked on the temporary EOEditingContext, the changes will be applied to the session's _defaultEditingContext_
. To apply them to the database, you can invoke _saveChanges_
to the session's _defaultEditingContext_
, after which you can destroy the object and the temporary EOEditingContext.

We discuss the second approach. The techniques presented here can be used to build a reusable framework that manages the nested editing contexts without doubly-nesting them.

####  Creating the Nested EOEditingContext

The following code creates a nested editing context.

#####  Figure 1. Java Code

```
EOEditingContext ec=session().defaultEditingContext();
```



```
EOEditingContext nestedEditingContext=new EOEditingContext(ec);
```


#####  Figure 2. Objective-C Code

```
EOEditingContext *ec=[[self session] defaultEditingContext];
```



```
EOEditingContext *nestedEditingContext=[[EOEditingContext alloc] initWithParentObjectStore:ec];
```


####  Faulting the Original EO into the Nested EOEditingContext

Using the new convenience API from EOUtilities

#####  Figure 3. Java Code

```
EOEnterpriseObject editingObject=(EOEnterpriseObject) EOUtilities.localInstanceOfObject (nestedEditingContext, objectToEdit);
```


Using the standard API

#####  Figure 4. Java Code

```
EOGlobalID gid=objectToEdit.editingContext().globalIDForObject(objectToEdit);
```



```
EOEnterpriseObject editingObject=nestedEditingContext.faultForGlobalID(gid, nestedEditingContext);
```


Using the new convenience API from EOUtilities

#####  Figure 5. Objective-C Code

```
id editingObject=[nestedEditingContext localInstanceOfObject: objectToEdit];
```


Using the standard API

#####  Figure 6. Objective-C Code

```
gid=[[objectToEdit editingContext] globalIDForObject: objectToEdit];
```



```
id editingObject=[nestedEditingContext faultForGlobalID: gid editingContext: nestedEditingContext];
```


####  Saving All the Changes to the Database

The following code saves the changes to a nested editing context.

#####  Figure 7. Java Code

```
try {
```



```
     nestedEditingContext.saveChanges();
```



```
     session().defaultEditingContext().saveChanges();
```



```
}
```



```
catch (EOValidationException e) { // handle save error
```



```

```


#####  Figure 8. Objective-C Code

```
NS_DURING
```



```
     [ nestedEditingContext saveChanges];
```



```
     [[[self session] defaultEditingContext] saveChanges];
```



```
NS_HANDLER // handle save error and the exception in variable localException
```



```
NS_ENDHANDLER
```


#####  Figure 9. WebScript Code

```
NSException *e=[nestedEditingContext tryToSaveChanges];
```



```
     if  (!e)
```



```
     e=[[[self session] defaultEditingContext] saveChanges];
```



```
     if (e) {
```



```
     // handle save error and the exception in variable e
```



```
}
```


####  Issues to Consider

You should consider the following issues:

· You need to ensure that the nested EOEditingContexts are retained.

· You probably want to keep track of the nested EOEditingContexts so that you can eventually free them. The session might be a good place to store these references.

· You might want to keep track of the editing page for a given nested EOEditingContext so that you can jump back to that page if the user jumps off the edit page, and then requests to edit the same original object.

· You might want to restrict the user by only allowing one editable object at a time. You can present the user with an AlertPanel page that asks if the user wants to abort a previous unfinished edit, jump back to an unfinished edit, or cancel attempting to edit a second object.

· Care must be taken to avoid creating a doubly-nested EOEditingContext. You must ensure that the object you will edit is within the session's _defaultEditingContext_
.

· Remember that the EOEditingContext does not retain its objects (unless
_instancesRetainAllObjects_
is YES, i.e., when you're writing in Java). Instead, it listens for deallocation notifications and automatically removes the object from the editing context. Therefore, it is important to ensure that the object being edited is retained by something for the life of the nested editing context.

##  See Also

· EOEditingContext

· EOObjectStore

· EOObjectStoreCoordinator

· EOUtilities

##  Questions

· How do I safely edit an object and not worry if the user forgets to revert undesired changes?

· How do I use the nested EOEditingContexts to aid in complex WOF edit screens?

· How do I copy an object from a parent EOEditingContext into a nested EOEditingContext?

##  Keywords

· Faulting

· Nested

· EOEditingContext

· Complex Edit Screens

· EOGlobalID

· EOUtilities

##  Revision History

24 July, 1998. David Scheck. First Draft.
18 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
