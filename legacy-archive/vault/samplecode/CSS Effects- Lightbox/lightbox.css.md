---
title: 'CSS Effects: Lightbox'
apple_id: DTS40010105
resource_type: Sample Code
platform: Safari|iOS|macOS
topic: null
technology: null
published: '2010-11-01'
source_url: https://developer.apple.com/library/archive/samplecode/lightbox/Listings/lightbox_css.html
archived_at: '2026-07-18T03:29:48.260505Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CSS Effects: Lightbox](CSS%20Effects-%20Lightbox.md)


[Next](lightbox.html.md)[Previous](ReadMe.txt.md)

# lightbox.css

```
 /*

File: lightbox.css

Abstract: Stylesheet for lightbox

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

header {
    font-family: Impact, cursive;
}

.image-container {
    /* Make the images look clickable */
    cursor: pointer;
}

.caption {
    margin: 0;
    padding: 5px;
    font-size: 9pt;
    text-align: center;
    width: 200px;
    -webkit-box-sizing: border-box;
}

ul.thumbs {
    list-style-type: none;
}

ul.thumbs > li {
    display: inline-block;
    margin: 20px;
    vertical-align: top;
    -webkit-box-shadow: rgba(0, 0, 0, 0.5) 0 5px 10px;
}

/* Lightbox-specific */

#lightbox-overlay {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: rgba(0, 0, 0, 0.7);
    opacity: 0.01;
    -webkit-transition: opacity 1s;
    -webkit-transform: translate3d(0, 0, 0);
    text-align: center; /* to center the #overlay-box */
}

#lightbox-overlay.slow-mode {
    -webkit-transition: opacity 5s;
}

#lightbox-overlay.visible {
    opacity: 1;
}

/* This is the white box the contains initially the loading indicator, then the full size image */
#overlay-box {
    position: relative;
    margin-top: 100px;
    margin: auto;
    background-color: white;
    border: 1px solid white;  
    display: inline-block;

    -webkit-border-radius: 12px;
    -webkit-transform: translate3d(0, 0, 0);
    -webkit-transition-property: -webkit-transform, opacity;
}

/* Scale transition to hide the loading indicator */
#overlay-box.initial {
    -webkit-transition-duration: 500ms;
    -webkit-transform: scale3d(0.01, 0.01, 0.01);
    opacity: 0;
}

#lightbox-overlay.slow-mode #overlay-box.initial {
    -webkit-transition-duration: 2000ms;
    -webkit-transform: scale3d(0.01, 0.01, 0.01);
    opacity: 0;
}

/* Scale transition to show the full size image */
#overlay-box.final {
    -webkit-transition-duration: 1000ms;
    -webkit-transform: scale3d(1, 1, 1);
    opacity: 1;
}

#lightbox-overlay.slow-mode #overlay-box.final {
    -webkit-transition-duration: 4000ms;
    -webkit-transform: scale3d(1, 1, 1);
    opacity: 1;
}


/* The loading indicator */
@-webkit-keyframes spin {
    from { -webkit-transform: rotate(0); }
    to  { -webkit-transform: rotate(360deg); }
}

.load-indicator {
    width: 80px;
    height: 80px;
    margin: 10px;
    background: url('chasing-arrows.png') no-repeat;
    display: none;

    -webkit-background-size: 100% 100%;
    -webkit-animation: spin 0.8s infinite linear;
}

#overlay-box.loading .load-indicator {
    display: block;
}

#lightbox-overlay.slow-mode .load-indicator {
    -webkit-animation: spin 2.4s infinite linear;
}

.overlay-contents {
}

.overlay-contents img {
    margin: 10px;
}

.overlay-contents .caption {
    margin-top: 10px;
    margin-left: 10px;
    text-align: left;
    padding: 5px 0;
}

/* the button to close the overlay */
#close-button {
    position: absolute;
    top: -12px;
    right: -12px;
    width: 30px;
    height: 30px;
    background-image: url('close_button.png');
    background-position: 0 0;
    -webkit-tap-highlight-color: transparent;
    -webkit-transition: opacity 0.5s;
    opacity: 0;
}

/* State of the button at the end of the transition */
#close-button.visible {
    opacity: 1;
}

/* hover state for close button */
#close-button:hover {
    background-position: 0 30px;
}
```

[Next](lightbox.html.md)[Previous](ReadMe.txt.md)

