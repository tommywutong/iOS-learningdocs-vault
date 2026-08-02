---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/Troubleshooting.html
archived_at: '2026-07-15T07:12:08.496677Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Document%20Revision%20History.md)[Previous](Controller%20Key-Value%20Observing%20Compliance.md)

# Troubleshooting Cocoa Bindings

Applications that use Cocoa bindings can provide a challenge when attempting to troubleshoot problems. This article outlines some of the common issues encountered in applications that use Cocoa bindings and provides clues as to correcting the problem.

This is typically due to your application modifying the collection content in a manner that is not key-value-observing compliant. Modifying an array using `addObject:` or `removeObject:` is not sufficient.

You must either implement the indexed accessors for the collection key in your model class, or ask the model for a key-value-observing aware collection proxy using one of the following methods:

```objc
- (NSMutableArray *)mutableArrayValueForKey:(NSString *)key
- (NSMutableArray *)mutableArrayValueForKeyPath:(NSString *)keyPath

- (NSMutableSet *)mutableSetValueForKey:(NSString *)key
- (NSMutableSet *)mutableSetValueForKeyPath:(NSString *)keyPath
```

These return collection proxy objects that you can then use with the NSMutableArray or NSMutableSet mutation methods, and the appropriate key-value observing notifications are sent.

You can also modify the contents through the collection controller using the methods described in [Programmatically Modifying a Controller’s Contents](Providing%20Controller%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbxfuytqmzsha2q).

If you change the value of an item in the user interface programmatically, for example sending an NSTextField a `setStringValue:` message, the model is not updated with the new value.

This is the expected behavior. Instead you should change the model object using a key-value-observing compliant manner.

If changes made to a model value programmatically are not being reflected in the user interface, this typically indicates that the model object is not key-value-observing compliant for the property, or that you are modifying the value in a manner that is bypassing key-value observing. You should ensure that:

- The model class has automatic key-value observing enabled or implements manual key-value observing for the property.
- That you are changing the value using an accessor method, or using a key-value-coding compliant method. Changing the value of an instance variable directly does not provide key-value observing change notifications.
- If your model property is a collection, that you're modifying the content in a key-value-observing compliant manner. See [My collection controller isn’t displaying the current data](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbyfuytqmryga4q) for more information.

A common source of problems when using bindings is that a binding is established to the wrong key path. It is easy to miss the debug messages in the run log or console when the application doesn’t behave as expected.

The following is an example of a debug message that is output to the run log or console:

```
2005-05-10 03:53:29.764 VuesActivity[2216] *** NSRunLoop ignoring exception '[<Member 0x379180> valueForUndefinedKey:]:
this class is not key value coding-compliant for the key named.' that raised during posting of delayed perform
with target 37f6d0 and selector 'invokeWithTarget:'
```

This message indicates that the instance of the Member class is not key-value-coding compliant for the key "named". In this case the error is that the correct Member key is in fact "name".

You can get more information about an error by setting the bindings debug level default. This can be done on the command line as follows:

```
defaults write com.yourdomain.yourapplication NSBindingDebugLogLevel 1
```

You can also set the debugging level in Xcode:

1. Select the application executable in the Executables group.
2. Choose the Get Info menu item in the File menu.
3. Select the Arguments tab in the executables info panel.
4. Add `-NSBindingDebugLogLevel 1` to the “Arguments to be passed at launch” list.

After setting the debug level default, the same problem that generated the above error message now generates the following error:

```
2005-05-10 04:02:32.146 VuesActivity[2241] Cocoa Bindings: Error accessing value for key path selection.named
of object <NSArrayController: 0x349ba0>[object class: Member, number of selected objects: 1]
(from bound object <NSTextField: 0x344380>): [<Member 0x37a660> valueForUndefinedKey:]: this class
is not key value coding-compliant for the key named.
```

This provides more information that can aid you in tracking down which item in Interface Builder has been bound to the wrong key path. In this case it indicates that the binding is between an NSTextField and an NSArrayController with an object class of Member, using the `selection.named` key path.

With the binding debug level set to 1, any binding made to a non-existent key will cause a debug message to be printed to the console, even if the binding has disabled the “Raises For Not Applicable Keys” option.

Currently only a debug level of 1 is supported.

If you implement a subclass of NSView and create an Interface Builder palette for that subclass, your subclass’ implementation of `bind:toObject:withKeyPath:options:` must call the super implementation. If you don’t when you establish a binding in Interface Builder, the binding values disappear and the binding names become disabled and uneditable.

If you disable editing for an NSTextField in Interface Builder, and then establish a binding to it, you may find that the field then becomes editable when your application is running. This is typically due to the value binding having the “Conditionally Sets Editable” binding option enabled.

Similarly, if a control becomes hidden or enabled, you should check that the “Conditionally Sets Hidden” and “Conditionally Sets Enabled” options of the value binding have the expected settings.

Key-value coding handles the conversion of NSNumbers and NSValues to some well-known scalar and structure types, but unsigned int is not currently supported. In the context of bindings, you should consider transforming the value using an NSValueTransformer, or in the specific case of NSTextField, NSFormatter.

This is often caused because the NSTreeController’s children key path has not been set. You can verify that this is the cause by checking the console or run log for debug messages. See [Traversing Tree Content with an NSTreeController](Providing%20Controller%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbxfuytqnjqgqyq) for more information.

```
2005-06-23 02:46:53.198 MyApplication[6777] Cocoa Bindings: Cannot perform operation if childrenKeyPath is nil.
```


Tableview columns that contain NSPopUpButtonCell, or any cell type other than NSTextField can’t be sorted if the cell’s selection is bound using the `selectedObject` or `selectedObjects` bindings. If the selection is bound to selectedValue, selectedTag or selectedIndex, the column is sortable.

[Next](Document%20Revision%20History.md)[Previous](Controller%20Key-Value%20Observing%20Compliance.md)

