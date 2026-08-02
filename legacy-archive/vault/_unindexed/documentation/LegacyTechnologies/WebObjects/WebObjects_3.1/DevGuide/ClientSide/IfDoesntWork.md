---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/DevGuide/ClientSide/IfDoesntWork.html
archived_at: '2026-07-15T07:46:34.669120Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](ClientSideComponents.mif.md)
[!Previous Section](Introduction.md)

# __If Client-Side Components Do Not Work__

After you install WebObjects, the Java client-side components feature should "just work" (assuming you have a Java-enabled browser). Unfortunately, files are inadvertently moved or deleted sometimes. The following checklist will assist you in situations like these. For Java client-side components to work, the following parts must be in place.

- You must have a Java-enabled browser.
- The following packages and classes must be installed in _`DOCUMENT_ROOT`___/WebObjects/Java__:

  : next.util.PropertyListUtilities.class: next.util.KeyValueCoding.class: next.wo.client.Association.class: next.wo.client.SimpleAssociation.class: next.wo.client.SimpleAssociationDestination.class
- In addition, the __next.wo.client.controls__ package, which contains the applet classes (TextFieldApplet, ButtonApplet, and so on), must be installed in the same location. See "[Client-Side Applet Controls](../../Reference/ClientSideComponents/Applets/CSControls.mif.book.md)" for descriptions of each supported applet.

When NeXT's Java package is installed, it is written to _`NEXT_ROOT`___/NextLibrary/Java__ as well as to _`DOCUMENT_ROOT`___/WebObjects/Java__. If your _`DOCUMENT_ROOT`_ has been deleted or corrupted, you can copy the packages in _`NEXT_ROOT`___/NextLibrary/Java__ to _`DOCUMENT_ROOT`___/WebObjects/Jav__a.

Of course, if you intend to create your own applets or Association subclasses, or do other Java development, you must obtain Sun's JDK (Java Development Kit) or a similar product.

If you install the development version of WebObjects, you get examples of applications that use client-side components in _`NEXT_ROOT`___/NextDeveloper/Examples/WebObjects__ and example applet controls in the __next.wo.client.examples__ package (installed in both _`NEXT_ROOT`___/NextLibrary/Java__ and _`DOCUMENT_ROOT`___/WebObjects/Java__). The TimeOffJava example application contains the source code for the controls in __next.wo.client.examples__. You are strongly encouraged to read the application's ReadMe file before attempting to compile this source code.

__Note__: If Java client-side components don't seem to work on your system, do not set the CLASSPATH environment variable to point to the __next.\*__ packages in DOCUMENT_ROOT. Doing so might seem to resolve the problem, but this is true only in those situations where the browser and server reside on the same machine.

[!Table of Contents](ClientSideComponents.mif.md)
[!Next Section](Architecture.md)
