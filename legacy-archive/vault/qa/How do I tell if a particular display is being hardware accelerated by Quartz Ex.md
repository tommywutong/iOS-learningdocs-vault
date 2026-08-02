---
title: How do I tell if a particular display is being hardware accelerated by Quartz
  Extreme?
apple_id: DTS10001741
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2013-08-13'
source_url: https://developer.apple.com/library/archive/qa/qa1218/_index.html
archived_at: '2026-07-18T02:30:12.603957Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1218

# How do I tell if a particular display is being hardware accelerated by Quartz Extreme?

## Q:  How do I tell if a particular display is being hardware accelerated by Quartz Extreme?

A: As of Mac OS X 10.2 (Jaguar), there is a new API in "CGDisplayConfiguration.h" called `CGDisplayUsesOpenGLAcceleration` for just that purpose. "CGDisplayConfiguration.h" can be found in the Core Graphics framework (CoreGraphics.framework) which is part of the Application Services framework (ApplicationServices.framework).

__Listing 1__  Checking for OpenGL acceleration using CGDisplayUsesOpenGLAcceleration.

```c
/* Prototype for CGDisplayUsesOpenGLAcceleration() */
/*
 CGDisplayUsesOpenGLAcceleration() takes a CGDirectDisplayID
 parameter and returns a boolean_t result
 */


#include <ApplicationServices/ApplicationServices.h>;

/* Code that cares whether or not the display is accelerated */

if ( CGDisplayUsesOpenGLAcceleration( displayID ) )
{
    /* Provide full graphics */
}
else
{
    /* Provide reduced graphics */
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2013-08-13 | Updated formatting. |
| 2002-12-04 | New document that describes how to use CGDisplayUsesOpenGLAcceleration to see if a display is accelerated or not. |

