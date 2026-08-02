---
title: FinalCutPro_AppleEvents
apple_id: DTS10004110
resource_type: Sample Code
platform: macOS
topic: Apple Applications
technology: null
published: '2009-07-24'
source_url: https://developer.apple.com/library/archive/samplecode/FinalCutPro_AppleEvents/Listings/English_lproj_FCP_AE_Help_FCP_AE_Help_html.html
archived_at: '2026-07-18T03:08:40.077951Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [FinalCutPro_AppleEvents](FinalCutProAppleEvents.md)


[Next](English.lproj-FCPAEHelp-style-basic.css.md)[Previous](Controller.m.md)

# English.lproj/FCP_AE_Help/FCP_AE_Help.html

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"  "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<!-- This file is a trivial Apple Help document
    See "Apple Help Programming Guide" which can be found at
    http://developer.apple.com/referencelibrary/UserExperience/idxHelpTechnologies-date.html
 -->

<head>
    <title>FinalCutPro AppleEvents Help</title>
    <meta http-equiv="Content-type" content="text/html; charset=utf-8"/>
    <meta name="AppleTitle" content="FinalCutPro_AppleEvents Help"/>
    <meta name="AppleIcon" content="FCP_AE_Help/images/icon.gif"/>
    <link href="style/basic.css" rel="stylesheet" type="text/css" media="all" />
</head>

<body id="finalcutpro_appleevents_help">

    <h1><img id="iconimg" src="images/icon.gif" alt="Icon" height="32" width="32"/>Final Cut Pro  Apple Events</h1>

    <h2>Overview</h2>
    <p>
        FinalCutPro_AppleEvents is a simple test application that allows you to send Apple Events to the currently running instance of Final Cut Pro.
        Final Cut must be started beforehand.
    </p>
    <p>
        The possible Apple Events are the custom events defined in the <a href="http://developer.apple.com/documentation/AppleApplications/Reference/FinalCutPro_XML" title="Final Cut Pro XML Interchange Format">Final Cut Pro XML Interchange Format</a> document.
    </p>

    <h2>Other Uses</h2>
    <p>
        This application can also be used a simple driver for trying out pieces of FCP XML since XML returned from FCP is put into a text document window and sending XML to FCP is done from the frontmost currently open window.
    </p>

    <h2>Notes</h2>
    <p>
        In order to choose a project file you need to select the "Choose File…" item. Other items in the same pop-up menu allow you to switch to using the text field for entering a path or clearing the file reference. This was done to avoid having a button and a pop-up.
    </p>
    <p>
        The many of the tooltips show the symbolic names of the Apple Event parameter or attribute that the user interface element is modifying. This is to aid you in understanding what the resulting Apple Event will look like.
    </p>
    <p>
        You can see the underlying Apple Events via the method detailed in
        <a href="http://developer.apple.com/documentation/AppleScript/Conceptual/AppleEvents/debugging_aepg/debugging_aepg.html#//apple_ref/doc/uid/TP40001449-CH210-CHDBAAEE" title="Turning on Apple Event Logging">Turning on Apple Event Logging</a>
        which is part of the
        <a href="http://developer.apple.com/documentation/AppleScript/Conceptual/AppleEvents" title="Apple Events Programming Guide">Apple Events Programming Guide</a>.
    </p>

</body>
</html>
```

[Next](English.lproj-FCPAEHelp-style-basic.css.md)[Previous](Controller.m.md)

