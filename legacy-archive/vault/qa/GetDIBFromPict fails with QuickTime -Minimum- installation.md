---
title: GetDIBFromPict fails with QuickTime "Minimum" installation
apple_id: DTS10003416
resource_type: QA
platform: macOS
topic: null
technology: QuickTime
published: '2004-09-28'
source_url: https://developer.apple.com/library/archive/qa/qa1294/_index.html
archived_at: '2026-07-18T02:30:21.327243Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1294

# GetDIBFromPict fails with QuickTime "Minimum" installation

## Q:  My application calls the `GetDIBFromPict` function, and this works fine provided QuickTime was installed on the machine using the "Recommended" installation option. However, if the user instead chose the "Minimum" installation option the `GetDIBFromPict` function always returns zero, and sometimes a QuickTime dialog pops up telling me additional software is required. I need to know ahead of time whether or not the `GetDIBFromPict` function is going to fail. Is this possible?

A: You can't check for the various QuickTime installations ("Minimal", "Recommended" and so on). However, you can check for the presence of any of the QuickTime components required by a given function such as `GetDIBFromPict` or by a given QuickTime movie.

For example, `GetDIBFromPict` requires the QuickTime BMP movie export component. You can check for this component using the Component Manager `FindNextComponent` function as shown below:

__Listing 1__  Checking for the presence of the BMP movie exporter component.

```c
#include <QuickTimeComponents.h>

Boolean isBMPExporterAvailable()
{
    ComponentDescription cd;
    Component aComponent = 0;

    cd.componentType            = MovieExportType;
    cd.componentSubType         = kQTFileTypeBMP;
    cd.componentManufacturer    = 0;
    cd.componentFlags           = 0;
    cd.componentFlagsMask       = cmpIsMissing;

    aComponent = FindNextComponent( 0, &cd ) ;

    return (aComponent != 0);
}
```

[Technical Q&A QA1093, 'Determining required components for QuickTime movies'](https://developer.apple.com/qa/qa2001/qa1093.html) describes techniques for determining which components are required for a given movie.

Finally, you can disable any error dialog from appearing if the necessary components are not present on the user's machine. See [Technical Q&A QA1164, 'Disabling QuickTime Error Dialogs When Opening or Tasking a Movie'](https://developer.apple.com/qa/qa2001/qa1164.html).

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2004-09-28 | New document that demonstrates how to check for any available QuickTime components required by individual QuickTime functions. |

