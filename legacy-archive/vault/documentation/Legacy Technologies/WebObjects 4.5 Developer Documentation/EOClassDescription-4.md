---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/More/EOClassDescription.html
archived_at: '2026-07-15T08:11:40.071898Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md) 

# EOClassDescription

## How Does It Work?

As noted above, Enterprise Objects Framework implements a
default subclass of EOClassDescription in EOAccess, EOEntityClassDescription.
In the typical scenario in which an enterprise object has a corresponding
model file, a particular operation (such as validating a value)
results in the broadcast of an EOClassDescriptionNeeded... notification
(an [EOClassDescriptionNeededForClassNotification](EOClassDescription-3.md#apple-ijaucrkcizbes) or
an [EOClassDescriptionNeededForEntityNameNotification](EOClassDescription-3.md#apple-ijaucrcdizcec)).
When an EOModel object receives such a notification, it registers
the metadata (class description) for the EOEntity on which the enterprise
object is based. (EOModel and EOEntity are defined in EOAccess.)

An enterprise object takes advantage of the metadata registered
for it by using the EOClassDescription-related methods defined in
the EOEnterpriseObject informal protocol (and implemented in a category
of NSObject). Primary among these methods is [classDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5rwyyltoncgk43dojuxa5djn5xa), which returns the
class description associated with the enterprise object. Through
this class description the enterprise object has access to all of
the information relating to its entity in a model file.

In addition to methods that return information based on an
enterprise object's class description, the EOClassDescription-related
methods the [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq) informal
protocol defines include methods that are automatically invoked
when a particular operation occurs. These include validation methods
and methods that are invoked whenever an enterprise object is inserted
or fetched.

All of this comes together in your running application. When
a user tries to perform a particular operation on an enterprise
object (such as attempting to delete it), the EOEditingContext sends
these validation messages to your enterprise object, which in turn
(by default) forwards them to its EOClassDescription. Based on the
result, the operation is either accepted or refused. For example, referential
integrity constraints in your model might state that you can't
delete a department object that has employees. If a user attempts
to delete a department that has employees, an exception is returned and
the deletion is refused.

## Using EOClassDescription

For the most part, you don't need to programmatically interact
with EOClassDescription. It extends the behavior of your enterprise
objects transparently. However, there are two cases in which you
do need to programmatically interact with it:

- When you override EOClassDescription-related
  EOEnterpriseObject methods in an enterprise object class. These
  methods are used to perform validation and to intervene when enterprise
  objects based on EOModels are created and fetched. (The EOModel
  class is defined in EOAccess.) For objects that don't have EOModels,
  you can override a different set of EOEnterpriseObject methods; this
  is described in more detail in the section ["Working with Objects That Don't Have EOModels" on page 35](#apple-ijaucqsgjfbue).
- When you create a subclass of EOClassDescription

## Overriding Methods in an Enterprise Object

As described above, EOEnterpriseObject defines several EOClassDescription-related
methods. It's common for enterprise object classes to override
the following methods to either perform validation, to assign default
values ( [awakeFromInsertionInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33njfxhgzlsoruw63sjnzcwi2lunfxgoq3pnz2gk6duhi)),
or to provide additional initialization to newly fetched objects
( [awakeFromFetchInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33nizsxiy3ijfxekzdjoruw4z2dn5xhizlyoq5a)):

- [validateForSave](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojjwc5tf)
- [validateForDelete](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojcgk3dforsq)
- [validateForInsert](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojew443foj2a)
- [validateForUpdate](EOValidation-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2wmfwgszdboruw63rpozqwy2lemf2gkrtpojkxazdborsq)
- [awakeFromInsertionInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33njfxhgzlsoruw63sjnzcwi2lunfxgoq3pnz2gk6duhi):
- [awakeFromFetchInEditingContext:](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf5qxoyllmvdhe33nizsxiy3ijfxekzdjoruw4z2dn5xhizlyoq5a)
- [userPresentableDescription](EOEnterpriseObject-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2fnz2gk4tqojuxgzkpmjvgky3uf52xgzlskbzgk43fnz2gcytmmvcgk43dojuxa5djn5xa)

For example, an enterprise object class can implement a __validateForSave__ method
that checks the values of salary and jobLevel properties before
allowing the values to be saved to the database:

> ```
> - (NSException *)validateForSave
> {
>     if (salary > 1500 && jobLevel < 2)
>         return [NSException validationExceptionWithFormat:
>             @"The salary is too high for that position!"];
>     // pass the check on to the EOClassDescription
>     return [super validateForSave];
> }
> ```

For more discussion of this subject, see the chapter "Designing
Enterprise Objects" in the _Enterprise Objects Framework
Developer's Guide_, and the [EOEnterpriseObject](EOEnterpriseObject-3.md#apple-ijaueqsdjbfeq) informal
protocol specification.

## Working with Objects That Don't Have EOModels

Although an EOModel is the most common source of an EOClassDescription
for a class, it isn't the only one. Objects that don't have
an EOModel can implement EOClassDescription methods directly as instance
methods, and the rest of the Framework will treat them just as it
does enterprise objects that have this information provided by an
external EOModel.

There are a few reasons you might want to do this. First of
all, if your object implements the methods [entityName](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5sw45djor4u4ylnmu), [attributeKeys](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5qxi5dsnfrhk5dfjnsxs4y), [toOneRelationshipKeys](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq),
and [toOneRelationshipKeys](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of52g6t3omvjgk3dboruw63ttnbuxas3fpfzq),
EOEditingContexts can snapshot the object and thereby provide undo
for it.

For example, the following code excerpt shows an implementation
of attributeKeys for a Circle class:

> ```
> - (NSArray *)attributeKeys {
>     static NSArray *array = nil;
>     if (!array)
>         array = [[NSArray alloc] initWithObjects:@"radius", @"x",
>             @"y", @"color", nil];
>     return array;
> }
> ```

Secondly, you might want to implement EOClassDescription's
validation or referential integrity methods to add these features
to your classes.

Implementing EOClassDescription methods on a per-class basis
in this way is a good alternative to creating a subclass of EOClassDescription.

## Creating a Subclass of EOClassDescription

You create a subclass of EOClassDescription when you want
to use an external source of information other than an EOModel to
extend your objects. Another possible scenario is if you've added information
to an EOModel (such as in its user dictionary) and you want that
information to become part of your class description-in that case,
you'd probably want to create a subclass of the access layer's
EOEntityClassDescription.

When you create a subclass of EOClassDescription, you only
need to implement the methods that have significance for your subclass.

If you're using an external source of information other
than an EOModel, you need to decide when to register class descriptions,
which you do by invoking the method [registerClassDescription:forClass:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3smvtws43umvzeg3dbonzuizltmnzgs4dunfxw4otgn5zeg3dbonztu).
You can either register class descriptions in response to a EOClassDescriptionNeeded...
notification (an [EOClassDescriptionNeededForClassNotification](EOClassDescription-3.md#apple-ijaucrkcizbes) or
an [EOClassDescriptionNeededForEntityNameNotification](EOClassDescription-3.md#apple-ijaucrcdizcec)),
or you can register class descriptions at the time you initialize
your application (in other words, you can register all potential
class descriptions ahead of time). The default implementation in
Enterprise Objects Framework is based on responding to the EOClassDescriptionNeeded...
notifications. When an EOModel receives one of these notifications,
it supplies a class description for the specified class or entity
name by invoking [registerClassDescription:forClass:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3smvtws43umvzeg3dbonzuizltmnzgs4dunfxw4otgn5zeg3dbonztu)

## EOEntityClassDescription

There are only three methods in EOClassDescription that have
meaningful implementations (that is, that don't either return nil or
simply return without doing anything): [invalidateClassDescriptionCache](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3jnz3gc3djmrqxizkdnrqxg42emvzwg4tjob2gs33oinqwg2df), [registerClassDescription:forClass:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhug3dbonzuizltmnzgs4dunfxw4l3smvtws43umvzeg3dbonzuizltmnzgs4dunfxw4otgn5zeg3dbonztu),
and [propagateDeleteForObject:editingContext:](EOClassDescription-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2dnrqxg42emvzwg4tjob2gs33of5yhe33qmftwc5dfirswyzlumvdg64spmjvgky3uhjswi2lunfxgoq3pnz2gk6duhi).
The default behavior of the rest of the methods in Enterprise Objects
Framework comes from the implementation in the access layer's EOClassDescription
subclass EOEntityClassDescription. For more information, see the EOEntityClassDescription
class specification.

## The EOClassDescription's Delegate

You can assign a delegate to the EOClassDescription class.
EOClassDescription sends the message [shouldPropagateDeleteForObject:inEditingContext:forRelationshipKey:](EOClassDescription%20ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2dnrqxg42emvzwg4tjob2gs33oebbwyyltoncgk3dfm5qxizjponug65lmmrihe33qmftwc5dfirswyzlumvdg64spmjvgky3uhjuw4rlenf2gs3thinxw45dfpb2duztpojjgk3dboruw63ttnbuxas3fpe5a) to
its delegate when delete propagation is about to take place for
a particular object. The delegate can either allow or deny the operation
for a specified relationship key. For more information, see the
method description for [shouldPropagateDeleteForObject:inEditingContext:forRelationshipKey:](EOClassDescription%20ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2dnrqxg42emvzwg4tjob2gs33oebbwyyltoncgk3dfm5qxizjponug65lmmrihe33qmftwc5dfirswyzlumvdg64spmjvgky3uhjuw4rlenf2gs3thinxw45dfpb2duztpojjgk3dboruw63ttnbuxas3fpe5a).

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
