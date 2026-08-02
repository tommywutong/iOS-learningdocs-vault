---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/More/EOClassDescription.html
archived_at: '2026-07-15T08:11:38.021654Z'
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
(an [ClassDescriptionNeededForClassNotification](EOClassDescription.md#apple-ijaucrkcizbes) or
an [ClassDescriptionNeededForEntityNameNotification](EOClassDescription.md#apple-ijaucrcdizcec)).
When an EOModel object receives such a notification, it registers
the metadata (class description) for the EOEntity on which the enterprise
object is based. (EOModel and EOEntity are defined in EOAccess.)

An enterprise object takes advantage of the metadata registered
for it by using the EOClassDescription-related methods defined in
the EOEnterpriseObject interface (and implemented in EOCustomObject
and EOGenericRecord). Primary among these methods is [classDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwg3dbonzuizltmnzgs4dunfxw4), which returns the
class description associated with the enterprise object. Through
this class description the enterprise object has access to all of
the information relating to its entity in a model file.

In addition to methods that return information based on an
enterprise object's class description, the EOClassDescription-related
methods the [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq) interface defines
include methods that are automatically invoked when a particular
operation occurs. These include validation methods and methods that
are invoked whenever an enterprise object is inserted or fetched.

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
  is described in more detail in the section ["Working with Objects That Don't Have EOModels"](#apple-ijaucqsgjfbue).
- When you create a subclass of EOClassDescription

## Overriding Methods in an Enterprise Object

As described above, EOEnterpriseObject defines several EOClassDescription-related
methods. It's common for enterprise object classes to override
the following methods to either perform validation, to assign default
values ( [awakeFromInsertion](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o)), or to provide
additional initialization to newly fetched objects ( [awakeFromFetch](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna)):

- [validateForSave](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfgylwmu)
- [validateForDelete](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zeizlmmv2gk)
- [validateForInsert](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zes3ttmvzhi)
- [validateForUpdate](EOValidation.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpkzqwy2lemf2gs33of53gc3djmrqxizkgn5zfk4demf2gk)
- [awakeFromInsertion](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvew443foj2gs33o)
- [awakeFromFetch](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxwc53bnnsum4tpnvdgk5ddna)
- [userPresentableDescription](EOEnterpriseObject.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivxhizlsobzgs43fj5rguzldoqxxk43fojihezltmvxhiylcnrsuizltmnzgs4dunfxw4)

For example, an enterprise object class can implement a `validateForSave` method
that checks the values of salary and jobLevel properties before
allowing the values to be saved to the database:

> ```
> public void validateForSave() throw EOValidation.Exception {
>     if (salary > 1500 && jobLevel < 2) {
>         throw new EOValidation.Exception(
>             "The salary is too high for that position!");
>         }
>     // pass the check on to the EOClassDescription
>     super.validateForSave();
> }
> ```

For more discussion of this subject, see the chapter "Designing
Enterprise Objects" in the _Enterprise Objects Framework
Developer's Guide_, and the [EOEnterpriseObject](EOEnterpriseObject.md#apple-ijaueqsdjbfeq) interface specification.

## Working with Objects That Don't Have EOModels

Although an EOModel is the most common source of an EOClassDescription
for a class, it isn't the only one. Objects that don't have
an EOModel can implement EOClassDescription methods directly as instance
methods, and the rest of the Framework will treat them just as it
does enterprise objects that have this information provided by an
external EOModel.

There are a few reasons you might want to do this. First of
all, if your object implements the methods [entityName](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwk3tunf2hsttbnvsq), [attributeKeys](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxwc5duojuwe5lumvfwk6lt), [toOneRelationshipKeys](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg),
and [toOneRelationshipKeys](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxi32pnzsvezlmmf2gs33oonugs4clmv4xg),
EOEditingContexts can snapshot the object and thereby provide undo
for it.

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
which you do by invoking the method [registerClassDescription](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpojswo2ltorsxeq3mmfzxgrdfonrxe2lqoruw63q). You can either
register class descriptions in response to a EOClassDescriptionNeeded...
notification (an [ClassDescriptionNeededForClassNotification](EOClassDescription.md#apple-ijaucrkcizbes) or
an [ClassDescriptionNeededForEntityNameNotification](EOClassDescription.md#apple-ijaucrcdizcec)),
or you can register class descriptions at the time you initialize
your application (in other words, you can register all potential
class descriptions ahead of time). The default implementation in
Enterprise Objects Framework is based on responding to the EOClassDescriptionNeeded...
notifications. When an EOModel receives one of these notifications,
it supplies a class description for the specified class or entity
name by invoking [registerClassDescription](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpojswo2ltorsxeq3mmfzxgrdfonrxe2lqoruw63q)

## EOEntityClassDescription

There are only three methods in EOClassDescription that have
meaningful implementations (that is, that don't either return null or
simply return without doing anything): [invalidateClassDescriptionCache](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpnfxhmylmnfsgc5dfinwgc43tirsxgy3snfyhi2lpnzbwcy3imu), [registerClassDescription](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6q3mmfzxgrdfonrxe2lqoruw63rpojswo2ltorsxeq3mmfzxgrdfonrxe2lqoruw63q), and [propagateDeleteForObject](EOClassDescription.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinwgc43tirsxgy3snfyhi2lpnyxxa4tpobqwoylumvcgk3dforsum33sj5rguzldoq).
The default behavior of the rest of the methods in Enterprise Objects
Framework comes from the implementation in the access layer's
EOClassDescription subclass EOEntityClassDescription. For more information,
see the EOEntityClassDescription class specification.

## The EOClassDescription's Delegate

You can assign a delegate to the EOClassDescription class.
EOClassDescription sends the message [shouldPropagateDeleteForObject](EOClassDescription.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinwgc43tirsxgy3snfyhi2lpnyxeg3dbonzuizlmmvtwc5dff5zwq33vnrsfa4tpobqwoylumvcgk3dforsum33sj5rguzldoq) to
its delegate when delete propagation is about to take place for
a particular object. The delegate can either allow or deny the operation
for a specified relationship key. For more information, see the
method description for [shouldPropagateDeleteForObject](EOClassDescription.ClassDelegate.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinwgc43tirsxgy3snfyhi2lpnyxeg3dbonzuizlmmvtwc5dff5zwq33vnrsfa4tpobqwoylumvcgk3dforsum33sj5rguzldoq).

[![Table of Contents](attachments/images/up.gif)](../../EOControlTOC.md)
