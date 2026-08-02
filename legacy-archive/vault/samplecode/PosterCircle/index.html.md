---
title: PosterCircle
apple_id: DTS40007648
resource_type: Sample Code
platform: Safari|iOS
topic: null
technology: null
published: '2008-06-19'
source_url: https://developer.apple.com/library/archive/samplecode/PosterCircle/Listings/index_html.html
archived_at: '2026-07-18T03:19:29.840593Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [PosterCircle](PosterCircle.md)


[Next](PosterCircle.css.md)[Previous](README.txt.md)

# index.html

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
File: index.html
Abstract: Content layout for the PosterCircle sample.
          Displays a spinning cylinder made of three rings when this page loads.

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

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Strict//EN"
  "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
    <title>Poster Circle</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    <meta name="viewport" content="initial-scale=0.60, minimum-scale=0.60, maximum-scale=0.60, width=device-width">
    <!-- The PosterCircle.js file implements each ring -->
    <script type="text/javascript" language="javascript" src="PosterCircle.js"></script>
    <!-- The PosterCircle.css file contains all required information to build the animations and transformations -->
    <link rel="stylesheet" href="PosterCircle.css" />
</head>
<body>
    <!-- All the id selectors and classes used below are defined in PosterCircle.css -->
    <div id="stage">
        <div id="rotate">
        <!-- The following div elements build the three rings of the cylinder. The "ring" class defines and styles each of these rings. -->
        <!-- The "ring-1," "ring-2," and "ring-3" id selectors implement the spinning animation for their respective rings in PosterCircle.css  -->
        <!-- PosterCircle.js uses these selectors to create the ring's circular shape and content -->
            <div id="ring-1" class="ring"></div>
            <div id="ring-2" class="ring"></div>
            <div id="ring-3" class="ring"></div>
        </div>
    </div>
</body>
</html>
```

[Next](PosterCircle.css.md)[Previous](README.txt.md)

