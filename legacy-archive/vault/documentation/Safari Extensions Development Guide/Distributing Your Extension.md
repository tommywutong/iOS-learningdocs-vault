---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/DistributingYourExtension/DistributingYourExtension.html
archived_at: '2026-07-27T06:57:07.795453Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Updating%20Extensions.md)[Previous](Converting%20Other%20Extensions%20and%20Greasemonkey%20Scripts.md)

# Distributing Your Extension

Safari extensions are distributed in the form of a signed, compressed folder with the file extension `.safariextz`. Building and signing your extension using Safari’s Extension Builder tool will create a `.safariextz` file that you can host on your web server. You may also submit the extension for inclusion in Apple’s Safari Extension Gallery, providing users with a one-click installation experience and automatic updates when new versions of your extension are released. Users can then install the extension in either of the following ways:

- By clicking an Install button in the Extensions Gallery.
- By opening the (`.safariextz`) file in Safari. (Safari will prompt the user to confirm the installation.)

__Important:__ These are the only permitted ways to install a Safari extension. You should not attempt to install your extension any other way.

## Putting Your Extension on a Web Server

To make your extension available via a web server:

1. Build and sign the extension in Extension Builder to create a `.safariextz` file.
2. Include a link to a copy of your `.safariextz` folder on your website. Be sure to include a description of what your extension does.
3. Make sure your web server is serving the extension using the MIME type `application/octet-stream`.

   Most web servers maintain a table of file extensions and MIME types, and provide an administrative tool for updating the table. For example, to add a MIME type to an Apache web server, use the `AddType` directive:

   ```
   AddType application/octet-stream .safariextz
   ```

   For IIS web servers, the MIME settings are typically accessed using the MMC by right-clicking the host computer name and choosing Properties, then adding a new MIME setting and file extension.

For more information, consult the vendor’s documentation for your web server, or do a web search for "add MIME type" + YourWebServer + YourVersionNumber.

__Tip:__ If necessary, you can arrange to serve multiple versions of your extension for compatibility with different Safari versions. To do this, set up your download URL as a CGI script (such as PHP, Perl, or Python) that examines the HTTP `User-Agent` header string to determine which version of Safari the user is using, and sends a redirect via the `Location` header to the appropriate `.safariextz` file.

## Submitting Your Extension to the Safari Extensions Gallery

Extensions in the Safari Extensions Gallery are hosted and signed by Apple, which means users can trust that the Safari Extension they are installing is the one you submitted. Only Safari extensions installed from the Safari Extensions Gallery can be updated automatically. To support automatic updating to the version available from the Safari Extensions Gallery, add the following line to your Update Manifest.

```
<key>Update From Gallery</key>
<true/>
```

To submit your extension to the Safari Extensions Gallery go to [https://developer.apple.com/safari/extensions/submission/](https://developer.apple.com/safari/extensions/submission/)

__Important:__ Previously, extensions were not hosted by the Extension Gallery; only a link to your server was provided. If you listed an extension on the Extension Gallery prior to the gallery hosting extensions, you must resubmit your extension to Apple before it will be displayed in the Extension Gallery.

[Next](Updating%20Extensions.md)[Previous](Converting%20Other%20Extensions%20and%20Greasemonkey%20Scripts.md)
