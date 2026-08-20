---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.12.html
archived_at: '2026-07-15T08:09:55.022187Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Sending%20E-mail%20from%20a%20WebObjects%20Application.md) [!](Dealing%20With%20Browser%20Backtracking.md)

#   Displaying Images Stored in a Database

##  Synopsis

Describes how to display images stored in a database.

##  Discussion

It is often useful to serve images from the database through the Web application server instead of storing copies of the images in the Web server's document directory. WebObjects 4.0 adds enhancements to WOImage and WOActiveImage to ease this process.

In the EOModel for the Movies example database, the TalentPhoto class has a
photo
attribute that stores an NSData representing the photograph image of an actor or director. You can use recent enhancements to the WOImage component to display the image of the actor in an application. This example uses the new
data
and
mimeType
bindings to accomplish this.

The following steps illustrate how to add database-stored images to an application. The example uses the Movies EOModel and a Wizard-generated application. To prepare the example, perform the following steps:

Start Project Builder.

1. 

   Create a new WebObjects Application project, selecting Wizard for assistance and Java as the primary language.
2. 

   Choose the "existing model" option and select the
   Movies.eomodeld
   file.
3. 

   Select the Talent entity.
4. 

   Choose Selected Record and Paginated for the layout.
5. 

   Include the
   firstName
   and
   lastName
   attributes to display, and
   lastName
   for the hyperlink.

To add the image, perform the following steps:

Open the
Main.wo
component in WebObjects Builder.

1. 

   Add a WOImage component to the WOForm (available from the Dynamic elements toolbar or from the Elements->WebObjects menu).
2. 

   In the inspector for the WOImage, add two attributes, one labeled
   data
   and the other labeled
   mimeType
   .
3. 

   Create the following bindings:

In the data field, enter
talentDisplayGroup.selectedObject.photo.photo

For mimeType , select image/gif.

1. 

   Build and run the example. When you select a talent that has an image in the database, the WOImage should display it.

In this example, the data in the database is assumed to be a GIF image. If different image types are stored, you could create an accessory on the class that either stores the type or determines it on-the-fly and returns the appropriate MIME type.

It is also possible to serve images created on-the-fly by the application. Bind the
data
attribute to a method returning the dynamically generated image. For an example of this, see the CreatePlots example in the
Developer/Examples/WebObjects/WebScript
folder.

##  See Also

- 

  [Providing for File Uploads](Providing%20for%20File%20Uploads.md#apple-giztknbt)
- 

  CreatePlots Example Application
- 

  WOImage specification in the _WebObjects Dynamic Element Specifications_
- 

  WOActiveImage specification in the _WebObjects Dynamic Element Specifications_

##  Questions

- 

  How do I display an image in my application when the image is in the database?

##  Keywords

- 

  WOImage
- 

  WOActiveImage
- 

  Components
- 

  Database
- 

  Images

##  Revision History

22 July, 1998. Timothy Joransen. First Draft.
19 November, 1998. Clif Liu. Second Draft.

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Sending%20E-mail%20from%20a%20WebObjects%20Application.md) [!](Dealing%20With%20Browser%20Backtracking.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
