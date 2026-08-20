---
title: HTML5VideoOverlays
apple_id: DTS40010109
resource_type: Sample Code
platform: Safari|iOS|macOS
topic: null
technology: null
published: '2010-06-23'
source_url: https://developer.apple.com/library/archive/samplecode/HTML5VideoOverlays/Listings/script_js.html
archived_at: '2026-07-18T03:11:36.343540Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [HTML5VideoOverlays](HTML5VideoOverlays.md)


[Next](style.css.md)[Previous](index.html.md)

# script.js

```
/*
File: script.js

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
function init() {

  var down = "mousedown"; var up = "mouseup"; 
  if ('createTouch' in document) { down = "touchstart"; up ="touchend"; }

  /* toggle appearance of all buttons when clicked or tapped, add additional listeners */
  var buttons = document.getElementsByClassName("button");
  for (var b = 0; b < buttons.length; b++) {
    buttons[b].addEventListener(up, function(evt) {toggleButtonAppearance(evt);}, false);
    buttons[b].addEventListener(down, function(evt) {toggleButtonAppearance(evt);}, false); 

    switch (buttons[b].id) {   
      /* handler for our 'status' div - it shows the 'Click to Play' button, progress indicator, and error indicator */   
      case "status":
        buttons[b].addEventListener(up, function(evt) {loadVideo(evt);}, false);
        break;
      /* toggle playback and the appearance of the play/pause button, once this button is clicked or tapped */
      case "playPauseButton":
        buttons[b].addEventListener(up, function(evt) {togglePlayPause(evt);}, false); 
        break;
      /* go fullscreen, once this button is clicked or tapped */
      case "fullscreenButton":
        buttons[b].addEventListener(up, function() {document.querySelector("video").webkitEnterFullscreen();}, false);
        break;
    }
  }
}

function toggleButtonAppearance(evt) {  
  var button = evt.target;
  var buttonState = button.className;
  button.className = buttonState.match(/active/) ? buttonState.split("active")[0] : buttonState + " active";
}
function loadVideo(evt) {
  evt.target.className = "progress showing";

  var myVideo = document.querySelector("video");
  myVideo.addEventListener("canplaythrough", playVideo, false);
  myVideo.addEventListener("error", reportError, false);  
  myVideo.load();
}

function playVideo() {
  /* hide the status div and image overlay */
  document.getElementById("overlay").className = "hidden";  
  document.getElementById("status").className = "hidden";

  /* play the video */
  document.querySelector("video").play(); 

  /* Show the play/pause button, in paused state. */
  document.getElementById("playPauseButton").className = "pause button showing";

  /* Only show our fullscreen button if going fullscreen programmatically is supported. */
  /* You can check to see if fullscreen mode is supported as soon as the media metadata has been loaded - in other words, once a loadedmetadata event is emitted.
  In this example, we're checking to see if fullscreen mode is supported once canplay is emitted.  canplay is emitted after loadedmetadata, so this is safe. */
  if (document.querySelector("video").webkitSupportsFullscreen) {
    document.getElementById("fullscreenButton").className = "fullscreen button showing";
  }
}

function reportError() {
  document.getElementById("status").className = "error button showing";
}

function togglePlayPause(evt) {
  var playPauseButton = evt.target;
  var myVideo = document.querySelector("video");

  if (myVideo.paused) {
    myVideo.play();
    playPauseButton.className = "pause button showing";
  }
  else {
    myVideo.pause();
    playPauseButton.className = "play button showing";
  }
}
```

[Next](style.css.md)[Previous](index.html.md)

