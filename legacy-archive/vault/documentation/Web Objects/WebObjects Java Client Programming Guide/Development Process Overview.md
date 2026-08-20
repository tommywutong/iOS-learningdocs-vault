---
title: WebObjects Java Client Programming Guide
apple_id: TP30001017
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2005-08-11'
source_url: https://developer.apple.com/library/archive/documentation/WebObjects/DesktopApplications/PuttingItAllTogether/PuttingItAllTogether.html
archived_at: '2026-07-18T02:18:40.211511Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects Java Client Programming Guide](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)


[Next](Java%20Client%20Concepts.md)[Previous](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)

# Development Process Overview

Direct to Java Client is composed of many complex technologies: the rule system, Enterprise Objects, the WebObjects frameworks, and Java Swing, to name a few. Once you have a basic understanding of these technologies, however, you’ll be able to build full-featured applications at a rapid rate. This chapter provides a recommended workflow and provides a narrative of the Java Client development process.

You might want to refer back to this chapter as you progress through the rest of the book.

A good workflow is essential to successful WebObjects application development. The recommended workflow in any WebObjects application is as follows:

1. Write specifications for the application.
2. Design and build the enterprise object models in EOModeler.
3. Test the models with Direct to Web or Direct to Java Client.
4. Refine the models appropriately.
5. Define access levels.
6. Design application flow.
7. Identify tasks.
8. Implement.

These steps are expanded on in the following sections.

A specification document for an application includes both high-level summaries of the application’s requirements and goals, as well as low-level implementation details. A specification should minimally answer these questions:

- What is the purpose of the application (high-level summary)?
- Whom does the application help (audience)?
- What are the chief goals of the application (in order of priority)?
- What problems will the application address?
- What won’t the application do (limitations)?
- What are the target platforms for the application (system requirements)?
- How will the application be installed?
- How will users update the client application?
- What are the performance requirements of the application?
- What are the application’s features (list the key items of each feature)?
- How is the application designed?
- What are the key user interface elements?
- What are the application’s key algorithms?
- How will the application be tested?

The work necessary in this step differs greatly depending on your data source. If the data for the application already exists, you can use EOModeler’s reverse engineering feature to build an EOModel from an existing data source. All that you need to do is set delete rules and optionality for relationships and determine which attributes are class properties or client-side class properties.

However, if you are starting from the beginning, you need to design the database before making model-specific adjustments. Specifically, you need to determine:

- the database tables (model entities)
- the database columns (model attributes)
- the relationships between tables

Then, you can customize the model with Enterprise Objects–specific settings such as optionality, delete rules, and class properties. You should try to follow these data modeling recommendations:

- The model’s relationships should be modeled in both directions to support robust searching capabilities (each relationship should have an inverse relationship).
- The model should not include any stored procedures or derived attributes in order to preserve data source-independence.
- Some of the model’s relationships should be mandatory to enforce business logic rules.
- Generally, the model should provide a solid foundation for the application’s business logic.
- The application should rely on the automatic primary-key generation features of Enterprise Objects.

The WebObjects project types Direct to Web Application and Direct to Java Client Application are good for testing your model. While EOModeler performs consistency checks on your model when you save it, it doesn’t guarantee that the model will actually work well. In this step, create either a Direct to Web Application or a Direct to Java Client Application, select your model or models, and experiment with adding data to your data source with each application.

If you encounter abnormal behaviors, refine the models, build and run the application again, and continue to test. Iterate through this process until you have a well-designed model.

Defining different access levels in your application is not a necessary part of the design process, but thinking about it early saves you time when it’s time to implement access controls. In this task, you should define the groups of users and what if any parts of the application should be restricted to a certain group or groups.

Although your application will ultimately be composed of hundreds of tasks, it’s important to identify the application’s primary tasks. Among other things, this helps you divide development work. In the JCRealEstatePhotos example, the primary tasks include

- importing photos
- searching for photos
- downloading photos

Within each primary task are many subtasks. The importing photos task includes subtasks such as choosing the photos to import and assigning them to a particular listing. The searching for photos task requires writing a user interface so users can provide search criteria, generating qualifiers from the search criteria, performing the fetch, and returning the results. The downloading photos phase includes adding photos to a downloads basket, selecting a downloads location, and performing the download.

In Direct to Java Client development, the most important part when identifying the application’s tasks is identifying user interfaces that Direct to Java Client doesn’t automatically provide you. This lets you plan development cycles to write nib files or custom controllers for custom user interfaces.

The decisions you make about application flow will most directly affect your application’s users. You have to think about how users will access the tasks you defined in the previous step. You should answer these questions:

- What can users see and do before authenticating?
- What can users see and do after authenticating?
- What functions are available from the application’s menus?
- Fundamentally, how do users _use_ the application?

Finally, after developing a good design for your application, can begin the implementation phase.

This section gives you a high-level overview of how a Direct to Java Client application works. It’s provided as an index of programming concerns. It identifies some common issues and questions developers have when building Java Client applications and provides links to sections within this document that provide answers.

When a Direct to Java Client application launches, it asks the rule system for the specifications and actions available to the application. Specifically, it asks for the default specifications as these are the first things displayed in the user interface. You can change the available and default specifications and actions by writing rules, as described in [The Documents Menu](Restricting%20Access%20to%20an%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhawviucykjcummzy) and [The Default Query Window](Restricting%20Access%20to%20an%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhawviucykjcumnbq).

The default Direct to Java Client application provides a query window for the application’s main entities immediately after the application launches. A common design pattern is to provide a login window instead. A login window implementation is discussed in [Building a Login Window](Building%20a%20Login%20Window.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgewviubr) and examples are provided in both the JCDiscussionBoard and JCRealEstatePhotos examples.

The rule system determines what the application’s main entities are using the heuristics described in [Entities Pane](Inside%20Assistant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgewviucykjcummzx). Rather than change how the rule system interprets an entity using Assistant, you should change your data model so that the rule system interprets that entity as the type of entity you want.

Direct to Java Client query windows have one particularly noticeable limitation: They provide query fields only for an entity’s to-one relationships. So, if you want to allow users to query on an entity’s to-many relationships, you’ll have to provide a custom query controller.

The default application produced by Direct to Java Client is probably not exactly what you want. You can use the Direct to Java Client Assistant to easily customize the application. It allows you to choose which properties are displayed in the application’s user interfaces, how those properties are aligned and placed, what types of associations the properties map to, and more. Assistant is described in [Inside Assistant](Inside%20Assistant.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgewviubr).

Assistant customizes applications by writing rules to the application’s `user.d2wmodel` file. It owns this file and you should never edit it. You can add custom rules to a file named `d2w.d2wmodel` that you add to projects. Assistant won’t touch the rules in that file. You should perform as many customizations in Assistant as you can because the more advanced customization techniques are more difficult, bug-prone, and are less maintainable than just using Assistant.

Although Assistant provides a user interface to configure a good number of the possible rules in a Direct to Java Client application, it is not exhaustive. Some rules that it does not provide editing of are described in [Common Rules](Common%20Rules.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgiwviubr). You can add these rules to an application’s `d2w.d2wmodel`.

After performing initial customizations of the user interface using Assistant, you want to write your application’s business logic. The more advanced customization techniques make it more difficult to adapt your application to changes in your data model and business logic, so you should try to lock both down at this point. See [Business Logic Partitioning](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcummzr) and [Prepare Application for Business Logic](Enhancing%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgmwviucykjcummjrha).

After you’ve used Assistant to customize the client application, you can consider other customization techniques. You can freeze XML, as described in [Freezing XML User Interfaces](Freezing%20XML%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgmwviubr), which allows you to manually edit the XML hierarchy for a particular user interface in an application. You can build custom interfaces using Interface Builder or by building custom controller classes, as described in [Nondirect Java Client Development](Nondirect%20Java%20Client%20Development.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgqwviubr) and [Building Custom Controllers With XML](Building%20Custom%20Controllers%20With%20XML.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqguwviubr). You may also want to consider using nib files within dynamically generated user interfaces, as described in [Mixing Static and Dynamic User Interfaces](Mixing%20Static%20and%20Dynamic%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgqwviubr). You can also explicitly ask the controller factory to generate user interfaces, as described in [Mixing Static and Dynamic User Interfaces](Mixing%20Static%20and%20Dynamic%20User%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgqwviubr).

Certain kinds of controllers, such as those that display HTML or controllers that use the controller factory, can also be used. See [Using HTML on the Client](Using%20HTML%20on%20the%20Client.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzsgawviubr) and [Generating Controllers With the Controller Factory](Generating%20Controllers%20With%20the%20Controller%20Factory.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhewviubr). If you’ve built Cocoa applications in Interface Builder, you may find that some familiar user interface elements don’t translate when you save Java Client nib files. See [Using and Extending Image Views in Nib Files](Using%20and%20Extending%20Image%20Views%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgywviubr), [Using Pop-up Menus in Nib Files](Using%20Pop-up%20Menus%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrg4wviubr), and [Using Custom Views in Nib Files](Using%20Custom%20Views%20in%20Nib%20Files.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrguwviubr).

If you want to add custom actions to dynamically generated user interfaces, such as form windows and query windows, you add subclasses of those controller classes (subclasses of EOFormController and EOQueryController, for example) to your project, add the actions in those classes, and tell the rule system to use them for particular tasks and entities. This is described in [Extend a Controller Class](Enhancing%20the%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgmwviucykjcummjtg4) and [Adding Custom Actions to Controllers](Adding%20Custom%20Actions%20to%20Controllers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgewviubr).

If you want to disable certain actions in dynamically generated user interfaces, you can just tell the rule system, as described in [Restricting Access to an Application](Restricting%20Access%20to%20an%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqhawviubr).

To add custom menu items to an application, you use D2WComponents and XML descriptions as described in [Adding Custom Menu Items](Adding%20Custom%20Menu%20Items.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrgawviubr). You cannot use Interface Builder to add custom menu items to any type or part of a nondirect Java Client application.

Near the end of the development cycle, you need to think about localization. Depending on how much of the dynamism you preserve when customizing Direct to Java Client applications, localization efforts may require no more time than translating the strings. See [Localizing Dynamic Components](Localizing%20Dynamic%20Components.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzrhawviubr). When you’re ready to deploy the client application, see [Deploying Client Applications](Deploying%20Client%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqg4wviubr) to learn about your options.

If your customers require strict client-server security, you need to learn more about the distribution layer, as described in [The Distribution Layer](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviubr). You probably want to consider using SSL as the distribution channel ([Using SSL](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcumnbu)) and you’ll likely implement some delegates in the distribution layer ([Delegates](The%20Distribution%20Layer.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytamjxfvbuqmzqgiwviucykjcumnbr)).

[Next](Java%20Client%20Concepts.md)[Previous](Introduction%20to%20WebObjects%20Java%20Client%20Programming%20Guide.md)

