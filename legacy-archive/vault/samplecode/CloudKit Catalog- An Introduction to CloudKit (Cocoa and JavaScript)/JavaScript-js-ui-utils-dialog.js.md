---
title: 'CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)'
apple_id: TP40014599
resource_type: Sample Code
platform: CloudKit JS|iOS
topic: null
technology: CloudKit
published: '2016-09-13'
source_url: https://developer.apple.com/library/archive/samplecode/CloudAtlas/Listings/JavaScript_js_ui_utils_dialog_js.html
archived_at: '2026-07-18T03:03:25.881004Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md) · [CloudKit Catalog: An Introduction to CloudKit (Cocoa and JavaScript)](CloudKit%20Catalog-%20An%20Introduction%20to%20CloudKit%20%28Cocoa%20and%20JavaScript%29.md)


[Next](JavaScript-js-ui-utils-tab-manager.js.md)[Previous](JavaScript-js-ui-utils-table.js.md)

# JavaScript/js/ui-utils/dialog.js

```
/*
Copyright (C) 2016 Apple Inc. All Rights Reserved.
See LICENSE.txt for this sample’s licensing information

Abstract:
A singleton which encapsulates the functionality of the app's modal dialog.
*/

CKCatalog.dialog = (function() {
  var self = {};

  var el = document.getElementById('dialog');
  var textEl = document.getElementById('dialog-text');

  self.hide = function() {
    el.classList.add('hide');
  };

  var dismissBtn = document.createElement('button');
  dismissBtn.className = 'link';
  dismissBtn.textContent = 'Close';
  dismissBtn.onclick = self.hide;

  var actions = document.createElement('div');
  actions.className = 'actions';
  actions.appendChild(dismissBtn);

  var customDismissButton = document.createElement('button');
  customDismissButton.className = 'link';

  var customActions = document.createElement('div');
  customActions.className = 'actions';
  customActions.appendChild(customDismissButton);

  var positionTextEl = function() {
    var rect = textEl.getBoundingClientRect();
    textEl.style.left = 'calc(50% - ' + (rect.width/2) + 'px)';
    textEl.style.top = 'calc(50% - ' + (rect.height/2) + 'px)';
  };

  self.show = function(text,dismissButtonOptions) {
    el.classList.remove('hide');
    textEl.innerHTML = text;

    if(dismissButtonOptions) {
      textEl.classList.remove('no-actions');

      customDismissButton.textContent = dismissButtonOptions.title;
      customDismissButton.onclick = function() {
        self.hide();
        dismissButtonOptions.action && dismissButtonOptions.action();
      };

      textEl.appendChild(customActions);
    } else {
      textEl.classList.add('no-actions');
    }

    positionTextEl();
  };

  self.showError = function(error) {
    // First log to the console in case anyone needs a stack trace.
    console.error(error);

    // Show the message in a dialog.
    el.classList.remove('hide');
    textEl.classList.remove('no-actions');
    if(error.ckErrorCode) {
      textEl.innerHTML = '<h2>Error: <span class="error-code">' + error.ckErrorCode + '</span></h2>' +
        '<p class="error">' +
          (error.reason ? 'Reason: '+error.reason : (error.message || 'An error occurred.')) +
        '</p>';
    } else {
      var message = error.message || 'An unexpected error occurred.';
      textEl.innerHTML = '<h2>Error</h2>' +
        '<p class="error">' + message + '</p>';
    }
    textEl.appendChild(actions);
    positionTextEl();
  };

  return self;
})();
```

[Next](JavaScript-js-ui-utils-tab-manager.js.md)[Previous](JavaScript-js-ui-utils-table.js.md)

