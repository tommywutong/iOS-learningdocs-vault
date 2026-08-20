---
title: Crossing To-Many Relationships with Cocoa Bindings
apple_id: DTS10004234
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: AppKit
published: '2013-04-04'
source_url: https://developer.apple.com/library/archive/samplecode/TwoManyControllers/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:27:24.475751Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Crossing To-Many Relationships with Cocoa Bindings](Crossing%20To-Many%20Relationships%20with%20Cocoa%20Bindings.md)


[Next](TwoManyControllers-APLDocument.h.md)[Previous](Crossing%20To-Many%20Relationships%20with%20Cocoa%20Bindings.md)

# ReadMe.txt

```

TwoManyControllers
==================

Abstract
-------- 
This sample demonstrates how NSArrayControllers can be used to produce a user interface that traverses multiple (in this case two) to-many relationships.  The basic model consists of a Product with a to-many relationship to a Version which in turn has a to-many relationship to a License.  That is, a product has many versions, and a version has many licenses. 

In this example, we would like the user to be able to select a single Product and display all the Licenses associated with that Product.  To accomplish this we use an intermediate NSArrayController that holds an array of all the Versions associated with the selected Product.  We then populate the Licenses NSArrayController with the distinct set of objects returned from asking every Version object in the Versions Array Controller (the arrangedObjects) for its Licenses key path. 


Usage
-----
Use the top half of the interface to add projects, versions, and licenses.  You need to add some sample data to appreciate the purpose of this sample.

Use the bottom portion of the UI select a product and view all of its licenses.  This is accomplished entirely using NSArrayControllers and bindings.


Model Details
-------------
Please refer to APLDocument.xcdatamodel within the project.


Bindings Details
----------------
Please refer to BindingsDiagram.pdf for a high level view of the bindings used in this sample.  The diagram should act as a good starting point in determining which bindings to inspect in Interface Builder.  The diagram aims to be less of an exhaustive reference for the details about each binding and more of a high-level guide to how the controllers and the UI in the sample interact.
```

[Next](TwoManyControllers-APLDocument.h.md)[Previous](Crossing%20To-Many%20Relationships%20with%20Cocoa%20Bindings.md)

