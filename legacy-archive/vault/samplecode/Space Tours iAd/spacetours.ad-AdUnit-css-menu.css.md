---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_css_menu_css.html
archived_at: '2026-07-18T03:25:14.359232Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-css-photos.css.md)[Previous](spacetours.ad-AdUnit-css-maps.css.md)

# spacetours.ad/AdUnit/css/menu.css

```
/*
    File: menu.css
Abstract: The menu CSS file.
 Version: 1.3

Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple
Inc. ("Apple") in consideration of your agreement to the following
terms, and your use, installation, modification or redistribution of
this Apple software constitutes acceptance of these terms.  If you do
not agree with these terms, please do not use, install, modify or
redistribute this Apple software.

In consideration of your agreement to abide by the following terms, and
subject to these terms, Apple grants you a personal, non-exclusive
license, under Apple's copyrights in this original Apple software (the
"Apple Software"), to use, reproduce, modify and redistribute the Apple
Software, with or without modifications, in source and/or binary forms;
provided that if you redistribute the Apple Software in its entirety and
without modifications, you must retain this notice and the following
text and disclaimers in all such redistributions of the Apple Software.
Neither the name, trademarks, service marks or logos of Apple Inc. may
be used to endorse or promote products derived from the Apple Software
without specific prior written permission from Apple.  Except as
expressly stated in this notice, no other rights or licenses, express or
implied, are granted by Apple herein, including but not limited to any
patent rights that may be infringed by your derivative works or by other
works in which the Apple Software may be incorporated.

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

Copyright (C) 2011 Apple Inc. All Rights Reserved.

*/

#menu-container {
  z-index: 1;
}

#menu {
  position: absolute;
  top: 170px;
  width: 320px;
  height: 310px;
  -webkit-transform: translateY(275px);
  -webkit-transition: -webkit-transform 400ms;
}

body.menu-visible #menu {
  -webkit-transform: translateY(0px);
}

#menu .menu-wrapper {
  position: absolute;
  left: 30px;
  top: 0px;
  width: 270px;
  height: 310px;
}

#menu .menu-wrapper .menu-button {
  position: absolute;
  left: 235px;
  top: 0px;
  width: 33px;
  height: 33px;
  background-color: transparent;
  background-image: url('../assets/menu/info-i.png'), url('../assets/menu/info-back.png');
  background-position: 9px 9px, top left;
  background-size: 15px 15px, 33px 33px;
  background-repeat: no-repeat;
}

#menu .menu-wrapper .menu-button.highlighted {
  background-image: url('../assets/menu/info-i.png'), url('../assets/menu/info-back.png');
}

#menu .menu-wrapper .button-container {
  position: absolute;
  top: 10px;
  left: 0px;
  width: 260px;
  height: 290px;
  border-width: 18px 18px;
  -webkit-box-sizing: border-box;
  -webkit-border-image: url("../assets/menu/menu-back.png") 37 37 37 37;
}

#menu .menu-wrapper .button-container .ad-button {
  position: absolute;
  left: 30px;
  width: 225px;
  height: 40px;
  background: none;
  border: none;
  color: white;
  font-size: 25px;
  text-align: left;
  background-image: none;
}

#menu .menu-wrapper .button-container .ad-button.highlighted {
  color: red;
  background-image: none;
}

#menu .menu-wrapper .menu-item:nth-of-type(1) {
  top: 5px;
}

#menu .menu-wrapper .menu-item:nth-of-type(2) {
  top: 55px;
}

#menu .menu-wrapper .menu-item:nth-of-type(3) {
  top: 105px;
}

#menu .menu-wrapper .menu-item:nth-of-type(4) {
  top: 155px;
}

#menu .menu-wrapper .menu-item:nth-of-type(5) {
  top: 205px;
}
```

[Next](spacetours.ad-AdUnit-css-photos.css.md)[Previous](spacetours.ad-AdUnit-css-maps.css.md)

