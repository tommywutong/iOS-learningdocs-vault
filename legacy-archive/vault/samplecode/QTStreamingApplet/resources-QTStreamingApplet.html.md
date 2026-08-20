---
title: QTStreamingApplet
apple_id: DTS10000983
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-06-28'
source_url: https://developer.apple.com/library/archive/samplecode/QTStreamingApplet/Listings/resources_QTStreamingApplet_html.html
archived_at: '2026-07-18T03:21:21.090353Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTStreamingApplet](QTStreamingApplet.md)


[Next](src-AppletTag.js.md)[Previous](resources-AppletTag.js.md)

# resources/QTStreamingApplet.html

```
<html>
<head>
<title>QTStreaming Applet</title>
<script src="AppletTag.js">
</script>
</head>
<body>

<script language=JavaScript>
    // for v3 browsers you need to use the 1.0 JS Syntax for creating an object
    // myAppletTag = new Object(); myAppletTag.code = ...
    var myAppletTag = { 
                archive:"QTStreamingApplet.jar",
        code:"QTStreamingApplet.class", 
        width: "320", 
        height: "260",
        align: "left"
    };
    AppletTag (myAppletTag, null);
</script>

<noscript>
    <applet code="QTStreamingApplet.class" archive="QTStreamingApplet.jar" width=320 height=260 align=left>
    <param name="total" value="2">
    <param name="url1" value="rtsp://qts13.liveonline.net/bloomberg">
    <param name="url2" value="rtsp://babeltower.apple.com/etvhi">
    </applet>
</noscript> 

</body>
</html>
```

[Next](src-AppletTag.js.md)[Previous](resources-AppletTag.js.md)

