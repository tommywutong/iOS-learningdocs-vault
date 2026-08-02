---
title: Mail Stationery Release Notes for OS X v10.5
apple_id: TP40004699
resource_type: Release Note
platform: macOS
topic: Data Management
technology: null
published: '2006-10-02'
source_url: https://developer.apple.com/library/archive/releasenotes/AppleApplications/MailStationeryRelNote/index.html
archived_at: '2026-07-18T02:50:20.480052Z'
---
> 导航：[总目录](../../README.md) · [releasenotes](../../_indexes/releasenotes.md)



# Mail Stationery Release Notes for OS X v10.5

Mail Stationery is a new feature in Mac OS v10.5. Each template by the Mail application allows users to customize their email messages. Each stationery template is a bundle that contains all the files needed to display the stationery.

#### Contents:

- [Stationery Bundles](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojzfvcg63tujruw422fnrsw2zlooreuixzr)
- [The Stationery Folder](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2dmojzfvcg63tujruw422fnrsw2zlooreuixzrge)

### Stationery Bundles

### The Description Property List

The `Description.plist` file is a property list that contains a table of contents describing all the other files in the stationery folder. It resides in the Resources folder of the stationery bundle.

The description property list contains a dictionary with the following keys:

- Stationery Name—The name of the stationery as it is displayed to the user. Required.
- Stationery ID—The unique identifier for the stationery. It is suggested that Mail create this entry. Required.
- HTML File—The name of the HTML file, including any extensions. Required.
- Thumbnail Image—The name of the file containing the thumbnail image of the stationery. This key is optional. If it is missing, Mail creates the thumbnail image, saves it into the stationery bundle, and adds the entry to the Description.
- Background Images—An array of the names of images referenced as background images in HTML. Required if the stationery has any background images.
- Tiled Background Image—The name of the background image for the HTML `BODY`. Required if the stationery has a `BODY` background image.
- Tiled Background Offset—A dictionary with information about the positioning of the `BODY` background image. This dictionary has four possible keys, Pixels X, Pixels Y, Fraction X, and Fraction Y. The first two keys correspond to CSS absolute values, and the latter two to CSS percentage values. Fraction values are float values from 0 to 1. If this entry is missing or incomplete, the values default to Fraction X being `0.5` and Pixels Y being `0`, corresponding to the CSS entry `background-position: 50% 0)`.
- Images—An array of the names of any local images referenced in `IMG` tags in the HTML. Required if the station has any local images other than background images.
- Composite Images—An array of dictionaries. Each dictionary represents one composite image referred to in the stationery's HTML file. See Composite Images for more information about the `IMG` tag and the component images. Each composite image referred to in the HTML file must have an entry. Each of the keys described below is required if the image the key identifies is present.

  - Composite Name—The value of the `SRC` attribute in the `IMG` tag that represents the composite image.
  - Base Image—The filename of the image that forms the base, or background, of the composite image.
  - Overlay Image—The filename of the image to be used as the top layer of the composite image.
  - Masks—An array of dictionaries; each corresponding to one mask file. The dictionaries are in left-to-right order of the drop zones they describe. For values that involve a coordinate system, the origin is assumed to be at the lower-left corner of the mask image, and the units are in pixels. Each mask dictionary should have the following keys:

    - Filename—The filename of the mask image.
    - Drop Zone Offset—The position of the lower-left corner of the bounding box containing the visible drop zone. This is an array of integers (x,y).
    - Drop Zone Angle—The angle, a float value measured in degrees, through which the user’s picture is rotated. Angles are measured counterclockwise.
    - Drop Zone Size—The width and height of the bounding box containing the visible drop zone. This is an array of integers (width, height).

### The HTML File

The HTML file defines the content of the stationery. It can contain any valid HTML that displays correctly in all the email clients. It should not contain any JavaScript. The following sections describe other types of content and HTML elements that can be used in the HTML file.

### HTML Content

By default, the content of the stationery is not editable by the user. Each region of the document that the user edits must be surrounded by an element, such as `DIV` or `SPAN`, with the `contenteditable` attribute set to `YES`.

This user editable element should have an attribute `apple-content-name`, whose value is a label for the editable section. These labels are used to indicate how the user's content is transfered when the user switches from one stationery to another. The standard values used in Apple's stationery are `body` and `title`. When the user switches from one stationery to another, the `body` content, if the user has edited it, is transfered to the `body` element of the new stationery, and likewise for `title`.

Precautions must be taken to ensure compatibility with common email client apps, which are often much less capable than most web browsers.

### Dynamic Elements

Dynamic elements are placeholders that can be inserted in the HTML file of the stationery. When the stationery is loaded into the New Message window, the dynamic element is replaced by static content. A dynamic element is represented by a `SPAN` element with the class name `AppleStationeryDynamicElement`. Any HTML contained in the `SPAN` element is discarded when the stationery is loaded—except in the case where desired content cannot be inserted. In that case, the contents of the `SPAN` is displayed. The `SPAN` tag must also have an `apple-content-type` attribute that specifies what the replacement content is. For example, a value of "full-name" for `apple-content-type` specifies that the dynamic element can be replaced by the user's full name. The following values for `apple-content-type` are available:

|  |  |
| --- | --- |
| **`full-name`** | : User’s full name from the Me card in Address Book. |
| **`first-name`** | : User’s first name from the Me card in Address Book. |
| **`email`** | : The email address of the account being used to send the message. |
| **`date`** | : The current date. |

A dynamic element of type `date` must also have a `date-format` attribute. Its value is a format string as used by `NSCalendarDate`.

### Images

Local images that you supply as resources in the stationery bundle and reference in `IMG` tags are embedded in the message when it's sent. The URL in each `IMG` tag or background attribute is a path relative to the bundle's Resources folder. All `IMG` elements need width and height attributes with absolute, not relative, values.

Background images that are referenced in the description property list are also be embedded in the message when it is sent. These images are very similar to local images, but are not specified in an `IMG` tag, and have a different key in the Description file.

### Composite Images

Composite images provide a way for templates to include images supplied by the user in more attractive and complex ways than ordinary messages. A composite image provides a static background image containing specific regions where the user can drop his or her own pictures. The user's pictures are sized and rotated as needed to fit the drop zones. After the user’s pictures have been layered on top of the base or background image, an overlay image, usually mostly transparent, may be composited on top if desired.

A composite image is specified in the HTML with an `IMG` tag whose `src` attribute is the name of the composite image. The path may not containing a trailing slash. This name is not a filename, but is the same as the Composite Name given in the description property list. Because the end user may see this name, it should be something appropriate for the user to see. The `IMG` tag also has the class name `AppleCompositeImage`.

Each mask image defines a region in which the user can drop a picture. The only data in the mask that is used is the alpha channel. When the user drops an image in the drop zone, the image is rotated by the drop zone angle specified in the description property list. It is then sized (maintaining its proportions) using the drop zone size, and positioned using the drop zone offset from the Description file. Next, the alpha from the mask is set as the alpha for the user's image.

If there is more than one mask image, providing more than one drop zone for user images, the zones allow the user images to appear to overlap. To achieve this effect, the mask images are used to crop the user images so they don't actually overlap. If there is an overlay image, it is be layered on top to produce the final composite image. When the message is sent, the single composite image is sent as part of the message. The individual components are not sent.

### Images

Images referenced by `IMG` tags or as background images are included in the Resources folder of the stationery bundle. They should also be listed in the Images entry in the description property list. When the message is sent, the data for these images is embedded in the message.

### Composite Images

If the stationery HTML file contains any references to composite images, the files used to produce the composite image are included in the Resources folder of the composite images section of the stationery bundle. They are identified with the Base Image, Overlay Image, and Masks keys in the `Description.plist` file, as described above.

### Thumbnail Image

Each stationery bundle should contain a thumbnail image of the stationery. If the thumbnail image is not present, Mail creates one and inserts an entry for it in the description property list. The thumbnail image should have dimensions 69 x 90 pixels.

### The Stationery Folder

Stationery bundles are stored in `/Library/Application Support/Apple/Mail/Stationery`. Inside this Stationery folder are folders that group the stationeries into categories. Each category folder contains stationery bundles.

The Stationery folder and each category folder contains a file named `TableOfContents.plist`. The file is initially optional because Mail constructs it or updates it when necessary. If new stationery bundles or new category folders are added without adding entries for them in the table of contents files, Mail automatically adds them to the appropriate table of contents file. However, it may be desirable to add entries manually for new stationery bundles and categories in order to control the order of presentation and the names presented to the user.

### Stationery Table of Contents

The table of contents file in the Stationery folder contains an an array of dictionaries, each of which represents one category folder. The order of the entries in the dictionary defines the order in which the categories are displayed to the user.

The dictionary representing a category has three keys, although Mail generates two of them automatically if they're missing. The required entry is Folder Name, which gives the filename of the category folder. The name Custom (including variations of case) is reserved and should not be used as a category folder name. The other entries are Display Name and Category ID. If Display Name is missing, Folder Name is used as the display name, and if Category ID is missing, a unique ID string is provided.

### Category Table of Contents

The table of contents file in a category folder contains an an array of dictionaries, each of which represents one stationery bundle. The order of the entries in the dictionary defines the order in which the stationeries are be displayed to the user.

The dictionary representing a stationery has four keys. The required entry, Folder Name, gives the filename, including the mail stationery extension, of the stationery bundle. The other three entries are Display Name, Thumbnail Image, and Stationery ID. If any of these last three entries are missing, Mail looks for them in the stationery description property list and add them to the table of contents. If the Stationery ID isn't found, Mail generates one.
