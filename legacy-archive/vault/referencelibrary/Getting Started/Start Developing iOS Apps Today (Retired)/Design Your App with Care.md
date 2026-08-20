---
title: Start Developing iOS Apps Today (Retired)
apple_id: TP40013837
resource_type: Guide
platform: iOS
topic: null
technology: null
published: '2013-10-22'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/DesignYourAppwithCare/DesignYourAppWithCare/DesignYourAppWithCare.html
archived_at: '2026-07-18T02:42:46.813007Z'
---
> 导航：[总目录](../../../README.md) · [referencelibrary](../../../_indexes/referencelibrary.md) · [Start Developing iOS Apps Today (Retired)](Document%20Revision%20History.md)



[Back to App Design](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/ApplicationDesign.html)
!
!
!

# Retired Document

__Important:__ This version of _Start Developing iOS Apps Today_ has been retired. The replacement version provides a new, more streamlined walkthrough of the basics. For information covering the same subject area as this page, please see ["App Development Process"](https://developer.apple.com/library/ios/referencelibrary/GettingStarted/RoadMapiOS/AppDevelopmentProcess.html#//apple_ref/doc/uid/TP40011343-CH4-SW1).

# Design Your App with Care

If you are a new to developing iOS apps, you might be wondering where the app development process starts. After devising your initial idea for an app, you need to turn that idea into an action plan for implementing your app. From a design perspective, you need to make some high-level decisions about the best course of action for implementing your ideas. You can then proceed with developing your app.

_iOS App Programming Guide_ explains in detail many of the concepts, architectures, and techniques mentioned in this article.

There are many ways to design an app, and many of the best approaches do not involve writing any code. A great app starts with a great idea that you then expand into a more full-featured product description. Early in the design phase, it helps to understand just what you want your app to do. Write down the set of high-level features that would be required to implement your idea. Prioritize those features based on what you think your users will need. Do a little research into iOS itself so that you understand its capabilities and how you might be able to use them to achieve your goals. Sketch out some rough interface designs on paper to visualize how your app might look.

The goal of your initial design is to answer some very important questions about your app. The set of features and the rough design of your interface help you think about what will be required later when you start writing code. At some point, you need to translate the information displayed by your app into a set of data objects. Similarly, the look of your app has an overwhelming influence on the choices you must make when implementing your user interface code. Doing your initial design on paper (rather than on the computer) gives you the freedom to come up with answers that are not limited by what is easy to do.

Of course, the most important thing you can do before starting your design is read _iOS Human Interface Guidelines._ That book describes several strategies for doing your initial design. It also offers tips and guidance about how to create apps that work well in iOS. _iOS Technology Overview_ describes the capabilities of iOS and how you might use those capabilities to achieve your design goals.

iOS assumes that all apps are built using the Model-View-Controller design pattern. Therefore, the first steps you can take toward achieving this goal are to choose approaches for the data and view portions of your app.

- Choose a basic approach for your data model:

  - __Existing data model code__—If you already have data model code written in a C-based language, you can integrate that code directly into your iOS apps. Because iOS apps are written in Objective-C, they work just fine with code written in other C-based languages. Of course, there is also a benefit to writing an Objective-C wrapper for any code that is not Objective-C.
  - __Custom objects data model__—A custom object typically combines some simple data (strings, numbers, dates, URLs, and so on) with the business logic needed to manage that data and ensure its consistency. Custom objects can store a combination of scalar values and pointers to other objects. For example, the Foundation framework defines classes for many simple data types and for storing collections of other objects. These classes make it much easier to define your own custom objects.
  - __Structured data model__—If your data is highly structured—that is, it lends itself to storage in a database—use Core Data (or SQLite) to store the data. Core Data provides a simple object-oriented model for managing your structured data. It also provides built-in support for some advanced features like undo and iCloud. (SQLite files cannot be used in conjunction with iCloud.)
- Decide whether you need support for documents:

  The job of a document is to manage your app’s in-memory data model objects and coordinate the storage of that data in a corresponding file (or set of files) on disk. Documents normally connote files that the user created but apps can use documents to manage files that are not user facing too. One big advantage of using documents is that the `UIDocument` class makes interacting with iCloud and the local file system much simpler. For apps that use Core Data to store their content, the `UIManagedDocument` class provides similar support.
- Choose an approach for your user interface:

  - __Building block approach__—The easiest way to create your user interface is to assemble it using existing view objects. Views represent visual elements such as tables, buttons, text fields, and so on. You use many views as-is but you can also customize the appearance and behavior of standard views as needed to meet your needs. You can also implement new visual elements using custom views and mix those views freely with the standard views in your interface. The advantages of views are that they provide a consistent user experience and they allow you to define complex interfaces quickly and with relatively little code.
  - __OpenGL ES–based approach__—If your app requires frequent screen updates or sophisticated rendering, you probably need to draw that content directly using OpenGL ES. The main use of OpenGL ES is for games and apps that rely heavily on sophisticated graphics and therefore need the best performance possible.

After you formulate your action plan, it is time to start coding. If you are new to writing iOS apps, it is good to take some time to explore the initial Xcode templates that are provided for development. These templates greatly simplify the work you have to do and make it possible to have an app up and running in minutes. These templates also allow you to customize your initial project to support your specific needs more precisely. To that end, when creating your Xcode project, you should already have answers to the following questions in mind:

- __What is the basic interface style of your app?__ Different types of app require different sets of initial views and view controllers. Knowing how you plan to organize your user interface lets you select an initial project template that is most suited to your needs. You can always change your user interface later, but choosing the most appropriate template first makes starting your project much easier.
- __Do you want to create a universal app or one targeted specifically for iPad or iPhone?__ Creating a universal app requires specifying different sets of views and view controllers for iPad and iPhone and dynamically selecting the appropriate set at runtime. Universal apps are preferred because they support more iOS devices but do require you to factor your code better for each platform.
- __Do you want your app to use storyboards?__ Storyboards simplify the design process by showing both the views and view controllers of your user interface and the transitions between them. Storyboards are supported in iOS 5 and later and are enabled by default for new projects. If your app must run on earlier versions of iOS, though, you cannot use storyboards and should continue to use nib files.
- __Do you want to use Core Data for your data model?__ Some types of apps lend themselves naturally to a structured data model, which makes them ideal candidates for using Core Data.

After you install Xcode, configure your iOS development team, and create an app project in Xcode, you can start developing your app. The following phases of app development are common:

1. Start writing your app’s primary code.

   For new apps, you probably want to start creating the classes associated with your app’s data model first. These classes usually have no dependencies on other parts of your app and should be something you can work on initially. You might also want to start playing around with designs for your user interface by adding views to your main storyboard or nib file. From these views, you can also start identifying the places in your code where you need to respond to interface-related changes. If your app supports iCloud, you should incorporate support for iCloud into your classes at an early stage.
2. Add support for app state changes.

   In iOS, the state of an app determines what it is allowed to do and when. App states are managed by high-level objects in your app but can affect many other objects as well, therefore, you need to consider how the current app state affects your data model and view code and update that code appropriately.
3. Create the resources needed to support your app.

   Apps submitted to the App Store are expected to have specific resources such as icons and launch images to make the overall user experience better. Well-factored apps also make heavy use of resource files to keep their code separate from the data that code manipulates. This factoring makes it much easier to localize your app, tweak its appearance, and perform other tasks without rewriting any code.
4. As needed, implement any app-specific behaviors that are relevant for your app.

   There are many ways to modify the way your app launches or interacts with the system. For example, you might want to implement local notifications for a certain feature.
5. Add the advanced features that make your app unique.

   iOS includes many other frameworks for managing multimedia, advanced rendering, game content, maps, contacts, location tracking, and many other advanced features. _iOS Technology Overview_ gives an overview of the frameworks and features you can incorporate into your apps.
6. Do some basic performance tuning for your app.

   All iOS apps should be tuned for the best possible performance. Tuned apps run faster but also use system resources, such as memory and battery life, more efficiently.
7. Iterate.

   App development is an iterative process. As you add new features, you might need to revisit some or all of the preceding steps to make adjustments to your existing code.

[On to Know the Core Objects of Your App](Know%20the%20Core%20Objects%20of%20Your%20App.md)
!
!
!
[Back to App Design](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/RoadMapiOS-Legacy/chapters/ApplicationDesign.html)
!
!
!
