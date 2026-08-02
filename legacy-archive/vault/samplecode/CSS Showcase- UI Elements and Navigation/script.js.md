---
title: 'CSS Showcase: UI Elements and Navigation'
apple_id: DTS40010108
resource_type: Sample Code
platform: Safari|macOS
topic: null
technology: null
published: '2010-06-22'
source_url: https://developer.apple.com/library/archive/samplecode/cssEffectsPart1/Listings/script_js.html
archived_at: '2026-07-18T03:29:02.713210Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CSS Showcase: UI Elements and Navigation](CSS%20Showcase-%20UI%20Elements%20and%20Navigation.md)


[Next](style-transitions.css.md)[Previous](Lobster-fontfacekit-Pablo%20Impallari%20Apache%202%20License.txt.md)

# script.js

```
 /*

 File: script.js

 Abstract: This example webpage showcases a variety of CSS visual 
 effects.  Buttons and other page elements are styled with CSS gradients
 and shadows, menus are animated with CSS transitions, custom fonts are 
 displayed with CSS web fonts, and elements are positioned, scaled, and 
 rotated on the page using CSS transforms.  The entire interface is drawn
 and animated without using any images or plug-ins.

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

function load() {
    // Set up the last two menu transitions.

    var blindsSubmenu = document.getElementById("blinds-submenu");
    setIncreasingTransitionDelay(blindsSubmenu, 0.25, 0.15);

    var zoomDownSubmenu = document.getElementById("zoom-down-submenu");
    setIncreasingTransitionDelay(zoomDownSubmenu, 0.25, 0.10);

    // Set up event handlers for collapsing menus on click. We need the 
    // touchend handler because the body isn't clickable on the iPad.
    document.body.addEventListener("click", collapseMenuFromEvent, false);
    document.body.addEventListener("touchend", collapseMenuFromEvent, false);

    // Set up event handlers for expanding menus.
    var menu = document.getElementById("navigation-menu");
    var menuItems = menu.children;
    for(var i = 0; i < menuItems.length; i++) {
        menuItems[i].addEventListener("click", expandMenuFromEvent, true);
        // Prevent the touchend handler on the body from firing when a button is clicked.
        menuItems[i].addEventListener("touchend", function(e) {e.stopPropagation();}, true);
    }
}

function setIncreasingTransitionDelay(containerElement, initialDelay, delayIncrement)
{
    var children = containerElement.children;
    for(var i = 0; i < children.length; i++)
        children[i].style["-webkit-transition-delay"] = (initialDelay + (i * delayIncrement)) + "s";
}

/* Expand the menu item that was clicked on, and expand this button. Also contract other buttons
 * on the menu bar if they're not contracted already.
 */
function expandMenuFromEvent(event)
{
    var currentlyExpandedMenuItem = document.getElementsByClassName("expanded")[0];
    if (currentlyExpandedMenuItem == this)
        return;
    else if (currentlyExpandedMenuItem) // Only allow one menu to be expanded at a time.
        currentlyExpandedMenuItem.removeClassName("expanded");
    else
        document.getElementById("navigation-menu").addClassName("expanded-menu");

    this.addClassName("expanded");
    event.stopPropagation();
}

/* Collapse the currently open menu and return the menu bar to its original appearance.
 */
function collapseMenuFromEvent(event)
{
    var currentlyExpandedMenuItem = document.getElementsByClassName("expanded")[0];
    if (!currentlyExpandedMenuItem)
        return;

    currentlyExpandedMenuItem.removeClassName("expanded");

    var navigationMenu = document.getElementById("navigation-menu");
    navigationMenu.removeClassName("expanded-menu");
}

/**
 *  Indicates whether the element has a given class name within its class attribute.
 */
Element.prototype.hasClassName = function (className) {
  return new RegExp('(?:^|\\s+)' + className + '(?:\\s+|$)').test(this.className);
};

/**
 *  Adds the given class name to the element's class attribute if it's not already there.
 */
Element.prototype.addClassName = function (className) {
  if (!this.hasClassName(className)) {
    this.className = [this.className, className].join(' ').replace(/^\s*|\s*$/g, "");
  }
};

/**
 *  Removes the given class name from the element's class attribute if it's there.
 */
Element.prototype.removeClassName = function (className) {
  if (this.hasClassName(className)) {
    var curClasses = this.className;
    this.className = curClasses.replace(new RegExp('(?:^|\\s+)' + className + '(?:\\s+|$)', 'g'), ' ').replace(/^\s*|\s*$/g, "");
  }
};
```

[Next](style-transitions.css.md)[Previous](Lobster-fontfacekit-Pablo%20Impallari%20Apache%202%20License.txt.md)

