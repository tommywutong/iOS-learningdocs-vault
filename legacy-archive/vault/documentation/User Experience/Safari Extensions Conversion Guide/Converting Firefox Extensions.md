---
title: Safari Extensions Conversion Guide
apple_id: TP40009993
resource_type: Guide
platform: Safari
topic: User Experience
technology: Safari Extensions
published: '2011-07-20'
source_url: https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/SafariExtensionsConversionGuide/Chapters/Firefox.html
archived_at: '2026-07-27T06:57:07.819960Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Extensions Conversion Guide](About%20Safari%20Extensions.md)


[Next](Converting%20Greasemonkey%20Scripts.md)[Previous](Converting%20Chrome%20Extensions.md)

# Converting Firefox Extensions

Both Firefox and Safari provide an extensions API, but the two APIs have substantially different functionality. As you bring your extension to Safari, you may find that some of the features you used in Firefox are in a different place in Safari, or are not available. You may still be able to bring your extension to Safari—consider the core functionality of your extension and determine how you can expose that functionality using the API that is provided. You should also examine the functionality provided in Safari that you didn’t have in Firefox, to understand how you might use it to improve your extension.

To start developing Safari extensions, just enable extensions from the Develop menu; there is no special setup procedure. Safari extensions are written using HTML5, CSS3, and JavaScript; the information stored in RDF and XUL files for Firefox extensions is stored in the `Info.plist` file for Safari Extensions. This file, which you create and edit using Extension Builder, contains all the metadata about your extension and a description of its user interface.

Extension Builder, which is part of Safari, serves as a central tool during every stage of extension development. You use Extension Builder to:

- Create a new extension
- Provide metadata such as your name, website, and a description of the extension
- Set up the user interface for your extension
- Install your extension so that you can test and debug it
- Sign and package your extension for distribution

Safari extensions must be digitally signed before they can be installed. To get your signing certificate, visit the Safari Dev Center.

[Next](Converting%20Greasemonkey%20Scripts.md)[Previous](Converting%20Chrome%20Extensions.md)
