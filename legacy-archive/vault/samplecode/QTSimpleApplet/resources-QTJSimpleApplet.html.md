---
title: QTSimpleApplet
apple_id: DTS10000982
resource_type: Sample Code
platform: macOS
topic: Cross Platform
technology: null
published: '2006-06-28'
source_url: https://developer.apple.com/library/archive/samplecode/QTSimpleApplet/Listings/resources_QTJSimpleApplet_html.html
archived_at: '2026-07-18T03:21:20.812021Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [QTSimpleApplet](QTSimpleApplet.md)


[Next](src-QTSimpleApplet.java.md)[Previous](resources-AppletTag.js.md)

# resources/QTJSimpleApplet.html

```
<html>
<head>
<title>QTSimpleApplet</title>
<script src="AppletTag.js">
</script>
</head>
<body>

<script language=JavaScript>
    // for v3 browsers you need to use the 1.0 JS Syntax for creating an object
    // myAppletTag = new Object(); myAppletTag.code = ...
    var myAppletTag = { 
                archive:"QTSimpleApplet.jar",
        code:"QTSimpleApplet.class", 
        width: "200", 
        height: "240"
    };

    AppletTag (myAppletTag, ["FILE", "Sample.mov"]);
</script>

<noscript>
    <applet code="QTSimpleApplet.class" archive="QTSimpleApplet.jar" width=200 height=240>
        <param name="file" value="Sample.mov">
    </applet>
</noscript> 

</body>
</html>
```

[Next](src-QTSimpleApplet.java.md)[Previous](resources-AppletTag.js.md)

