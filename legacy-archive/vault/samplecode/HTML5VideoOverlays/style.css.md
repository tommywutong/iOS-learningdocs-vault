---
title: HTML5VideoOverlays
apple_id: DTS40010109
resource_type: Sample Code
platform: Safari|iOS|macOS
topic: null
technology: null
published: '2010-06-23'
source_url: https://developer.apple.com/library/archive/samplecode/HTML5VideoOverlays/Listings/style_css.html
archived_at: '2026-07-18T03:11:36.402324Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HTML5VideoOverlays](HTML5VideoOverlays.md)


[Next](Document%20Revision%20History.md)[Previous](script.js.md)

# style.css

```
/*
File: style.css

Abstract: HTML5 Video Element Overlays

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
*/

/** play/pause and fullscreen button styles **/
#playPauseButton {
  position: absolute;
  top: 440px;
  left: 50px;
  width: 70px;
}
#playPauseButton.play:before {
    content: "PLAY";
    margin-left: 3px;
}
#playPauseButton.pause:before {
    content: "PAUSE";
    margin-left: -3px;
}
#fullscreenButton {
  position: absolute;
  top: 450px;
  left: 820px;
  width: 10px;
  height: 10px;
  -webkit-border-radius: 16px;
}

#fullscreenButton:before {
  content: url(media/arrows.png);
  position: relative;
  top: -11px;
  left: -11px;
}

/** styles for different status states (progress indicator, error) **/
#status {
  position: absolute;
  z-index: 2; top: 260px; left: 330px;
}
#status.clicktoplay:before {  
  content: "CLICK TO PLAY";    
}
#status.progress:before {  
  content: url(media/spinner.gif);
  position: absolute;
  left: 82px;
  top: -12px;  
}
#status.error:before { 
  content: "OH NO! ERROR!";    
  color: yellow;
}

/** styles for showing and hidden states **/
#overlay.showing {
  opacity: 1.0;
}
.showing {
  opacity: 0.8;
  position: absolute;
  z-index: 1;
}
.hidden {
  opacity: 0;
  position: absolute;
  z-index: -1;
}

/** animations to fade out the overlay image and "Click To Play" button **/
#overlay, #status {
  -webkit-transition-property: opacity, z-index;
  -webkit-transition-duration: 0.8s, 0s;
  -webkit-transition-delay: 0, 2s;
}

/** general body and button styles **/
body {
  background-color: #666666;
  color: white; 
  margin: 30px;
  font-family: 'Verdana', 'Lucida Grande';
}
.button {
  -webkit-border-radius: 30px; 
  -webkit-box-shadow: 4px 4px 8px black;
  position: absolute; 
  height: 20px; 
  width: 200px;   
  padding: 17px; 
  background-color: #6699cc;
  font-size: 20px; 
  letter-spacing: 1px;
  text-shadow: 2px 2px 3px #003366;
  text-align: center; 
  line-height: 20px;
  -webkit-user-select: none;

  /** animations to fade in the play/pause and fullscreen buttons **/  
  -webkit-transition-property: opacity;
  -webkit-transition-duration: 2s;
}
.active {  
  background-color: #336699;
}
a {
  color:white;
  font-size: 12px;
  text-decoration: none;
}
a:hover {
  text-decoration: underline;
}
a:visited {
  color: #6699cc;
}
video {
  -webkit-box-shadow: 12px 12px 20px black;
}
```

[Next](Document%20Revision%20History.md)[Previous](script.js.md)

