---
title: JISApplet
apple_id: DTS10000961
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JISApplet/Listings/classes_test_html.html
archived_at: '2026-07-18T03:13:09.680288Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JISApplet](JISApplet.md)


[Next](src-JISApplet.java.md)[Previous](AppletTag.js.md)

# classes/test.html

```
<html>
<head>
<title>JISApplet</title>
<script src="../../AppletTag.js">
</script>
</head>
<body>

<script language=JavaScript>
    // for v3 browsers you need to use the 1.0 JS Syntax for creating an object
    // myAppletTag = new Object(); myAppletTag.code = ...
    var myAppletTag = { 
        code:"JISApplet.class", 
        width: "200", 
        height: "200"
    };

    AppletTag (myAppletTag, ["media", "crossfad.gif", "ext", "gif"]);
</script>

<noscript>
    <applet code="JISApplet.class" width=200 height=200>
        <param name="media" value="crossfad.gif">
        <param name="ext" value="gif">
    </applet>
</noscript> 

</body>
</html>
```

[Next](src-JISApplet.java.md)[Previous](AppletTag.js.md)

