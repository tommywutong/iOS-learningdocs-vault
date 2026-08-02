---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOApplication.framework/Java/Interfaces/EOController.Enumeration.html
archived_at: '2026-07-15T08:11:36.945650Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOApplication Reference

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

# EOController.Enumeration

> **__Implements:__**
> : java.util.Enumeration

> **__Package:__**
> : com.apple.client.eoapplication

---

## Interface Description

---

EOController.Enumeration is
an interface that defines an enumeration that iterates over a set
of EOController objects. It adds one method to the java.util.Enumeration
interface: [nextController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsfzcw45lnmvzgc5djn5xc63tfpb2eg33oorzg63dmmvza),
which simply returns the next controller in the enumeration's
set. The __nextController__ method saves you
from having to cast the returned object to an EOController.

Use the EOController method [controllerEnumeration](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) to get an EOController.Enumeration.
You can create three types of enumerations:

**[SubcontrollersEnumeration](EOController.md#apple-inceqrckjjdeq)**
: Includes all the descendants of a controller-the controller's
subcontrollers, their subcontrollers, and so on down the controller
hierarchy-not including the controller itself.

**[SupercontrollersEnumeration](EOController.md#apple-inceqrkgifduc)**
: Includes all the ancestors of a controller-the controller's
supercontroller, its supercontroller, and so on up the controller
hierarchy-not including the controller itself.

**[ControllerAndSubcontrollersEnumeration](EOController.md#apple-inceqskbjbdue)**
: Includes a controller and all its descendants.

You can further restrict the controllers included in an enumeration
by specifying an interface the controllers must implement in order
to be included. For more information, see the method description for [controllerEnumeration](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) in the EOController class
specification.

## Instance Methods

---

### nextController

`public abstract EOController nextController()`

Returns the next controller
in the enumeration. Use this method instead of __nextElement__ because
it saves you a cast and because it's implementation is more efficient.

__See Also:__
[controllerEnumeration](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) (EOController)

---

[![Table of Contents](attachments/images/up.gif)](../EOApplicationTOC.md)

__DRAFT__
