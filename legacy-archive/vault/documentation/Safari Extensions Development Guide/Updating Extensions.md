---
title: Safari Extensions Development Guide
apple_id: TP40009977
resource_type: Guide
platform: Safari|macOS
topic: null
technology: Safari Extensions
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Tools/Conceptual/SafariExtensionGuide/UpdatingExtensions/UpdatingExtensions.html
archived_at: '2026-07-27T06:57:07.802396Z'
---
> 导航：[总目录](../../README.md) · [documentation](../../_indexes/documentation.md) · [Safari Extensions Development Guide](About%20Safari%20Extensions.md)


[Next](Document%20Revision%20History.md)[Previous](Distributing%20Your%20Extension.md)

# Updating Extensions

Your extension should provide a way for Safari to automatically check for updates and offer to download and install an update when one becomes available.

To enable automatic updates, create a text file with the `.plist` file extension and put it on a web server, then include the URL of the file in the Update Manifest field of Extension Builder. The `.plist` file is an XML file with this basic structure:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>Extension Updates</key>
   <array>
     <dict>
       <key>CFBundleIdentifier</key>
       <string>com.yourCompany.safari.yourExtensionName</string>
       <key>Developer Identifier</key>
       <string>YourCertificateID</string>
       <key>CFBundleVersion</key>
       <string>Your current bundle version</string>
       <key>CFBundleShortVersionString</key>
       <string>Your current display version</string>
       <key>URL</key>
       <string>Your-.safariextz-URL</string>
     </dict>
   </array>
</dict>
</plist>
```

Copy the structure, but replace the contents of the `<string>` elements with the data for your extension, leaving all other elements exactly as shown:

- If your Developer ID is shown in Extension Builder as

  `Safari Developer: (12A345BCDE) you@yourmail.com`

  then `YourCertificateID` for the update manifest is `12A345BCDE`.
- The value you supply for `Your-.safariextz-URL` must be a valid URL from which to download the current version of your extension. Be sure your web server associates the `.safariextz` file extension with the MIME type `application/octet-stream`. For more information, see [Putting Your Extension on a Web Server](Distributing%20Your%20Extension.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tsnzxfvbuqmjzfvjvomi).

If you have more than one extension, you can maintain a single update manifest for all of them. The form for multiple extensions is:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
   <key>Extension Updates</key>
   <array>
      <dict>
        <key>CFBundleIdentifier</key>
        <string>com.yourCompany.safari.firstExtensionName</string>
        ...
      </dict>
      <dict>
        <key>CFBundleIdentifier</key>
        <string>com.yourCompany.safari.nextExtensionName</string>
        ...
      </dict>
   </array>
</dict>
</plist>
```

Include one `<dict>` element inside the `<array>` element for every extension.

[Next](Document%20Revision%20History.md)[Previous](Distributing%20Your%20Extension.md)
