---
title: WikiSampleThemeWithJavaScript
apple_id: DTS40007725
resource_type: Sample Code
platform: macOS
topic: System Administration
technology: null
published: '2008-06-02'
source_url: https://developer.apple.com/library/archive/samplecode/WikiServerSampleTheme2/Listings/ReadMe_txt.html
archived_at: '2026-07-18T03:28:15.846605Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [WikiSampleThemeWithJavaScript](WikiSampleThemeWithJavaScript.md)


[Next](theme2.wikitheme-AddDiggLink.js.md)[Previous](WikiSampleThemeWithJavaScript.md)

# ReadMe.txt

```
ÒWikiSampleThemeWithJavaScriptÓ shows how to extend an existing Wiki Theme using JavaScript. 

This sample contains the theme.plist, screen.css, AddDiggLink.js, print.css, and preview.png files. The theme.plist file sets up the basic theme properties, screen.css imports the existing themeÕs CSS styles, AddDiggLink.js adds a "Digg" link to weblog entry pages, print.css imports the default print style sheet, and  preview.png is a thumbnail image for the theme chooser.


Using the Sample
1. In order to install a new Wiki Server theme on Mac OS X Server, copy 
   the *.wikitheme directory into 
   /Library/Application\Support/Apple/WikiServer/Themes/ and verify
   permissions so that the files are readable by the _teamsserver user. 

2. Restart the teams service. Do the following in Terminal:
   sudo serveradmin stop teams;
   sudo serveradmin start teams;

3. Select your new theme from the group settings page.
   http://YOUR_SERVER/groups/GROUP_NAME/settings/

For more information on extending your Wiki Server or installing themes, 
read the documentation in the following PDF:
http://images.apple.com/server/macosx/docs/Extending_Your_Wiki_Server.pdf


Feedback and Bug Reports
Please send all feedback about this sample by connecting to the Contact ADC <http://developer.apple.com/contact/feedback.html> page.
Please submit any bug reports about this sample to the Bug Reporting <http://developer.apple.com/bugreporter> page.
```

[Next](theme2.wikitheme-AddDiggLink.js.md)[Previous](WikiSampleThemeWithJavaScript.md)

