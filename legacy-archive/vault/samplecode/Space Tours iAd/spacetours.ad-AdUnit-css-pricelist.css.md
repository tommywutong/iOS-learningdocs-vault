---
title: Space Tours iAd
apple_id: DTS40010222
resource_type: Sample Code
platform: iAd Producer|iOS
topic: User Experience
technology: null
published: '2011-03-08'
source_url: https://developer.apple.com/library/archive/samplecode/SpaceTours/Listings/spacetours_ad_AdUnit_css_pricelist_css.html
archived_at: '2026-07-18T03:25:14.470117Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [Space Tours iAd](Space%20Tours%20iAd.md)


[Next](spacetours.ad-AdUnit-css-store.css.md)[Previous](spacetours.ad-AdUnit-css-photos.css.md)

# spacetours.ad/AdUnit/css/pricelist.css

```
/*
    File: pricelist.css
Abstract: The pricelist CSS file.
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

#pricelist {
  position: absolute;
  width: 320px;
  height: 480px;
}

.pricelist-frame {
  position: absolute;
  left: 30px;
  top: 145px;
  width: 260px;
  height: 300px;
  border-width: 18px 18px;
  -webkit-box-sizing: border-box;
  -webkit-border-image: url("../assets/menu/menu-back.png") 37 37 37 37;
  -webkit-transition: opacity 500ms;
}

/* Make sure that when the menu is visible the pricelist frame hides itself. Note
   the transition specified above which causes this to be a fade rather
   than a quick snap. */
body.menu-visible .pricelist-frame {
  opacity: 0;
}

/* Configure the table of prices. They are all contained within a table
   view - set the width and height of the view so that the scrolling
   code knows the bounds in which it is supposed to work. */
#pricelist .ad-table-view {
  width: 225px;
  height: 265px;
}

/* Each element in the table is a cell. */
#pricelist .ad-table-view-cell {
  border-bottom: none;
  border-top: none;
  height: 30px;
}

/* We've added some span elements to the cell. Set up their display. */
#pricelist .ad-table-view-cell span {
  font-size: 12px;
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica;
  white-space : nowrap;
  overflow : hidden;
  text-overflow: ellipsis;
}

/* A special style for the name of the item being sold */
#pricelist .ad-table-view-cell span.name {
  position: absolute;
  left: 8px;
  top: 9px;
  max-width: 140px;
}

/* A special style for the price of the item being sold */
#pricelist .ad-table-view-cell span.price {
  position: absolute;
  left: 150px;
  top: 9px;
  max-width: 75px;
  text-align: right;
}

/* Give the top and bottom of the table a little rounded corners
   so we get some indication of where we are in the list. */
#pricelist .ad-table-view-cell:first-of-type {
  -webkit-border-radius: 10px 10px 0 0;
}

#pricelist .ad-table-view-cell:last-of-type {
  -webkit-border-radius: 0 0 10px 10px;
}

/* Next, give the even and odd cells a slightly different style
   so we get a striped table. */
#pricelist .ad-table-view-cell:nth-of-type(even) {
  background-color: #51997F;
  color: black;
  text-shadow: rgba(0, 0, 0, 0.8) 0px -1px 0px;
}

#pricelist .ad-table-view-cell:nth-of-type(odd) {
  background-color: #6BAFE0;
  color: black;
  text-shadow: rgba(0, 0, 0, 0.8) 0px -1px 0px;
}
```

[Next](spacetours.ad-AdUnit-css-store.css.md)[Previous](spacetours.ad-AdUnit-css-photos.css.md)

