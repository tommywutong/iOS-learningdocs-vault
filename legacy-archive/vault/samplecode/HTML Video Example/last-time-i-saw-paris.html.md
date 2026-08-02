---
title: HTML Video Example
apple_id: DTS40007723
resource_type: Sample Code
platform: Safari
topic: null
technology: null
published: '2008-06-02'
source_url: https://developer.apple.com/library/archive/samplecode/HTML_video_example/Listings/last_time_i_saw_paris_html.html
archived_at: '2026-07-18T03:11:42.284705Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HTML Video Example](HTML%20Video%20Example.md)


[Next](last-time.css.md)[Previous](acquicktime.js.md)

# last-time-i-saw-paris.html

```
<!--
    Important:

    This is sample code demonstrating API, technology or techniques in development.
    Although this sample code has been reviewed for technical accuracy, it is not 
    final. Apple is supplying this information to help you plan for the adoption of 
    the technologies and programming interfaces described herein. This information 
    is subject to change, and software implemented based on this sample code should 
    be tested with final operating system software and final documentation. Newer 
    versions of this sample code may be provided with future seeds of the API or 
    technology. For information about updates to this and other developer 
    documentation, view the New & Updated sidebars in subsequent documentation seeds.
-->

<!--
    File: last-time-i-saw-paris.html
    Abstract: Content layout for the "Last Time I Saw Paris" sample.

    Version: 1.0

    Disclaimer: IMPORTANT:  This Apple software is supplied to you by
    Apple Inc. ("Apple") in consideration of your agreement to the
    following terms, and your use, installation, modification or
    redistribution of this Apple software constitutes acceptance of these
    terms.  If you do not agree with these terms, please do not use,
    install, modify or redistribute this Apple software.

    In consideration of your agreement to abide by the following terms, and
    subject to these terms, Apple grants you a personal, non-exclusive
    license, under Apple's copyrights in this original Apple software (the
    "Apple Software"), to use, reproduce, modify and redistribute the Apple
    Software, with or without modifications, in source and/or binary forms;
    provided that if you redistribute the Apple Software in its entirety and
    without modifications, you must retain this notice and the following
    text and disclaimers in all such redistributions of the Apple Software.
    Neither the name, trademarks, service marks or logos of Apple Inc.
    may be used to endorse or promote products derived from the Apple
    Software without specific prior written permission from Apple.  Except
    as expressly stated in this notice, no other rights or licenses, express
    or implied, are granted by Apple herein, including but not limited to
    any patent rights that may be infringed by your derivative works or by
    other works in which the Apple Software may be incorporated.

    The Apple Software is provided by Apple on an "AS IS" basis.  APPLE
    MAKES NO WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION
    THE IMPLIED WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY AND FITNESS
    FOR A PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND
    OPERATION ALONE OR IN COMBINATION WITH YOUR PRODUCTS.

    IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL
    OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
    SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
    INTERRUPTION) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION,
    MODIFICATION AND/OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED
    AND WHETHER UNDER THEORY OF CONTRACT, TORT (INCLUDING NEGLIGENCE),
    STRICT LIABILITY OR OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE
    POSSIBILITY OF SUCH DAMAGE.

    Copyright (C) 2008 Apple Inc. All Rights Reserved.

-->

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
    <head>
        <meta http-equiv="Content-type" content="text/html; charset=utf-8" />

        <meta name = "viewport" content = "width=device-width">

        <title>The Last Time I Saw Paris</title>

        <link type="text/css" href="last-time.css" rel="stylesheet" />
        <script type="text/javascript" src="ac_quicktime.js"></script>

        <script>
            function jumpToTime(timeInSecs)
            {
                try
                {
                    var vid = document.getElementById("paris_video");
                    if ( vid && ('VIDEO' == vid.tagName) && vid.currentTime )
                    {
                        // video tag, use it
                        vid.currentTime = timeInSecs;
                        return;
                    }

                    // browser apparently doesn't support video, look for embed then for an object
                    vid = document.getElementById("paris_embed");
                    if ( !vid ) 
                        vid = document.getElementById("paris_obj");
                    if ( vid && vid.GetTimeScale ) 
                    {
                        // time in QuickTime is in timescale units per second, convert from param in seconds
                        var timeScale = vid.GetTimeScale();
                        vid.SetTime(timeInSecs * timeScale);
                    }
                }
                catch(e) {} 
            }
            // 
        </script> 
    </head>
    <body>
        <div id="content">
            <h1>The Last Time I Saw Paris <span id=studio>1954 Metro-Goldwyn-Mayer</span></h1>
            <hr>
            <p>A film from Metro-Goldwyn-Mayer, lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et </p>
            <p>The film stars <a href="javascript:jumpToTime(11.7)">Van Johnson</a> and Elizabeth Taylor, with <a href="javascript:jumpToTime(65)">Eva Gabor</a>, Donna Reed,
            and Roger Moore. Johnson and Gabor compete in a road race through the streets of Monaco in a <a href="javascript:jumpToTime(30.9)">Jaguar XK120 Roadster</a>.</p>

            <video id="paris_video" controls >
                <source src="media/last-time-race-start.mp4" type="video/mp4">
                <source src="media/last-time-race-start.ogg" type="video/ogg">
                <script>
                    QT_WriteOBJECT('media/last-time-race-start.mp4',
                        '40em', '31em',             // width & height
                        '',                         // required version of the ActiveX control, we're OK with the default value
                        'scale', 'tofit',           // scale to fit element size exactly so resizing works
                        'emb#id', 'paris_embed',    // ID for embed tag only
                        'obj#id', 'paris_obj');     // ID for object tag only
                </script> 
            </video>

            <p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr,  sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.

            <p>Duis autem vel eum iriure dolor in hendrerit in vulputate velit esse molestie consequat, vel illum dolore eu feugiat nulla facilisis at vero eros et accumsan et iusto odio dignissim qui blandit praesent luptatum zzril delenit augue duis dolore te feugait nulla facilisi. Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh euismod tincidunt ut laoreet dolore magna aliquam erat volutpat.
        </div>
    </body>
</html>
```

[Next](last-time.css.md)[Previous](acquicktime.js.md)

