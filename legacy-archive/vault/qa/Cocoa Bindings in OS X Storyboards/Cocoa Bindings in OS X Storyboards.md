---
title: Cocoa Bindings in OS X Storyboards
apple_id: DTS40016747
resource_type: QA
platform: macOS
topic: Data Management
technology: AppKit
published: '2016-04-04'
source_url: https://developer.apple.com/library/archive/qa/qa1871/_index.html
archived_at: '2026-07-18T02:35:09.578694Z'
---
> 导航：[总目录](../../README.md) · [qa](../../_indexes/qa.md)



Technical Q&A QA1871

# Cocoa Bindings in OS X Storyboards

## Q:  Given that there is no File’s Owner in an OS X storyboard, how can I bind the UI elements in my view controller scenes to my application's model objects?

A: In an OS X storyboard, every scene has a controller. We use that controller to manage the content of the scene and interact with the other parts of the application, thus you don’t need a File’s Owner object anymore. (For more information on File’s Owner, see the [About File's Owner](https://developer.apple.com/library/mac/documentation/Cocoa/Conceptual/LoadingResources/CocoaNibs/CocoaNibs.html#//apple_ref/doc/uid/10000051i-CH4-SW15) section of Resource Programming Guide.)

In your view controller scene, the controller is an object of the `NSViewController` subclass. You can use its `representedObject` property, or make any number of other properties that are more type-safe, to represent the model your view controller works with, and then bind through them.

For Cocoa bindings to work correctly, be sure that the model properties are ready for use when Cocoa bindings need them. This is especially important when you need to load the model data immediately after the application launch. To achieve that, there are two cases to consider:

- For a document based application, you can set up the model properties in the `-makeWindowControllers` method of your document class, as shown in Listing 1.

  __Listing 1__  Document based application

```objc
- (void)makeWindowControllers {

    /* Your code to set up the window controller(s) for your document*/

    // Set up the view controller’s representedObject property here,
    // assume the contentViewController of the current window controller
    // is the view controller you working with.
    yourViewController = (YourViewController *)windowController.contentViewController;
    yourViewController.representedObject = <your_model_object>;
}
```
- For a non-document based application, you might set up the model properties in the `-awakeFromNib` method of your view controller class, as shown in Listing 2.

  __Listing 2__  Non-document based application

```objc
- (void)awakeFromNib {
    [super awakeFromNib];
    if (! self.representedObject) {
        self.representedObject = <your_model_object>;
    }
}
```

Once the model properties have been set up, you can safely use key paths starting with "self.representedObject" (or other properties you defined). Figure 1 shows you how to bind an `NSArrayController` object within a view controller scene to the `managedObjectContext` property of the view controller's `representedObject` (which represents a document object owning that property).

__Figure 1__  Binding to the view controller's model property

!!

Be aware that the object of a model property may be replaced when it is written back through Cocoa bindings. As an example, when you bind an `NSArrayController` object to an `NSMutableArray` property, `NSArrayController` uses the `mutableArrayValueForKey:` method defined in `NSKeyValueCoding.h` to write back changes. Your `NSMutableArray` object will be replaced with a new array if you don't implement the array mutation methods for the property. The details are covered in `NSKeyValueCoding.h`.

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2016-04-04 | Adjusted the image size and added the content related to the mutability of model properties. |
| 2016-03-31 | Adjusted the image size and added the content related to the mutability of model properties. |
|  | Adjusted the image size and added the content related to the mutability of model properties. |
| 2016-02-18 | New document that describes how to bind the UI elements in view controller scenes to an application's model objects. |

