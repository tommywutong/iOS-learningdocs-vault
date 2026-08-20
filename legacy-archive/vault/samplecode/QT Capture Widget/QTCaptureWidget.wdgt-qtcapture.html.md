---
title: QT Capture Widget
apple_id: DTS10004436
resource_type: Sample Code
platform: macOS
topic: Networking, Internet, & Web
technology: null
published: '2007-08-27'
source_url: https://developer.apple.com/library/archive/samplecode/QTCaptureWidget/Listings/QTCaptureWidget_wdgt_qtcapture_html.html
archived_at: '2026-07-18T03:20:01.302328Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QT Capture Widget](QT%20Capture%20Widget.md)


[Next](QTCaptureWidget.wdgt-qtcapture.js.md)[Previous](QTCaptureWidget.wdgt-qtcapture.css.md)

# QTCaptureWidget.wdgt/qtcapture.html

```
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <style type="text/css" title="AppleStyle">
        @import "qtcapture.css";
    </style>

    <script type="text/javascript" src="file:///System/Library/WidgetResources/AppleClasses/AppleButton.js" charset="utf-8"></script>

    <script type="text/javascript" src="localizedStrings.js" charset="utf-8"></script>
    <script type="text/javascript" src="Parts/utilities.js" charset="utf-8"></script>
    <script type="text/javascript" src="Parts/setup.js" charset="utf-8"></script>
    <script type="text/javascript" src="Parts/Text.js" charset="utf-8"></script>

    <script type="text/javascript" src="Parts/GlassButton.js" charset="utf-8"></script>
    <script type="text/javascript" src="qtcapture.js" charset="utf-8"></script>
<script type="text/javascript" src="Parts/Button.js" charset="utf-8"></script>

<script type="text/javascript" src="file:///System/Library/WidgetResources/AppleClasses/AppleAnimator.js" charset="utf-8"></script>
<script type="text/javascript" src="file:///System/Library/WidgetResources/AppleClasses/AppleInfoButton.js" charset="utf-8"></script>
<script type="text/javascript" src="Parts/InfoButton.js" charset="utf-8"></script>
</head>
<body onload="load();">
    <div id="front">
        <img id="frontImg" src="Images/front.png" alt="">
    <embed name="qtcaptureplugin" width="330" height="320" type="application/x-qtcaptureplugin" id="qtcaptureplugin"></embed>


    <div id="startRecordButton"></div>
    <div id="stopRecordButton"></div>


    <div class="info" id="infobutton"></div>
    <div apple-text-overflow="ellipsis" id="deviceStatusText"></div>

    </div>
    <div id="back">
       <img id="backImg" src="Images/back.png" alt="">
        <img src="Images/DevelopedWith.png" alt="Created with Dashcode" id="backDevelopedWith">
        <div id="done"></div>
    </div>

</body>
</html>
```

[Next](QTCaptureWidget.wdgt-qtcapture.js.md)[Previous](QTCaptureWidget.wdgt-qtcapture.css.md)

