---
title: Getting Started with Apple Applications
apple_id: TP30001084
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-08-10'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_AppleApplications/_index.html
archived_at: '2026-07-18T02:39:21.169240Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Apple publishes a variety of applications for the Macintosh platform, many of which are distributed free with Macintosh computers.

If you are a plug-in developer, you can create a visual effect plug-in for either the Macintosh or the Windows version of iTunes, Apple’s music management software, that presents visual effects while music is playing. Plug-ins for iTunes are written in C.

If you are a content developer, you can create new widgets for Dashboard, an environment designed to keep useful information at your fingertips. Dashboard widgets are built using standard web technologies, like HTML, CSS, and JavaScript.

If you are a hardware developer, you can build XML printing preset files for iPhoto, Apple’s still photo management software, to enhance its compatibility with your printer. Preset files for iPhoto are written in XML.

If you are an application developer, your application can:

- Access the data in AddressBook, Apple’s centralized database for the user’s contact and other personal information
- Import and export projects to and from Final Cut Pro, Apple’s professional video editing software, using the Final Cut Pro XML Interchange Format
- Exchange documents with Keynote, Apple’s presentation software, using the Keynote XML File Format (APXL)

### Start Here

If you plan to work in Cocoa, Apple’s object-oriented programming environment, read [Cocoa Fundamentals Guide](../../documentation/Cocoa/Cocoa%20Fundamentals%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzu) to learn about the concepts behind Cocoa and get started with Cocoa development.

If you are creating a Dashboard widget, you should be familiar with the web technologies present in Web Kit, the underlying technology behind Dashboard. [About Safari JavaScript](../../documentation/Apple%20Applications/WebKit%20DOM%20Programming%20Topics/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgmydambrgiztc) discusses using JavaScript in Web Kit and, by extension, Dashboard widgets.

To link your application with AddressBook, you need to add C or Objective-C code to it. To exchange data with Keynote or Final Cut Pro, your application needs to be able to import or export XML files in the required format. Apple provides C functions in Mac OS that help your code parse XML.

If your new or existing application is going to exchange data with Keynote or Final Cut Pro, you need to understand the facilities that Apple provides to parse XML. Start by reading [Introduction to XML](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFXML/CFXML.html#//apple_ref/doc/uid/10000138) to understand the XML syntax and learn how to call functions in the Mac OS that extract data from XML files.

### Choose a Learning Path

Regardless of whether you plan to develop a plug-in for a Macintosh application or add data-exchange code to your own application, you will need to choose a suitable programming environment. To learn about Apple’s recommended programming tool set for Mac OS, read the ADC topic page for [XCode](https://developer.apple.com/tools/xcode/). It describes the features of Xcode and tells you where to get the software you need.

#### Enhancing an Apple Application With a Plug-In or Widget

- If you are creating a new widget, either as an add-on for an existing application or as a new stand-alone application, read Dashboard Programming Guide to learn how to create and add useful features to a widget.
- If you are creating a visual effect plug-in for iTunes, and you are programming for Mac OS, read Technical Note TN2016, [iTunes Visual Plug-ins](https://developer.apple.com/technotes/tn/tn2016.html), to understand the general structure of a visual effect plug-in and learn how iTunes discovers and registers it. Windows developers should read Technical Note TN2098, [iTunes Visual Plug-ins for Windows](https://developer.apple.com/technotes/tn2002/tn2098.html).

#### Exchanging Data With an Apple Application

- If you want your application to access user data stored in AddressBook, read [Address Book Programming Guide for Mac](../../documentation/User%20Experience/Address%20Book%20Programming%20Guide%20for%20Mac/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqgeyto2i). It describes the Mac OS Address Book and provides references in both Procedural and Objective C. If you are working in Cocoa, you should also read [Address Book Objective-C Reference Collection](https://developer.apple.com/documentation/addressbook) to learn about the Objective-C framework where address data is stored.
- If you want your application to import and export projects to and from Final Cut Pro, read the document [Final Cut Pro XML Interchange Format](../../documentation/Apple%20Applications/Final%20Cut%20Pro%207%20XML%20Interchange%20Format.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnbz) to learn about the interchange format and see examples of three possible applications—enhancing a batch list, simplifying subtitling, and helping users choose effect parameters.
- If you want your application to exchange documents with Keynote, read [Developer Opportunities Using Keynote and APXL](https://developer.apple.com/appleapplications/keynote-apxl.html) to learn how your application can use Keynote’s display capabilities. You’ll also find several links to more detailed technical documents, including a link to the formal APXL definition.

#### Writing a Printer Preset File for iPhoto

If you are creating a printer preset file for iPhoto, read [Creating Printing Presets for iPhoto](../../documentation/Printing/Creating%20Printing%20Presets%20for%20iPhoto/Creating%20Printing%20Presets%20for%20iPhoto.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydqnjz) to learn about the file structure, which is simply a text file written in XML, and see a sample listing.

### Next Steps

The [Apple Applications Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000418) links to several high-level resource pages, which you can bookmark for easy access.

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000418)

  Conceptual and how-to information for Apple applications.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000418)

  Focused, detailed descriptions in reference format for Apple applications.
- [Release Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000872-TP30000418)

  Late-breaking news and highlights of new or changed features in the latest releases of relevant Apple applications.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000418)

  Sample applications demonstrating several techniques for communicating with Apple applications.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000418)

  Technically detailed documents on issues related to Apple applications.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000418)

  Programming tips, code snippets, and FAQs by Apple’s support engineers.
- Mailing Lists

  The Dashboard Development List ([dashboard-dev](http://lists.apple.com/mailman/listinfo/dashboard-dev)) is a list devoted to issues facing widget developers.

