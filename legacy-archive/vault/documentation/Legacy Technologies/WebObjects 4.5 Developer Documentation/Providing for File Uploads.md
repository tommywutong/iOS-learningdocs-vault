---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/WebObjects/Topics/ProgrammingTopics.10.html
archived_at: '2026-07-15T08:09:53.746163Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
Programming Topics

[!](WebObjects%20Programming%20Topics.md) [!](Generating%20a%20Static%20Site.md) [!](Sending%20E-mail%20from%20a%20WebObjects%20Application.md)

#   Providing for File Uploads

##  Synopsis

Discusses how to enable your WebObjects application to upload files.

##  Discussion

Most of today's Web browsers permit the attachment of files to a form submission, useful for such tasks as adding a Microsoft Word document to a resume database or storing a photograph of an employee being added to a company directory. WebObjects 4.0 adds the WOFileUpload component to support RFC 1867, which defines a method of submitting form information using "multipart MIME." Previous versions of WebObjects required additional support that is available from the NeXTanswers on-line support system (see NeXTanswer #2505).

The following browsers work with the WebObjects WOFileUpload component:

- 

  Netscape Navigator 2.x and greater
- 

  Microsoft Internet Explorer version 4.x and greater
- 

  Microsoft Internet Explorer version 3.01, if the "RFC 1867" add-on is installed
- 

  Omnigroup OmniWeb version 2.x and greater
- 

  Other browsers that support RFC 1867

To add file-upload support, you must have the WOFileUpload component in a WOForm. You must also add an additional binding to the WOForm to specify that the browser should use multipart MIME encoding to submit the form information (which includes the attached files).

The following steps illustrate how to add file upload support to your application. The example uses the Movies EOModel and a Wizard-generated application. You will add the capability to upload the image of the
talent
to the application. The image is the
photo
attribute of the
TalentPhoto
object. The
TalentPhoto
object is referenced by the
photo
relationship of the currently selected
talent
.

To prepare the example, perform the following steps:

Start ProjectBuilder.

1. 

   Create a new "WebObjects Application" project, selecting "Wizard" for assistance and "Java" as the primary language.
2. 

   Choose the "Existing Model" option and select the
   Movies.eomodeld
   file.
3. 

   Select the "Talent" Entity.
4. 

   Choose "Selected Record" and "Paginated" for the layout.
5. 

   Include the "firstName" and "lastName" attributes to display, and the "lastName" for the hyperlink.

To add file upload support, perform the following steps:

Open the "Main.wo" component in WebObjectsBuilder.

1. 

   Inspect the WOForm at the bottom of the page.
2. 

   Add an attribute named "enctype" and set its value to "multipart/form-data".
3. 

   Add a variable "filename" of type String to the component.
4. 

   Add a "Custom WebObject" component to the WOForm (available from the Dynamic elements toolbar or from the "Elements->WebObjects" menu).
5. 

   In the inspector for the component, enter "WOFileUpload" for the class name, and add two attributes, one labeled "filePath" and the other labeled "data".
6. 

   Create the following bindings:

|  |  |
| --- | --- |
|   Attributes |   Binding |
|   data |    talentDisplayGroup.selectedObject.photo.photo |
|   filePath |    filename |

7. 

   Build and run the example. You should see a text field and button where the WOFileUpload component was. You can click on the button to select a file. When the form is submitted, the attribute bound to "data" contain the contents of the file being uploaded.

In this example, you should upload "GIF" images that are photographs of people. When you click "Save to Database", the file data is committed to the database as a
BLOB
since the attribute is a NSData object.

##  See Also

- 

  [Displaying Images Stored in a Database](Displaying%20Images%20Stored%20in%20a%20Database.md#apple-ge3tgobz)
- 

  RFC 1867 (available at: http://info.internet.isi.edu:80/in-notes/rfc/files/rfc1867.txt)
- 

  WOFileUpload specification in the _WebObjects Dynamic Element Specifications_

##  Questions

- 

  How do I enable my application to upload files?

##  Keywords

- 

  Upload

##  Revision History

22 July 1998. Timothy Joransen. First Draft.
19 November 1998. Clif Liu. Second Draft.

```

```

---

© 1999 Apple Computer, Inc.

[!](WebObjects%20Programming%20Topics.md) [!](Generating%20a%20Static%20Site.md) [!](Sending%20E-mail%20from%20a%20WebObjects%20Application.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
