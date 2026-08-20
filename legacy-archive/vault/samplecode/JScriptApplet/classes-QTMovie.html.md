---
title: JScriptApplet
apple_id: DTS10000962
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/JScriptApplet/Listings/classes_QTMovie_html.html
archived_at: '2026-07-18T03:13:14.092024Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [JScriptApplet](JScriptApplet.md)


[Next](src-JScriptApplet.java.md)[Previous](AppletTag.js.md)

# classes/QTMovie.html

```
<HTML>
    <HEAD>
        <TITLE>Communication between JS and Java using QTJ</TITLE>
    </HEAD>

    <BODY>
        <OBJECT classid="clsid:8AD9C840-044E-11D1-B3E9-00805F499D93"
            ID="JScriptApplet"
            WIDTH="200" HEIGHT="200"
            ALIGN="baseline"
            CODEBASE="http://java.sun.com/products/plugin/1.1/jinstall-11-win32.cab#Version=1,1,0,0">
            <PARAM NAME="code" VALUE="JScriptApplet.class">
            <PARAM NAME="type" VALUE="application/x-java-applet;version=1.1">
            <PARAM NAME="file" VALUE="jumps.mov">
            <COMMENT> <!-- This wont' work in Netscape version 4 or less See read me --> 
                <EMBED TYPE="application/x-java-applet;version=1.1"
                    CODE="JScriptApplet.class"
                    NAME="JScriptApplet"
                    WIDTH="200" HEIGHT="200"
                    ALIGN="baseline"
                    FILE="jumps.mov"
                    PLUGINSPAGE="http://java.sun.com/products/plugin/1.1/plugin-install.html">
                    <NOEMBED>
            </COMMENT>
                        No JDK 1.1 support for APPLET!!
                    </NOEMBED>
                </EMBED>
        </OBJECT>

        <SCRIPT LANGUAGE=JavaScript>
            function PauseButton () {
                if (document.JScriptApplet.isPlaying())
                    document.Form1.Pause.value = " Play";
                else
                    document.Form1.Pause.value = "Pause";
                document.JScriptApplet.pause();
            }

            function ResetButton () {
                document.Form1.Pause.value = " Play";
                document.JScriptApplet.resetTime(0);
            }

            function ChangeLocation () {
                var loc = document.Form1.Location.value;
                if ((loc < 0) || (loc >= document.JScriptApplet.getMaxTime()))
                    document.Form1.Location.value = document.JScriptApplet.getMovieTime();
                else {
                    document.Form1.Pause.value = " Play";           
                    document.JScriptApplet.resetTime(loc);
                }
            }
        </SCRIPT>

        <P>
        <HR>
        <FORM NAME=Form1>
            <INPUT TYPE=button NAME="Pause" VALUE=" Play" ONCLICK="PauseButton();">
            <INPUT TYPE=button NAME="Reset" VALUE="Reset" ONCLICK="ResetButton();"><BR>
            Enter a location in the movie:
            <INPUT TYPE=text NAME="Location" VALUE="0" ONBLUR="ChangeLocation();"><BR>
        </FORM>
    </BODY>
</HTML>
```

[Next](src-JScriptApplet.java.md)[Previous](AppletTag.js.md)

