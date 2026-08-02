---
title: 'CSS Effects: Lightbox'
apple_id: DTS40010105
resource_type: Sample Code
platform: Safari|iOS|macOS
topic: null
technology: null
published: '2010-11-01'
source_url: https://developer.apple.com/library/archive/samplecode/lightbox/Listings/lightbox_html.html
archived_at: '2026-07-18T03:29:48.340113Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CSS Effects: Lightbox](CSS%20Effects-%20Lightbox.md)


[Next](lightbox.js.md)[Previous](lightbox.css.md)

# lightbox.html

```
<!DOCTYPE html>
<!--
 File: lightbox.html

 Abstract: Sample page with lightbox

 Version: 1.1

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

 Copyright (C) 2010 Apple Inc. All Rights Reserved.
-->
<html lang="en">
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <title>Lightbox Sample</title>
  <link rel="stylesheet" href="shared.css" type="text/css" media="screen" title="no title" charset="utf-8">
  <link rel="stylesheet" href="lightbox.css" type="text/css" media="screen" title="no title" charset="utf-8">

  <script src="utilities.js" type="text/javascript" charset="utf-8"></script>
  <script src="lightbox.js" type="text/javascript" charset="utf-8"></script>

</head>
<body onresize="positionLightbox()">

  <header>
    <h1>Summer in Sicily</h1>
  </header>

  <nav></nav>

  <article>
    <section>
      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>

      <ul class="thumbs">
        <li class="image-container"><img src="images/thumbs/DSC_2040.JPG" srchighres="images/large/DSC_2040.JPG"><p class="caption">Summer flowers</p></li>
        <li class="image-container"><img src="images/thumbs/DSC_2046.JPG" srchighres="images/large/DSC_2046.JPG"><p class="caption">Taormina, Mazzaro' bay</p></li>
        <li class="image-container"><img src="images/thumbs/DSC_2069.JPG" srchighres="images/large/DSC_2069.JPG"><p class="caption">View from our room</p></li>
        <li class="image-container"><img src="images/thumbs/DSC_2072.JPG" srchighres="images/large/DSC_2072.JPG"><p class="caption">Our hotel</p></li>
        <li class="image-container"><img src="images/thumbs/DSCN1204.JPG" srchighres="images/large/DSCN1204.JPG"><p class="caption">View from the sea</p></li>
        <li class="image-container"><img src="images/thumbs/DSC_2083.JPG" srchighres="images/large/DSC_2083.JPG"><p class="caption">Giardini Naxos by night</p></li>
        <li class="image-container"><img src="images/thumbs/DSC_2307.JPG" srchighres="images/large/DSC_2307.JPG"><p class="caption">Boats on the beach</p></li>
        <li class="image-container"><img src="images/thumbs/DSC_2308.JPG" srchighres="images/large/DSC_2308.JPG"><p class="caption">The old fortress</p></li>
      </ul>
    </section>

  </article>

  <footer>
    <p>First Posted: June 2010</p>
  </footer>
</body>
</html>
```

[Next](lightbox.js.md)[Previous](lightbox.css.md)

