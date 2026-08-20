---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Interfaces/EOEditable.html
archived_at: '2026-07-15T08:11:36.972734Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOEditable

> __Implemented by:__ : EOAssociationController,
> : EODocumentController,
> : EORangeValueController

> **__Package:__**
> : com.apple.client.eoapplication

---

## Interface Description

---

[EOEditable](#apple-inducskdinbeg) is
an interface that defines an API for managing the editability of
a branch of the controller hierarchy. EOEditable controllers usually
base the editability of their user interfaces on the editability of
their supercontrollers. Thus, by default all the EOEditable subcontrollers
of an editable controller are also editable. To enable or disable
a portion of an application's user interface, you need only message the
highest level controller associated with that user interface.

## Constants

---

EOEditable defines the following `int` constants
to identify the editability of an EOEditable controller:

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| NeverEditable | The controller is never editable. |
| AlwaysEditable | The controller is always editable. |
| IfSupercontrollerEditable | The controller is editable only if its supercontroller is editable. If none of the controller's ancestors implement EOEditable, then its the same as if the controller is `AlwaysEditable`. |

## Instance Methods

---

### editability

`public abstract int editability()`

Returns the editability of
the receiver, one of [NeverEditable](#apple-inceqrckjjdeq), [AlwaysEditable](#apple-inceqrkgifduc), or [IfSupercontrollerEditable](#apple-inceqskbjbdue). The
default behavior should be to return `IfSupercontrollerEditable`.

---

### isEditable

`public abstract boolean isEditable()`

Returns `true` if
the receiver is editable, and `false` otherwise. The
default behavior should be to return `true` if
the receiver is currently editable. The receiver is editable if:

- The receiver's editability is [AlwaysEditable](#apple-inceqrkgifduc).
- The receiver's editability is [IfSupercontrollerEditable](#apple-inceqskbjbdue) and sending [isEditable](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpivsgs5dbmjwgkl3joncwi2lumfrgyzi) to the first EOEditable
  ancestor of the receiver returns `true`.

---

### setEditability

`public abstract void setEditability(int editability)`

Sets the
receiver's editability to _editability_,
one of [NeverEditable](#apple-inceqrckjjdeq), [AlwaysEditable](#apple-inceqrkgifduc), or [IfSupercontrollerEditable](#apple-inceqskbjbdue).

---

### supercontrollerEditabilityDidChange

`public abstract void supercontrollerEditabilityDidChange()`

Invoked to notify the receiver
that the editability of its supercontroller changed, giving the
receiver the opportunity to update its user interface to match the
editability of the supercontroller.

---

### takeResposibilityForEditabilityOfAssociation

`public abstract void takeResposibilityForEditabilityOfAssociation(com.apple.client.eointerface.EOAssociation association)`

Invoked when one of the receiver's
subcontrollers is disposed as a transient controller. This
method instructs the receiver to assume responsibility for managing
the editability of the subcontroller's EOAssociation, _association_.

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
