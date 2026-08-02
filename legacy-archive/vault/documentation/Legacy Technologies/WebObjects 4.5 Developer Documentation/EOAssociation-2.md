---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOInterface.framework/Java/Classes/More/EOAssociation.html
archived_at: '2026-07-15T08:11:45.176999Z'
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

In the com.apple.yellow.eointerface package, an EOAssociation
is tied to a single display object. Each EOAssociation assumes the
roles defined for one or more outlets of this object. An EOControlAssociation,
for example, appropriates the target and action outlets of the NSControl
it is bound to. When the user activates the control or changes its
value, the action is fired and the EOAssociation correspondingly
updates a property of the display group's selected enterprise object. An
EOControlAssociation also sets itself as the control's delegate
in order to receive various editing and validation messages.

In the com.apple.yellow.eointerface package, any outlets an
association claims cannot be used for other purposes. The class
method [objectKeysTaken](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpn5rguzldorfwk6ltkrqwwzlo) returns the names
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
are sent a [subjectChanged](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg5lcnjswg5cdnbqw4z3fmq) message. This message
does not indicate which EODisplayGroup has changed, so the receiver
must query each one. When an EOAssociation wishes to modify the
contents of a EODisplayGroup, it typically does so through the [setValueForAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a).
This process and the querying of display groups are described under ["Monitoring Changes from the Display Object"](#apple-infemq2hincee).

## Setting up an EOAssociation Programmatically

Although you normally use the Interface Builder application
(and the EOPalette palette) to set up EOAssociations, you can do
so programmatically as well. Because EOAssociation coordinates the actions
of many objects, linking a display object to a display group is
a multi-step process, as shown by the following code fragment; this
fragment assumes that salaryText and employeeGroup already exist.

> ```
> JTextComponent salaryText;
> EODisplayGroup employeeGroup;
> EOTextAssociation association;
>
> association = new EOTextAssociation(salaryText);
> association.bindAspect(EOTextAssociation.ValueAspect, employeeGroup, "salary");
> association.bindAspect(
>     EOTextAssociation.EnabledAspect, employeeGroup, "eligibleForRaise");
> association.establishConnection();
> ```

Although an association is initialized with the display object
it monitors, this really represents only half of the required initialization;
the association and therefore the display object have yet to be
bound to any display group. The two invocations of [bindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwe2lomraxg4dfmn2a) define
the specifics of the field's interaction with employeeGroup. Once
these aspects have been bound, [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) causes
the association to register as an observer of employeeGroup and
complete its internal initialization. Note that when using the com.apple.yellow.eointerface APIs
you can safely release a newly instantiated association once you invoke `establishConnection` because
this method retains the association for the lifespan of the display object.

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

If you're creating a com.apple.yellow.eointerface.EOAssociation
subclass, a significant part of creating an EOAssociation subclass
is defining and advertising what the subclass works with. The characteristics
that your subclass should define are:

**Aspects (required)**
: Your EOAssociation subclass must define an `aspects` class
method that returns an NSArray of aspect names, as Strings. Some
standard aspects are:_value,_ the value of an
attribute or relationship; _enabled,_ whether
the control should be enabled; _titles,_ all
existing values for an attribute; and _selectedTitle,_
the value of the selected attribute (bound to the same key as "titles").

**What the subclass works with (required)**
: Interface Builder asks each EOAssociation subclass if
it can work with a given object when it displays its Connections
Inspector. Your subclass should implement the [isUsableWithObject](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpnfzvk43bmjwgkv3jorue6ytkmvrxi) class
method to examine the object provided and return true if it can work
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
for one or two of these, it should define an [aspectSignatures](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxazldorjwsz3omf2hk4tfom) class method that returns
an NSArray of Strings corresponding to the aspects defined for the
class. Each string should contain a subset of the string "A1M",
where "A" indicates that the aspect can be used with attributes
(where the value is a value-bearing object such as String or Number), "1"
that it can be used with to-one relationships (where the value is
an enterprise object), and "M" indicates that the aspect can
be used with to-many relationships (where the value is an array
of enterprise objects). EOControlAssociation only displays single
attributes, so its aspect signature for "value" and "enabled"
is the array ("A", "A"). EOMasterDetailAssociation only
works with relationships, so the aspect signature for its aspect
"parent" is the array ("1M").

**Which outlets it uses (optional)**
: Interface Builder disables connections to outlets used
by an EOAssociation, so if your subclass uses any it should advertise
them by defining the [objectKeysTaken](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpn5rguzldorfwk6ltkrqwwzlo) class method to return
an NSArray containing the names of the outlets. These are typically
the standard "target", "delegate", "dataSource", and
so on.

**EOAssociation classes superseded (optional)**
: If your EOAssociation subclass applies uniquely to display
objects that other kinds of EOAssociations simply happen to work
with, it should implement the [associationClassesSuperseded](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmfzxg33dnfqxi2lpnzbwyyltonsxgu3vobsxe43fmrswi) class
method to return an array of these classes. EOPopUpAssociation,
for example, works with EOPopUpButton, which as a subclass of NSControl
is also eligible for the EOControlAssociation. Since this isn't
a meaningful or useful EOAssociation for a pop-up button, EOPopUpAssociation
supersedes it, and Interface Builder doesn't present it in its
Connections Inspector when a pop-up button is selected.

**Display name (optional)**
: If you want your subclass to be listed in Interface
Builder's Associations pop-up list with a name other than that
of its class, it can override the [displayName](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpmruxg4dmmf4u4ylnmu) to return that name.
This is often done to truncate long names so they fit in the pop-up
button.

**Primary aspect (optional)**
: If your subclass implements the [primaryAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6qltonxwg2lboruw63rpobzgs3lboj4uc43qmvrxi) class method, Interface
Builder automatically selects it the first time the user drags a
connection from the display object and chooses your EOAssociation
subclass in the Connections Inspector.

**Binding ability (optional)**
: If your subclass defines aspects that are mutually
exclusive, available only for a particular kind of display object,
or are otherwise not always available, you might want to implement the
instance method [canBindAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwgyloijuw4zcbonygky3u) to
check these types of conditions. Interface Builder uses this information
to enable and disable aspects, to guide the user in property setting
up EOAssociations.

**Priority (optional)**
: EOAssociation uses the default EODelayedObserver priority
of EODelayedObserverPriorityThird. If your subclass need a higher
or lower priority, it should override the `priority` method
appropriately. EOMasterDetailAssociation, for example, uses EODelayedObserverPrioritySecond
to catch updates before other EOAssociations based on it.

## Setting Up

EOAssociation's constructor is

> ```
> public EOAssociation(Object object)
> ```

but you rarely need to write custom initialization code in
this method. Instead, you override [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny),
which is where the real initialization takes place, as described
above in ["Setting up an EOAssociation Programmatically"](#apple-infemqsfivbeq).

Your subclass's implementation of [establishConnection](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk43umfrgy2ltnbbw63tomvrxi2lpny) should
first invoke the superclass implementation to initialize the observation
of bound EODisplayGroups and then establish their notification relationship
with the display object. Once the association has been bound to
its display groups and appropriately attached to its display object
it is ready to perform real work.

## Monitoring Changes from the EODisplayGroup

An EOAssociation is notified of changes in EODisplayGroup
selections and changes through EODelayedObserver's `subjectChanged` method.
An EOAssociation sublcass, in its implementation of this method,
propagates these changes to the display object. Because subjectChanged
provides no additional information about the change that triggered
its invocation, associations must query their bound display groups
for details. The EOAssociation method [displayGroupForAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4cgn5zec43qmvrxi),
in conjunction with EODisplayGroup's [contentsChanged](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6y3pnz2gk3tuonbwqylom5swi) and [selectionChanged](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643fnrswg5djn5xeg2dbnztwkza), faciliate efficient
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
enterprise object by invoking [setValueForAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a) with
the display object's new contents. Complex associations might set
enterprise object values more directly via EODisplayGroup's [setSelectedObjectValue](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gkzcpmjvgky3ukzqwy5lf) , [setValueForObject](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3u), or [setValueForObjectAtIndex](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forlgc3dvmvdg64spmjvgky3uif2es3temv4a) in conjunction
with EOAssocation"s [displayGroupKeyForAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwi2ltobwgc6khojxxk4clmv4um33sifzxazldoq).
An association with a button as its display object might go even
further, sending the message defined by its "action" aspect
to the enterprise objects selected in a display group whenever the
button is clicked.

For display objects that support editing, such as text fields,
an association must observe events signifying the beginning or end
of an editing operation and then inform the appropriate display
groups using EODisplayGroup's [associationDidBeginEditing](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfseezlhnfxekzdjoruw4zy) and [associationDidEndEditing](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc6yltonxwg2lboruw63senfsek3teivsgs5djnztq).
This operation is important because a display group requests an
end to editing when it is asked to perform tasks such as the insertion
of a new enterprise object or a save. It requests and end to editing
by sending an [endEditing](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxwk3teivsgs5djnztq) message to the association
it believes currently has an edit in progress. Implementations of `endEditing` should
attempt to propagate the current state of the display object to
the receiver's display groups and return false if this attempt
fails, indicating that the request has been disallowed. EOAssociations
that support the display of multiple values and the notion of a
selection must also propagate changes in this selection to the appropriate
display groups using EODisplayGroup's [setSelectionIndexes](EODisplayGroup.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpiruxg4dmmf4uo4tpovyc643forjwk3dfmn2gs33ojfxgizlymvzq).

## Validation

Although validation of values entered by the user can happen
in several places, EOAssociations generally concern themselves only
with data entry errors. These errors are typically caught by the display
object or an NSFormatter, and result in a message to the delegate
of the display object. For example, an NSControl sends `controlIsValidObject` and `controlDidFailToFormatStringErrorDescription` to
its delegate, allowing the delegate to validate values itself or
to handle errors caught by an NSFormatter. Your implementation of
a method such as `controlIsValidObject` should
simply try to save the new value, using EOAssociation's [setValueForAspect](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5a) or [setValueForAspectAtIndex](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxgzlukzqwy5lfizxxeqltobswg5cborew4zdfpa),
returning true or false as that message does. For `controlDidFailToFormatStringErrorDescription`,
the typical response should be to invoke [shouldEndEditing](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgo) or [shouldEndEditingAtIndex](EOAssociation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifzxg33dnfqxi2lpnyxxg2dpovwgirlomrcwi2lunfxgoqlujfxgizly).

[![Table of Contents](attachments/images/up.gif)](../../EOInterfaceTOC.md)
