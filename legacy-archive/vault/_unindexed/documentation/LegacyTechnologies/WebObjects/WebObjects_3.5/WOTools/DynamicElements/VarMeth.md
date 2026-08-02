---
title: WebObjects 3.5 Developer Documentation
apple_id: TP40006773
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.5/WOTools/DynamicElements/VarMeth.htm
archived_at: '2026-07-15T07:56:43.666323Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Table of Contents](DynElTOC.md) [!Previous Section](ObjBrwsr.md)

## Creating Variables and Methods in WebObjects Builder

At the bottom of the object browser, there is a pull-down menu called Edit _sourcefile._ It has three items:

- __Add Variable/Method__ allows you to add a key (an instance variable or a method that returns a value) to your source file.
- __Add Action__ allows you to add the template for an action (a method that takes no parameters and returns a component).
- __View Source File__ opens the source file in a Project Builder window.

When you choose Add Variable/Method, the following panel opens:
!
In this panel, you specify:

- The name of the key.
- Its type.

You can choose the type from the pop-up list or type it in directly. You can also use the radio buttons to specify whether the variable is an array.

- How the key is implemented.

The key can be an instance variable whose value is accessed directly, or a method that returns a value (not necessarily associated with an instance variable). You can also create a method that sets the value of an instance variable.

When you click Add, the key's name appears in the object browser (below __application__ and __session__). To see what was added to your source code, choose View Source File from the pop-up menu in the object browser. You'll see something like the following:!
When you choose Add Action, the following panel appears:!
When you click Add, the following code is added to your source file:!
WebObjects Builder provides these ways to add variables and methods for your convenience. Of course, you can add variables and methods directly to your component's code by editing them in Project Builder.
__Note:__ To delete a key or action, you must delete it from the source code in Project Builder. Also, the Add Variable/Method and Add Action commands apply only to a component's code file. To add variables and methods to the application and session code files, or to any other code files, you must edit them directly in Project Builder.

[!Table of Contents](DynElTOC.md) [!Next Section](AddDspGp.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
