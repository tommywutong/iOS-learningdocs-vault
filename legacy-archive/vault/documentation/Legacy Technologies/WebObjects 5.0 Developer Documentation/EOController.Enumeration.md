---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOApplicationRef/Java/Interfaces/EOController.Enumeration.html
archived_at: '2026-07-15T08:13:43.258146Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md) 

# EOController.Enumeration

> **__Implements:__**
> : java.util.Enumeration

> **__Package:__**
> : com.webobjects.eoapplication

---

## Interface Description

---

EOController.Enumeration is an interface that defines an enumeration that iterates over a set of EOController objects. It adds one method to the java.util.Enumeration interface: [nextController](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpinxw45dsn5wgyzlsfzcw45lnmvzgc5djn5xc63tfpb2eg33oorzg63dmmvza), which simply returns the next controller in the enumeration's set. The __nextController__ method saves you from having to cast the returned object to an EOController.

Use the EOController method [controllerEnumeration](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) to get an EOController.Enumeration. You can create three types of enumerations:

**[SubcontrollersEnumeration](EOController.md#apple-inceqrckjjdeq)**
: Includes all the descendants of a controller-the controller's subcontrollers, their subcontrollers, and so on down the controller hierarchy-not including the controller itself.

**[SupercontrollersEnumeration](EOController.md#apple-inceqrkgifduc)**
: Includes all the ancestors of a controller-the controller's supercontroller, its supercontroller, and so on up the controller hierarchy-not including the controller itself.

**[ControllerAndSubcontrollersEnumeration](EOController.md#apple-inceqskbjbdue)**
: Includes a controller and all its descendants.

You can further restrict the controllers included in an enumeration by specifying an interface the controllers must implement in order to be included. For more information, see the method description for [controllerEnumeration](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) in the EOController class specification.

## Instance Methods

---

### nextController

`public abstract EOController nextController()`

Returns the next controller in the enumeration. Use this method instead of __nextElement__ because it saves you a cast and because it's implementation is more efficient.

__See Also:__ [controllerEnumeration](EOController.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpinxw45dsn5wgyzlsf5rw63tuojxwy3dfojcw45lnmvzgc5djn5xa) (EOController)

---

© 2001 Apple Computer, Inc. (Last Published April 14, 2001)

[![Table of Contents](attachments/EOApplicationRef/Java/Art/up.gif)](../WebObjectsTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
