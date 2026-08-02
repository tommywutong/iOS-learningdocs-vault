---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/ObjC_classic/Classes/More/EOAssociation.html
archived_at: '2026-07-15T08:11:45.653274Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOInterface Reference

[![Table of Contents](attachments/images/up.gif)](../../EOInterfaceTOC.md)

# EOAssociation

## How EOAssociations Work

An EOAssociation monitors its display object for user input
or other events while also observing changes in the selection or
contents of its EODisplayGroups. The basic purpose of an EOAssociation
is to assure that changes at one end are reflected on the other.
When the selection in a display group changes, for example, the
association updates the state of its display object to reflect this
new selection. The following sections describe this process in detail.

## The Display Object

In the Yellow Box, an EOAssociation is tied to a single display
object. Each EOAssociation assumes the roles defined for one or
more outlets of this object. An EOControlAssociation, for example, appropriates
the target and action outlets of the NSControl it is bound to. When
the user activates the control or changes its value, the action
is fired and the EOAssociation correspondingly updates a property
of the display group's selected enterprise object. An EOControlAssociation
also sets itself as the control's delegate in order to receive
various editing and validation messages.

In the Yellow Box, any outlets an association claims cannot
be used for other purposes. The class method [objectKeysTaken](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3pmjvgky3ujnsxs42umfvwk3q) returns the names
of any outlets a given EOAssociation subclass appropriates, and
InterfaceBuilder disables them in its Connections Inspector if the
inspected object has been associated. A button acting as an EOControlAssociation's
display object, for example, has its target outlet dimmed.

Although display objects are typically user-interface controls
such as text fields and pop-up menus, they can be any kind of object.
A notable example of this is an EOMasterDetailAssociation, where
the display object is a "detail" EODisplayGroup populated with
the destination enterprise objects of a relationship in the "master"
display group. See the EOMasterDetailAssociation class specification
for more information on master-detail configurations.

## Bindings: Aspects, EODisplayGroups, and Keys

Although an EOAssociation has only one display object it may
have any number of aspects. Aspects define the EODisplayGroup characteristics
that the association observes. Aspects are bound to a display group
by a key of the enterprise objects contained by the association.
Depending upon a given EOAssociation subclass, aspects may be optional
or mandatory. They might all have to be bound to a single EODisplayGroup
or they may span several. Some aspects can be mutually exclusive.

On the display side, aspects are typically bound to visible
facets of the EOAssociation's display object, such as the value
or values it displays and any interactive state. Each aspect's
value is determined by the contents of the enterprise-object property
in the EODisplayGroup that the aspect is bound to. This value may
be taken from all enterprise objects in the EODisplayGroup or only
those in the current selection. Some aspects are "read-only"
in that they merely reflect the contents of the display group, but others
change enterprise-object values when the display object is manipulated.

An EOControlAssociation, for example, defines "value"
and "enabled" aspects. To configure a text field to display
the salary for the selected enterprise object you must create an
EOControlAssociation with the text field as its display object and
bind the EOControlAssociation's "value" aspect to the appropriate
display group's "salary" key. You might also bind the EOControlAssociation's
"enabled" aspect to some key such as "eligibleForRaise"
so that the text field is made editable if this property evaluates
to non-zero. When focus leaves the text field, the newly entered
value is sent to the EODisplayGroup.

A multi-valued aspect can represent the destination of a to-many
relationship or it can define a range of possible values for an
enterprise object's property. EOComboBoxAssociation, for example,
has a "titles" aspect that defines all possible values for a
key, and all these values then appear in the pop-up menu. If, for
example, you bind the "titles" aspect to the "name" key
of an EODisplayGroup containing Departments, you get a pop-up menu
containing the names of all departments. EOComboBoxAssociation also
has a "selectedObject" aspect which, when bound to a relationship property
of an enterprise object, determines the selection in the "titles"
display group.

As EODelayedObservers, EOAssociations add themselves to the
list of objects observing the display groups they are bound to.
When a display group changes its selection or contents, observing EOAssociations
are sent a [subjectChanged](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zxkytkmvrxiq3imfxgozle) message. This message
does not indicate which EODisplayGroup has changed, so the receiver
must query each one. When an EOAssociation wishes to modify the
contents of a EODisplayGroup, it typically does so through the [setValue:forAspect:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2).
This process and the querying of display groups are described under ["Monitoring Changes from the Display Object"](#apple-infemq2hincee).

## Setting up an EOAssociation Programmatically

Although you normally use the Interface Builder application
(and the EOPalette palette) to set up EOAssociations, you can do
so programmatically as well. Because EOAssociation coordinates the actions
of many objects, linking a display object to a display group is
a multi-step process, as shown by the following code fragment; this
fragment assumes that salaryText and employeeGroup already exist.

> ```
> NSTextField *salaryText;
> EODisplayGroup *employeeGroup;
> EOControlAssociation *association;
>
> association = [[EOControlAssociation alloc] initWithObject:salaryText];
> [association bindAspect:@"value" displayGroup:employeeGroup key:@"salary"];
> [association bindAspect:@"enabled" displayGroup:employeeGroup key:@"eligibleForRaise"];
> [association establishConnection];
> [association release];
> ```

Although an association is initialized with the display object
it monitors, this really represents only half of the required initialization;
the association and therefore the display object have yet to be
bound to any display group. The two invocations of [bindAspect:displayGroup:key:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rgs3teifzxazldoq5gi2ltobwgc6khojxxk4b2nnsxsoq) define
the specifics of the field's interaction with employeeGroup. Once
these aspects have been bound, [establishConnection](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o) causes
the association to register as an observer of employeeGroup and
complete its internal initialization. Note that in the Yellow Box
you can safely release a newly instantiated association once you
invoke __establishConnection__ because this
method retains the association for the lifespan of the display object.

## Creating a Subclass of EOAssociation

If none of the standard EOAssociation subclasses meets your
needs, you can create a new one without much effort. To do so, you
need to define four areas of functionality:

- What your subclass monitors and which display
  objects it can work with.
- How your subclass establishes its connections with its display
  object and its EODisplayGroups
- How it updates the display object to reflect display group
  changes.
- How it monitors the display object and updates the EODisplayGroups.

The following four sections describe how to do each of these.

## Defining Capabilities

If you're creating a Yellow Box subclass, a significant
part of creating an EOAssociation subclass is defining and advertising
what the subclass works with. The characteristics that your subclass
should define are:

**Aspects (required)**
: Your EOAssociation subclass must define an __aspects__ class
method that returns an NSArray of aspect names, as NSStrings. Some
standard aspects are:_value_, the value of an
attribute or relationship; _enabled_, whether
the control should be enabled; _titles_, all
existing values for an attribute; and _selectedTitle_,
the value of the selected attribute (bound to the same key as "titles").

**What the subclass works with (required)**
: Interface Builder asks each EOAssociation subclass if
it can work with a given object when it displays its Connections
Inspector. Your subclass should implement the [isUsableWithObject:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3jonkxgylcnrsvo2lunbhwe2tfmn2du) class
method to examine the object provided and return YES if it can work
with that object. This method can examine the class of the object
provided, or any of its attributes, to determine whether it can
work with the object. For example, EOPopUpAssociation verifies that
the object is an NSPopUpButton, while EOMasterDetailAssociation
checks that the object is an EODisplayGroup whose data source is
an EODetailDataSource.

**Aspect signatures (optional)**
: Aspects by default are made available for any kind of
property-single-valued attributes, to-one relationships, and to-many
relationships. If your subclass has aspects that only have meaning
for one or two of these, it should define an [aspectSignatures](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3bonygky3uknuwo3tbor2xezlt) class method that returns
an NSArray of NSStrings corresponding to the aspects defined for
the class. Each string should contain a subset of the string "A1M",
where "A" indicates that the aspect can be used with attributes
(where the value is a value-bearing object such as NSString or NSNumber),
"1" that it can be used with to-one relationships (where the
value is an enterprise object), and "M" indicates that the aspect
can be used with to-many relationships (where the value is an array
of enterprise objects). EOControlAssociation only displays single
attributes, so its aspect signature for "value" and "enabled"
is the array ("A", "A"). EOMasterDetailAssociation only
works with relationships, so the aspect signature for its aspect
"parent" is the array ("1M").

**Which outlets it uses (optional)**
: Interface Builder disables connections to outlets used
by an EOAssociation, so if your subclass uses any it should advertise
them by defining the [objectKeysTaken](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3pmjvgky3ujnsxs42umfvwk3q) class method to return
an NSArray containing the names of the outlets. These are typically
the standard "target", "delegate", "dataSource", and
so on.

**EOAssociation classes superseded (optional)**
: If your EOAssociation subclass applies uniquely to display
objects that other kinds of EOAssociations simply happen to work
with, it should implement the [associationClassesSuperseded](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3bonzw6y3jmf2gs33oinwgc43tmvzvg5lqmvzhgzlemvsa) class
method to return an array of these classes. EOPopUpAssociation,
for example, works with EOPopUpButton, which as a subclass of NSControl
is also eligible for the EOControlAssociation. Since this isn't
a meaningful or useful EOAssociation for a pop-up button, EOPopUpAssociation
supersedes it, and Interface Builder doesn't present it in its
Connections Inspector when a pop-up button is selected.

**Display name (optional)**
: If you want your subclass to be listed in Interface
Builder's Associations pop-up list with a name other than that
of its class, it can override the [displayName](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3enfzxa3dbpfhgc3lf) to return that name.
This is often done to truncate long names so they fit in the pop-up
button.

**Primary aspect (optional)**
: If your subclass implements the [primaryAspect](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhuc43tn5rwsylunfxw4l3qojuw2ylspfaxg4dfmn2a) class method, Interface
Builder automatically selects it the first time the user drags a
connection from the display object and chooses your EOAssociation
subclass in the Connections Inspector.

**Binding ability (optional)**
: If your subclass defines aspects that are mutually
exclusive, available only for a particular kind of display object,
or are otherwise not always available, you might want to implement the
instance method [canBindAspect:displayGroup:key:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5rwc3scnfxgiqltobswg5b2mruxg4dmmf4uo4tpovydu23fpe5a) to
check these types of conditions. Interface Builder uses this information
to enable and disable aspects, to guide the user in property setting
up EOAssociations.

**Priority (optional)**
: EOAssociation uses the default EODelayedObserver priority
of EODelayedObserverPriorityThird. If your subclass need a higher
or lower priority, it should override the __priority__ method
appropriately. EOMasterDetailAssociation, for example, uses EODelayedObserverPrioritySecond
to catch updates before other EOAssociations based on it.

## Setting Up

EOAssociation's designated initializer is [initWithObject:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5uw42luk5uxi2cpmjvgky3uhi), but you rarely need
to override this method. Instead, you override [establishConnection](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o),
which is where the real initialization takes place, as described
above in ["Setting up an EOAssociation Programmatically"](#apple-infemqsfivbeq).

Your subclass's implementation of [establishConnection](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sxg5dbmjwgs43iinxw43tfmn2gs33o) should
first invoke the superclass implementation to initialize the observation
of bound EODisplayGroups and then establish their notification relationship
with the display object. Once the association has been bound to
its display groups and appropriately attached to its display object
it is ready to perform real work.

## Monitoring Changes from the EODisplayGroup

An EOAssociation is notified of changes in EODisplayGroup
selections and changes through EODelayedObserver's __subjectChanged__ method.
An EOAssociation sublcass, in its implementation of this method,
propagates these changes to the display object. Because subjectChanged
provides no additional information about the change that triggered
its invocation, associations must query their bound display groups
for details. The EOAssociation method [displayGroupForAspect:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sgs43qnrqxsr3sn52xartpojaxg4dfmn2du),
in conjunction with EODisplayGroup's [contentsChanged](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwg33oorsw45dtinugc3thmvsa) and [selectionChanged](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlmmvrxi2lpnzbwqylom5swi), faciliate efficient
aspect-by-aspect change analysis. Once you have determined the set
of affected aspects, your subclass must update its display object
to reflect their new values. How this is done is specific to the
class of display object and to the aspects your EOAssocation subclass
supports.

## Monitoring Changes from the Display Object

When an EOAssociation is notified of a change to the state
of its display object, it must update the affected display groups
so that they reflect the new state. Updating can involve changing
a display-group value, sending messages to the display group, or
sending messages to some set of the enterprise objects the display
group contains. As a simple example, an association with a "value"
aspect would update the value of the bound display group's selected
enterprise object by invoking [setValue:forAspect:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2) with
the display object's new contents. Complex associations might set
enterprise object values more directly via EODisplayGroup's [setSelectedObjectValue:forKey:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldorswit3cnjswg5cwmfwhkzj2mzxxes3fpe5a) , [setValue:forObject:key:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uhjvwk6j2), or [setValue:forObjectAtIndex:key:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzlukzqwy5lfhjtg64spmjvgky3uif2es3temv4du23fpe5a) in
conjunction with EOAssocation"s [displayGroupKeyForAspect:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sgs43qnrqxsr3sn52xas3fpfdg64sbonygky3uhi).
An association with a button as its display object might go even
further, sending the message defined by its "action" aspect
to the enterprise objects selected in a display group whenever the
button is clicked.

For display objects that support editing, such as text fields,
an association must observe events signifying the beginning or end
of an editing operation and then inform the appropriate display
groups using EODisplayGroup's [associationDidBeginEditing:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrbgkz3jnzcwi2lunfxgooq) and [associationDidEndEditing:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxwc43tn5rwsylunfxw4rdjmrcw4zcfmruxi2lom45a).
This operation is important because a display group requests an
end to editing when it is asked to perform tasks such as the insertion
of a new enterprise object or a save. It requests and end to editing
by sending an [endEditing](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5sw4zcfmruxi2lom4) message to the association
it believes currently has an edit in progress. Implementations of __endEditing__ should
attempt to propagate the current state of the display object to
the receiver's display groups and return NO if this attempt fails,
indicating that the request has been disallowed. EOAssociations
that support the display of multiple values and the notion of a
selection must also propagate changes in this selection to the appropriate
display groups using EODisplayGroup's [setSelectionIndexes:](EODisplayGroup-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2enfzxa3dbpfdxe33voaxxgzluknswyzldoruw63sjnzsgk6dfom5a).

## Validation

Although validation of values entered by the user can happen
in several places, EOAssociations generally concern themselves only
with data entry errors. These errors are typically caught by the display
object or an NSFormatter, and result in a message to the delegate
of the display object. For example, an NSControl sends __control:isValidObject:__ and __control:didFailToFormatString:errorDescription:__ to
its delegate, allowing the delegate to validate values itself or
to handle errors caught by an NSFormatter. Your implementation of
a method such as __control:isValidObject:__ should simply
try to save the new value, using EOAssociation's [setValue:forAspect:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2) or [setValue:forAspect:atIndex:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwk5cwmfwhkzj2mzxxeqltobswg5b2mf2es3temv4du),
returning YES or NO as that message does. For __control:didFailToFormatString:errorDescription:__,
the typical response should be to invoke [shouldEndEditingForAspect:invalidInput:errorDescription:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5a) or [shouldEndEditingForAspect:invalidInput:errorDescription:index:](EOAssociation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bonzw6y3jmf2gs33of5zwq33vnrsek3teivsgs5djnztum33sifzxazldoq5gs3twmfwgszcjnzyhk5b2mvzhe33sirsxgy3snfyhi2lpny5gs3temv4du).

[![Table of Contents](attachments/images/up.gif)](../../EOInterfaceTOC.md)
