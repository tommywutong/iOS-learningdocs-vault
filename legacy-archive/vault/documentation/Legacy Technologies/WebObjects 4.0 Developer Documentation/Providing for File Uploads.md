---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Documentation/Developer/WebObjects/Topics/FileUpload.html
archived_at: '2026-07-15T08:01:11.461998Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[WebObjects Programming Topics](WebObjects%20Programming%20Topics.md)

# Providing for File Uploads

##  Synopsis

Discusses how to enable your WebObjects application to upload files.

##  Discussion

Most of today's Web browsers permit the attachment of files to a form submission, useful for such tasks as adding a Microsoft Word document to a resume database or storing a photograph of an employee being added to a company directory. WebObjects 4.0 adds the WOFileUpload component to support RFC 1867, which defines a method of submitting form information using "multipart MIME." Previous versions of WebObjects required additional support that is available from the NeXTanswers on-line support system (see NeXTanswer #2505).

The following browsers work with the WebObjects WOFileUpload component:

· Netscape Navigator 2.x and greater

· Microsoft Internet Explorer version 4.x and greater

· Microsoft Internet Explorer version 3.01, if the "RFC 1867" add-on is installed

· Omnigroup OmniWeb version 2.x and greater

· Other browsers that support RFC 1867

To add file-upload support, you must have the WOFileUpload component in a WOForm. You must also add an additional binding to the WOForm to specify that the browser should use multipart MIME encoding to submit the form information (which includes the attached files).

The following steps illustrate how to add file upload support to your application. The example uses the Movies EOModel and a Wizard-generated application. You will add the capability to upload the image of the _talent_
to the application. The image is the _photo_
attribute of the _TalentPhoto_
object. The _TalentPhoto_
object is referenced by the _photo_
relationship of the currently selected _talent_
.

To prepare the example, perform the following steps:

1. Start ProjectBuilder.

2. Create a new "WebObjects Application" project, selecting "Wizard" for assistance and "Java" as the primary language.

3. Choose the "Existing Model" option and select the Movies.eomodeld file.

4. Select the "Talent" Entity.

5. Choose "Selected Record" and "Paginated" for the layout.

6. Include the "firstName" and "lastName" attributes to display, and the "lastName" for the hyperlink.

To add file upload support, perform the following steps:

1. Open the "Main.wo" component in WebObjectsBuilder.

2. Inspect the WOForm at the bottom of the page.

3. Add an attribute named "enctype" and set its value to "multipart/form-data".

4. Add a variable "filename" of type String to the component.

5. Add a "Custom WebObject" component to the WOForm (available from the Dynamic elements toolbar or from the "Elements->WebObjects" menu).

6. In the inspector for the component, enter "WOFileUpload" for the class name, and add two attributes, one labeled "filePath" and the other labeled "data".

7. Create the following bindings:

|  |  |
| --- | --- |
|   Attributes |   Binding |
|   data |   _talentDisplayGroup.selectedObject.photo.photo_ |
|   filePath |   _filename_ |

8. Build and run the example. You should see a text field and button where the WOFileUpload component was. You can click on the button to select a file. When the form is submitted, the attribute bound to "data" contain the contents of the file being uploaded.

In this example, you should upload "GIF" images that are photographs of people. When you click "Save to Database", the file data is committed to the database as a _BLOB_
since the attribute is a NSData object.

##  See Also

· Displaying Images Stored in a Database

· RFC 1867 (available at: http://info.internet.isi.edu:80/in-notes/rfc/files/rfc1867.txt)

· WOFileUpload Dynamic Element

##  Questions

· How do I enable my application to upload files?

##  Keywords

· File Upload

##  Revision History

22 July 1998. Timothy Joransen. First Draft.
19 November 1998. Clif Liu. Second Draft.

```

```


Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
