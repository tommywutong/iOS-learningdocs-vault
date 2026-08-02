---
title: Cocoa Bindings Programming Topics
apple_id: 10000167i
resource_type: Guide
platform: macOS
topic: General
technology: AppKit
published: '2014-07-15'
source_url: https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaBindings/CocoaBindings.html
archived_at: '2026-07-15T07:11:59.497568Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](What%20Are%20Cocoa%20Bindings.md)

# Introduction to Cocoa Bindings Programming Topics

Cocoa bindings is a collection of technologies you can use in your applications to fully implement a Model-View-Controller paradigm where models encapsulate application data, views display and edit that data, and controllers mediate between the two. Cocoa bindings reduces the code dependencies between models, views and controllers, supports multiple ways of viewing your data, and automatically synchronizes views when models change. Cocoa bindings provides extensible controllers, protocols for models and views to adopt, and additions to classes in Foundation and the Application Kit. You can eliminate most of your glue code by using bindings available in Interface Builder to connect controllers with models and views.

Cocoa bindings is ideal for developers writing new applications who have some familiarity with Cocoa, and for developers of existing applications who want to simply clean up or eliminate their existing glue code. In most cases, Cocoa bindings can be used to replace traditional Cocoa mechanisms such as target-action, delegation, and some data source protocols. However, great care has been taken to ensure that both approaches can be used side by side within the same application.

This document assumes that you have read _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_, _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_ and _[Value Transformer Programming Guide](../Value%20Transformer%20Programming%20Guide/Introduction%20to%20Value%20Transformers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tk2i)_.

The following articles cover key concepts in understanding how Cocoa bindings works:

- [What Are Cocoa Bindings?](What%20Are%20Cocoa%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3telkdjjbeksscjbea) describes the advantages that Cocoa bindings offers developers; provides a brief summary of how they work; and what design patterns you should use to adopt the technology.
- [How Do Bindings Work?](How%20Do%20Bindings%20Work.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3tglkdjjbeksscjbea) describes in detail the technologies supporting Cocoa bindings and how they interact.
- [User Defaults and Bindings](User%20Defaults%20and%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytaojsfvbegskdifceqqy) describes the role of the NSUserDefaultsController and how it works with NSUserDefaults.
- [Providing Controller Content](Providing%20Controller%20Content.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbxfvbegskdifceqqy) describes how to set and modify the content of NSObjectController and its subclasses.
- [Working With a Controller’s Selection](Working%20With%20a%20Controller%E2%80%99s%20Selection.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbwfvbegskdifceqqy) describes how to get a controller’s selection and change the current selection.
- [Bindings Message Flow](Bindings%20Message%20Flow.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbzfvbegskdifceqqy) illustrates the flow of messages between model, view and controller objects in a bindings application.

These articles contain tasks that teach you how to use Cocoa bindings:

- [Creating a Master-Detail Interface](Creating%20a%20Master-Detail%20Interface.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsga4talkcineugqkejbbq) explains how to implement a basic master-detail interface where a table view is used in the master interface to display a collection of objects, and other views used in the detail interface to display the selected object in the collection.
- [Displaying Images Using Bindings](Displaying%20Images%20Using%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydalkcineugqkejbbq) describes the various options when displaying images in columns and contains an example of a custom value transformer.
- [Implementing To-One Relationships Using Pop-Up Menus](Implementing%20To-One%20Relationships%20Using%20Pop-Up%20Menus.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydclkcineugqkejbbq) explains how to implement editable to-one relationship as pop-up menus.
- [Filtering Using a Custom Array Controller](Filtering%20Using%20a%20Custom%20Array%20Controller.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgmydelkcineugqkejbbq) explains how to add a search field to the master interface to filter the objects it displays.
- [Controller Key-Value Observing Compliance](Controller%20Key-Value%20Observing%20Compliance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdiojtfvjvomi) details the properties for which the controller classes provide key-value observing change notifications.
- [Troubleshooting Cocoa Bindings](Troubleshooting%20Cocoa%20Bindings.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdcnbyfvbegskdifceqqy) describes a number of common problems encountered with Cocoa bindings applications and provides methods for correcting the issues.

There are other technologies, not fully covered in this topic, that are fundamental to how bindings work. You may want to read these topics if you want a better understanding of the underpinnings of Cocoa bindings, or if you want to use these technologies independent from bindings. For example, this topic does not explain how to use the methods defined in the key-value observing protocol. Refer to these documents for more details:

- _Developing Cocoa Applications Using Bindings: A Tutorial_ takes you through the steps of building the familiar Currency Converter application using Cocoa bindings.
- _[Cocoa Bindings Reference](../Cocoa%20Bindings%20Reference/Introduction%20to%20Cocoa%20Bindings%20Reference.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ds2i)_ enumerates the classes that support Cocoa bindings and provides descriptions of the bindings for each class, along with the supported options and placeholders.
- _[Key-Value Coding Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueCoding/index.html#//apple_ref/doc/uid/10000107i)_ covers all the features of the key-value coding protocol that allows objects to indirectly access the properties of other objects.
- _[Key-Value Observing Programming Guide](../Key-Value%20Observing%20Programming%20Guide/Introduction%20to%20Key-Value%20Observing%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3to2i)_ covers all the features of the key-value observing protocol that allows objects to observe changes in other objects.
- _[Value Transformer Programming Guide](../Value%20Transformer%20Programming%20Guide/Introduction%20to%20Value%20Transformers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3tk2i)_ describes how to use value transformers to convert values from one type to another.
- _[Sort Descriptor Programming Topics](../Sort%20Descriptor%20Programming%20Topics/Introduction%20to%20Sort%20Descriptors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge3ti2i)_ describes how to use sort descriptors that specify how collections are sorted.
[Next](What%20Are%20Cocoa%20Bindings.md)

