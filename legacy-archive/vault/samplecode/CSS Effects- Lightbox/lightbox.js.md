---
title: 'CSS Effects: Lightbox'
apple_id: DTS40010105
resource_type: Sample Code
platform: Safari|iOS|macOS
topic: null
technology: null
published: '2010-11-01'
source_url: https://developer.apple.com/library/archive/samplecode/lightbox/Listings/lightbox_js.html
archived_at: '2026-07-18T03:29:48.387826Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CSS Effects: Lightbox](CSS%20Effects-%20Lightbox.md)


[Next](shared.css.md)[Previous](lightbox.html.md)

# lightbox.js

```
//
// File:       lightbox.js
//
// Abstract:   Lightbox class implementation
//
// Version:    1.1
//
// Disclaimer: IMPORTANT:  This Apple software is supplied to you by Apple Inc. ("Apple")
//             in consideration of your agreement to the following terms, and your use,
//             installation, modification or redistribution of this Apple software
//             constitutes acceptance of these terms.  If you do not agree with these
//             terms, please do not use, install, modify or redistribute this Apple
//             software.
//
//             In consideration of your agreement to abide by the following terms, and
//             subject to these terms, Apple grants you a personal, non - exclusive
//             license, under Apple's copyrights in this original Apple software ( the
//             "Apple Software" ), to use, reproduce, modify and redistribute the Apple
//             Software, with or without modifications, in source and / or binary forms;
//             provided that if you redistribute the Apple Software in its entirety and
//             without modifications, you must retain this notice and the following text
//             and disclaimers in all such redistributions of the Apple Software. Neither
//             the name, trademarks, service marks or logos of Apple Inc. may be used to
//             endorse or promote products derived from the Apple Software without specific
//             prior written permission from Apple.  Except as expressly stated in this
//             notice, no other rights or licenses, express or implied, are granted by
//             Apple herein, including but not limited to any patent rights that may be
//             infringed by your derivative works or by other works in which the Apple
//             Software may be incorporated.
//
//             The Apple Software is provided by Apple on an "AS IS" basis.  APPLE MAKES NO
//             WARRANTIES, EXPRESS OR IMPLIED, INCLUDING WITHOUT LIMITATION THE IMPLIED
//             WARRANTIES OF NON - INFRINGEMENT, MERCHANTABILITY AND FITNESS FOR A
//             PARTICULAR PURPOSE, REGARDING THE APPLE SOFTWARE OR ITS USE AND OPERATION
//             ALONE OR IN COMBINATION WITH YOUR PRODUCTS.
//
//             IN NO EVENT SHALL APPLE BE LIABLE FOR ANY SPECIAL, INDIRECT, INCIDENTAL OR
//             CONSEQUENTIAL DAMAGES ( INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
//             SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
//             INTERRUPTION ) ARISING IN ANY WAY OUT OF THE USE, REPRODUCTION, MODIFICATION
//             AND / OR DISTRIBUTION OF THE APPLE SOFTWARE, HOWEVER CAUSED AND WHETHER
//             UNDER THEORY OF CONTRACT, TORT ( INCLUDING NEGLIGENCE ), STRICT LIABILITY OR
//             OTHERWISE, EVEN IF APPLE HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
//
// Copyright ( C ) 2010 Apple Inc. All Rights Reserved.
//

function Lightbox()
{
    this.isiPad = (navigator.userAgent.indexOf('iPad') != -1);
    this.lightboxContainers = document.querySelectorAll('.image-container');
    this.setupEventHandlers();
}

// Add event handlers for all the image-container elements on the page
Lightbox.prototype.setupEventHandlers = function()
{
    for (var i = 0; i < this.lightboxContainers.length; ++i) {
        var curContainer = this.lightboxContainers[i];
        if (this.isiPad)
              curContainer.addEventListener('touchend', this.containerClicked.bind(this, curContainer), false);
        else
              curContainer.addEventListener('click', this.containerClicked.bind(this, curContainer), false);
    }
}

Lightbox.prototype.containerClicked = function(container)
{
    switch (event.type) {
        case 'click':
            this.slowMode = event.shiftKey;
            this.enterLightbox(container);
            break;

        case 'touchend':
            this.slowMode = container == this.lightboxContainers[0];
            this.enterLightbox(container);
            break;
    }
}

// Enter the lightbox
Lightbox.prototype.enterLightbox = function(container)
{
    this.makeOverlay();
    this.adaptOverlay(container);
    this.showOverlay();
}

// Create the overlay and the elements in it
Lightbox.prototype.makeOverlay = function()
{
    if (this.overlay)
        return;

    // The overlay itself
    this.overlay = document.createElement('div');
    this.overlay.id = 'lightbox-overlay';
    this.overlay.style.height = document.height + 'px';
    this.overlay.addEventListener('webkitTransitionEnd', this, false);

    // The box to host the content
    this.overlayBox = document.createElement('div');
    this.overlayBox.id = 'overlay-box';
    this.overlay.appendChild(this.overlayBox);

    // The loading indicator
    this.loadIndicator = document.createElement('div');
    this.loadIndicator.className = 'load-indicator';
    this.overlayBox.appendChild(this.loadIndicator);

    // The container for the content to be displayed
    this.overlayContents = document.createElement('div');
    this.overlayContents.className = 'overlay-contents';
    this.overlayBox.appendChild(this.overlayContents);

    // The button to close the lightbox
    this.overlay.closeButton = document.createElement('div');
    this.overlay.closeButton.id = 'close-button';
    this.overlayBox.appendChild(this.overlay.closeButton);

    // Add the event handler for the close button
    var self = this;
    this.overlay.closeButton.addEventListener('click', function() {
        self.hideOverlay();
    }, false);
}

// Start the image loading and show the loading indicator
Lightbox.prototype.adaptOverlay = function(container)
{
    this.overlayContents.removeAllChildren()

    if (this.slowMode)
        this.overlay.addClassName('slow-mode');
    else
        this.overlay.removeClassName('slow-mode');

    // Grab the image
    var originalImage = container.querySelectorAll('img')[0];
    var highResImageURL = originalImage.getAttribute('srchighres');
    if (!highResImageURL)
        highResImageURL = originalImage.src;

    // Create the image element and add the event handlers
    this.overlayImage = new Image();
    this.overlayImage.addEventListener('load', this, false);
    this.overlayImage.addEventListener('error', this, false);

    this.imageLoaded = false;

    var self = this;
    window.setTimeout(function() {
                      self.overlayImage.src = highResImageURL;
                      }, this.slowMode ? 3000 : 1500);

    // Copy the caption
    var originalCaption = container.querySelectorAll('.caption')[0];
    this.overlayContents.overlayCaption = originalCaption.cloneNode(true);  // Deep clone.
}

// Show the overlay
Lightbox.prototype.showOverlay = function()
{
    document.body.appendChild(this.overlay);
    this.overlayBox.style.marginTop = document.body.scrollTop + 250 + 'px';
    this.overlay.transitionInProgress = true;
    this.overlayBox.addClassName('loading');

    // Start the transition
    var self = this;
    window.setTimeout(function() {
                      self.overlay.addClassName('visible');
                      }, 200);
}

// Handle the transition to show the image
Lightbox.prototype.fitToImage = function()
{
    if (this.overlayBox.hasClassName('final'))
        return;

    this.overlayBox.removeClassName('loading');
    this.overlayContents.appendChild(this.overlayImage);
    this.overlayContents.appendChild(this.overlayContents.overlayCaption);
    this.overlayBox.style.marginTop = document.body.scrollTop + 50 + 'px';
    this.overlay.closeButton.addClassName('visible');

    var self = this;
    window.setTimeout(function() {
                      self.overlayBox.addClassName('final');
                      }, 0);
}

// Hide the overlay
Lightbox.prototype.hideOverlay = function()
{
    this.overlay.className = '';
    this.overlayBox.removeClassName('initial');
    this.overlayBox.removeClassName('final');
    this.overlay.closeButton.removeClassName('visible');
}

// Remove the overlay from the document
Lightbox.prototype.removeOverlay = function()
{
    document.body.removeChild(this.overlay);
}

// Handle the overlay transitions
Lightbox.prototype.transitionDone = function()
{
    if (this.overlay.hasClassName('visible')) {
        // Start the transitions to shrink the loading indicator
        var self = this;
        window.setTimeout(function() {
                      self.overlayBox.addClassName('initial');
                      }, 0);
    } else
        this.removeOverlay();
}

// Event handler for the lightbox class
Lightbox.prototype.handleEvent = function(event)
{
    switch (event.type)
    {
    case 'webkitTransitionEnd':
        if (event.target == this.overlayBox) {
            // Handle transitions on the overlay box
            this.fitToImage();
            break;
        }

        if (event.target == this.overlay) {
            // The overlay trasition has completed
            this.overlay.transitionInProgress = false;
            if (this.imageLoaded)
                this.transitionDone();
        }
        break;

    case 'error':
        // Something went wrong when trying to load the image. Remove the overlay.
        this.removeOverlay();
        break;

    case 'load':
        this.imageLoaded = true;
        if (!this.transitionInProgress)
            this.transitionDone();
        break;            
  }
}

// Resize the overlay when the window size changes
Lightbox.prototype.repositionLightbox = function()
{
    if (this.overlay)
        this.overlay.style.height = document.height + 'px';
}

var gLightbox;
function positionLightbox()
{
    gLightbox.repositionLightbox();
}
function setupLightbox()
{
    gLightbox = new Lightbox();
}

window.addEventListener('load', setupLightbox, false);
```

[Next](shared.css.md)[Previous](lightbox.html.md)

