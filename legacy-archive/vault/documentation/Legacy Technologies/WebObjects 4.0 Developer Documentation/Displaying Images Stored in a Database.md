---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/DatabaseImages.html
archived_at: '2026-07-15T08:01:02.023843Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Displaying Images Stored in a Database

##  Synopsis

Describes how to display images stored in a database.

##  Discussion

It is often useful to serve images from the database through the Web application server instead of storing copies of the images in the Web server's document directory. WebObjects 4.0 adds enhancements to WOImage and WOActiveImage to ease this process.

In the EOModel for the Movies example database, the _TalentPhoto_
class has a _photo_
attribute that stores an NSData representing the photograph image of an actor or director. You can use recent enhancements to the WOImage component to display the image of the actor in an application. This example uses the new "data" and "mimeType" bindings to accomplish this.

The following steps illustrate how to add database-stored images to an application. The example uses the Movies EOModel and a Wizard-generated application. To prepare the example, perform the following steps:

1. Start ProjectBuilder.

2. Create a new "WebObjects Application" project, selecting "Wizard" for assistance and "Java" as the primary language.

3. Choose the "existing model" option and select the Movies.eomodel file.

4. Select the "Talent" Entity.

5. Choose "Selected Record" and "Paginated" for the layout.

6. Include the "firstName" and "lastName" attributes to display, and the "lastName" for the hyperlink.

To add the image, perform the following steps:

1. Open the Main.wo component in WebObjectsBuilder.

2. Add a WOImage component to the WOForm (available from the Dynamic elements toolbar or from the "Elements->WebObjects" menu).

3. In the inspector for the WOImage, add two attributes, one labeled "data" and the other labeled "mimeType."

4. Create the following bindings:

In the data field, enter _talentDisplayGroup.selectedObject.photo.photo._

For mimeType , select "image/gif".

5. Build and run the example. When you select a talent that has an image in the database, the WOImage should display it.

In this example, the data in the database is assumed to be a GIF image. If different image types are stored, you could create an accessory on the class that either stores the type, or determines it on-the-fly and returns the appropriate MIME type.

It is also possible to serve images created on-the-fly by the application. Bind the "data" attribute to a method returning the dynamically generated image. An example of this use is the CreatePlots example in the Developer/Examples/WebObjects/WebScript folder.

##  See Also

· File Upload

· CreatePlots Example Application

· Documentation on WOImage and WOActiveImage Dynamic Elements

##  Questions

· How do I display an image in my application when the image is in the database?

##  Keywords

· WOImage

· WOActiveImage

· Components

· Database Images

· Dynamic Images

##  Revision History

22 July, 1998. Timothy Joransen. First Draft.

19 November, 1998. Clif Liu. Second Draft.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
