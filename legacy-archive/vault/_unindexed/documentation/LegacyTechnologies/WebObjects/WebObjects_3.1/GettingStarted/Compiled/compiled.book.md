---
title: WebObjects 3.1 Developer Documentation
apple_id: TP40006772
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-11-29'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_3.1/GettingStarted/Compiled/compiled.book.html
archived_at: '2026-07-15T07:48:30.484022Z'
---
> 导航：[总目录](../../../../../../../README.md) · 未编入索引的页面


[!Top](../GettingStartedTOC.md)

# Creating a Compiled Application

---

This chapter shows you how to use Project Builder and WebObjects Builder to include compiled code in a WebObjects application. The application you'll create in this chapter is called Registration. The first page of the Registration application looks like this:!
Registration is similar to the GuestBook application that you created when you worked through the first tutorial in this book, but it's a little more complex. Registration has these additional features:

- It validates the information that the users enter.
- The list of registrants persists between invocations of the application.
- It has multiple submit buttons.
- It has more than one component.

You'll write Registration in the Java programming language. You can also write WebObjects applications in the Objective-C language. Writing an application in Objective-C requires slightly different steps than writing an application in Java. Those differences are noted at the end of the tutorial.

## Table of Contents

[****
: __Deciding to use compiled code__](Deciding.md#apple-giztm)

[****
: __Set up Project Builder and WebObjects Builder__](SetUp.md#apple-ge3dm)

[****
: __Create a project__](NewProject.md#apple-gi2dk)

[****
: The main method](mainMethod.md#apple-hayde)[****
: Frameworks](Frameworks.md#apple-g43tq)

[****
: __Create custom classes__](CustomClasses.md#apple-gy4dooa)

[****
: Implement RegistrationManager](CustomClasses.md#apple-gy4dqmi)[****
: Implement Person](Person.md#apple-gy4tsoa)

[****
: __Implement Application.java__](Application.md#apple-g4ydmny)

[****
: __Create the Main component__](MainComponent.md#apple-geydenq)

[****
: Create the Main component's interface](MainComponent.md#apple-geydomq)[****
: Create a dictionary class](MainComponent.md#apple-geydemy)[****
: Create and bind variables](MainComponent.md#apple-g43to)[****
: Create multiple submit buttons](MainComponent.md#apple-geydmma)[****
: Implement the methods](MainComponent.md#apple-geytimq)[****
: Bind the submit buttons](MainComponent.md#apple-gezdeoi)

[****
: __Create a second component__](Registrants.md#apple-he2to)

[****
: Create the component's interface](Registrants.md#apple-he4ds)[****
: Create variables](Registrants.md#apple-geydamq)[****
: Bind elements to the script](Registrants.md#apple-geydcma)[****
: Implement Registrants](Registrants.md#apple-g44de)[****
: Add Registrants.wo to the project](Registrants.md#apple-geydgoi)

[****
: __Build the application__](Build.md#apple-ha4dm)

[****
: __Run the application__](RunApp.md#apple-ha2di)

[****
: __Deploy the application__](Deploy.md#apple-geytioi)

[****
: __Notes for Objective-C Developers__](ObjCNotes.md#apple-heztk)

[****
: Creating an Objective-C project](ObjCNotes.md#apple-g44tiny)[****
: Objective-C main function](ObjCNotes.md#apple-g44tsmi)[****
: Subclassing WebObjects classes](ObjCNotes.md#apple-ge4ds)[****
: Accessing compiled code from a script](ObjCNotes.md#apple-geydena)[****
: Accessing script methods from compiled code](ObjCNotes.md#apple-haydg)[****
: Using C and C++ in WebObjects applications](ObjCNotes.md#apple-ha2tk)

[!First Section](Deciding.md)
