---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/Concepts/HowDoBindingsWork.html
archived_at: '2026-07-15T07:12:02.508241Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cocoa Bindings Programming Topics](Introduction%20to%20Cocoa%20Bindings%20Programming%20Topics.md)


[Next](Providing%20Controller%20Content.md)[Previous](What%20Are%20Cocoa%20Bindings.md)

# How Do Bindings Work?

This article provides a conceptual explanation of how Cocoa bindings work. It describes:

- How connections between model and controller, and controller and view, are established using key-value binding
- Unbinding
- The NSEditor and NSEditorRegistration protocols
- The technologies that Cocoa bindings use to support communication between the model, view, and controller, namely key-value coding, and key-value observing
- How the various technologies interact

You should already be familiar with the concepts presented in [What Are Cocoa Bindings?](What%20Are%20Cocoa%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3telkdjjbeksscjbea).

This section presents an overview of the technologies that make Cocoa bindings work and how they interact. They are discussed in greater detail in the following sections.

Cocoa bindings rely on other technologies—key-value coding (KVC) and key-value observing (KVO)—to communicate changes between objects, and on key-value binding (KVB) to bind a value in one object to a property in another. Cocoa bindings also use two protocols—NSEditor and NSEditorRegistration—that help to ensure that any pending edits are either discarded or committed before user interface elements are disposed of.

To understand how these technologies work together, consider a drawing application that allows the user to draw graphic objects such as circles and rectangles on screen. Among other properties, a graphic object has a shadow that may be offset a variable distance from the center of the graphic at an arbitrary angle. An inspector displays the offset and angle of the selected graphic object’s shadow in a pair of text fields and a custom view—a joystick—as shown in Figure 1.

__Figure 1__  Example drawing application

!

The implementation of the inspector is illustrated in Figure 2. Both the text fields and the joystick are bound to the `selection` of an NSArrayController. The controller’s `contentArray` is bound to an array of Graphic objects. A Graphic has instance variables to represent its shadow’s angle in radians and its offset from its center.

__Figure 2__  Bindings for example graphics application

!

The text fields’ values are bound to the angle and offset of the graphic object’s shadow; the joystick provides a graphical representation of angle and offset. The angle in the text field is displayed in degrees, and the angle used internally by the joystick is specified in radians. The bindings for both of these specify a reversible value transformer that converts between radians and degrees.

The complete sequence of events that occurs when a user edits a value in the angle text field is illustrated in [Figure 3](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tgljsgaytaobwfvbecssjircueri).

__Figure 3__  The complete edit cycle

!

1. The user enters a new value in the Angle text field. The text field uses the NSEditorRegistration protocol to indicate that an edit has begun, and when it is complete. The text field’s binding specifies a reversible radians-to-degrees value transformer, so the new value is converted to radians.
2. Using KVC, through the controller the view updates the model object’s `shadowAngle` variable.
3. Through KVO, the model informs the controller that an update has been made to its `shadowAngle` variable.
4. Through KVO, the controller informs the joystick and the angle text field that an update has been made to its content’s `shadowAngle` variable.

Notice that the Offset text field was not involved in the cycle in any way. Cocoa bindings impose no more overhead than is necessary.

The next sections explain in greater detail how bindings are established and how the underlying technologies operate.

This section first describes the technologies that support bindings and shows how they play their parts. It also explains what steps you must take in order to take advantage of these technologies.

Key-value binding is used to establish bindings. The NSKeyValueBindingCreation informal protocol declares methods to establish and remove bindings between objects. In addition, it provides a means for a class to advertise the bindings that it exposes.

In most cases you need to use `bind:toObject:withKeyPath:options:`, and then only when you establish bindings programatically. Use of the `unbind:` is discussed in Unbinding. The other methods—the class method `exposeBinding:` and the instance methods `exposedBindings` and `valueClassForBinding:`—are useful only in an Interface Builder palette.

Together the NSEditorRegistration and NSEditor protocols allow views to notify a controller that an edit is underway and to ensure that any pending edits are committed as and when necessary.

The NSEditorRegistration informal protocol is implemented by controllers to provide an interface for a view—the editor—to inform the controller when it has uncommitted changes. When an edit is initiated, the view sends the controller an `objectDidBeginEditing:` message. When the edit is complete (for example when the user presses Return) the view sends an `objectDidEndEditing:` message.

The controller is responsible for tracking which editors have uncommitted changes and requesting that they commit or discard any pending edits when appropriate—for example, if the user closes the window or quits the application. The request takes the form of a `commitEditing` or `discardEditing` message, defined by the NSEditor informal protocol. NSController provides an implementation of this protocol, as do the Application Kit user interface elements that support binding.

Key-value coding (KVC) provides a unified way to access an object’s properties by name (key) without requiring use of custom accessor methods. The NSKeyValueCoding protocol specifies among others two methods, `valueForKey:` and `setValue:forKey:`, that give access to an object’s property with a specified name. In addition, the methods `setValue:forKeyPath:` and `valueForKeyPath:` give access to properties across relationships using key paths of the form _relationship.property_, for example, `content.lastName`.

A binding for a given property specifies an object and a key path to a property of that object. Given this information, the bound object can use key-value coding—specifically `setValue:forKeyPath:`—to update the object to which it is bound without having to hard-code an accessor method, as illustrated in Figure 4.

__Figure 4__  Key-value coding in Cocoa bindings

!!

Since Cocoa bindings rely on KVC, your model and controller objects must be KVC-compliant for other objects to be able to bind to them. To support KVC you simply have to follow a set of conventions for naming your accessor methods, briefly summarized here:

- For an attribute or to-one relationship named `<key>`, implement methods named `<key>` and, if the attribute is read-write, `set<Key>`:—the case is important.
- For a to-many relationship implement either a method named `<key>` or both `countOf<Key>` and `objectIn<Key>AtIndex:`. The latter pair is useful if the related objects are not stored in an array. It is up to you to retrieve an appropriate value for the specified index—it does not matter how the value is derived. For a mutable to-many relationship, you should also implement either `set<Key>` (if you implemented `<key>`) or `insertObject:in<Key>AtIndex:` and `removeObjectFrom<Key>AtIndex:`.

For full details of all the methods declared by the NSKeyValueCoding protocol, see _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_.

KVO is a mechanism that allows an object to register to receive notifications of changes to values in other objects. To register, an observer sends the object it wants to observe an `addObserver:forKeyPath:options:context:` message that specifies:

- The object that is observing (very often `self`)
- The key path to observe (for example, `selection.name`)
- What information will be sent on notification (for example, old value and new value)
- Optionally, contextual information to be sent back on notification (for example, a flag to indicate what binding is being affected)

An observed object communicates changes directly to observers by sending them an `observeValueForKeyPath:ofObject:change:context:` message (defined by the NSKeyValueObserving informal protocol)—there is no independent notifier object akin to NSNotificationCenter. Figure 5 illustrates how a change to a model value (the shadow angle) is communicated to views using KVO.

__Figure 5__  Key-value observing in Cocoa bindings

!!

The message is sent to observers for every change to an observed property, independently of how the change was triggered. (Note that the protocol itself makes no assumptions about what the observer actually does with the information.)

One other important aspect of KVO is that you can register the value of a key as being dependent on the value of one or more others. A change in the value associated with one of the “master” keys triggers a change notification for the dependent key’s value. For example, the drawing bounds of a graphic object may be dependent on the offset and angle of the associated shadow. If either of those values changes, any objects observing the drawing bounds must be notified.

The main requirement to make use of KVO is that your model objects be KVO-compliant. In most cases this actually requires no effort—the runtime system adds support automatically. By default, all invocations of KVC methods result in observer notifications. You can also implement manual support—see _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_ for more details.

Typically the only reason you would explicitly unbind an object is if you modify the user interface programatically and want to remove a binding. If you change an objects binding’s values it should first clear any preexisting values.

If you implement a custom view or controller with custom bindings, you should ensure that it clears any bindings before it is deallocated—in particular it should release any objects that were retained for the specified binding in the `bind:toObject:withKeyPath:options:` method and should deregister as an observer of any objects for which it registered as an observer. It may be convenient to implement this logic in an `unbind:` method that you then call as the first step in `dealloc`.

This section examines bindings in more detail. It decomposes—from the perspective of a custom view, a joystick—what happens when a binding is established. This serves two purposes: it makes explicit what code is involved in establishing a binding and responding to changes, and it gives a conceptual overview of how to create your own bindings-enabled views.

A binding specifies what aspect of one object should be bound to what property in another, such that a change in either is reflected in the other. For a given binding, an object therefore records the target object for the binding, the associated key path, and any options that were specified.

You can establish bindings easily in Interface Builder using the Bindings pane of the Info window. In Interface Builder, the `angle` binding for a joystick that displays the offset and angle of graphics object’s shadow might look like Figure 6.

__Figure 6__  Bindings for a joystick’s angle in Interface Builder

!

Establishing this binding in Interface Builder is equivalent to programatically sending this message to the joystick:

```
[joystick bind:@"angle" toObject:GraphicController withKeyPath:@"selection.shadowAngle" options:options];
```

The arguments have the following meanings:

__`@"angle"`__: Identifies an attribute whose value can be bound to the value of a property in another object. Note that the binding name need not necessarily correspond to the name of an actual instance variable.

__`GraphicController`__: The object containing the bound-to property.

__`@"selection.shadowAngle"`__: The key path that identifies the bound-to property.

__`options`__: A dictionary that specifies any options such as placeholders, or in this case, a value transformer.

The information defined by the arguments can be stored in the bound object (in this case the joystick) as instance variables, as discussed next.

This example, and those that follow, assume that the joystick is represented by the class Joystick with instance variables as defined in the interface shown in Listing 1.

__Listing 1__  Interface for the Joystick class

```objc
@interface Joystick : NSView
{
    float angle;
    id observedObjectForAngle;
    NSString *observedKeyPathForAngle;
    NSValueTransformer *angleValueTransformer;
    // ...
}
```

In its `bind:toObject:withKeyPath:options:` method an object must as a minimum do the following:

- Determine which binding is being set
- Record what object it is being bound to using what keypath and with what options
- Register as an observer of the keypath of the object to which it is bound so that it receives notification of changes

The code sample in Listing 2 shows a partial implementation of Joystick’s `bind:toObject:withKeyPath:options:` method dealing with just the `angle` binding.

__Listing 2__  Partial implementation of the bind:toObject:withKeyPath:options method for the Joystick class

```objc
static void *AngleBindingContext = (void *)@"JoystickAngle";

- (void)bind:(NSString *)binding
 toObject:(id)observableObject
 withKeyPath:(NSString *)keyPath
 options:(NSDictionary *)options
{
 // Observe the observableObject for changes -- note, pass binding identifier
 // as the context, so you get that back in observeValueForKeyPath:...
 // This way you can easily determine what needs to be updated.

if ([binding isEqualToString:@"angle"])
 {
    [observableObject addObserver:self
                   forKeyPath:keyPath
                  options:0
                  context:AngleBindingContext];

    // Register what object and what keypath are
    // associated with this binding
    observedObjectForAngle = [observableObject retain];
    observedKeyPathForAngle = [keyPath copy];

    // Record the value transformer, if there is one
    angleValueTransformer = nil;
    NSString *vtName = [options objectForKey:@"NSValueTransformerName"];
    if (vtName != nil)
    {
        angleValueTransformer = [NSValueTransformer
            valueTransformerForName:vtName];
    }
 }
 // Implementation continues...
```

This partial implementation does not record binding options other than a value transformer (although it may simply be that the binding does not allow for them). It nevertheless illustrates the basic principles of establishing a binding. Notice in particular the contextual information passed in the `addObserver:forKeyPath:options:context:` message; this is returned in the `observeValueForKeyPath:ofObject:change:context:` method and can be used to determine which binding is affected by the value update.

As noted earlier, there are two aspects to change management—responding to view-initiated changes that must be propagated ultimately to the model, and responding to model-initiated changes that must be reflected in the view. This section illustrates both, and shows how KVC and KVO play their parts.

Recall that the joystick was bound to the controller with the following method:

```
[joystick bind:@"angle" toObject:GraphicController withKeyPath:@"selection.shadowAngle" options:options];
```

From the perspective of view-initiated updates the method can be interpreted as follows:

__`bind: @"angle"`__: If whatever is associated with `angle` changes,

__`toObject: GraphicController`__: tell the specified object (GraphicController) that

__`withKeyPath: @"selection.shadowAngle"`__: the value of its (the GraphicController’s) `selection.shadowAngle` has changed

__`options: options`__: using any of these options that may be appropriate.

If the value associated with `angle` changes—typically when a user clicks or drags the mouse within the view—the joystick should pass the new value to the controller using KVC, as illustrated in Figure 4. The joystick should therefore respond to user input as follows:

- Determine new values for angle and offset
- Update its own display as appropriate
- Communicate new values to the controller to which it is bound

Listing 3 shows a partial implementation of an update method for the Joystick class. The excerpt deals just with the `angle` binding. It illustrates the use of key-value coding to communicate the new value (transformed by the value transformer if appropriate) to the observed object.

__Listing 3__  Update method for the Joystick class

```objc
-(void)updateForMouseEvent:(NSEvent *)event
{
    float newAngleDegrees;
    // calculate newAngleDegrees...

    [self setAngle:newAngleDegrees];

    if (observedObjectForAngle != nil)
    {
        NSNumber *newControllerAngle = nil;

        if (angleValueTransformer != nil)
        {
            newControllerAngle =
                [angleValueTransformer reverseTransformedValue:
                    [NSNumber numberWithFloat:newAngleDegrees]];
        }
        else
        {
            newControllerAngle = [NSNumber numberWithFloat:newAngleDegrees];
        }
        [observedObjectForAngle setValue: newControllerAngle
                  forKeyPath: observedKeyPathForAngle];
    }
    // ...
}
```

Note that this example omits several important details, such as editor registration and checking that the value transformer allows reverse transformations.

Recall again that the joystick was bound to the controller with the following method:

```
[joystick bind:@"angle" toObject:GraphicController withKeyPath:@"selection.shadowAngle" options:options];
```

From the perspective of model-initiated updates the method can be interpreted as follows:

__`toObject: GraphicController`__: If the GraphicController’s

__`withKeyPath:@"selection.shadowAngle"`__: `selection.shadowAngle` changes

__`bind:@"angle"`__: update whatever is associated with the exposed `angle` key

__`options:options`__: using the options specified (for example, using a value transformer).

The receiver therefore registered as an observer of the specified object’s key path (`selection.shadowAngle`) in its `bind:toObject:withKeyPath:options:` method, as was shown in Listing 2. Observed objects notify their observers by sending them an `observeValueForKeyPath:ofObject:change:context:` message. Listing 4 shows a partial implementation for the Joystick class for handling the observer notifications that result.

The fundamental requirement of the `observeValueForKeyPath:ofObject:change:context:` method is that the value associated with the relevant attribute is updated. This excerpt also shows how it can capture placeholder information that might be used in the display method to give visual feedback to the user, in this case using an instance variable that indicates that for some reason the angle is “bad.”

__Listing 4__  Observing method for the Joystick class

```objc
- (void)observeValueForKeyPath:(NSString *)keyPath
              ofObject:(id)object
            change:(NSDictionary *)change
               context:(void *)context
{
    // You passed the binding identifier as the context when registering
    // as an observer--use that to decide what to update...

    if (context == AngleObservationContext)
    {
        id newAngle = [observedObjectForAngle
            valueForKeyPath:observedKeyPathForAngle];
        if ((newAngle == NSNoSelectionMarker) ||
            (newAngle == NSNotApplicableMarker) ||
            (newAngle == NSMultipleValuesMarker))
        {
            badSelectionForAngle = YES;
        }
        else
        {
            badSelectionForAngle = NO;
            if (angleValueTransformer != nil)
            {
                newAngle = [angleValueTransformer
                    transformedValue:newAngle];
            }
            [self setValue:newAngle forKey:@"angle"];
        }
    }
    // ...

    [self setNeedsDisplay:YES];
}
```

In most controls the display method alters the visual representation depending on the current selection.

[Next](Providing%20Controller%20Content.md)[Previous](What%20Are%20Cocoa%20Bindings.md)

